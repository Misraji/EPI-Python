"""EPI Python — Exercise 5.17: The Sudoku Checker Problem

Chapter 5: Arrays
Textbook: pages 60–61 (printed page numbers; problem, figure, hint and
start of the solution on page 60; both programs and the complexity
analysis on page 61).

PROBLEM (from the textbook)
---------------------------
Section context ("Multidimensional arrays", page 60): so far the chapter
has dealt with one-dimensional arrays. A 2D array is an array whose
entries are themselves arrays, and the idea extends naturally to k
dimensions. Such arrays arise in image processing, board games, graphs,
modeling spatial phenomena, and more. Often (not always) all the inner
arrays of a 2D array A have the same length; A is then an m x n
rectangular array (or simply an n x n array), m being the number of
entries of A and n the number of entries of A[0]. Elements are usually
referred to by row index i and column index j, written A[i][j].

Problem context: "Sudoku is a popular logic-based combinatorial number
placement puzzle. The objective is to fill a 9 x 9 grid with digits
subject to the constraint that each column, each row, and each of the nine
3 x 3 sub-grids that compose the grid contains unique integers in [1,9].
The grid is initialized with a partial assignment as shown in Figure
5.2(a); a complete solution is shown in Figure 5.2(b)."
(Figure 5.2 shows (a) a partially filled 9 x 9 grid and (b) its complete
solution.)

"Check whether a 9 x 9 2D array representing a partially completed Sudoku
is valid. Specifically, check that no row, column, or 3 x 3 2D subarray
contains duplicates. A 0-value in the 2D array indicates that entry is
blank; every other entry is in [1,9]."

HINT (from the textbook)
------------------------
"Directly test the constraints. Use an array to encode sets."

SOLUTION DEVELOPMENT (following the textbook)
---------------------------------------------
There is no real room for algorithmic optimization here; the problem is
about writing clean code.

Nine row constraints, nine column constraints and nine sub-grid
constraints must be checked. Bit arrays are a convenient way to detect a
violation, i.e. to make sure no number in [1, 9] appears more than once
in a unit.

The book prints two programs:
  1. `is_valid_sudoku(partial_assignment)`: a helper `has_duplicate`
     drops the zeros from a block and compares its length with the size
     of its set; it is applied to every row and column, then to every
     region. Implemented here as `is_valid_sudoku`.
  2. A "Pythonic solution that exploits the power of list comprehension"
     (book comment): build one key per (row, digit), (column, digit) and
     (region, digit) for every filled cell, count the keys with
     collections.Counter, and require that no key occurs more than once.
     Implemented here as `is_valid_sudoku_pythonic`.

ADDITIONAL EXAMPLES (added for learning; not printed in this exercise)
---------------------------------------------------------------------
    A 9 x 9 grid of zeros (completely blank) -> valid (True).
"""



# Python standard library: specialized container types.
# Module documentation: https://docs.python.org/3/library/collections.html
# Counter API: https://docs.python.org/3/library/collections.html#collections.Counter
# `from module import name` binds just that name, so the code can write
# `Counter(...)` instead of `collections.Counter(...)`.
from collections import Counter

# Python standard library: mathematical functions.
# Module documentation: https://docs.python.org/3/library/math.html
# isqrt API: https://docs.python.org/3/library/math.html#math.isqrt
from math import isqrt


