# Advanced Python Development Guide

**Project:** Elements of Programming Interviews in Python — annotated learning repository  
**Audience:** A programmer who knows basic Python syntax, but is new to Python development tools  
**Status:** Optional reference. You do **not** need to master this material before solving EPI exercises.

This guide complements the beginner-oriented `PYTHON_DEVELOPMENT_GUIDE.md`. Its focus is **static type checking, timing, CPU profiling, and memory diagnostics**, especially for algorithm exercises and LeetCode-style problems.

> Commands in this guide assume the final repository uses `src/epi_python/` for the importable package and a root-level `tests/` directory. Run them **from the repository root**, after creating your virtual environment and installing the project in editable mode, as described in `PYTHON_DEVELOPMENT_GUIDE.md`.

## 1. Which tool should I use?

| Question | Tool | Included with Python? |
|---|---|---|
| Does the result match the expected answer? | `pytest` | No |
| Are function arguments and return types consistent? | `mypy` | No |
| Is one algorithm faster than another on comparable inputs? | `timeit` | **Yes** |
| Which functions consume the execution time? | `cProfile` and `pstats` | **Yes** |
| How much time does this one operation take? | `time.perf_counter()` | **Yes** |
| Where is Python-managed memory being allocated? | `tracemalloc` | **Yes** |

**Recommended sequence:** make the solution correct with tests; optionally check types; benchmark realistic inputs; profile **only when** investigating performance. Correctness comes before optimization.

## 2. Setup: optional advanced tooling

The complete repository should declare regular developer tools in `pyproject.toml`, with **mypy as an optional advanced dependency**, for example:

```toml
[project.optional-dependencies]
dev = ["pytest", "pytest-cov", "ruff"]
advanced = ["mypy"]
```

These are examples of configuration that the *future complete repository* should provide; do not assume an older sample ZIP already declares these extras.

```bash
# Install the project, normal development tools, and advanced tools.
python -m pip install -e ".[dev,advanced]"

# Check that the type checker is installed.
python -m mypy --version

# Show available options.
python -m mypy --help
```

If the advanced extra has not been configured yet, install mypy in the active virtual environment with `python -m pip install mypy`.

`-e` means *editable installation*: edits to `src/epi_python/` are reflected without reinstalling the package. `.[dev,advanced]` requests two named optional dependency groups declared by this project.

No separate installation is required for `timeit`, `cProfile`, `pstats`, `time`, or `tracemalloc`: they are part of the Python standard library.

## 3. Static type checking with mypy

### 3.1 Mental model

Python normally checks operations **at runtime**, while the program executes. A static type checker analyzes code **before execution** using type annotations. It can find mismatches without running the program, but it does not replace tests or prove that an algorithm is correct.

```python
# A type annotation says that this function expects a list of integers
# and returns an integer. Python itself does not enforce these hints.
def total(values: list[int]) -> int:
    return sum(values)

print(total([2, 3, 5]))  # Valid: prints 10.
print(total("hello"))    # Type mismatch: mypy can flag this call.
```

The last statement may also fail at runtime for this particular function. The important distinction is that **mypy can warn without executing it**.

### 3.2 Commands

```bash
# Check one annotated source file.
python -m mypy src/epi_python/chapter_12_hash_tables/pg_164_is_letter_constructible_from_magazine.py

# Check all implementation files recursively.
python -m mypy src/epi_python/

# Also analyze function bodies that do not have type annotations.
python -m mypy --check-untyped-defs src/epi_python/

# Stronger checking, useful for your own newly written, fully annotated code.
python -m mypy --strict path/to/my_new_algorithm.py
```

### 3.3 How to read results

A diagnostic usually includes `filename:line: error: message`. Go to that source line, compare the inferred type with the expected type, and decide whether the call, function signature, or type annotation is incorrect.

**Important for EPI:** the textbook contains many *unannotated* functions. By default, mypy checks relatively little inside unannotated functions. `--check-untyped-defs` inspects their bodies, but unannotated arguments are still effectively `Any`, so checks remain limited. We should **preserve original textbook signatures** unless there is a specific reason to change them; additional typing can be introduced separately and gradually.

