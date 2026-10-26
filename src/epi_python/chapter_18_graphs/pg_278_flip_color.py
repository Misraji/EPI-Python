"""EPI Python — Exercise 18.2: Paint a Boolean Matrix

Chapter 18: Graphs
Textbook: pages 278–280 (printed page numbers; problem and Figure 18.6 on
278, hint, solution, both programs and discussion on 279, variants on 280).

PROBLEM (from the textbook)
---------------------------
Let A be a Boolean 2D array encoding a black-and-white image. The entry
A(a, b) can be viewed as encoding the color at entry (a, b). Call two
entries adjacent if one is to the left, right, above or below the other.
Note that the definition implies that an entry can be adjacent to at most
four other entries, and that adjacency is symmetric, i.e., if e0 is
adjacent to entry e1, then e1 is adjacent to e0.

Define a path from entry e0 to entry e1 to be a sequence of adjacent
entries, starting at e0, ending at e1, with successive entries being
adjacent. Define the region associated with a point (i, j) to be all points
(i', j') such that there exists a path from (i, j) to (i', j') in which all
entries are the same color. In particular this implies (i, j) and (i', j')
must be the same color.

Implement a routine that takes an n x m Boolean array A together with an
entry (x, y) and flips the color of the region associated with (x, y). See
Figure 18.6 for an example of flipping.

Figure 18.6 (book): the color of all squares associated with the first
square marked with an x in (a) have been recolored to yield the coloring
in (b). The same process yields the coloring in (c).

HINT (from the textbook)
------------------------
Solve this conceptually, then think about implementation optimizations.

SOLUTION DEVELOPMENT (following the textbook)
---------------------------------------------
As in Solution 18.1, graph search avoids the cost of enumerative or random
search. Treat each entry as a vertex, with edges between adjacent entries.

We want every vertex reachable from (x, y) whose color equals that of
(x, y). Breadth-first search is natural here:

1. Initialise a queue with (x, y).
2. Repeatedly pop a point p from the queue. Record p's initial color, then
   flip p's color.
3. Examine p's neighbours; each neighbour whose color equals p's initial
   color is added to the queue.
4. Stop when the queue is empty.

Correctness: any point added to the queue is reachable from (x, y) by a
path of same-colored points, and every point reachable that way is
eventually added. (Flipping a point as soon as it is enqueued also marks it
as visited, so it is never enqueued twice.)

The book gives TWO programs, both named flip_color in the book:
  - an iterative BFS using collections.deque — here flip_color;
  - a recursive version in the spirit of DFS that needs no explicit queue,
    using the function call stack instead — here flip_color_recursive.

ADDITIONAL EXAMPLES (added for learning; not printed in this exercise)
---------------------------------------------------------------------
    board = [[1, 1, 0],
             [1, 0, 0]]
    flip_color(0, 0, board) flips the region of 1s containing (0, 0):
    board becomes [[0, 0, 0], [0, 0, 0]].
"""

# Python standard library: specialized container types.
# Module documentation: https://docs.python.org/3/library/collections.html
# deque API: https://docs.python.org/3/library/collections.html#collections.deque
from collections import deque


# Type hints: x and y are ints, `a` is a list of rows of ints (0/1), and
# `-> None` means the function returns nothing useful — it modifies `a` in
# place. Python does not enforce annotations at run time.
def flip_color(x: int,y: int,a: list[list[int]]) -> None:
    """Iterative breadth-first implementation in the textbook."""

    # Remember the region's original color before anything is flipped.
    color=a[x][y]

    # collections.deque is a double-ended queue: append() adds on the right
    # and popleft() removes from the left, both in O(1) time. (A plain list's
    # pop(0) would be O(n) because every element shifts.) deque([(x, y)])
    # starts the BFS queue holding just the starting entry.
    queue=deque([(x,y)])

    # 1 - v turns 0 into 1 and 1 into 0: the flip. Flipping on enqueue also
    # marks the entry as visited (it no longer has the region's color).
    a[x][y]=1-a[x][y]

    # A non-empty deque is truthy, so this loops until the queue is empty.
    while queue:

        # popleft() removes the oldest element efficiently (FIFO traversal),
        # which is what makes the search breadth-first. The returned tuple
        # is unpacked into i and j.
        i,j=queue.popleft()

        # The four direction offsets: right, left, down, up.
        for dx,dy in ((0,1),(0,-1),(1,0),(-1,0)):
            nx,ny=i+dx,j+dy

            # Chained comparisons check bounds (0 <= nx < rows, etc.); `and`
            # short-circuits so a[nx][ny] is read only when in bounds.
            if 0<=nx<len(a) and 0<=ny<len(a[nx]) and a[nx][ny]==color:

                # Book comment: flips the color.
                a[nx][ny]=1-a[nx][ny]
                queue.append((nx,ny))


