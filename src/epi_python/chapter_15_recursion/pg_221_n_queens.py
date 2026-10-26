"""EPI Python — Exercise 15.2: Generate All Nonattacking Placements of n-Queens

Chapter 15: Recursion
Textbook: pages 221–222 (printed page numbers; problem and solution start on 221).

PROBLEM (from the textbook)
---------------------------
"A nonattacking placement of queens is one in which no two queens are in
the same row, column, or diagonal."  Figure 15.4 shows "the only two ways
in which four queens can be placed on a 4 x 4 chessboard."

"Write a program which returns all distinct nonattacking placements of n
queens on an n x n chessboard, where n is an input to the program."

HINT (from the textbook)
------------------------
"If the first queen is placed at (i, j), where can the remaining queens
definitely not be placed?"

SOLUTION DEVELOPMENT (following the textbook)
---------------------------------------------
Brute force: try every way of putting n queens on the n^2 squares. There
are C(n^2, n) ("n^2 choose n") such placements, a number that grows very
quickly with n.

Improvement: two queens can never share a row, so only enumerate
placements that put exactly one queen in each row. These can never clash on
a row, but can still clash on a column or a diagonal. Such a placement is
represented as an array of length n whose i-th entry is the column of the
queen in row i.

Worked example from the book, n = 4 (an underscore is an undecided row):

* Put row 0's queen in column 0 and look at placements (0, _, _, _).
  - (0, 0, _, _): column conflict, so all of these are skipped.
  - (0, 1, _, _): diagonal conflict, skipped.
  - (0, 2, 0, _): column conflict with row 0.
  - (0, 2, 1, _): diagonal conflict between (row 1, col 2) and
    (row 2, col 1); (0, 2, 2, _): column conflict between (row 1, col 2)
    and (row 2, col 2).
  - (0, 2, 3, _): diagonal conflict.
  - (0, 3, _, _): both (0, 3, 1, _) and (0, 3, 2, _) lead to conflicts.
  So no nonattacking placement has a queen at row 0, column 0.
* The first nonattacking placement found is (1, 3, 0, 2); the only other
  one is (2, 0, 3, 1).

The book's program n_queens(n) uses a nested recursive helper
solve_n_queens(row) that tries every column for the current row, keeps the
column only if it conflicts with none of the earlier rows' queens, and
records a copy of the placement when row == n. This file implements the
same algorithm with the helper named `solve`.

Conflict test: an earlier queen at (prior_row, prior_col) attacks the new
square (row, col) if they share a column (|prior_col - col| == 0) or a
diagonal (|prior_col - col| == row - prior_row, i.e. equal horizontal and
vertical distance).
"""


def n_queens(n: int) -> list[list[int]]:
    """Return all nonattacking placements as lists of column indices.

    Entry i of each returned list is the column of the queen in row i.
    This is the textbook's recursive backtracking implementation
    (n_queens with nested helper solve_n_queens, renamed `solve` here).
    """

    # Type hints such as `n: int` and `-> list[list[int]]` document the
    # intended types (an int in, a list of lists of ints out). Python does
    # not check or enforce them at run time.
    result=[]

    # `[0]*n` builds a list of n zeros. Repeating a list of immutable ints
    # with `*` is safe. This list is the single shared partial placement
    # that the recursion overwrites row by row.
    placement=[0]*n

    # Nested helper: it can read and mutate the enclosing `result` and
    # `placement` lists. Mutation (append / item assignment) does not rebind
    # those names, so no `nonlocal` declaration is required.
    def solve(row: int) -> None:

        # All n queens are legally placed. `list(placement)` stores a COPY,
        # because the shared `placement` list keeps changing as the
        # recursion backtracks; appending `placement` itself would make
        # every result refer to the same (eventually overwritten) list.
        if row==n:
            result.append(list(placement))
            return
        for col in range(n):

            # Test whether a queen at (row, col) conflicts with any queen
            # placed earlier.
            #
            # `placement[:row]` slices the columns of rows 0 .. row-1 (the
            # already-decided rows); later entries are stale and ignored.
            #
            # `enumerate(seq)` yields (index, item) pairs, so prior_row is
            # the earlier row number and prior_col its queen's column.
            #
            # `all(<generator expression>)` returns True only if every
            # produced value is true; it stops at the first False
            # (short-circuits), and returns True for an empty sequence
            # (row 0 has no earlier queens, so every column is allowed).
            #
            # `abs(prior_col-col) not in (0, row-prior_row)` is True when
            # the column distance is neither 0 (same column) nor equal to
            # the row distance (same diagonal).
            if all(abs(prior_col-col) not in (0,row-prior_row)
                   for prior_row,prior_col in enumerate(placement[:row])):
                placement[row]=col
                solve(row+1)

    solve(0)
    return result


# TEXTBOOK POST-SOLUTION DISCUSSION (page 222)
# --------------------------------------------
# The running time is at least the number of nonattacking placements that
# must be output. No exact formula for this count as a function of n is
# known; it is conjectured to tend to n!/c^n with c approximately 2.54,
# which is super-exponential.
#
# VARIANTS (each stated in the book; no solution given)
# ----------------------------------------------------
# 1. Compute the number of nonattacking placements of n queens on an
#    n x n chessboard.
# 2. Compute the smallest number of queens that can be placed to attack
#    each uncovered square.
# 3. Compute a placement of 32 knights, or 14 bishops, 16 kings or 8 rooks
#    on an 8 x 8 chessboard in which no two pieces attack each other.


# TEXTBOOK CODE COMPARISON
# ------------------------
# * Names: book nested helper `solve_n_queens(row)` and shared list
#   `col_placement`; file uses `solve(row: int) -> None` and `placement`.
#   Type hints are added in the file (`n: int`, `-> list[list[int]]`).
# * Book initializes both in one statement after the helper:
#   `result, col_placement = [], [0] * n`; file initializes `result` and
#   `placement` in two statements before the helper.
# * Conflict test: book `abs(c - col) not in (0, row - i) for i, c in
#   enumerate(col_placement[:row])`; file uses the same expression with the
#   loop variables renamed `prior_row`, `prior_col`.
# * The book's two code comments ("All queens are legally placed." and
#   "Test if a newly placed queen will conflict any earlier queens placed
#   before.") are not in the original file's code; equivalent explanations
#   are given in the comments above.
# * Algorithm and output order are otherwise the same.


# Python executes this block only when this source file is run directly.
# When pytest imports the file, this block is skipped automatically.
# Documentation: https://docs.python.org/3/library/__main__.html
if __name__ == '__main__':

    # The textbook's own example: n = 4 has exactly two nonattacking
    # placements, (1, 3, 0, 2) and (2, 0, 3, 1) (Figure 15.4).
    # `sorted(...)` returns a new sorted list, so the check does not depend
    # on the order in which the search produces the placements.
    #
    # `assert` stops the program with an AssertionError if the condition is
    # false. This is a quick smoke check; the pytest suite in tests/
    # provides the thorough automated verification.
    placements=n_queens(4)
    print('4-queens placements:',placements)
    assert sorted(placements)==[[1,3,0,2],[2,0,3,1]]
