"""EPI Python — Exercise 18.8: Team Photo Day — 2

Chapter 18: Graphs
Textbook: pages 286–288 (printed page numbers; problem, hint and solution
start on 286, program and complexity on 287, variant on 288).

PROBLEM (from the textbook)
---------------------------
How would you generalize your solution to Problem 13.9 on Page 193, to
determine the largest number of teams that can be photographed
simultaneously subject to the same constraints?

(Context, Problem 13.9: one team can be placed behind another in the photo
only if the placement constraints of that problem are met. This exercise
asks for the longest sequence of teams, each placeable behind the one
before it.)

HINT (from the textbook)
------------------------
Form a DAG in which paths correspond to valid placements.

SOLUTION DEVELOPMENT (following the textbook)
---------------------------------------------
Build a DAG G with one vertex per team and an edge from vertex X to vertex Y
if and only if Team X can be placed behind Team Y.

Every sequence of teams in which each team can be placed behind its
predecessor corresponds to a path in G. So the answer is the length of the
LONGEST path in the DAG.

One way to compute it: order the vertices topologically. Then the longest
path ending at a vertex v is the maximum of the longest paths ending at v's
fan-ins (the vertices with an edge into v), extended by v itself.

The book's program has class GraphVertex (fields edges and max_distance)
and find_largest_number_teams(G) with two nested helpers:
  - build_topological_ordering(), a DFS that appends each vertex when it
    finishes; read backwards, this list is a topological order;
  - find_longest_path(vertex_order), which pops vertices in topological
    order and pushes "longest path so far + 1" along each outgoing edge.
This file follows that structure.

(The "Advanced graph algorithms" section and Figure 18.9 that appear
between Exercises 18.7 and 18.8 on pages 286–287 are chapter material, not
part of this exercise.)

ADDITIONAL EXAMPLES (added for learning; not printed in this exercise)
---------------------------------------------------------------------
    Edges a -> b, a -> c, b -> d, c -> d (a diamond). The longest path is
    a -> b -> d (or a -> c -> d), which has 3 vertices, so the answer is 3
    and d.max_distance ends up as 3.
"""


class GraphVertex:
    """A team in the DAG (the textbook's GraphVertex for this exercise).

    edges: teams reachable by one valid placement step.
    max_distance: first used as a "visited" flag by the DFS (0 = unvisited,
    set to 1 when visited), then as the number of vertices on the longest
    path found so far that ends at this vertex.
    """

    # __init__ is the constructor run by GraphVertex().
    def __init__(self):

        # Annotated attribute; 'GraphVertex' is a string (forward
        # reference) because the class is still being defined.
        self.edges: list['GraphVertex']=[]
        self.max_distance=0


# Type hints: `g` is a list of all vertices (teams); the result is an int.
# Python does not enforce annotations at run time.
def find_largest_number_teams(g: list[GraphVertex]) -> int:
    """Longest path (in vertices) in the team DAG (textbook program)."""

    # Nested helper 1: DFS-based topological ordering.
    def build_topological_ordering() -> list[GraphVertex]:

        # Recursive DFS. It appends `cur` only after all its descendants
        # are appended ("finishing order"). Reversing that order gives a
        # topological order: every edge u -> v has u before v.
        def dfs(cur: GraphVertex) -> None:

            # Mark visited; 1 is also the correct starting length (a path
            # consisting of just this vertex).
            cur.max_distance=1
            for neighbor in cur.edges:

                # `not 0` is True, so this recurses only into unvisited
                # vertices.
                if not neighbor.max_distance:
                    dfs(neighbor)

            # `vertex_order` is defined in the enclosing function below; the
            # nested function can use it because it is only mutated
            # (append), never reassigned, so no `nonlocal` is needed. It
            # exists by the time dfs is first called.
            vertex_order.append(cur)

        # Annotated local variable: a list of GraphVertex.
        vertex_order: list[GraphVertex]=[]

        # Start a DFS from every vertex not yet visited, so vertices in all
        # parts of the graph are ordered.
        for vertex in g:
            if not vertex.max_distance:
                dfs(vertex)
        return vertex_order

    # Nested helper 2: longest path by relaxing edges in topological order.
    def find_longest_path(vertex_order: list[GraphVertex]) -> int:
        max_distance=0

        # list.pop() with no argument removes and returns the LAST item.
        # Popping from the end walks the finishing order backwards, i.e. in
        # topological order, and empties the list as it goes.
        while vertex_order:
            u=vertex_order.pop()

            # Built-in max(a, b) returns the larger value. By the time u is
            # popped, all its fan-ins have already pushed their values into
            # u.max_distance, so it is final.
            max_distance=max(max_distance,u.max_distance)
            for v in u.edges:

                # Extending the best path ending at u by v gives a path of
                # length u.max_distance + 1 ending at v.
                v.max_distance=max(v.max_distance,u.max_distance+1)
        return max_distance

    return find_longest_path(build_topological_ordering())


# TEXTBOOK POST-SOLUTION DISCUSSION (page 287)
# --------------------------------------------
# Computing the topological ordering is O(|V| + |E|) and dominates the
# running time. |V| is the number of teams. The number of edges |E| depends
# on the heights, but can be as large as O(|V|^2), e.g. when there is a path
# of length |V| - 1.
#
# (Python note: dfs is recursive; very long chains of teams can exceed the
# default recursion limit of about 1000 calls and raise RecursionError.)
#
# VARIANTS
# --------
# Variant (stated in the book; no solution given): Let T = {T0, T1, ...,
# T(n-1)} be a set of tasks. Each task runs on a single generic server.
# Task Ti has a duration tau_i, and a set Pi (possibly empty) of tasks that
# must be completed before Ti can be started. The set is feasible if there
# does not exist a sequence of tasks <T0, T1, ..., T(n-1), T0> starting and
# ending at the same task such that for each consecutive pair of tasks, the
# first task must be completed before the second task can begin.
# Given an instance of the task scheduling problem, compute the least amount
# of time in which all the tasks can be performed, assuming an unlimited
# number of servers. Explicitly check that the system is feasible.


# TEXTBOOK CODE COMPARISON
# ------------------------
# - GraphVertex: same fields (`edges = []`, `max_distance = 0`); file adds
#   the hint `self.edges: list['GraphVertex']`.
# - Book: `def find_largest_number_teams(G):`; file renames the parameter
#   to `g` and adds type hints to the outer function and all three nested
#   functions (build_topological_ordering, dfs, find_longest_path), and to
#   `vertex_order`.
# - dfs: book loop variable `next` (which shadows the built-in next()); file
#   uses `neighbor`.
# - build_topological_ordering: book loop `for g in G:`; file
#   `for vertex in g:` (needed, since `g` is now the parameter name).
# - find_longest_path and the final return match the book.


# Python executes this block only when this source file is run directly.
# When pytest imports the file, this block is skipped automatically.
# Documentation: https://docs.python.org/3/library/__main__.html
if __name__ == '__main__':

    # An added "diamond" DAG: a -> b, a -> c, b -> d, c -> d. Unpacking a
    # 4-element list comprehension creates four separate vertices. The `;`
    # separators put several statements on one line (legal, uncommon style).
    a,b,c,d=[GraphVertex() for _ in range(4)]
    a.edges=[b,c];b.edges=[d];c.edges=[d]
    print('Largest number of teams:',find_largest_number_teams([a,b,c,d]))

    # The longest path a -> b -> d has 3 vertices, so d.max_distance is 3.
    # `assert` raises AssertionError if the condition is False.
    assert d.max_distance==3
