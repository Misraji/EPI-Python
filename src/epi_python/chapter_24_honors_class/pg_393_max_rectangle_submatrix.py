"""EPI Python — Exercise 24.30: Find the Maximum 2D Subarray

Chapter 24: Honors Class
Textbook: pages 392–395 (printed page numbers; problem starts on 392,
solution on 393).

PROBLEM (from the textbook)
---------------------------
"The following problem has applications to image processing.

Let A be an n x m Boolean 2D array. Design efficient algorithms for the
following two problems:
  * What is the largest 2D subarray containing only 1s?
  * What is the largest square 2D subarray containing only 1s?
What are the time and space complexities of your algorithms as a function
of n and m?"

HINT (from the textbook)
------------------------
"How would you efficiently check if A[i, i + a][j, j + b] satisfies the
constraints, assuming you have already performed similar checks?"

SOLUTION DEVELOPMENT (following the textbook)
---------------------------------------------
Brute force: a 2D subarray is determined by two diagonally opposite
corners, so there are O(m^2 n^2) of them; checking each one entry by entry
costs O(m^3 n^3) in total. Processing subarrays by size and reusing results
brings this to O(m^2 n^2): A[i, i + a][j, j + b] is feasible (all 1s) exactly
when A[i, i + a - 1][j, j + b - 1], A[i + a, i + a][j, j + b - 1],
A[i, i + a - 1][j + b, j + b] and A[i + a, i + a][j + b, j + b] are
feasible, an O(1) test once smaller results are stored. That needs
O(m^2 n^2) storage.

Improved approach (lower time and space): for every feasible entry A[i][j]
record (h_ij, w_ij), where h_ij is the largest L such that all of
A[i, i + L - 1][j, j] are 1 and w_ij is the largest L such that all of
A[i, i][j, j + L - 1] are 1. These take O(mn) time and O(mn) space to
compute. Then, for each feasible A[i][j], find the largest 2D subarray
having A[i][j] as its corner (the book calls it the bottom-left corner): go
through the entries A[i, i + h_ij - 1][j] in vertical order, keeping w as
the smallest w seen so far; the subarray with corners A[i][j] and A[i'][j]
on its left side has area (i' - i + 1) * w. Track the best area over all
entries. The book prints this as its first program, max_rectangle_submatrix.

Largest square: compute (h_ij, w_ij) as before. If s is the side of the
largest square with corner A[i + 1][j + 1], then the largest square at
A[i][j] has side at most s + 1, reached exactly when h_ij >= s + 1 and
w_ij >= s + 1. In general the side is min(s + 1, h_ij, w_ij), an O(1)
computation, so the total time is O(mn), a factor of n better. Pruning can
speed things up: having found a feasible H x W subarray, any entry with
h_ij <= H and w_ij <= W need not be processed. The book prints this as its
second program, max_square_submatrix.

A qualitatively different O(nm) approach reduces the problem to n instances
of the largest rectangle under the skyline problem (Problem 17.8, page 270).
For each A[i][j], let h_ij be the largest value such that A[i, i + h_ij - 1][j]
is all 1s (h_ij = 0 when A[i][j] = 0). For each of the n rows, starting with
the topmost, compute the largest 2D subarray whose bottom edge lies on that
row in O(m) time with Solution 17.8 (page 271); the h values for a row can be
computed in O(m) from the previous row's values. The answer is the maximum
over the n instances. The book prints this as a third program, again named
max_rectangle_submatrix.

This file contains max_rectangle_submatrix (the first, (h, w)-based
approach) and max_square_submatrix (a square DP related to the second
program); the skyline-based third program is not included. See the code
comparison block for details.

ADDITIONAL EXAMPLES (added for learning; not printed in this exercise)
---------------------------------------------------------------------
    [[1, 1, 0],
     [1, 1, 1],
     [1, 1, 1]]   -> largest rectangle area 6 (rows 1-2, all columns),
                     largest square area 4 (any 2 x 2 block of 1s)
"""


# Type hints: `a: list[list[int]]` means a list of rows, each a list of
# ints (0 or 1); `-> int` is the area returned. Annotations are not
# enforced at run time.
def max_rectangle_submatrix(a: list[list[int]]) -> int:
    """Return the area of the largest all-1s rectangle in `a`.

    Follows the textbook's first program: precompute vertical and
    horizontal runs of 1s (the book's (h, w) pairs), then from each entry
    walk down its vertical run tracking the minimum width. Runs in
    O(m n^2) time, O(mn) space.
    """

    # Added guard (not in the book): an empty matrix has no rectangle.
    if not a:return 0

    # Tuple unpacking: number of rows and columns.
    rows,cols=len(a),len(a[0])

    # vertical[i][j]  = h: count of consecutive 1s from (i, j) downward.
    # horizontal[i][j] = w: count of consecutive 1s from (i, j) rightward.
    # Each comprehension creates a separate row list per row of `a` (`_`
    # marks the unused loop variable), avoiding shared-row aliasing.
    vertical=[[0]*cols for _ in a]
    horizontal=[[0]*cols for _ in a]

    # reversed(range(rows)) iterates rows - 1, ..., 0 so that the entries
    # below and to the right are already computed.
    # Docs: https://docs.python.org/3/library/functions.html#reversed
    for i in reversed(range(rows)):
        for j in reversed(range(cols)):

            # A nonzero entry (1) is truthy.
            if a[i][j]:

                # Conditional expression `x if cond else y`: use the run
                # length from the next row/column if it exists, else 0.
                vertical[i][j]=1+(vertical[i+1][j] if i+1<rows else 0)
                horizontal[i][j]=1+(horizontal[i][j+1] if j+1<cols else 0)
    maximum=0
    for i in range(rows):
        for j in range(cols):

            # Walk down from (i, j) through its vertical run of 1s. A
            # rectangle of `height` rows with corner (i, j) can be only as
            # wide as the narrowest horizontal run among those rows.
            # Starting at cols plays the role of the book's float('inf');
            # for a 0 entry vertical[i][j] is 0 and the loop does nothing.
            min_width=cols
            for height in range(1,vertical[i][j]+1):
                min_width=min(min_width,horizontal[i+height-1][j])
                maximum=max(maximum,height*min_width)
    return maximum


