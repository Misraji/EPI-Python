"""EPI Python 18.5, textbook printed page 282: Clone a graph.

QUESTION: Clone the directed graph reachable from a starting vertex, preserving labels and edges.

TEXTBOOK ALGORITHM: Breadth-first traversal creates a mapping from original vertices to corresponding clones.

The complete question, hints, solution development, and variants are in the
adjacent page-numbered reference Markdown, extracted from the supplied PDF.
This executable implementation restores syntax damaged by the PDF text layer;
minor type annotations, examples, and assertions are educational additions.

Run: python -m epi_python.chapter_18_graphs.pg_282_clone_graph
Test: python -m pytest tests/chapter_18_graphs/test_pg_282_clone_graph.py -v
"""

# collections.deque documentation: https://docs.python.org/3/library/collections.html#collections.deque
from collections import deque


class GraphVertex:
    def __init__(self,label: int):
        self.label=label
        self.edges: list['GraphVertex']=[]


def clone_graph(g: GraphVertex | None) -> GraphVertex | None:
    if g is None:
        return None
    queue=deque([g])
    vertex_map={g:GraphVertex(g.label)}
    while queue:
        v=queue.popleft()
        for e in v.edges:
            if e not in vertex_map:
                vertex_map[e]=GraphVertex(e.label)
                queue.append(e)
            vertex_map[v].edges.append(vertex_map[e])
    return vertex_map[g]


if __name__ == '__main__':
    a,b=GraphVertex(1),GraphVertex(2)
    a.edges=[b]
    b.edges=[a]
    clone=clone_graph(a)
    print('Cloned graph:',clone.label,clone.edges[0].label)
    assert clone is not a and clone.edges[0].edges[0] is clone
