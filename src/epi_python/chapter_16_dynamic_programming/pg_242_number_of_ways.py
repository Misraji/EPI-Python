"""EPI Python — Exercise 16.3: Count the Number of Ways to Traverse a 2D Array

Chapter 16: Dynamic Programming
Textbook: pages 242–244 (printed page numbers; problem and solution start on 242).

PROBLEM (from the textbook)
---------------------------
"In this problem you are to count the number of ways of starting at the
top-left corner of a 2D array and getting to the bottom-right corner. All
moves must either go right or down. For example, we show three ways in a
5 x 5 2D array in Figure 16.5. (As we will see, there are a total of 70
possible ways for this example.)"

"Write a program that counts how many ways you can go from the top-left to
the bottom-right in a 2D array."

HINT (from the textbook)
------------------------
"If i > 0 and j > 0, you can get to (i, j) from (i - 1, j) or (i, j - 1)."

SOLUTION DEVELOPMENT (following the textbook)
---------------------------------------------
Brute force: enumerate every path recursively. The number of paths explodes
combinatorially, so this is very slow.

Only the NUMBER of paths is wanted. Because every move goes down or right,
the number of ways to reach the bottom-right entry equals the number of
ways to reach the entry just above it plus the number of ways to reach the
entry just to its left. Treating (0, 0) as the origin, in general:

    ways(i, j) = ways(i - 1, j) + ways(i, j - 1),

and if i = 0 or j = 0 there is exactly one way to reach (i, j).

Coded naively this recursion is exponential, because it recomputes the same
locations over and over. Caching the results fixes this. For the 5 x 5
example, the cached counts form the matrix of Figure 16.6 (ways to reach
(i, j) for 0 <= i, j <= 4):

    1   1   1   1   1
    1   2   3   4   5
    1   3   6  10  15
    1   4  10  20  35
    1   5  15  35  70

The book's program number_of_ways(n, m) uses a nested memoized helper
compute_number_of_ways_to_xy(x, y) and a 2D cache whose zero entries mean
"not computed yet". This file implements the same algorithm.

ADDITIONAL EXAMPLES (added for learning; not printed in this exercise)
---------------------------------------------------------------------
    number_of_ways(3, 4) -> 10   (= C(5, 2): 3 right moves and 2 down moves)
"""


def number_of_ways(n: int, m: int) -> int:
    """Count right/down paths in an n-row, m-column array (textbook version).

    Memoized top-down recursion, as printed in the book. Returns 0 for a
    nonpositive dimension (a guard not in the book).
    """

    # Type hints such as `n: int` document intended types only; Python does
    # not enforce them at run time.
    if n <= 0 or m <= 0:
        return 0

    # 2D cache: ways[x][y] = number of paths to (x, y), with 0 meaning "not
    # computed yet" (every reachable cell has at least one path, so 0 can
    # never be a real answer). The list comprehension creates n
    # independent rows; `[[0]*m]*n` would repeat ONE shared row n times.
    # `_` is the conventional name for an unused loop variable.
    ways = [[0] * m for _ in range(n)]

    # Nested recursive helper. It reads and assigns items of the enclosing
    # `ways` list; item assignment does not rebind the name, so no
    # `nonlocal` declaration is needed.
    def compute_number_of_ways_to_xy(x: int, y: int) -> int:

        # The origin: exactly one way (the empty path).
        if x == 0 and y == 0:
            return 1
        if ways[x][y] == 0:

            # Conditional expressions `a if cond else b`: in row 0 nothing
            # is above, and in column 0 nothing is to the left, so those
            # contributions are 0.
            ways_top = compute_number_of_ways_to_xy(x - 1, y) if x > 0 else 0
            ways_left = compute_number_of_ways_to_xy(x, y - 1) if y > 0 else 0
            ways[x][y] = ways_top + ways_left
        return ways[x][y]

    # The bottom-right corner has indices (n - 1, m - 1).
    return compute_number_of_ways_to_xy(n - 1, m - 1)


# TEXTBOOK POST-SOLUTION DISCUSSION (page 243)
# --------------------------------------------
# Time O(nm) and space O(nm), where n is the number of rows and m the number
# of columns: each cell is computed once, in O(1) time given its
# neighbours.
#
# A more analytical solution: every path from (0, 0) to (n - 1, m - 1) is a
# sequence of m - 1 horizontal steps and n - 1 vertical steps, so the count
# is C(n + m - 2, n - 1) = C(n + m - 2, m - 1) = (n + m - 2)! /
# ((n - 1)! (m - 1)!).
#
# VARIANTS (pages 243–244; each stated in the book; no solution given)
# --------------------------------------------------------------------
# 1. Solve the same problem using O(min(n, m)) space.
# 2. Solve the same problem with obstacles, given as a Boolean 2D array in
#    which true marks an obstacle.
# 3. A fisherman is in a rectangular sea. The value of the fish at point
#    (i, j) is given by an n x m 2D array A. Compute the maximum value of
#    fish the fisherman can catch on a path from the upper leftmost point to
#    the lower rightmost point, moving only down or right (Figure 16.7
#    shows alternate paths; different fish types have different, known
#    values).
# 4. Solve the same problem when the fisherman can begin and end at any
#    point. He must still move down or right. (The value at (i, j) may be
#    negative.)
# 5. A decimal number is a sequence of digits over {0, 1, ..., 9} of length
#    1 or more whose first element is not 0. Call a decimal number D
#    monotone if D[i] <= D[i + 1] for 0 <= i < |D|. Write a program which
#    takes a positive integer k and computes the number of decimal numbers
#    of length k that are monotone.
# 6. Call a decimal number D, as defined above, strictly monotone if
#    D[i] < D[i + 1] for 0 <= i < |D|. Write a program which takes a
#    positive integer k and computes the number of decimal numbers of length
#    k that are strictly monotone.


# TEXTBOOK CODE COMPARISON
# ------------------------
# * Book's cache is named `number_of_ways` (the same name as the outer
#   function) and is created after the helper; file names it `ways` and
#   creates it before the helper.
# * Book base case `if x == y == 0:` (chained comparison); file
#   `if x == 0 and y == 0:` (same meaning).
# * Book `ways_top = 0 if x == 0 else ...` / `ways_left = 0 if y == 0 else
#   ...`; file `... if x > 0 else 0` / `... if y > 0 else 0` (same meaning
#   for valid indices).
# * File adds the guard `if n <= 0 or m <= 0: return 0` and type hints.


# Python executes this block only when this source file is run directly.
# When pytest imports the file, this block is skipped automatically.
# Documentation: https://docs.python.org/3/library/__main__.html
if __name__ == '__main__':

    # Added example: a 3 x 4 grid has C(3 + 4 - 2, 3 - 1) = C(5, 2) = 10
    # right/down paths.
    # `assert` stops the program with an AssertionError if the condition is
    # false; this is a quick smoke check, the pytest suite is thorough.
    print('3x4 grid paths:', number_of_ways(3,4))
    assert number_of_ways(3,4) == 10