def max_square_submatrix(a: list[list[int]]) -> int:
    """Return the area of the largest all-1s square in `a`.

    Corresponds to the textbook's second program (largest square in O(mn)
    time), but uses a different recurrence; see TEXTBOOK CODE COMPARISON.
    """

    # Added guard (not in the book): an empty matrix has no square.
    if not a:return 0
    rows,cols=len(a),len(a[0])

    # table[i][j] = side of the largest all-1s square whose top-left corner
    # (in row/column index terms) is (i, j). One fresh row per row of `a`.
    table=[[0]*cols for _ in a]
    largest=0

    # Process from the bottom-right so neighbours below/right are known.
    for i in reversed(range(rows)):
        for j in reversed(range(cols)):
            if a[i][j]:

                # A square at (i, j) can extend one beyond the smallest of
                # the squares starting below, to the right, and diagonally
                # below-right; out-of-range neighbours count as 0 via the
                # conditional expressions. min() with several arguments
                # returns the smallest.
                table[i][j]=1+min(table[i+1][j] if i+1<rows else 0,
                                  table[i][j+1] if j+1<cols else 0,
                                  table[i+1][j+1] if i+1<rows and j+1<cols else 0)

                # `**` is exponentiation: area = side squared.
                largest=max(largest,table[i][j]**2)
    return largest


# TEXTBOOK POST-SOLUTION DISCUSSION (pages 393–395)
# -------------------------------------------------
# First program: the work per entry A[i][j] is proportional to the number of
# rows, O(n), so the overall time is O(mn^2); space is O(mn).
#
# Square program: O(mn) time (an O(1) computation per entry), a factor of n
# better than the rectangle program; pruning (skipping entries with
# h_ij <= H and w_ij <= W once an H x W subarray is known) speeds it up
# further in practice.
#
# Skyline program: for each row, O(m) to update the h values (given the
# previous row's) plus O(m) for the largest rectangle under the skyline, so
# O(m) per row and O(mn) in total. The additional space is O(m), for the h
# values and the skyline computation. The largest all-1s square can be
# computed similarly with a minor variant of Solution 17.8 (page 271).
#
# VARIANTS
# --------
# * Solve the largest square 2D subarray problem using O(m) time.
#   (stated in the book; no solution given) [as printed; "O(m)" may be
#   intended as O(m) space or per row]


# TEXTBOOK CODE COMPARISON
# ------------------------
# * max_rectangle_submatrix: book `def max_rectangle_submatrix(A)` builds
#   one table of `MaxHW = collections.namedtuple('MaxHW', ('h', 'w'))`
#   entries using `reversed(list(enumerate(A)))`; file (parameter `a`,
#   type hints added, empty-input guard added) uses two separate int
#   tables `vertical` and `horizontal` with `reversed(range(...))`. In the
#   area loop the book only processes an entry when
#   `v and table[i][j].w * table[i][j].h > max_rect_area` (a pruning test)
#   and starts `min_width = float('inf')`; the file has no pruning test,
#   starts `min_width=cols`, and loops `height` from 1 instead of `a` from 0
#   (area `height*min_width` vs `min_width * (a + 1)`). Result the same.
# * max_square_submatrix: book builds the same MaxHW table and a second
#   table `s`, computing `side = min(table[i][j].h, table[i][j].w)` then
#   `min(s[i + 1][j + 1] + 1, side)`; file uses the different recurrence
#   `1 + min(below, right, diagonal)` on a single table, with no (h, w)
#   table. Same answers, different formulation; empty-input guard added.
# * Book's third program (skyline-based `max_rectangle_submatrix(A)` using
#   `calculate_largest_rectangle` from Solution 17.8 and
#   `table = [x + y if y else 0 for x, y in zip(table, row)]`) is missing
#   from the file.
# * No `collections` import in the file (book uses collections.namedtuple).


# Python executes this block only when this source file is run directly.
# When pytest imports the file, this block is skipped automatically.
# Documentation: https://docs.python.org/3/library/__main__.html
if __name__=='__main__':

    # Added example grid (see module docstring).
    g=[[1,1,0],[1,1,1],[1,1,1]]
    print('Largest rectangle/square:',max_rectangle_submatrix(g),max_square_submatrix(g))

    # `assert` stops with an AssertionError if the condition is false; a
    # quick smoke check. pytest provides the more thorough verification.
    assert max_rectangle_submatrix(g)==6 and max_square_submatrix(g)==4
