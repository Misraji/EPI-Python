# Local validation report

This report describes checks **actually executed** on the generated repository, not intended future tests.

## Results

- **Indexed EPI exercises:** 264
- **Chapter packages:** 24 (`src/epi_python/chapter_*`)
- **PDF-text reference exercise documents:** 264 (OCR text, **not** verified verbatim)
- **Chapter introduction documents:** 24 (OCR text, **not** verified verbatim)
- **Compiled Python exercise modules:** 72
- **Matching exercise test modules:** 72 (plus a separate independent-property-test module)
- **pytest:** **356 passed**, no failures
- **Standalone `python -m ...` entry-point smoke runs:** **72 passed / 72 checked**, no failures or timeouts. See `standalone_validation.json` for per-program command/exit evidence.
- **Python syntax:** `python -m compileall -q src/epi_python tests` succeeded.
- **pytest with pytest-cov:** 356 passed; 51% overall statement coverage across the package. The `if __name__ == "__main__"` demonstrations are deliberately not exercised by pytest imports, which lowers that aggregate figure.

## Reproduce the checks

```bash
python -m pip install -e ".[dev]"
python -m compileall -q src/epi_python tests
python -m pytest -v
python -m pytest --cov=epi_python --cov-report=term-missing
```

## What this does *not* prove

- Not every textbook exercise has runnable code. **192 exercises remain reference-only.** `exercise_manifest.json` and `EXERCISE_INDEX.md` identify them.
- OCR transcriptions remain error-prone and have not been visually corrected against every page of the original PDF.
- Most executable programs are independently reconstructed learning solutions, not verified line-by-line reproductions of the author's printed source. Only exercise 12.2 preserves its two earlier reviewed implementations from the supplied example.
- A green pytest suite does not prove full correctness for every possible input, nor that every possible algorithm variant has been implemented.
- The Ruff CLI and mypy CLI were not available in the local build environment, so **no Ruff format/lint pass or mypy type-check pass is claimed**. Run them after installing the project with the declared developer and advanced extras.
- No GitHub Actions run is claimed before you push this archive to your repository.

## Progression towards complete conversion

For each reference-only exercise, manually review its printed source and explanations against the actual PDF page image, transcribe and comment all complete algorithms, write standalone examples and pytest tests, and then update the `source_py`, `test_py`, and `status` fields in `exercise_manifest.json`. Validate that new module before marking it complete.
