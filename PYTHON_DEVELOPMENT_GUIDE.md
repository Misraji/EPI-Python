# Python Development Guide — From Basics to Professional Workflow

**Audience:** You know the basics of Python from the official Python tutorial, but may have never set up a professional Python project. This guide intentionally explains unfamiliar tools, syntax, and options instead of assuming you have used them before.

**Learning approach:** Follow the commands on a real EPI exercise, make a small change, run its examples, and inspect its tests. When something fails, learn to read the error before changing anything.

All terminal commands below run from the repository root (`epi-python/`) unless noted otherwise. A command beginning with `python -m` runs a module using your selected Python interpreter.

## 1. Mental model: a Python project

A Python **module** is normally a `.py` file. A **package** is a collection of modules that can be imported together. In this project, `epi_python` is an importable package with subpackages organized by textbook chapter.

```text
epi-python/                            Git repository root
├── pyproject.toml                     project metadata and tool configuration
├── src/epi_python/                    actual importable Python package
│   ├── __init__.py                    identifies the regular package
│   └── chapter_12_hash_tables/
│       ├── __init__.py
│       ├── pg-159-README.md           chapter introduction (unverified PDF text)
│       └── pg_164_is_letter_constructible_from_magazine.py
└── tests/                              root-level automated tests
    └── chapter_12_hash_tables/
        └── test_pg_164_is_letter_constructible_from_magazine.py
```

The top-level directory is deliberately spelled `src/`, a common convention for packages. Python is asked to import from the installed package `epi_python`, *not* from `src` itself. `__init__.py` is a normal Python module used to identify the containing directory as a package; a minimal one can be empty.

**Official references:** https://packaging.python.org/en/latest/discussions/src-layout-vs-flat-layout/ and https://docs.python.org/3/tutorial/modules.html#packages

## 2. Which Python interpreter am I using?

```bash
python --version
python -c "import sys; print(sys.executable)"
```

`-c` runs the Python expression you supply. `sys.executable` prints the path of the Python interpreter currently running. This is useful when a tool appears to have been installed in the wrong environment.

In some systems the command is `python3` rather than `python`. Use the command that resolves to your intended Python 3.11+ interpreter.

**Reference:** https://docs.python.org/3/using/cmdline.html

## 3. Virtual environments: `venv`

**Problem:** Two Python projects might require different versions of pytest or another library. Installing everything globally makes projects interfere with each other.

**Solution:** Give each project its own *virtual environment*: a directory containing an isolated Python interpreter and installed third-party libraries.

```bash
# macOS and Linux: make the virtual environment.
python3 -m venv .venv

# Activate it for this shell session.
source .venv/bin/activate

# Confirm that Python points into this project's .venv folder.
python -c "import sys; print(sys.executable)"

# When finished working for the day:
deactivate
```

On Windows PowerShell:

```powershell
py -m venv .venv
.venv\Scripts\Activate.ps1
python --version
```

`-m venv` means "run Python's standard-library module named `venv`". Activation temporarily changes the shell's command-search path so `python` and `pip` point into the new environment. The `.gitignore` file excludes `.venv/`; don't commit a machine-specific virtual environment.

**Reference:** https://docs.python.org/3/library/venv.html

## 4. pip, PyPI, and dependencies

- **PyPI** is the Python Package Index: a public catalog of downloadable Python packages.
- **pip** is the standard package installer.
- A **dependency** is a package this project needs to work.
- A **development dependency** is a tool needed to work on the source or tests, but not necessarily to run the actual algorithms.

```bash
# Upgrade the package installer in your active environment.
python -m pip install --upgrade pip

# Install THIS package together with its optional developer tools.
python -m pip install -e ".[dev]"

# Show installed packages.
python -m pip list

# Show information about pytest and its installed location.
python -m pip show pytest
```

In `".[dev]"`, the `.` means *the current directory* and `[dev]` selects the optional dependency group defined in `pyproject.toml`. `-e` means *editable*: code changes to this project's `src/` package are picked up immediately without having to reinstall it.

The commands use `python -m pip` instead of `pip` so the package is installed into the environment associated with the **same Python interpreter** used to run the project.

**References:** https://pip.pypa.io/en/stable/ and https://packaging.python.org/en/latest/tutorials/installing-packages/

## 5. What is `pyproject.toml`?

It's the project's standardized **configuration and metadata** file. It tells build/install tools the package's name, version, Python requirement and dependencies. It also supplies settings for tools such as pytest and Ruff.

`.toml` is a plain-text configuration format with sections and key/value pairs:

```toml
[project]
name = "epi-python"
version = "0.1.0"
requires-python = ">=3.11"

[project.optional-dependencies]
dev = ["pytest>=8", "pytest-cov>=5", "ruff>=0.6"]
advanced = ["mypy>=1.10"]

[tool.pytest.ini_options]
testpaths = ["tests"]

[tool.ruff]
line-length = 88
```

