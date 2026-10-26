"""EPI Python — Exercise 15.9: Implement a Sudoku Solver

Chapter 15: Recursion
Textbook: pages 230–232 (printed page numbers; problem and solution start on 230).

PROBLEM (from the textbook)
---------------------------
"Implement a Sudoku solver. See Problem 5.17 on Page 60 for a definition of
Sudoku."
(Problem 5.17: a 9 x 9 grid, divided into nine 3 x 3 subgrids, must be
filled with digits 1-9 so that no row, column or subgrid contains a digit
twice; some entries are given in advance.)

HINT (from the textbook)
------------------------
"Apply the constraints to speed up a brute-force algorithm."

SOLUTION DEVELOPMENT (following the textbook)
---------------------------------------------
Brute force: try every possible assignment to the empty entries, and check
each complete assignment for validity with Solution 5.17 (page 60). This is
wasteful: if an early choice already breaks a constraint, there is no point
in continuing with it.

Backtracking: visit the 2D array entries one at a time. For an empty entry,
try each value; if the updated array is still valid, recurse; otherwise try
the next value. When every entry has been filled the search succeeds.

Checking validity by calling Solution 5.17 on the whole grid would work,
but it is much faster to use the fact that the array satisfied the
constraints BEFORE the new value was added: only the row, column and
subgrid of the newly added entry need checking.

Example from the book: start at the lower-left entry of the configuration
in Figure 5.2(a) on page 60. Putting a 1 there breaks no row, column or
subgrid constraint, so move on to the next entry in that row. A 1 cannot go
there (the row would contain two 1s), but a 2 is acceptable.

The book's program solve_sudoku(partial_assignment) has a nested
solve_partial_sudoku(i, j), which itself contains a nested
valid_to_add(i, j, val); a module-style constant EMPTY_ENTRY = 0 marks
empty cells. This file implements the same backtracking search (see
TEXTBOOK CODE COMPARISON for the differences).

ADDITIONAL EXAMPLES (added for learning; not printed in this exercise)
---------------------------------------------------------------------
A 4 x 4 Sudoku (2 x 2 subgrids), 0 = empty:
    [[1, 0, 0, 4],          solved in place to
     [0, 4, 1, 0],          a valid completed grid;
     [0, 1, 4, 0],          solve_sudoku returns True.
     [4, 0, 0, 1]]
"""

# Python standard library: iterator building blocks.
# Module documentation: https://docs.python.org/3/library/itertools.html
# itertools.product API: https://docs.python.org/3/library/itertools.html#itertools.product
import itertools

# Python standard library: mathematical functions.
# Module documentation: https://docs.python.org/3/library/math.html
# math.isqrt API: https://docs.python.org/3/library/math.html#math.isqrt
import math