def flip_color_recursive(x: int,y: int,a: list[list[int]]) -> None:
    """Recursive DFS version also printed in EPI.

    (The book names this second program flip_color as well.) The function
    call stack replaces the explicit queue.
    """

    # Record the original color, then flip this entry (book comment:
    # "Flips.").
    color=a[x][y]
    a[x][y]=1-a[x][y]
    for dx,dy in ((0,1),(0,-1),(1,0),(-1,0)):
        nx,ny=x+dx,y+dy

        # Recurse into every in-bounds neighbour that still has the
        # original color. Note: a very large region can exceed Python's
        # default recursion limit (about 1000 nested calls) and raise
        # RecursionError; the BFS version has no such limit.
        if 0<=nx<len(a) and 0<=ny<len(a[nx]) and a[nx][ny]==color:
            flip_color_recursive(nx,ny,a)


# TEXTBOOK POST-SOLUTION DISCUSSION (page 279)
# --------------------------------------------
# BFS version: time complexity is the same as BFS, i.e. O(mn). Its space
# complexity is a little better than the BFS worst case, since at most
# O(m + n) vertices are at the same distance from a given entry.
#
# Recursive version: time complexity is the same as DFS.
#
# Both algorithms differ slightly from textbook BFS and DFS. The array
# already has a color per entry, so no auxiliary color field per vertex is
# needed. And because we only need reachability, two colors suffice, while
# BFS/DFS traditionally use three colors to track state. (A third color
# lets one answer questions such as finding cycles in directed graphs, which
# is not relevant here.)
#
# VARIANTS
# --------
# Variant 1 (stated in the book; no solution given): Design an algorithm for
# computing the black region that contains the most points.
#
# Variant 2 (stated in the book; no solution given): Design an algorithm
# that takes a point (a, b), sets A(a, b) to black, and returns the size of
# the black region that contains the most points. Assume this algorithm will
# be called multiple times, and you want to keep the aggregate run time as
# low as possible.


# TEXTBOOK CODE COMPARISON
# ------------------------
# - Names: the book calls BOTH programs `flip_color(x, y, A)`; the file
#   names the BFS version `flip_color` and the DFS version
#   `flip_color_recursive`, renames parameter `A` to `a`, and adds type
#   hints.
# - BFS: the book defines `Coordinate = collections.namedtuple(...)` inside
#   the function and enqueues Coordinate objects, reading them with
#   `x, y = q.popleft()`; the file enqueues plain tuples and pops into
#   `i, j`. The book's queue is `q` and its neighbours are computed via
#   `for d in (...)` with `next_x, next_y = x + d[0], y + d[1]`; the file
#   unpacks `dx, dy` and uses `nx, ny`.
# - Imports: book `collections.deque`; file `from collections import
#   deque`.
# - The book's inline comments ("Flips.", "Flips the color.") are
#   reflected in the file's new comments.
# - Logic is otherwise identical in both versions.


# Python executes this block only when this source file is run directly.
# When pytest imports the file, this block is skipped automatically.
# Documentation: https://docs.python.org/3/library/__main__.html
if __name__ == '__main__':

    # An added example: the 1-region containing (0, 0) is (0,0), (0,1) and
    # (1,0); flipping it leaves an all-zero board. Only the BFS version is
    # demonstrated here; pytest also exercises flip_color_recursive.
    board=[[1,1,0],[1,0,0]]
    flip_color(0,0,board)
    print('Flipped region:',board)

    # `assert` raises AssertionError if the condition is False; a quick
    # smoke check, while pytest does the thorough testing.
    assert board==[[0,0,0],[0,0,0]]
