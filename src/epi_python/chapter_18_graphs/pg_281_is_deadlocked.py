"""EPI Python — Exercise 18.4: Deadlock Detection

Chapter 18: Graphs
Textbook: pages 281–282 (printed page numbers; problem, hint, solution and
the GraphVertex class on 281, is_deadlocked, complexity and variants on
282).

PROBLEM (from the textbook)
---------------------------
High performance database systems use multiple processes and resource
locking. These systems may not provide mechanisms to avoid or prevent
deadlock: a situation in which two or more competing actions are each
waiting for the other to finish, which precludes all these actions from
progressing. Such systems must support a mechanism to detect deadlocks, as
well as an algorithm for recovering from them.

One deadlock detection algorithm makes use of a "wait-for" graph to track
which other processes a process is currently blocking on. In a wait-for
graph, processes are represented as nodes, and an edge from process P to Q
implies Q is holding a resource that P needs and thus P is waiting for Q to
release its lock on that resource. A cycle in this graph implies the
possibility of a deadlock. This motivates the following problem.

Write a program that takes as input a directed graph and checks if the
graph contains a cycle.

HINT (from the textbook)
------------------------
Focus on "back" edges.

SOLUTION DEVELOPMENT (following the textbook)
---------------------------------------------
Run DFS on the graph G. DFS keeps a color per vertex:
  - white: not yet discovered (every vertex at the start);
  - gray: discovered, and still being processed (on the DFS stack);
  - black: DFS has finished processing it.

1. If DFS finds an edge from a gray vertex to another gray vertex, G has a
   cycle and we can stop at once.
2. Conversely, if a cycle exists, let v be the first vertex of the cycle
   that DFS reaches. DFS will visit v's predecessor in the cycle, u, before
   v finishes, and then discover the edge u -> v from a gray vertex to a
   gray vertex.
3. So: a cycle exists if and only if DFS discovers a gray-to-gray edge.
4. The graph need not be strongly connected, so examine every vertex and
   start a DFS from each one not yet explored.

The book's program defines a class GraphVertex (colors white, gray, black =
range(3), a color field and an edge list) and a function is_deadlocked(G)
with a nested recursive has_cycle(cur). This file implements the same
three-color DFS on a plain adjacency list of integers (see TEXTBOOK CODE
COMPARISON below).

ADDITIONAL EXAMPLES (added for learning; not printed in this exercise)
---------------------------------------------------------------------
adjacency[i] lists the vertices that vertex i waits for:
    []                  -> False (no processes)
    [[1], [2], []]      -> False (0 -> 1 -> 2, no cycle)
    [[1], [2], [0]]     -> True  (0 -> 1 -> 2 -> 0)
    [[0]]               -> True  (a self-loop is a cycle)
"""


# Type hints: `adjacency: list[list[int]]` means a list whose i-th entry is
# the list of successors of vertex i; `-> bool` is the result type. Python
# does not enforce annotations at run time.
def is_deadlocked(adjacency: list[list[int]]) -> bool:
    """Detect a directed cycle in a wait-for graph using DFS colors.

    The textbook's three-color DFS (book: is_deadlocked(G) with nested
    has_cycle), here operating on integer adjacency lists.
    """

    # `[0] * n` builds a list of n zeros: one color per vertex. 0 plays the
    # role of the book's white, 1 gray and 2 black.
    state=[0]*len(adjacency)  # 0 unseen, 1 visiting, 2 completed

    # Nested recursive helper (book: has_cycle). It reads `state` and
    # `adjacency` from the enclosing function; it only changes list
    # elements, never rebinds the names, so no `nonlocal` is needed.
    def visit(node):

        # Reaching a gray (visiting) vertex: we followed an edge back into
        # the current DFS path, so there is a cycle.
        if state[node]==1:
            return True

        # A black (completed) vertex was fully explored without finding a
        # cycle; there is nothing new to learn from it.
        if state[node]==2:
            return False

        # Mark gray, explore every successor, and stop early on a cycle.
        state[node]=1
        for neighbor in adjacency[node]:
            if visit(neighbor):
                return True

        # All successors done: mark black.
        state[node]=2
        return False

    # any(...) over a generator expression: start a DFS from each vertex that
    # is still white (`if state[index]==0` filters the others out). any()
    # returns True as soon as one DFS reports a cycle and stops evaluating
    # the rest; with no vertices it returns False. The filter condition is
    # checked lazily, so vertices coloured by earlier DFS runs are skipped.
    return any(visit(index) for index in range(len(adjacency)) if state[index]==0)


# TEXTBOOK POST-SOLUTION DISCUSSION (page 282)
# --------------------------------------------
# Time complexity is that of DFS, O(|V| + |E|): every vertex is iterated
# over, and constant time is spent per edge.
#
# Space complexity is O(|V|), the maximum recursion depth: if the recursion
# went deeper than |V| calls, some vertex would have to repeat, which means
# a cycle, and the search terminates early in that case.
#
# (Python note: the default recursion limit is about 1000 calls, so very
# long paths can raise RecursionError in this recursive implementation.)
#
# VARIANTS
# --------
# Variant 1 (stated in the book; no solution given): Solve the same problem
# for an undirected graph.
#
# Variant 2 (stated in the book; no solution given): Write a program that
# takes as input an undirected graph, which you can assume to be connected,
# and checks if the graph remains connected if any one edge is removed.


# TEXTBOOK CODE COMPARISON
# ------------------------
# - Graph representation differs: the book defines `class GraphVertex`
#   with class attributes `white, gray, black = range(3)` and instance
#   fields `color` and `edges` (a list of GraphVertex objects), and
#   `is_deadlocked(G)` takes a list of GraphVertex objects. The file has NO
#   GraphVertex class; `is_deadlocked(adjacency: list[list[int]]) -> bool`
#   takes integer adjacency lists and keeps colors in a separate `state`
#   list (0/1/2 instead of white/gray/black).
# - Helper: book `has_cycle(cur)`; file `visit(node)` (no type hints on
#   the helper).
# - Control flow: the book's helper returns True on gray, marks gray, then
#   `any(next.color != GraphVertex.black and has_cycle(next) for next in
#   cur.edges)`, then marks black. The file explicitly returns False on a
#   black vertex and uses a for loop instead of any(); same result.
# - Outer call: book `any(vertex.color == GraphVertex.white and
#   has_cycle(vertex) for vertex in G)`; file uses a generator with an
#   `if state[index]==0` filter. Equivalent.
# - The book's comments ("Visiting a gray vertex means a cycle.", "Marks
#   current vertex as a gray one.", "Traverse the neighbor vertices.",
#   "Marks current vertex as black.") are reflected in the new comments.


# Python executes this block only when this source file is run directly.
# When pytest imports the file, this block is skipped automatically.
# Documentation: https://docs.python.org/3/library/__main__.html
if __name__ == "__main__":

    # Executable demonstration cases (added); pytest has the full set. They
    # show an empty graph, a chain with no cycle, a 3-cycle and a
    # self-loop.
    #
    # `assert` raises AssertionError if its condition is False; these are
    # quick smoke checks.
    result=is_deadlocked([])
    print('is_deadlocked', result)
    assert result == False
    result=is_deadlocked([[1], [2], []])
    print('is_deadlocked', result)
    assert result == False
    result=is_deadlocked([[1], [2], [0]])
    print('is_deadlocked', result)
    assert result == True
    result=is_deadlocked([[0]])
    print('is_deadlocked', result)
    assert result == True
