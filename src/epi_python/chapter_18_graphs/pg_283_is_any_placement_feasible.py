"""EPI Python — Exercise 18.6: Making Wired Connections

Chapter 18: Graphs
Textbook: pages 283–284 (printed page numbers; problem, Figure 18.8, hint
and solution start on 283, proof, program and discussion on 284).

PROBLEM (from the textbook)
---------------------------
Consider a collection of electrical pins on a printed circuit board (PCB).
For each pair of pins, there may or may not be a wire joining them. This is
shown in Figure 18.8, where vertices correspond to pins, and edges indicate
the presence of a wire between pins. (The significance of the colors is
explained later.)

Design an algorithm that takes a set of pins and a set of wires connecting
pairs of pins, and determines if it is possible to place some pins on the
left half of a PCB, and the remainder on the right half, such that each
wire is between left and right halves. Return such a division, if one
exists. For example, the light vertices and dark vertices in Figure 18.8
are such division.

Figure 18.8 (book): a set of pins and wires between them, drawn as a graph
whose vertices are shaded light or dark.

HINT (from the textbook)
------------------------
Model as a graph and think about the implication of an odd length cycle.

SOLUTION DEVELOPMENT (following the textbook)
---------------------------------------------
Brute force: try every partition of the pins into two sets — far too many
partitions.

Better: let connectivity guide the partition. Number the pins 0 .. p - 1
and build an undirected graph G whose vertices are pins, with an edge for
each wire. Assume G is connected for simplicity (otherwise analyse each
connected component independently).

1. Run BFS from any vertex v0 and put v0 (arbitrarily) on the left half.
2. Every vertex at an odd distance from v0 goes on the right half (and
   every vertex at an even distance on the left).

Why this works: in BFS of an undirected graph, each newly discovered edge
either goes from a distance-d vertex to an undiscovered vertex (which then
gets distance d + 1), or joins two vertices both at distance d.
  - If no edge ever joins two vertices of the same distance k, every wire
    runs between a distance-k and a distance-(k + 1) vertex, i.e. between
    the left and right halves: success.
  - If some edge joins two distance-k vertices u and v, stop: no valid
    partition exists. Take a, the first common ancestor of u and v in the
    BFS tree (one exists because the search began at v0). The tree paths
    p_u and p_v from a to u and to v have equal length, so going from a to
    u along p_u, across edge (u, v), and back to a along p_v is a cycle of
    ODD length. In any two-set partition with all edges crossing, every
    cycle must have an even number of edges (each back-and-forth trip adds
    two edges and it must return to its start). So an odd cycle makes the
    partition impossible.

The book's program is class GraphVertex (fields d, the BFS distance with -1
meaning unvisited, and edges) plus is_any_placement_feasible(G) with a
nested bfs(s). This file follows that structure.

ADDITIONAL EXAMPLES (added for learning; not printed in this exercise)
---------------------------------------------------------------------
    A 4-cycle 0-1-2-3-0 is feasible: {0, 2} on one side, {1, 3} on the
    other. (A triangle, an odd cycle, would not be feasible.)
"""

# Python standard library: specialized container types.
# Module documentation: https://docs.python.org/3/library/collections.html
# deque API: https://docs.python.org/3/library/collections.html#collections.deque
from collections import deque


class GraphVertex:
    """A pin: BFS distance d (-1 = unvisited) and a list of wired pins.

    The textbook's GraphVertex for this exercise.
    """

    # __init__ is the constructor, run by GraphVertex().
    def __init__(self):
        self.d=-1

        # Annotated attribute; 'GraphVertex' is a string forward reference
        # because the class is still being defined. For an undirected graph,
        # each wire must be listed in BOTH vertices' edges lists.
        self.edges: list['GraphVertex']=[]


