"""EPI Python — Exercise 18.1: Search a Maze

Chapter 18: Graphs
Textbook: pages 276–278 (printed page numbers; problem on 276, Figure 18.5,
hint, solution and start of the program on 277, end of the program and
complexity on 278).

PROBLEM (from the textbook)
---------------------------
It is natural to apply graph models and algorithms to spatial problems.
Consider a black and white digitized image of a maze—white pixels represent
open areas and black spaces are walls. There are two special white pixels:
one is designated the entrance and the other is the exit. The goal in this
problem is to find a way of getting from the entrance to the exit, as
illustrated in Figure 18.5 on the next page.

Given a 2D array of black and white entries representing a maze with
designated entrance and exit points, find a path from the entrance to the
exit, if one exists.

Figure 18.5 (book): (a) a maze, (b) a path from entrance S to exit E,
(c) a shortest path from entrance to exit — two different solutions.

HINT (from the textbook)
------------------------
Model the maze as a graph.

SOLUTION DEVELOPMENT (following the textbook)
---------------------------------------------
Background (the chapter's "Graph search" section, page 276): DFS and BFS
both find the vertices reachable from a start vertex in O(|V| + |E|) time.
DFS uses O(|V|) space, implicitly, on the function call stack (worst case:
one path through every vertex); BFS also uses O(|V|) space for its queue
(worst case: the start vertex has an edge to every other vertex). BFS can
give distances from the start; DFS can detect cycles and has the notions of
discovery time and finishing time.

1. Brute force: enumerate every path from entrance to exit. The number of
   paths is astronomical (book Solution 16.3, page 242). Pruning — stopping
   when a path hits a black pixel — helps, but the worst case is still very
   bad.

2. Random walk: repeatedly move from a white pixel to a random adjacent
   white pixel. Given enough time this finds a path if one exists, but it
   revisits pixels, which slows progress. This suggests the fix: remember
   which pixels have already been visited — exactly what DFS and BFS do.

3. Graph model: each white pixel is a vertex; vertex v(i,j) is the white
   entry at (i, j) of the 2D array; edges join adjacent white pixels. Run
   DFS from the entrance vertex. If DFS discovers the exit vertex, a path
   exists. With recursive DFS the path is simply the chain of vertices in
   the current call stack.

4. BFS from the entrance also works, and its path would be a SHORTEST path.
   But BFS is harder to implement because its queue must be coded
   explicitly, while DFS gets its stack for free from recursion. The
   problem does not ask for a shortest path, so DFS is preferred.

The book's program is search_maze(maze, s, e) with a nested recursive
helper search_maze_helper(cur); this file follows it closely.

ADDITIONAL EXAMPLES (added for learning; not printed in this exercise)
---------------------------------------------------------------------
With this file's encoding (WHITE = 1 open, BLACK = 0 wall):

    maze = [[1, 1, 0],
            [0, 1, 1],
            [1, 0, 1]]
    search_maze(maze, (0, 0), (2, 2)) returns a path that starts at (0, 0)
    and ends at (2, 2), e.g. (0,0) -> (0,1) -> (1,1) -> (1,2) -> (2,2).
"""

# Python standard library: specialized container types.
# Module documentation: https://docs.python.org/3/library/collections.html
# namedtuple API: https://docs.python.org/3/library/collections.html#collections.namedtuple
from collections import namedtuple


# namedtuple creates an immutable tuple class with named fields:
# Coordinate(2, 3) can be read as .x (row) and .y (column) and still
# compares equal to the plain tuple (2, 3), which the __main__ demo relies on.
Coordinate = namedtuple('Coordinate', ('x','y'))

# Pixel colours. NOTE: this file uses WHITE = 1 (open) and BLACK = 0 (wall);
# the book uses `WHITE, BLACK = range(2)`, i.e. WHITE = 0 and BLACK = 1.
WHITE, BLACK = 1, 0