**When to use it:** especially when learning `list[int]`, `dict[str, int]`, `T | None`, data classes, optional results, custom node types, and larger programs with many function calls.

Official reference: https://mypy.readthedocs.io/en/stable/getting_started.html  
CLI options: https://mypy.readthedocs.io/en/stable/command_line.html  
Python annotations: https://docs.python.org/3/library/typing.html

## 4. Performance timing with `timeit`

### 4.1 Mental model

A **benchmark** measures how long an operation takes. `timeit` runs a code fragment repeatedly and reports an execution time. This is often what you want when comparing two EPI solutions on the **same input**. It measures elapsed runtime, not algorithmic Big-O complexity.

`timeit` separates **setup** (imports and test-data creation) from the **operation being measured**. This avoids including setup work in each timed iteration.

### 4.2 Compare the two solutions from EPI page 164

The following commands assume the complete repository contains the page-164 module with the two functions from our example.

```bash
# Benchmark the explicit frequency-table implementation.
python -m timeit \
  -s "from epi_python.chapter_12_hash_tables.pg_164_is_letter_constructible_from_magazine import is_letter_constructible_from_magazine as solve; letter='a'*3000+'b'*3000; magazine='b'*3000+'a'*3000" \
  "solve(letter, magazine)"

# Benchmark the Counter-subtraction implementation using the SAME data.
python -m timeit \
  -s "from epi_python.chapter_12_hash_tables.pg_164_is_letter_constructible_from_magazine import is_letter_constructible_from_magazine_pythonic as solve; letter='a'*3000+'b'*3000; magazine='b'*3000+'a'*3000" \
  "solve(letter, magazine)"
```

- `python -m timeit` executes the standard-library timing module as a command-line program.
- `-s "..."` runs setup statements before the timed loops.
- The final quoted expression is the operation being timed.
- `timeit` automatically chooses a loop count unless you explicitly provide one.
- `-n 100` sets calls per repetition; `-r 5` sets the number of repetitions.
- Reported results depend on your computer and Python version: **the guide makes no speed claims for either implementation**.

For algorithm questions, repeat the comparison with small, medium, and large input sizes, and with best-/worst-case patterns if relevant. Ensure that each function receives a valid, equivalent input. If a function mutates its input, prepare a fresh input outside the timed section or explicitly account for copying costs.

Official reference: https://docs.python.org/3/library/timeit.html

### 4.3 Measure an operation inside Python

Use `time.perf_counter()` when a standalone script needs to measure a larger block of work:

```python
# Official documentation: https://docs.python.org/3/library/time.html#time.perf_counter
import time


def count_squares(n: int) -> int:
    return sum(i * i for i in range(n))


start = time.perf_counter()
result = count_squares(1_000_000)
elapsed_seconds = time.perf_counter() - start
print(f"result={result}, elapsed={elapsed_seconds:.6f} seconds")
```

`perf_counter()` gives a high-resolution performance clock. For tiny functions, prefer `timeit`, because a single measurement can be dominated by noise.

## 5. CPU profiling with `cProfile`

### 5.1 Mental model: timing versus profiling

- **Timing:** *How long did the program take?*
- **Profiling:** *Where did the program spend its time?*

`cProfile` records function calls and reports call counts and elapsed time. It is usually the first built-in tool to use after a benchmark reveals a performance problem.

### 5.2 Profile a standalone EPI module

```bash
# Profile execution of this program's __main__ demonstration code.
python -m cProfile -s cumulative \
  -m epi_python.chapter_12_hash_tables.pg_164_is_letter_constructible_from_magazine

# Save profiler data for later analysis instead of displaying it immediately.
python -m cProfile -o epi-example.prof \
  -m epi_python.chapter_12_hash_tables.pg_164_is_letter_constructible_from_magazine

# View a saved profile, sorted by cumulative time, showing 20 entries.
python -c "import pstats; pstats.Stats('epi-example.prof').sort_stats('cumulative').print_stats(20)"
```

`-m` is for an importable Python module, just as in `python -m epi_python...`. `-s cumulative` sorts the printed report by cumulative time. `-o` writes a machine-readable profile file; it does not print the normal sorted report at the same time.