`[project]` is standardized packaging metadata. `[tool.pytest.ini_options]` is read by pytest. `[tool.ruff]` is read by Ruff. **TOML is not Python**; Python does not execute this file as code.

We use setuptools as the package build backend, configured in `[build-system]` and `[tool.setuptools.packages.find]`. Most EPI programs use only the Python standard library; pytest and Ruff are tools used *while developing*.

**References:** https://packaging.python.org/en/latest/guides/writing-pyproject-toml/ and https://toml.io/en/

## 6. Imports and `python -m`

An ordinary Python import looks like:

```python
from epi_python.chapter_12_hash_tables.pg_164_is_letter_constructible_from_magazine import (
    is_letter_constructible_from_magazine,
)
```

Read the dotted path from left to right: package, chapter subpackage, source module, then symbol (function). Editable installation makes it importable no matter which EPI file the tests live in.

Run a standalone exercise:

```bash
python -m epi_python.chapter_12_hash_tables.pg_164_is_letter_constructible_from_magazine
```

`python -m package.module` asks Python to **locate that importable module and execute it as a script**. Don't append `.py` to a dotted module name. This avoids path hacks, and works with the repository's `src/` layout after editable installation.

Every reviewed exercise includes:

```python
if __name__ == "__main__":
    # Executed when you run the module, not when another module imports it.
    ...
```

The `...` above is illustrative syntax, not a runnable example for your own module.

**References:** https://docs.python.org/3/tutorial/modules.html and https://docs.python.org/3/library/__main__.html

## 7. Unit testing with pytest

A **unit test** checks a small piece of behavior with specified inputs and expected outputs. pytest is a very popular third-party Python testing framework.

```bash
# All tests:
python -m pytest -v

# One chapter:
python -m pytest tests/chapter_12_hash_tables/ -v

# One algorithm's test module:
python -m pytest tests/chapter_12_hash_tables/test_pg_164_is_letter_constructible_from_magazine.py -v

# Discover tests without running them:
python -m pytest --collect-only -q
```

pytest automatically discovers files named `test_*.py` and functions named `test_*`. It runs the test function and treats failed `assert` expressions as test failures. `-v` means *verbose*: display each test's name. `-q` means *quiet*.

### Parameterized tests

Rather than duplicating a test function ten times, pytest can call one function with a table of test cases:

```python
import pytest

@pytest.mark.parametrize(
    ("number", "expected"),
    [(0, 0), (1, 1), (3, 0), (7, 1)],
)
def test_parity(number, expected):
    assert parity(number) == expected
```

The decorator instructs pytest to generate four test instances; the example above assumes you've imported `parity`. Our actual tests include full imports.

### Fixtures

A **fixture** sets up reusable test data or resources, and pytest injects it into tests by matching the fixture function's name:

```python
import pytest

@pytest.fixture
def sorted_numbers():
    return [1, 2, 2, 3, 5]

def test_last(sorted_numbers):
    assert sorted_numbers[-1] == 5
```

Fixtures are common in production Python, though our simple algorithms often don't need them.

**Reference:** https://docs.pytest.org/en/stable/getting-started.html and https://docs.pytest.org/en/stable/how-to/parametrize.html

## 8. Troubleshooting test failures

```bash
python -m pytest -x -v                       # stop after first failure
python -m pytest -k "palindrome" -v         # select test names containing text
python -m pytest -s -v                       # show print() output
python -m pytest --tb=short                  # shorter Python traceback
```

A **traceback** displays the call stack leading to an exception. Read the last error line first (exception type and message), then the indicated source filename and line number.