# Type hints: `g` is a list of GraphVertex objects (all pins) and the result
# is a bool. Python does not enforce annotations at run time.
def is_any_placement_feasible(g: list[GraphVertex]) -> bool:
    """Return True iff the pins can be split into two halves (textbook BFS).

    Side effect: each vertex's d is set to its BFS distance; vertices with
    even d form one half and odd d the other.
    """

    # Nested BFS over one connected component, starting at `start`.
    def bfs(start: GraphVertex) -> bool:
        start.d=0

        # collections.deque: a double-ended queue with O(1) append() on the
        # right and popleft() on the left, giving BFS its FIFO order.
        q=deque([start])
        while q:

            # popleft() removes and returns the oldest queued vertex.
            v=q.popleft()
            for neighbor in v.edges:

                # Unvisited vertex: it lies one level further from start.
                if neighbor.d==-1:
                    neighbor.d=v.d+1
                    q.append(neighbor)

                # `%` is the remainder operator; d % 2 is 0 for even and 1
                # for odd distances, i.e. which half the pin is on. A wire
                # between two pins on the same half makes placement
                # impossible.
                elif neighbor.d % 2 == v.d % 2:
                    return False
        return True

    # all(...) over a generator expression: run bfs from every vertex that
    # is still unvisited (`if v.d == -1`), one per connected component.
    # all() stops and returns False at the first component that fails; with
    # an empty graph it returns True. The filter is evaluated lazily, so
    # vertices reached by earlier BFS runs are skipped.
    return all(bfs(v) for v in g if v.d==-1)


# TEXTBOOK POST-SOLUTION DISCUSSION (page 284)
# --------------------------------------------
# The complexity is that of BFS: O(p + w) time, where p is the number of
# pins and w the number of wires, and O(p) space.
#
# Graphs that can be partitioned this way are called bipartite graphs, also
# known as 2-colorable graphs (each vertex gets one of two colors and no
# two neighbours share a color).
#
# VARIANTS
# --------
# The book states no variants for this exercise.


# TEXTBOOK CODE COMPARISON
# ------------------------
# - GraphVertex: same fields (`d = -1`, `edges = []`); the file adds the
#   hint `self.edges: list['GraphVertex']`.
# - Book: `def is_any_placement_feasible(G):` with nested `def bfs(s):`;
#   file renames the parameters to `g` and `start`, and adds type hints.
# - BFS loop: the book PEEKS at the front with `q[0]`, iterating
#   `for t in q[0].edges`, and removes the front afterwards with
#   `del q[0]`; the file pops the front first with `v = q.popleft()`.
#   Equivalent.
# - Conflict test differs: book `elif t.d == q[0].d: return False` (equal
#   BFS distance, as in the proof); file `elif neighbor.d % 2 == v.d % 2:
#   return False` (equal distance PARITY). In BFS on an undirected graph a
#   neighbour's distance differs by at most 1, so the two tests detect the
#   same conflicts.
# - Imports: book `collections.deque`; file `from collections import
#   deque`. The book's comment "Unvisited vertex." is reflected in the new
#   comments. The outer `all(...)` call matches the book.


# Python executes this block only when this source file is run directly.
# When pytest imports the file, this block is skipped automatically.
# Documentation: https://docs.python.org/3/library/__main__.html
if __name__ == '__main__':

    # An added example: four pins wired in a square 0-1-2-3-0 (an even
    # cycle). `for _ in range(4)` uses `_` as a conventional name for a loop
    # variable that is not needed.
    vertices=[GraphVertex() for _ in range(4)]

    # Each wire is undirected, so it is appended to both endpoints' edges.
    # The `;` puts two statements on one line (legal but uncommon style).
    for a,b in ((0,1),(1,2),(2,3),(3,0)):
        vertices[a].edges.append(vertices[b]);vertices[b].edges.append(vertices[a])
    print('Bipartite:',is_any_placement_feasible(vertices))

    # `assert` raises AssertionError if the condition is False. Calling the
    # function again is fine: all d values are already set, so no BFS runs
    # and all() over an empty sequence returns True.
    assert is_any_placement_feasible(vertices)
