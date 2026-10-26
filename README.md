**Verified continuation checkpoint:** [CONTINUATION_STATUS.md](CONTINUATION_STATUS.md) — 60 additional exercise files worked on; 1,005 passing pytest tests.


**Most recent verified changes:** [CONTINUATION_STATUS.md](CONTINUATION_STATUS.md) — 20 additional exercise files reviewed; 1,001 passing tests.

# Elements of Programming Interviews in Python — learning repository

This private-study repository converts the **user-supplied 2016/2017 EPI Python PDF** into a page-indexed study tree. The goal is to learn Python, its standard library, and professional development workflows while practicing the algorithms.

## Read this first: coverage and accuracy

**217 runnable exercises**, each with an independently executable `.py` module
and its own pytest file. **47 conceptual exercise references** remain as Markdown.
The previous 215 exercises have their OCR/extracted textbook excerpts
**embedded as commented text in the corresponding Python file** and its
redundant exercise Markdown file removed.

**Important**: OCR text is explicitly labeled UNVERIFIED in each program.
It may include damaged code, misread mathematical symbols, overlapping pages,
and incomplete discussions; treat it as an aid to the original PDF, not as a
certified transcription. Many executable implementations remain educational reconstructions; not every
alternative book implementation has been recovered. Six 20-exercise remediation batches (see `TEXTBOOK_REMEDIATION_CHECKPOINT.md` and `TEXTBOOK_REMEDIATION_CHECKPOINT2.md` through `TEXTBOOK_REMEDIATION_CHECKPOINT6.md`) have now improved 120 existing programs and recovered several PDF implementations not originally represented as executable code. These are **verified repair batches, not 120 new exercises**.
Consult [TEXTBOOK_FIDELITY_TODO.md](TEXTBOOK_FIDELITY_TODO.md) for items that
require manual verification against the original PDF.

The original book is **not bundled** in this archive; keep the PDF separately.
This repository is intended for private study only; attribution is in
`ATTRIBUTION.md`.

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
├── TEXTBOOK_FIDELITY_TODO.md
├── PYTHON_DEVELOPMENT_GUIDE.md
├── ADVANCED_PYTHON_DEVELOPMENT_GUIDE.md
├── pyproject.toml
├── .github/workflows/python-tests.yml
├── src/epi_python/
│   ├── chapter_04_primitive_types/
│   │   ├── pg-023-README.md   # PDF chapter introduction (unverified)
│   │   ├── pg_024_parity.py   # program plus embedded PDF excerpt
│   │   └── ...
│   ├── chapter_20_design_problems/
│   │   └── pg_*.md           # conceptual questions without Python code
│   └── ...
└── tests/chapter_04_primitive_types/
    └── test_pg_024_parity.py
```

## Find an exercise

See [EXERCISE_INDEX.md](EXERCISE_INDEX.md) for every chapter, exercise, and printed page number. Reference pages are **printed book pages**, not the PDF viewer's numbering. This PDF has 14 preliminary pages, so **printed page 164 is PDF page 178**.

## Documentation policy

Programs should have a program-level problem description and algorithm explanation, time/space complexity, official online documentation links directly above imports and API calls, a blank line before explanatory comments, standalone examples under `if __name__ == "__main__":`, and corresponding pytest tests. Preserve multiple complete implementations, when the book supplies them, and test each independently. Add any new tools/commands to the appropriate development guide.

## Validation and GitHub setup

Use `python -m pytest -v` to run the suite. Historical checkpoint counts in `VALIDATION.md` apply to the earlier repository snapshot; the current merged version has been re-tested without changing implementations. Read [VALIDATION.md](VALIDATION.md) for exact local test evidence and implementation limitations. Use [PRIVATE_GITHUB_SETUP.md](PRIVATE_GITHUB_SETUP.md) to put this repository in your own **private** GitHub repository.
