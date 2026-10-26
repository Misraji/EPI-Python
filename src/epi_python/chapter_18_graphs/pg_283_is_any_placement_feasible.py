"""EPI Python 18.6, textbook printed page 283: Making wired connections.

QUESTION: Determine whether graph vertices can be divided into two sets with each edge crossing sets.

TEXTBOOK ALGORITHM: Assign BFS levels and reject an edge joining vertices of identical level parity.

The complete question, hints, solution development, and variants are in the
adjacent page-numbered reference Markdown, extracted from the supplied PDF.
This executable implementation restores syntax damaged by the PDF text layer;
minor type annotations, examples, and assertions are educational additions.

Run: python -m epi_python.chapter_18_graphs.pg_283_is_any_placement_feasible
Test: python -m pytest tests/chapter_18_graphs/test_pg_283_is_any_placement_feasible.py -v
"""

# collections.deque documentation: https://docs.python.org/3/library/collections.html#collections.deque
from collections import deque


class GraphVertex:
    def __init__(self):
        self.d=-1
        self.edges: list['GraphVertex']=[]


def is_any_placement_feasible(g: list[GraphVertex]) -> bool:
    def bfs(start: GraphVertex) -> bool:
        start.d=0
        q=deque([start])
        while q:
            v=q.popleft()
            for neighbor in v.edges:
                if neighbor.d==-1:
                    neighbor.d=v.d+1
                    q.append(neighbor)
                elif neighbor.d % 2 == v.d % 2:
                    return False
        return True

    return all(bfs(v) for v in g if v.d==-1)


if __name__ == '__main__':
    vertices=[GraphVertex() for _ in range(4)]
    for a,b in ((0,1),(1,2),(2,3),(3,0)):
        vertices[a].edges.append(vertices[b]);vertices[b].edges.append(vertices[a])
    print('Bipartite:',is_any_placement_feasible(vertices))
    assert is_any_placement_feasible(vertices)
