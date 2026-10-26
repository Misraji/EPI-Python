# Elements of Programming Interviews in Python — learning repository

This private-study repository converts the **user-supplied 2016/2017 EPI Python PDF** into a page-indexed study tree. The goal is to learn Python, its standard library, and professional development workflows while practicing the algorithms.

## Read this first: coverage and accuracy

The PDF's text layer is visibly damaged, including within Python snippets. **Do not assume an extracted text block is valid Python or a faithful transcription.** For this reason the repository deliberately separates:

1. **Reference transcriptions:** every table-of-contents exercise has a page-numbered Markdown transcript and every chapter has a page-numbered introduction, marked as **unverified PDF text**. Code, formulae, and diagrams may be corrupted or lost. Overlapping exercises on the same page may share text.
2. **Runnable learning examples:** only individually reviewed, executable Python implementations have `.py` files, standalone demos, and pytest tests. Unless explicitly stated, these are **educational reconstructions**, not verified verbatim textbook code. They retain the same exercise's core algorithmic objective.
3. **Conceptual questions:** kept as Markdown, not given speculative runnable programs.

**Checkpoint status: 215 executable exercises; 968 passing tests; 0 programming exercises remaining; 49 conceptual.** This is **not yet a finished, fully validated conversion of every textbook solution**. Check `PROGRESS.md` and `exercise_manifest.json` for exact coverage. No placeholder modules masquerade as completed solutions; missing files mean unimplemented exercises.

The original book is **not bundled** in this GitHub archive; keep your legally obtained PDF separately. The extracted text in this repository is intended for the owner's private study only; attribution is in `ATTRIBUTION.md`.

## Quick start (macOS/Linux)

```bash
# At repository root:
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"

# Run one runnable exercise and see its built-in demonstrations:
python -m epi_python.chapter_12_hash_tables.pg_164_is_letter_constructible_from_magazine

# Run just the tests for that exercise:
python -m pytest tests/chapter_12_hash_tables/test_pg_164_is_letter_constructible_from_magazine.py -v

# Run a chapter, or the entire suite:
python -m pytest tests/chapter_12_hash_tables/ -v
python -m pytest -v
```

Windows PowerShell activation: `.venv\Scripts\Activate.ps1` (after `py -m venv .venv`).

## Development tools

```bash
python -m ruff check .              # lint
python -m ruff format --check .    # check formatting (no changes)
python -m ruff format .            # format in place
python -m pytest --cov=epi_python --cov-report=term-missing
```

For the **why**, not just the commands, read [PYTHON_DEVELOPMENT_GUIDE.md](PYTHON_DEVELOPMENT_GUIDE.md). For optional static types, timing, and profiling, see [ADVANCED_PYTHON_DEVELOPMENT_GUIDE.md](ADVANCED_PYTHON_DEVELOPMENT_GUIDE.md).

## Repository layout

```text
epi-python/
├── README.md
├── PROGRESS.md
├── PYTHON_DEVELOPMENT_GUIDE.md
├── ADVANCED_PYTHON_DEVELOPMENT_GUIDE.md
├── pyproject.toml
├── .github/workflows/python-tests.yml
├── src/epi_python/
│   ├── chapter_04_primitive_types/
│   │   ├── pg-023-README.md                # OCR-text chapter introduction
│   │   ├── pg_024_exercise_04_01_....md   # OCR-text exercise reference
│   │   └── pg_024_parity.py               # runnable when verified
│   └── ...
└── tests/chapter_04_primitive_types/
    └── test_pg_024_parity.py
```

Both directory and `.py` filenames follow Python-compatible `snake_case`. Markdown chapter introduction filenames intentionally retain the requested `pg-NNN-README.md` convention. Program names were adapted from the exercise's function in the Python code when reconstructed; the manifest lists the exact files available.

## Find an exercise

See [EXERCISE_INDEX.md](EXERCISE_INDEX.md) for every chapter, exercise, and printed page number. Reference pages are **printed book pages**, not the PDF viewer's numbering. This PDF has 14 preliminary pages, so **printed page 164 is PDF page 178**.

## Documentation policy

New verified implementations should have a program-level problem description and algorithm explanation, time/space complexity, official online documentation links directly above imports and API calls, a blank line before explanatory comments, standalone examples under `if __name__ == "__main__":`, and corresponding pytest tests. Preserve multiple complete implementations, when the book supplies them, and test each independently. Add any new tools/commands to the appropriate development guide.

## Validation and GitHub setup

Run `python scripts/validate_repository.py` to reproduce the current checkpoint and save its source hashes and test evidence. Read [VALIDATION.md](VALIDATION.md) for exact local test evidence and implementation limitations. Use [PRIVATE_GITHUB_SETUP.md](PRIVATE_GITHUB_SETUP.md) to put this repository in your own **private** GitHub repository.
