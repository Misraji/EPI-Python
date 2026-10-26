"""EPI exercise 5.17, printed page 60: The Sudoku checker problem.

EDUCATIONAL RECONSTRUCTION — not a verbatim verified code transcription.
Problem: The Sudoku checker problem.
Method/complexity: Check all rows/columns/square subgrids; O(n²) time and O(n²) keys for Counter alternative.
For the book's original explanation and variants, see:
    pg_060_exercise_05_17_the_sudoku_checker_problem.md

Run: python -m epi_python.chapter_05_arrays.pg_060_sudoku_checker
Test: python -m pytest tests/chapter_05_arrays/test_pg_060_sudoku_checker.py -v
"""

# collections.Counter is a mapping from values to occurrence counts.
# Documentation: https://docs.python.org/3/library/collections.html#collections.Counter
from collections import Counter

# math.isqrt returns the exact integer square root without rounding.
# Documentation: https://docs.python.org/3/library/math.html#math.isqrt
from math import isqrt


def is_valid_sudoku(grid: list[list[int]]) -> bool:
    """Check filled rows, columns, and square regions; zero means blank."""
    n = len(grid)
    region = isqrt(n)
    if not n or region * region != n or any(len(row) != n for row in grid):
        return False

    def no_duplicates(values):
        filled = [x for x in values if x != 0]
        return all(isinstance(x, int) and 1 <= x <= n for x in filled) and len(filled) == len(set(filled))

    for i in range(n):
        if not no_duplicates(grid[i]) or not no_duplicates([grid[j][i] for j in range(n)]):
            return False
    for start_r in range(0, n, region):
        for start_c in range(0, n, region):
            block = [grid[r][c] for r in range(start_r, start_r + region)
                     for c in range(start_c, start_c + region)]
            if not no_duplicates(block):
                return False
    return True


def is_valid_sudoku_pythonic(grid: list[list[int]]) -> bool:
    """Alternative solution counting row/column/region-value combinations."""
    n = len(grid)
    region = isqrt(n)
    if not n or region * region != n or any(len(row) != n for row in grid):
        return False
    keys = []
    for i, row in enumerate(grid):
        for j, digit in enumerate(row):
            if digit == 0:
                continue
            if not isinstance(digit, int) or not 1 <= digit <= n:
                return False
            keys.extend((('row', i, digit), ('column', j, digit),
                         ('region', i // region, j // region, digit)))

    # Counter(keys) records how often each constraint is used.
    # A count greater than one means the same digit appears twice in a region.
    return max(Counter(keys).values(), default=0) <= 1


if __name__ == "__main__":
    empty = [[0] * 9 for _ in range(9)]
    print("empty Sudoku valid:", is_valid_sudoku(empty))
    assert is_valid_sudoku(empty)
    assert is_valid_sudoku_pythonic(empty)