Distinguish a **test assertion failure** (program ran but output was wrong) from an **import/collection error** (Python couldn't import or parse the file) and a **runtime exception** (e.g. `IndexError` or `KeyError`).

**Reference:** https://docs.pytest.org/en/stable/how-to/output.html

## 9. Code coverage

Test coverage answers **which lines executed during the test suite**, not whether the results are correct. Use it to notice unused branches and overlooked error cases.

```bash
python -m pytest --cov=epi_python --cov-report=term-missing
python -m pytest --cov=epi_python --cov-report=html
```

The HTML report is written under `htmlcov/` and can be opened in a browser. Both pytest coverage commands require the installed `pytest-cov` package, declared in the `dev` extra. You do not need to chase 100% coverage at the expense of useful tests; include expected outputs, edge cases, and independent comparisons where feasible.

**Reference:** https://pytest-cov.readthedocs.io/en/latest/

## 10. Formatting and linting: Ruff vs Black

- **Formatting** changes whitespace, quote style, line breaks and other *appearance* details, while preserving intended behavior.
- **Linting** detects suspicious code, unused imports, certain bugs, and maintainability problems. It can suggest repairs.
- **Ruff** provides both a formatter and a linter, so we don't need Black as a separate dependency here.
- **Black** is another common formatter. Learn what it is, but the repository uses Ruff for both checks.

```bash
# Check suspicious patterns without changing files:
python -m ruff check .

# Show what formatting is needed WITHOUT rewriting files:
python -m ruff format --check .

# Format a SINGLE source module:
python -m ruff format src/epi_python/chapter_04_primitive_types/pg_024_parity.py

# Format everything (makes changes to your working tree):
python -m ruff format .

# See suggested automated fixes without applying them:
python -m ruff check --diff .
```

**Learning note:** Formatting is not the same as teaching. Don't let automation erase useful explanation paragraphs or make the textbook algorithm less recognizable. Check `git diff` before committing automatic changes.

**References:** https://docs.astral.sh/ruff/ and https://black.readthedocs.io/en/stable/

## 11. Debugging: `breakpoint()`, `pdb`, tracebacks

To stop at a particular location inside a Python function, temporarily insert:

```python
breakpoint()
```

Python enters the standard-library debugger, `pdb`. Useful interactive debugger commands include:

| Command | Meaning |
|---|---|
| `n` | Run the next line, without stepping into called functions |
| `s` | Step into a called Python function |
| `p variable` | Evaluate/print an expression or variable |
| `l` | Show surrounding source lines |
| `c` | Continue running to the next breakpoint |
| `q` | Quit the debugger |

You can also run a Python module inside pdb:

```bash
python -m pdb -m epi_python.chapter_04_primitive_types.pg_024_parity
```

For pytest failures you can ask pytest to enter pdb:

```bash
python -m pytest --pdb -x tests/chapter_04_primitive_types/
```

**Reference:** https://docs.python.org/3/library/pdb.html

## 12. Logs versus `print()`

`print()` is excellent for your first exploratory runs. Python's `logging` module is useful when programs become larger and you need configurable diagnostics.

```python
# Standard-library logging documentation:
# https://docs.python.org/3/library/logging.html
import logging

logging.basicConfig(level=logging.INFO)
logging.info("Starting algorithm")
```

Logging lets you distinguish debug, info, warning, error, and critical messages. We don't require it for a small EPI solution.

## 13. Docstrings, type hints, and `help()`

A function's first string literal is a **docstring**. `help(function)` displays documentation in Python's help system; your editor may show it in tooltips.

```python
def square(x: int) -> int:
    """Return the square of the supplied integer."""
    return x * x

help(square)
```

Here `x: int` is a **type annotation** (expected argument type), and `-> int` states the intended return type. Python doesn't enforce annotations automatically. Optional type-checking tools such as `mypy` analyze them; see the advanced guide.

**References:** https://peps.python.org/pep-0257/ and https://docs.python.org/3/library/typing.html

## 14. Git and GitHub workflow

- **Git** records versions of your files in a local repository.
- **GitHub** can host your private Git repository and run automated tests through GitHub Actions.
- **`.gitignore`** prevents caches, `.venv`, temporary logs and other generated files from being accidentally tracked.
- **`git diff`** shows what changed since the previous committed version.

```bash
# If this is a fresh downloaded directory, initialize local version control:
git init

git status
git add README.md src tests pyproject.toml
# Or add all tracked-eligible project files:
git add .

git diff --cached

git commit -m "Initialize EPI Python study repository"
```

Create your private remote repository on GitHub, follow the URL and branch instructions GitHub provides, and only then push. A `git push` doesn't automatically create a new private repository on GitHub.

The `.github/workflows/python-tests.yml` workflow installs the project and runs pytest on each push and pull request. This is **CI (continuous integration)**: a remote check that changes still pass automated tests. The remote run will only exist once the files have been pushed to GitHub.

**References:** https://git-scm.com/docs and https://docs.github.com/en/actions

## 15. A complete exercise development cycle

1. Open [`EXERCISE_INDEX.md`](EXERCISE_INDEX.md); pick a chapter and textbook page.
2. Read the original chapter introduction and exercise reference Markdown. If the PDF extraction looks corrupted, consult your original PDF.
3. For an implemented exercise, read the module's question, algorithm explanation, imports, and explanatory API comments.
4. Activate `.venv` and use `python -m epi_python.chapter_...pg_...` to run the self-contained examples.
5. Run the matching pytest test file with `python -m pytest tests/.../test_...py -v`.
6. Deliberately change a return value, observe a failing assertion, then restore correct behavior.
7. Use `breakpoint()` and inspect local variables if you cannot understand a failure.
8. Check with `python -m ruff check .` and `python -m ruff format --check .`.
9. Inspect your changes with `git diff`, then commit when tests pass.
10. Observe your GitHub Actions run after you push to your private repository.

### What should I learn next?

First finish enough exercises that all of this feels routine. Later explore `ADVANCED_PYTHON_DEVELOPMENT_GUIDE.md` for optional **mypy static type checking, timeit benchmarking, cProfile function profiling, and tracemalloc memory diagnostics**.

The goal is not to memorize dozens of tools. It's to make a small professional loop—**code → run → test → debug → format → commit**—feel natural.
