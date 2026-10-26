"""EPI Python 18.8, textbook printed page 286: Team photo day - 2.

QUESTION: Find the largest number of photograph-compatible teams using a directed acyclic graph.

TEXTBOOK ALGORITHM: Generate a topological order by DFS, then propagate longest-path lengths along outgoing edges.

The complete question, hints, solution development, and variants are in the
adjacent page-numbered reference Markdown, extracted from the supplied PDF.
This executable implementation restores syntax damaged by the PDF text layer;
minor type annotations, examples, and assertions are educational additions.

Run: python -m epi_python.chapter_18_graphs.pg_286_find_largest_number_teams
Test: python -m pytest tests/chapter_18_graphs/test_pg_286_find_largest_number_teams.py -v
"""

class GraphVertex:
    def __init__(self):
        self.edges: list['GraphVertex']=[]
        self.max_distance=0


def find_largest_number_teams(g: list[GraphVertex]) -> int:
    def build_topological_ordering() -> list[GraphVertex]:
        def dfs(cur: GraphVertex) -> None:
            cur.max_distance=1
            for neighbor in cur.edges:
                if not neighbor.max_distance:
                    dfs(neighbor)
            vertex_order.append(cur)

        vertex_order: list[GraphVertex]=[]
        for vertex in g:
            if not vertex.max_distance:
                dfs(vertex)
        return vertex_order

    def find_longest_path(vertex_order: list[GraphVertex]) -> int:
        max_distance=0
        while vertex_order:
            u=vertex_order.pop()
            max_distance=max(max_distance,u.max_distance)
            for v in u.edges:
                v.max_distance=max(v.max_distance,u.max_distance+1)
        return max_distance

    return find_longest_path(build_topological_ordering())


if __name__ == '__main__':
    a,b,c,d=[GraphVertex() for _ in range(4)]
    a.edges=[b,c];b.edges=[d];c.edges=[d]
    print('Largest number of teams:',find_largest_number_teams([a,b,c,d]))
    assert d.max_distance==3
