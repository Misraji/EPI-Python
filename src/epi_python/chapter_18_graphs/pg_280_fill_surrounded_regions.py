"""EPI Python — Exercise 18.3: Compute Enclosed Regions

Chapter 18: Graphs
Textbook: pages 280–281 (printed page numbers; problem, Figure 18.7, hint
and solution on 280, program and complexity on 281).

PROBLEM (from the textbook)
---------------------------
This problem is concerned with computing regions within a 2D grid that are
enclosed. See Figure 18.7 for an illustration of the problem.

Figure 18.7 (book): three of the four white squares in (a) are enclosed,
i.e., there is no path from any of them to the boundary that only passes
through white squares. (b) shows the white squares that are not enclosed.

The computational problem can be formalized using 2D arrays of Bs (blacks)
and Ws (whites). Figure 18.7(a) is encoded by

        B B B B
    A = W B W B
        B W W B
        B B B B

Figure 18.7(b) is encoded by

        B B B B
        W B B B
        B B B B
        B B B B

Let A be a 2D array whose entries are either W or B. Write a program that
takes A, and replaces all Ws that cannot reach the boundary with a B.

HINT (from the textbook)
------------------------
It is easier to compute the complement of the desired result.

SOLUTION DEVELOPMENT (following the textbook)
---------------------------------------------
Solve the inverse problem: find the Ws that CAN reach the boundary. This is
simpler because if a W is adjacent to a W that can reach the boundary, then
the first W can reach it too.

1. The Ws on the boundary form the initial set.
2. Find Ws neighbouring those, and keep growing the set.
3. Each newly found W that can reach the boundary must be recorded, and
   later searched from for further Ws. A queue is a reasonable structure
   for the Ws still to be processed.

This is breadth-first search started from a SET of vertices (all boundary
cells) rather than from a single vertex. Afterwards every W not reached is
enclosed and becomes B.

The book's program is fill_surrounded_regions(board); it temporarily marks
boundary-reachable Ws with 'T' and finally rewrites the board.

ADDITIONAL EXAMPLES (added for learning; not printed in this exercise)
---------------------------------------------------------------------
    B B B B        B B B B
    B W W B   ->   B B B B   (the W block in the middle cannot reach the
    B B W B        B B B B    boundary and becomes B)
    B W B B        B W B B   (this W is on the boundary and stays W)
"""

# Python standard library: specialized container types.
# Module documentation: https://docs.python.org/3/library/collections.html
# deque API: https://docs.python.org/3/library/collections.html#collections.deque
from collections import deque


# Type hints: `board` is a list of rows of one-character strings ('B' or
# 'W'); `-> None` means the board is modified in place and nothing useful is
# returned. Python does not enforce annotations at run time.
def fill_surrounded_regions(board: list[list[str]]) -> None:
    """Replace enclosed Ws with Bs (the textbook's multi-source BFS)."""

    # Added guard (not in the book): an empty board, or one whose first row
    # is empty, has nothing to do. `not []` is True.
    if not board or not board[0]:
        return
    n,m=len(board),len(board[0])

    # collections.deque is a double-ended queue with O(1) append on the
    # right and popleft() on the left, ideal for a BFS (FIFO) queue.
    #
    # The initial queue holds EVERY boundary cell, built with two nested
    # list comprehensions joined by `+`:
    #   - for each row i, the left and right columns (j in (0, m-1));
    #   - for each column j, the top and bottom rows (i in (0, n-1)).
    # Corner cells appear twice; that is harmless because a cell is only
    # processed while it is still 'W'.
    q=deque([(i,j) for i in range(n) for j in (0,m-1)]
            + [(i,j) for j in range(m) for i in (0,n-1)])
    while q:

        # popleft() removes the oldest queued cell (FIFO = breadth-first).
        x,y=q.popleft()

        # Chained comparisons check bounds; neighbours are enqueued without
        # checking, so out-of-range or non-W cells are simply skipped here.
        if 0<=x<n and 0<=y<m and board[x][y]=='W':
            board[x][y]='T'  # Temporary mark for boundary-connected whites.

            # deque.extend(iterable) appends each item on the right: queue
            # all four neighbours for later examination.
            q.extend([(x-1,y),(x+1,y),(x,y-1),(x,y+1)])

    # Final rewrite with a nested list comprehension and a conditional
    # expression: every cell that is not 'T' (i.e. 'B' or an enclosed 'W')
    # becomes 'B', and every 'T' goes back to 'W'.
    #
    # `board[:] = ...` is SLICE ASSIGNMENT: it replaces the CONTENTS of the
    # existing list object, so the caller's list sees the change. Plain
    # `board = ...` would only rebind the local name and the caller would
    # see nothing.
    board[:]=[['B' if c != 'T' else 'W' for c in row] for row in board]


# TEXTBOOK POST-SOLUTION DISCUSSION (page 281)
# --------------------------------------------
# Time and space complexity are those of BFS: O(mn), where m and n are the
# number of rows and columns of A.
#
# VARIANTS
# --------
# The book states no variants for this exercise.


# TEXTBOOK CODE COMPARISON
# ------------------------
# - Book: `def fill_surrounded_regions(board):`; file adds the type hint
#   `board: list[list[str]]` and `-> None`.
# - The file adds an early `if not board or not board[0]: return` guard;
#   the book has none (it would fail on an empty board at board[0]).
# - Imports: book `collections.deque`; file `from collections import
#   deque`.
# - Initial queue: book builds it as
#   `[(i, j) for k in range(n) for i, j in ((k, 0), (k, m - 1))] +
#   [(i, j) for k in range(m) for i, j in ((0, k), (n - 1, k))]`; the file
#   uses `[(i, j) for i in range(n) for j in (0, m-1)] + [(i, j) for j in
#   range(m) for i in (0, n-1)]`. Same cells, same order.
# - The rest (popleft loop, 'T' marking, extend with four neighbours, and
#   the final `board[:] = [['B' if c != 'T' else 'W' ...]]` rewrite) matches
#   the book; the file adds an inline comment on the 'T' line.


# Python executes this block only when this source file is run directly.
# When pytest imports the file, this block is skipped automatically.
# Documentation: https://docs.python.org/3/library/__main__.html
if __name__ == '__main__':

    # An added 4 x 4 example. list('BBBB') turns a string into a list of its
    # characters, ['B', 'B', 'B', 'B'], giving a mutable row.
    board=[list('BBBB'),list('BWWB'),list('BBWB'),list('BWBB')]
    fill_surrounded_regions(board)
    print('Enclosed whites filled:',board)

    # The interior Ws were enclosed and became B; the W on the bottom edge
    # survives. `assert` raises AssertionError if the condition is False.
    assert board==[list('BBBB'),list('BBBB'),list('BBBB'),list('BWBB')]