# `grid: list[list[int]]` is a type hint for "a list of lists of ints"
# (a 2D array); `-> bool` documents a True/False result. Python does not
# enforce annotations at run time. Built-in generics like list[...] need
# Python 3.9 or newer.
# Documentation: https://docs.python.org/3/library/typing.html
def is_valid_sudoku(grid: list[list[int]]) -> bool:
    """Check filled rows, columns, and square regions; zero means blank.

    This is the textbook's first program, `is_valid_sudoku`, generalised
    to any n x n grid with n a perfect square and with extra input checks.
    """
    n = len(grid)

    # math.isqrt(n) returns the exact integer square root (the floor of
    # the real square root) of a nonnegative int, with no floating-point
    # rounding. It gives the region width (3 for a 9 x 9 grid). Available
    # since Python 3.8.
    # Documentation: https://docs.python.org/3/library/math.html#math.isqrt
    region = isqrt(n)

    # Shape checks added in this repository (not in the book): reject an
    # empty grid, a size that is not a perfect square, or a ragged grid.
    # any(...) is True if at least one item of the generator expression is
    # true, here "some row has the wrong length".
    # Documentation: https://docs.python.org/3/library/functions.html#any
    if not n or region * region != n or any(len(row) != n for row in grid):
        return False

    # Nested helper (the book's version is `has_duplicate`, the logical
    # opposite). It reads `n` from the enclosing function. Book comment on
    # its helper: "Return True if subarray partial_assignment[start_row:
    # end_row][start_col:end_col] contains any duplicates in {1, 2, ...,
    # len(partial_assignment)}; otherwise return False."
    def no_duplicates(values):

        # List comprehension with a filter: keep only the filled cells.
        filled = [x for x in values if x != 0]

        # all(...) is True when every item is true. isinstance(x, int)
        # checks the value's type; `1 <= x <= n` is a chained comparison.
        # A set keeps one copy of each value, so equal lengths mean no
        # repeats. (The range/type test is an addition; the book only
        # compares the lengths.)
        # Documentation: https://docs.python.org/3/library/functions.html#all
        return all(isinstance(x, int) and 1 <= x <= n for x in filled) and len(filled) == len(set(filled))

    # Book comment: "Check row and column constraints." Row i is grid[i];
    # column i is gathered by the list comprehension of grid[j][i].
    for i in range(n):
        if not no_duplicates(grid[i]) or not no_duplicates([grid[j][i] for j in range(n)]):
            return False

    # Book comment: "Check region constraints." range(0, n, region) gives
    # the top-left row/column of each region: 0, 3, 6 for a 9 x 9 grid.
    for start_r in range(0, n, region):
        for start_c in range(0, n, region):

            # A comprehension with two `for` clauses works like nested
            # loops (rows outer, columns inner), flattening the region into
            # one list.
            block = [grid[r][c] for r in range(start_r, start_r + region)
                     for c in range(start_c, start_c + region)]
            if not no_duplicates(block):
                return False
    return True


