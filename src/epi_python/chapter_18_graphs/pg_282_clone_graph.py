"""EPI Python — Exercise 18.5: Clone a Graph

Chapter 18: Graphs
Textbook: pages 282–283 (printed page numbers; problem, hint, solution and
start of the program on 282, end of the program and complexity on 283).

PROBLEM (from the textbook)
---------------------------
Consider a vertex type for a directed graph in which there are two fields:
an integer label and a list of references to other vertices. Design an
algorithm that takes a reference to a vertex u, and creates a copy of the
graph on the vertices reachable from u. Return the copy of u.

HINT (from the textbook)
------------------------
Maintain a map from vertices in the original graph to their counterparts in
the clone.

SOLUTION DEVELOPMENT (following the textbook)
---------------------------------------------
Traverse the graph starting from u. Whenever the traversal meets a vertex
or an edge not yet in the clone, add it to the clone. New vertices are
recognised with a hash table that maps each vertex of the original graph
to its counterpart in the new graph. (This map is also what stops cycles
from causing infinite copying: a vertex already in the map is never copied
again.)

Any standard graph traversal works; the book's code uses breadth-first
search. The book's program consists of class GraphVertex (fields label and
edges) and function clone_graph(G); this file follows it.

ADDITIONAL EXAMPLES (added for learning; not printed in this exercise)
---------------------------------------------------------------------
Two vertices pointing at each other, a(1) <-> b(2): the clone of a is a NEW
vertex labelled 1 whose single edge leads to a new vertex labelled 2, whose
edge leads back to the clone of a (not to the original a).
"""

# Python standard library: specialized container types.
# Module documentation: https://docs.python.org/3/library/collections.html
# deque API: https://docs.python.org/3/library/collections.html#collections.deque
from collections import deque


class GraphVertex:
    """A directed-graph vertex: an integer label and a list of out-edges.

    The textbook's GraphVertex class for this exercise. Instances use the
    default identity-based hashing and equality, so each vertex OBJECT is a
    distinct dictionary key, even if two vertices share a label.
    """

    # __init__ is the constructor, run when GraphVertex(label) is called.
    # `label: int` is a type hint (not enforced by Python).
    def __init__(self,label: int):
        self.label=label

        # An annotated attribute: edges is a list of GraphVertex objects.
        # The class name is written as the STRING 'GraphVertex' (a forward
        # reference) because the class is not fully defined yet at this
        # point in the source.
        self.edges: list['GraphVertex']=[]


# Type hints: `GraphVertex | None` (Python 3.10+ union syntax) means "a
# GraphVertex or None". Python does not enforce annotations at run time.
def clone_graph(g: GraphVertex | None) -> GraphVertex | None:
    """Return a deep copy of the graph reachable from g (textbook BFS)."""

    # No start vertex: nothing to copy.
    if g is None:
        return None

    # collections.deque is a double-ended queue with O(1) append() on the
    # right and popleft() on the left, which gives the FIFO order of BFS.
    queue=deque([g])

    # A dict literal mapping original vertex -> its clone. The start vertex
    # is cloned immediately (with the same label but no edges yet).
    vertex_map={g:GraphVertex(g.label)}
    while queue:

        # popleft() removes the oldest queued vertex (breadth-first order).
        v=queue.popleft()
        for e in v.edges:

            # Book comment: try to copy vertex e. `in` on a dict tests keys;
            # a vertex not yet in the map has not been cloned, so clone it
            # and queue it so its own edges are copied later.
            if e not in vertex_map:
                vertex_map[e]=GraphVertex(e.label)
                queue.append(e)

            # Book comment: copy edge v->e, between the two clones.
            vertex_map[v].edges.append(vertex_map[e])
    return vertex_map[g]


# TEXTBOOK POST-SOLUTION DISCUSSION (page 283)
# --------------------------------------------
# Space complexity is O(|V| + |E|), which is the space occupied by the
# result. Excluding the result, the space complexity is O(|V|), coming from
# the hash table and the BFS queue.
#
# (The book does not state the time bound separately here; each reachable
# vertex is dequeued once and each edge copied once.)
#
# VARIANTS
# --------
# The book states no variants for this exercise.


# TEXTBOOK CODE COMPARISON
# ------------------------
# - GraphVertex: book `def __init__(self, label):` with `self.label = label`
#   and `self.edges = []`; file adds the hints `label: int` and
#   `self.edges: list['GraphVertex']`.
# - Book: `def clone_graph(G):` starting with `if not G: return None`; file
#   `def clone_graph(g: GraphVertex | None) -> GraphVertex | None:` with
#   `if g is None: return None` (parameter renamed G -> g; explicit None
#   test instead of truthiness, equivalent for GraphVertex objects).
# - Book queue variable `q` built with `collections.deque([G])`; file
#   `queue` built with `deque([g])` via `from collections import deque`.
# - Loop body identical; the book's comments "Try to copy vertex e." and
#   "Copy edge v->e." are reflected in the new comments.


# Python executes this block only when this source file is run directly.
# When pytest imports the file, this block is skipped automatically.
# Documentation: https://docs.python.org/3/library/__main__.html
if __name__ == '__main__':

    # An added two-vertex cycle a(1) <-> b(2).
    a,b=GraphVertex(1),GraphVertex(2)
    a.edges=[b]
    b.edges=[a]
    clone=clone_graph(a)
    print('Cloned graph:',clone.label,clone.edges[0].label)

    # `is` tests object identity. The clone must be a different object from
    # a, and following two edges from the clone must come back to the clone
    # itself (the cycle is reproduced inside the copy). `assert` raises
    # AssertionError if the condition is False.
    assert clone is not a and clone.edges[0].edges[0] is clone
