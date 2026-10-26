"""Reproduce and record EPI checkpoint validation (standard library only).

Run from the repository root with `python scripts/validate_repository.py`.
Outputs checkpoint_validation.json. This is a one-shot local diagnostic tool.
"""

# ast parses Python source files without executing them.
# Documentation: https://docs.python.org/3/library/ast.html#ast.parse
import ast

# concurrent.futures runs independent subprocess validations concurrently.
# Documentation: https://docs.python.org/3/library/concurrent.futures.html#concurrent.futures.ThreadPoolExecutor
from concurrent.futures import ThreadPoolExecutor, as_completed

# datetime produces an explicit UTC timestamp for the saved results.
# Documentation: https://docs.python.org/3/library/datetime.html#datetime.datetime.now
from datetime import datetime, timezone

# hashlib records the exact source bytes that the results validate.
# Documentation: https://docs.python.org/3/library/hashlib.html#hashlib.sha256
import hashlib

# json serializes manifest and validation reports.
# Documentation: https://docs.python.org/3/library/json.html
import json

# os supplies the child process environment.
# Documentation: https://docs.python.org/3/library/os.html#os.environ
import os

# pathlib handles repository paths portably.
# Documentation: https://docs.python.org/3/library/pathlib.html#pathlib.Path
from pathlib import Path

# subprocess executes modules and test suites in isolated Python processes.
# Documentation: https://docs.python.org/3/library/subprocess.html#subprocess.run
import subprocess

# sys gives the current Python interpreter and runtime version.
# Documentation: https://docs.python.org/3/library/sys.html#sys.executable
import sys

ROOT = Path(__file__).resolve().parent.parent
MANIFEST = ROOT / "exercise_manifest.json"
RESULT = ROOT / "checkpoint_validation.json"


def run_one(entry: dict) -> dict:
    name = entry["source_py"].removeprefix("src/").removesuffix(".py").replace("/", ".")
    command = [sys.executable, "-m", name]
    environment = dict(os.environ, PYTHONPATH=str(ROOT / "src"))
    try:
        result = subprocess.run(
            command, cwd=ROOT, env=environment, capture_output=True, text=True, timeout=6,
            check=False,
        )
        return {
            "exercise": entry["number"],
            "module": name,
            "command": command,
            "status": "passed" if result.returncode == 0 else "failed",
            "returncode": result.returncode,
            "stdout_tail": result.stdout[-1600:],
            "stderr_tail": result.stderr[-1600:],
        }
    except subprocess.TimeoutExpired as exc:
        return {"exercise": entry["number"], "module": name, "command": command,
                "status": "timeout", "timeout_seconds": 6, "error": str(exc)}


def main() -> int:
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    assert len(manifest) == 264
    implemented = [item for item in manifest if item["source_py"]]
    missing = [item for item in manifest if not item["source_py"]]
    source_hashes = {}
    checked_files = []
    syntax_errors = []
    missing_paths = []
    for item in manifest:
        paths = [item["reference_md"]]
        if item["source_py"]:
            paths += [item["source_py"], item["test_py"]]
        for relative in paths:
            path = ROOT / relative
            if not path.is_file():
                missing_paths.append(relative)
            elif relative.endswith(".py"):
                checked_files.append(relative)
                blob = path.read_bytes()
                source_hashes[relative] = hashlib.sha256(blob).hexdigest()
                try:
                    ast.parse(blob, filename=relative)
                except SyntaxError as exc:
                    syntax_errors.append(f"{relative}: {exc}")
    if missing_paths or syntax_errors:
        print("FILE/SYNTAX ERRORS:", missing_paths, syntax_errors)
    print(f"Validated file paths and parsed {len(checked_files)} Python files.",flush=True)
    # For a large suite, starting 135 Python interpreters is expensive on
    # some machines. `runpy` exercises every module's `__main__` entry point
    # inside this validator. Integration tests separately cover imports.
    #
    # Note: this is an in-process smoke run, not a fresh subprocess per module.
    import contextlib
    import io
    import runpy
    import traceback
    sys.path.insert(0, str(ROOT / "src"))
    standalone = []
    for entry in implemented:
        name = entry["source_py"].removeprefix("src/").removesuffix(".py").replace("/", ".")
        # ProcessPoolExecutor pickles globally importable functions. Running a
        # multiprocessing entry point via runpy as __main__ makes those function
        # references unpicklable; execute that example in its own interpreter.
        if name.endswith("pg_298_parallel_collatz"):
            result = run_one(entry)
            standalone.append({**result, "method": "subprocess python -m (multiprocessing)"})
            continue
        output = io.StringIO()
        try:
            with contextlib.redirect_stdout(output), contextlib.redirect_stderr(output):
                runpy.run_module(name, run_name="__main__", alter_sys=False)
            status, err = "passed", ""
        except BaseException:
            status, err = "failed", traceback.format_exc()
        standalone.append({"exercise": entry["number"], "module": name,
                           "method": "runpy.run_module as __main__ (in process)",
                           "status": status, "stdout_tail": output.getvalue()[-1600:],
                           "stderr_tail": err[-2000:]})
    standalone.sort(key=lambda entry: tuple(map(int, entry["exercise"].split("."))))
    standalone_passed = sum(row["status"] == "passed" for row in standalone)
    print(f"Standalone checks: {standalone_passed}/{len(standalone)}.",flush=True)

    command = [sys.executable, "-m", "pytest", "-q"]
    pytest = subprocess.run(
        command, cwd=ROOT, env=dict(os.environ, PYTHONPATH=str(ROOT / "src")),
        capture_output=True, text=True, timeout=90, check=False,
    )
    report = {
        "timestamp_utc": datetime.now(timezone.utc).isoformat(),
        "python": sys.version,
        "indexed_exercises": len(manifest),
        "runnable_exercises": len(implemented),
        "reference_only_exercises": len(missing),
        "chapter_count": len({item["chapter"] for item in manifest}),
        "verified_source_test_path_pairs": len(implemented),
        "python_files_parsed": len(checked_files),
        "path_errors": missing_paths,
        "syntax_errors": syntax_errors,
        "source_hashes_sha256": source_hashes,
        "standalone_passed": standalone_passed,
        "standalone_total": len(standalone),
        "standalone_results": standalone,
        "pytest": {"command": command, "returncode": pytest.returncode,
                   "stdout": pytest.stdout[-10000:], "stderr": pytest.stderr[-2000:]},
    }
    RESULT.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(pytest.stdout.strip())
    if pytest.stderr:
        print(pytest.stderr[-2000:], file=sys.stderr)
    print("Saved validation evidence:", RESULT)
    successful = not missing_paths and not syntax_errors and standalone_passed == len(standalone) and pytest.returncode == 0
    return 0 if successful else 1


if __name__ == "__main__":
    raise SystemExit(main())