def is_valid_sudoku_pythonic(grid: list[list[int]]) -> bool:
    """Alternative solution counting row/column/region-value combinations.

    This is the textbook's second program, `is_valid_sudoku_pythonic`,
    written with explicit loops and with extra input checks.
    """
    n = len(grid)

    # math.isqrt(n): exact integer square root, used as the region width
    # without float rounding (the book uses int(math.sqrt(...))).
    # Documentation: https://docs.python.org/3/library/math.html#math.isqrt
    region = isqrt(n)
    if not n or region * region != n or any(len(row) != n for row in grid):
        return False
    keys = []

    # `enumerate(seq)` yields (index, item) pairs, so i/j are row/column
    # indices and row/digit are the items.
    # Documentation: https://docs.python.org/3/library/functions.html#enumerate
    for i, row in enumerate(grid):
        for j, digit in enumerate(row):

            # Blank cell: nothing to record. `continue` jumps to the next
            # loop iteration.
            if digit == 0:
                continue

            # Value check added in this repository.
            if not isinstance(digit, int) or not 1 <= digit <= n:
                return False

            # One key per constraint the digit takes part in. Tagging each
            # tuple with 'row'/'column'/'region' keeps the three kinds
            # apart (the book separates them by putting str(c) in
            # different tuple positions instead). `//` is floor division:
            # i // region is the region's row number (0..region-1).
            # list.extend appends every item of the given tuple.
            # Documentation: https://docs.python.org/3/tutorial/datastructures.html
            keys.extend((('row', i, digit), ('column', j, digit),
                         ('region', i // region, j // region, digit)))

    # Counter(keys) records how often each constraint is used.
    # A count greater than one means the same digit appears twice in a
    # region (or twice in a row or column).
    #
    # collections.Counter(iterable) builds a dict-like object mapping each
    # distinct item to its number of occurrences; `.values()` is a view of
    # those counts. max(..., default=0) returns the largest count, or 0 if
    # there are no keys at all (an empty grid), instead of raising
    # ValueError on an empty sequence.
    # Documentation: https://docs.python.org/3/library/collections.html#collections.Counter
    # Documentation: https://docs.python.org/3/library/functions.html#max
    return max(Counter(keys).values(), default=0) <= 1


# TEXTBOOK POST-SOLUTION DISCUSSION (page 61)
# ------------------------------------------
# For an n x n Sudoku grid with sqrt(n) x sqrt(n) subgrids, the time
# complexity is O(n^2) + O(n^2) + O(n^2 / (sqrt(n))^2 x (sqrt(n))^2) =
# O(n^2): the three terms are for checking the n row constraints, the n
# column constraints, and the n subgrid constraints respectively.
# Memory use is dominated by the bit array used for checking a
# constraint, so the space complexity is O(n).
#
# The book points to Solution 15.9 on page 230 for actually solving
# Sudoku instances.
#
# VARIANTS
# --------
# The book gives no variants for this exercise.


# TEXTBOOK CODE COMPARISON
# ------------------------
# - Book parameter `partial_assignment`; file `grid`, with type hints.
# - Both file functions add shape checks (empty grid, non-square size,
#   ragged rows) and a digit type/range check; the book has none.
# - `is_valid_sudoku`: book helper `has_duplicate(block)` uses
#   `list(filter(lambda x: x != 0, block))` and returns
#   `len(block) != len(set(block))`; file helper `no_duplicates(values)`
#   uses a list comprehension and returns the opposite sense plus the
#   range check. Book checks rows/columns with one `any(...)` generator
#   over i; file uses a `for` loop. Book computes
#   `region_size = int(math.sqrt(n))` and returns
#   `all(not has_duplicate([...]) for I ... for J ...)` with index ranges
#   `region_size * I .. region_size * (I + 1)`; file uses `isqrt` and
#   explicit loops over `range(0, n, region)` returning False early.
# - `is_valid_sudoku_pythonic`: book is a single expression,
#   `max(collections.Counter(k for i, row in enumerate(...) for j, c in
#   enumerate(row) if c != 0 for k in ((i, str(c)), (str(c), j),
#   (i / region_size, j / region_size, str(c)))).values(), default=0)
#   <= 1`. File builds a `keys` list in explicit loops with string tags
#   ('row', 'column', 'region') instead of the str(c) position trick, uses
#   `//` where the book prints `/` (in Python 3, `/` is true division and
#   gives fractions such as 0.333..., so the book's region key would not
#   group cells into regions as intended), imports `Counter` directly,
#   and uses `isqrt` instead of `int(math.sqrt(...))`.


# Python executes this block only when this source file is run directly.
# When pytest imports the file, this block is skipped automatically.
# Documentation: https://docs.python.org/3/library/__main__.html
if __name__ == "__main__":

    # A completely blank 9 x 9 grid (added example). `[[0] * 9 for _ in
    # range(9)]` builds nine SEPARATE row lists; `[[0] * 9] * 9` would
    # repeat one shared row object nine times. `_` is a conventional name
    # for a loop variable that is not used.
    empty = [[0] * 9 for _ in range(9)]

    # print() with several arguments separates them with a space.
    print("empty Sudoku valid:", is_valid_sudoku(empty))

    # `assert` stops the program with an AssertionError if the condition
    # is false. Both textbook versions must accept the blank grid. pytest
    # provides the more thorough automated verification.
    assert is_valid_sudoku(empty)
    assert is_valid_sudoku_pythonic(empty)
