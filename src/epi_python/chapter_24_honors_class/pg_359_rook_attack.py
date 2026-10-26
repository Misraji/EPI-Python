"""EPI Python — Exercise 24.7: Identify Positions Attacked by Rooks

Chapter 24: Honors Class
Textbook: pages 359–360 (printed page numbers; problem, figure and solution
on 359, the program and its analysis on 360).

PROBLEM (from the textbook)
---------------------------
This problem is concerned with computing squares in a chessboard which can
be attacked by rooks that have been placed at arbitrary locations. The
scenario is illustrated in Figure 24.1(a).

Write a program which takes as input a 2D array A of 1s and 0s, where the
0s encode the positions of rooks on an n x m chessboard, as shown in
Figure 24.1(b) and updates the array to contain 0s at all locations which
can be attacked by rooks, as shown in Figure 24.1(c).

Figure 24.1 (described): (a) an 8 x 8 chessboard with 5 rooks; (b) the same
placement encoded as an 8 x 8 array of 1s with a 0 at each rook; (c) the
result, where every square sharing a row or column with a rook is 0; only
squares in a rook-free row AND a rook-free column remain 1.

HINT (from the textbook)
------------------------
Make use of the first row and the first column.

SOLUTION DEVELOPMENT (following the textbook)
---------------------------------------------
With an extra n-bit array R and m-bit array C the problem is trivial:
  * initialize R and C to all 1s;
  * scan every entry of A; for each (i, j) with A[i][j] = 0, set R[i] and
    C[j] to 0. A 0 in R[i] then means row i must be cleared, and likewise
    for columns;
  * a second scan over all entries sets the 0s in A.
The drawback is O(n + m) additional storage.

The fix is to store the markers in A itself. If a row contains a single 0,
the whole row will be cleared anyway. So keep one extra bit r recording
whether Row 0 originally contains a 0; Row 0 can then play the role of C
(and likewise Column 0 the role of R). Writing a 0 into R[i] writes a value
that would end up at that location anyway, so no original information is
lost. If R[i] still holds a 1 after the first pass it keeps that value
unless r says Row 0 must be cleared. Columns are handled in exactly the
same way.

The book prints one program, `rook_attack(A)`, implemented in this file.

ADDITIONAL EXAMPLES (added for learning; not printed in this exercise)
---------------------------------------------------------------------
    [[1,1,1],          [[1,0,1],
     [1,0,1],    ->     [0,0,0],
     [1,1,1]]           [1,0,1]]
"""


def rook_attack(a: list[list[int]]) -> None:
    """Textbook implementation: first row/column used as O(1)-space markers.

    Mutates `a` in place. `list[list[int]]` documents a list of rows, each a
    list of ints; `-> None` means nothing is returned. Python does not
    enforce type hints.
    """

    # Added guard (not in the book): an empty board or an empty first row
    # would make a[0] / a[0][0] fail below.
    if not a or not a[0]:
        return
    m,n=len(a),len(a[0])

    # Record whether Row 0 / Column 0 originally contain a 0, BEFORE they
    # are overwritten with marker values (this is the extra bit r).
    #
    # any(iterable) returns True as soon as one item is truthy and False if
    # none is (False for an empty iterable). The argument is a generator
    # expression, evaluated lazily, so the scan stops at the first 0.
    # `not a[0][j]` is True exactly when the entry is 0.
    # https://docs.python.org/3/library/functions.html#any
    first_row_zero=any(not a[0][j] for j in range(n))
    first_column_zero=any(not a[i][0] for i in range(m))

    # First pass over the interior: a rook at (i, j) marks row i in Column 0
    # and column j in Row 0.
    for i in range(1,m):
        for j in range(1,n):
            if not a[i][j]:

                # Chained assignment: both targets receive 0.
                a[i][0]=a[0][j]=0

    # Clear each marked row (interior cells only).
    for i in range(1,m):
        if not a[i][0]:

            # A loop body may follow the colon on the same line when it is a
            # single simple statement.
            for j in range(1,n):a[i][j]=0

    # Clear each marked column (interior cells only).
    for j in range(1,n):
        if not a[0][j]:
            for i in range(1,m):a[i][j]=0

    # Finally clear Row 0 and Column 0 themselves if they originally held a
    # 0; this is done last so the markers are not destroyed too early.
    if first_row_zero:
        for j in range(n):a[0][j]=0
    if first_column_zero:
        for i in range(m):a[i][0]=0


# TEXTBOOK POST-SOLUTION DISCUSSION (page 360)
# --------------------------------------------
# Time: O(nm), since O(1) computation is performed per entry.
# Space: O(1) additional storage.
#
# VARIANTS
# The book gives no variants for this exercise.


# TEXTBOOK CODE COMPARISON
# ------------------------
# book: `def rook_attack(A)`; flags named `has_first_row_zero` and
#   `has_first_column_zero`; each inner loop body on its own indented line.
# file: parameter renamed `a: list[list[int]]` with `-> None`; flags renamed
#   `first_row_zero` / `first_column_zero`; added `if not a or not a[0]:
#   return` guard; single-statement loop bodies written on the same line.
#   Same algorithm and statements otherwise.


# Python executes this block only when this source file is run directly.
# When pytest imports the file, this block is skipped automatically.
# Documentation: https://docs.python.org/3/library/__main__.html
if __name__=='__main__':

    # A 3 x 3 board with one rook (0) in the centre: its whole row and
    # column become 0, the corners stay 1.
    # `assert` raises AssertionError if the board differs; the tests/ folder
    # holds the thorough pytest suite.
    board=[[1,1,1],[1,0,1],[1,1,1]]
    rook_attack(board)
    print('Rook attacked cells:',board)
    assert board==[[1,0,1],[0,0,0],[1,0,1]]