def solve_sudoku(partial_assignment: list[list[int]]) -> bool:
    """Fill the grid in place by backtracking; return whether it succeeded.

    This is the textbook's Sudoku solver (solve_sudoku with nested
    solve_partial_sudoku and valid_to_add). Empty entries are 0. On success
    the grid is completely filled; on failure every cell the search filled
    has been reset to 0. Unlike the book, the size is validated first.
    """

    # The book's EMPTY_ENTRY constant, here a local variable.
    empty_entry = 0
    n = len(partial_assignment)

    # math.isqrt(n) returns the exact integer square root (the largest int
    # r with r*r <= n), computed with integer arithmetic, so there is no
    # floating-point rounding. For a 9 x 9 grid it gives 3, the width of a
    # subgrid. (The book uses int(math.sqrt(...)) instead.)
    # Documentation: https://docs.python.org/3/library/math.html#math.isqrt
    region_size = math.isqrt(n)

    # Input check (not in the book): the grid must be nonempty, n must be a
    # perfect square, and every row must have n entries. `any(...)` returns
    # True as soon as one generated value is true. `raise ValueError(...)`
    # stops the function with an exception describing the bad argument.
    if not n or region_size * region_size != n or any(len(row) != n for row in partial_assignment):
        raise ValueError('Sudoku must be a nonempty square with square subregions')

    # Nested helper: can `value` be placed at row i, column j without
    # breaking a constraint? Only the affected column, row and subgrid are
    # examined, because the grid was valid before this placement.
    def valid_to_add(i: int, j: int, value: int) -> bool:

        # Column constraint: does `value` already appear in column j?
        # (The book labels this check "Check row constraints.")
        if any(value == partial_assignment[k][j] for k in range(n)):
            return False

        # Row constraint: `x in some_list` scans the list for x.
        # (The book labels this check "Check column constraints.")
        if value in partial_assignment[i]:
            return False

        # Region (subgrid) constraint. `//` is floor division, so
        # (region_i, region_j) identifies which subgrid holds (i, j); its
        # top-left corner is (region_size * region_i, region_size * region_j).
        region_i, region_j = i // region_size, j // region_size

        # itertools.product(range(r), repeat=2) lazily yields every pair
        # (a, b) with 0 <= a, b < r — the same pairs as two nested for
        # loops, i.e. every (row, column) offset inside the subgrid.
        # Generating them lazily avoids building a list of offsets.
        # `not any(...)` is True when no cell of the subgrid equals `value`.
        # Documentation: https://docs.python.org/3/library/itertools.html#itertools.product
        return not any(value == partial_assignment[region_size * region_i + a]
                           [region_size * region_j + b]
                       for a, b in itertools.product(range(region_size), repeat=2))

    # Nested recursive search starting at entry (i, j). It advances i first,
    # so it walks down column j and then moves to the next column.
    def solve_partial_sudoku(i: int, j: int) -> bool:

        # Past the last row: start again at row 0 of the next column. If
        # that was the last column, the entire grid has been filled without
        # conflict. `i, j = 0, j + 1` assigns both names at once (tuple
        # unpacking; the right side is evaluated first).
        if i == n:
            i, j = 0, j + 1
            if j == n:
                return True

        # Skip nonempty (given or already filled) entries.
        if partial_assignment[i][j] != empty_entry:
            return solve_partial_sudoku(i + 1, j)

        # Try each value 1..n. Checking only the constraints touched by
        # (i, j) BEFORE placing the value is much faster than placing it and
        # rechecking the whole grid.
        for value in range(1, n + 1):
            if valid_to_add(i, j, value):
                partial_assignment[i][j] = value
                if solve_partial_sudoku(i + 1, j):
                    return True

                # Undo the assignment (backtrack) and try the next value.
                partial_assignment[i][j] = empty_entry
        return False

    return solve_partial_sudoku(0, 0)


# TEXTBOOK POST-SOLUTION DISCUSSION (page 232)
# --------------------------------------------
# The program is specialized to 9 x 9 grids, so it makes no sense to talk
# about its time complexity: there is no size parameter that grows.
# However, solving Sudoku generalized to n x n grids is NP-complete, so it
# should not be hard to show that this algorithm, generalized to n x n
# grids, takes exponential time.
#
# VARIANTS
# --------
# The book states no variants for this exercise.


# TEXTBOOK CODE COMPARISON
# ------------------------
# * Structure: book nests `valid_to_add(i, j, val)` INSIDE
#   `solve_partial_sudoku(i, j)`; file defines `valid_to_add(i, j, value)`
#   and `solve_partial_sudoku` side by side inside `solve_sudoku`.
#   Parameter `val` -> `value`. Type hints added.
# * Book constant `EMPTY_ENTRY = 0` (assigned just before the initial call);
#   file local variable `empty_entry = 0` at the top.
# * Book computes `region_size = int(math.sqrt(len(partial_assignment)))`
#   inside every valid_to_add call, with `I`, `J` for the region indices;
#   file computes `region_size = math.isqrt(n)` once, with `region_i`,
#   `region_j`. File uses `n` where the book uses
#   `len(partial_assignment)` / `len(partial_assignment[i])`.
# * File adds an input check raising ValueError (not in the book).
# * Book's comments "Check row constraints." / "Check column constraints."
#   sit above the column and row checks respectively (labels swapped in the
#   book); the comments above describe what each check really does.
# * Search order, the check-before-place idea and the undo step match.


# Python executes this block only when this source file is run directly.
# When pytest imports the file, this block is skipped automatically.
# Documentation: https://docs.python.org/3/library/__main__.html
if __name__ == '__main__':

    # Added example: a small 4 x 4 Sudoku with 2 x 2 subgrids (0 = empty).
    # solve_sudoku fills `sample` in place and returns True on success.
    # `assert` stops the program with an AssertionError if the condition is
    # false; this is a quick smoke check, the pytest suite is thorough.
    sample = [[1, 0, 0, 4], [0, 4, 1, 0], [0, 1, 4, 0], [4, 0, 0, 1]]
    assert solve_sudoku(sample)
    print('Solved 4x4 Sudoku:', sample)