# Type hints: the maze is a list of rows (lists of ints), s and e are
# Coordinates, and the result is a list of Coordinates. Python does not
# enforce annotations at run time.
def search_maze(maze: list[list[int]], s: Coordinate, e: Coordinate) -> list[Coordinate]:
    """Return a path from s to e through white cells, or [] if none exists.

    The textbook's recursive DFS implementation. The maze is modified:
    visited cells are painted BLACK.
    """

    # `path: list[Coordinate] = []` is an annotated assignment (a variable
    # type hint). path holds the cells on the current DFS route, which is
    # exactly the chain of active recursive calls.
    path: list[Coordinate] = []

    # A nested function: it can read `maze`, `e` and `path` from the
    # enclosing function. It mutates `path` (append/del) but never rebinds
    # the name, so no `nonlocal` declaration is needed.
    def search_maze_helper(cur: Coordinate) -> bool:

        # Book comment: checks cur is within maze and is a white pixel.
        # Chained comparisons such as `0 <= cur.x < len(maze)` mean
        # `0 <= cur.x and cur.x < len(maze)`. `and` short-circuits, so the
        # maze is only indexed once the coordinates are known to be valid.
        if not (0 <= cur.x < len(maze) and 0 <= cur.y < len(maze[cur.x])
                and maze[cur.x][cur.y] == WHITE):
            return False

        # Add cur to the route and paint it BLACK so it is never visited
        # again (this replaces a separate "visited" set).
        path.append(cur)
        maze[cur.x][cur.y] = BLACK
        if cur == e:
            return True

        # map(f, iterable) returns a LAZY iterator that calls f on each item
        # only when asked for the next result. any(iterable) returns True as
        # soon as one item is truthy and stops consuming the iterator. So
        # the four neighbours (up, down, left, right) are explored one by
        # one, and the search stops at the first neighbour that reaches e.
        if any(map(search_maze_helper,
                   (Coordinate(cur.x-1,cur.y), Coordinate(cur.x+1,cur.y),
                    Coordinate(cur.x,cur.y-1), Coordinate(cur.x,cur.y+1)))):
            return True

        # Book comment: cannot find a path, remove the entry added in
        # path.append(cur). `del path[-1]` deletes the last list element
        # (backtracking).
        del path[-1]
        return False

    # Conditional expression `A if cond else B`: return the route if the
    # search from s succeeded, otherwise [] (no path between s and e).
    return path if search_maze_helper(s) else []


# TEXTBOOK POST-SOLUTION DISCUSSION (page 278)
# --------------------------------------------
# The time complexity is the same as for DFS: O(|V| + |E|).
#
# VARIANTS
# --------
# The book states no variants for this exercise.


# TEXTBOOK CODE COMPARISON
# ------------------------
# - Colour constants differ: book `WHITE, BLACK = range(2)` (WHITE = 0,
#   BLACK = 1); file `WHITE, BLACK = 1, 0` (WHITE = 1, BLACK = 0). Mazes
#   written for the book's encoding are inverted for this file.
# - Imports: book uses `collections.namedtuple(...)`; file uses
#   `from collections import namedtuple`. Coordinate fields are the same.
# - Book: `def search_maze(maze, s, e):` and `def search_maze_helper(cur):`;
#   file adds type hints to both and to `path`.
# - Book creates `path = []` AFTER defining the helper and ends with
#   `if not search_maze_helper(s): return []  # No path between s and e.`
#   then `return path`; file creates `path` before the helper and uses a
#   single conditional expression. Same behaviour.
# - The book's code comments ("Perform DFS to find a feasible path",
#   "Checks cur is within maze and is a white pixel", "Cannot find a path,
#   remove the entry added in path.append(cur)", "No path between s and
#   e") are not present as code comments in the original file; they are
#   referenced in the new comments.


# Python executes this block only when this source file is run directly.
# When pytest imports the file, this block is skipped automatically.
# Documentation: https://docs.python.org/3/library/__main__.html
if __name__ == '__main__':

    # An added 3 x 3 maze (1 = white/open, 0 = black/wall in this file).
    # The call paints visited cells black, so `maze` is changed afterwards.
    maze=[[1,1,0],[0,1,1],[1,0,1]]
    route=search_maze(maze,Coordinate(0,0),Coordinate(2,2))
    print('Maze route:',route)

    # `assert` raises AssertionError if the condition is False. A non-empty
    # list is truthy, and Coordinate(0, 0) == (0, 0) because a namedtuple is
    # a tuple. This is a quick smoke check; pytest does the thorough tests.
    assert route and route[0]==(0,0) and route[-1]==(2,2)