**Critical limitation:** a small five-example `__main__` demonstration has too little work to give a meaningful performance profile. For serious investigation, make a separate profiling driver that calls the target algorithm many times on sufficiently large, representative inputs. Keep benchmark/profiling drivers separate from the canonical textbook solution.

### 5.3 How to interpret the report

| Column | Interpretation |
|---|---|
| `ncalls` | How many times the function was called |
| `tottime` | Time inside the function itself, excluding time in called functions |
| `cumtime` | Time inside the function **and** functions it called |
| `filename:lineno(function)` | Which function produced the statistics |

Start by sorting by **cumulative time** to find costly call chains. Sort by **internal time** (`-s time`) when investigating where execution actually occurs. Profilers add overhead: use them to locate hot spots, not as your definitive before-and-after speed measurement.

Official reference: https://docs.python.org/3/library/profile.html

## 6. Optional: inspect memory allocations with `tracemalloc`

Memory is particularly relevant when comparing an `O(1)`-extra-space approach to one that builds a large list, dictionary, or set.

```python
# Official documentation: https://docs.python.org/3/library/tracemalloc.html
import tracemalloc


tracemalloc.start()

# Replace this operation with the algorithm you want to inspect.
result = [i * i for i in range(100_000)]

current_bytes, peak_bytes = tracemalloc.get_traced_memory()
print(f"Current traced allocation: {current_bytes / 1024:.1f} KiB")
print(f"Peak traced allocation:    {peak_bytes / 1024:.1f} KiB")

tracemalloc.stop()
```

`tracemalloc` measures **traced Python memory allocations**, not total process memory. It adds overhead, so **do not enable it during timing benchmarks**. This section is optional, not a requirement for every EPI exercise.

Official reference: https://docs.python.org/3/library/tracemalloc.html

## 7. Useful command reference

The commands below assume the future, finalized `src/` package layout and an active virtual environment.

| Task | Command |
|---|---|
| Install optional tools | `python -m pip install -e ".[dev,advanced]"` |
| Check one exercise's types | `python -m mypy src/epi_python/chapter_12_hash_tables/pg_164_is_letter_constructible_from_magazine.py` |
| Check the package's types | `python -m mypy src/epi_python/` |
| Examine unannotated function bodies | `python -m mypy --check-untyped-defs src/epi_python/` |
| Time a small expression | `python -m timeit "sum(range(1000))"` |
| Profile one exercise's `__main__` | `python -m cProfile -s cumulative -m epi_python.chapter_12_hash_tables.pg_164_is_letter_constructible_from_magazine` |
| Save profile data | `python -m cProfile -o epi-example.prof -m epi_python.chapter_12_hash_tables.pg_164_is_letter_constructible_from_magazine` |
| Read saved profile data | `python -c "import pstats; pstats.Stats('epi-example.prof').sort_stats('cumulative').print_stats(20)"` |

Add `*.prof` and any other generated performance output to `.gitignore` in the full repository. Performance evidence is environment-dependent; don't put arbitrary benchmark results into the source repository as if they were portable facts.

## 8. Suggested learning order for an EPI exercise

1. **Understand** the question, examples, and algorithm.
2. **Run** the solution file's built-in examples.
3. **Test** the solution with its dedicated pytest module.
4. **Experiment** with changed inputs and edge cases.
5. **Optionally type-check** your own annotated implementation.
6. **Benchmark** alternate correct implementations on comparable test data.
7. **Profile** only when a timing result merits investigation.
8. **Explain** what you learned: complexity, Python API use, and any measured bottleneck.

There is no expectation to perform steps 5–7 for every EPI program. They become valuable when comparing implementations, solving time-limit-exceeded problems, or debugging a real performance issue.

## 9. Reference documentation

- Static typing: https://docs.python.org/3/library/typing.html
- Mypy: https://mypy.readthedocs.io/en/stable/
- Timing: https://docs.python.org/3/library/timeit.html
- Performance clock: https://docs.python.org/3/library/time.html#time.perf_counter
- CPU profiling: https://docs.python.org/3/library/profile.html
- Memory allocation tracing: https://docs.python.org/3/library/tracemalloc.html
- Python packaging and `pyproject.toml`: https://packaging.python.org/en/latest/guides/writing-pyproject-toml/
