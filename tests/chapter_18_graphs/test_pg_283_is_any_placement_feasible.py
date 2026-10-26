# pytest documentation: https://docs.pytest.org/en/stable/
from epi_python.chapter_18_graphs.pg_283_is_any_placement_feasible import GraphVertex, is_any_placement_feasible


def make_graph(n,edges):
    v=[GraphVertex() for _ in range(n)]
    for a,b in edges:
        v[a].edges.append(v[b]);v[b].edges.append(v[a])
    return v


def test_even_cycle():
    assert is_any_placement_feasible(make_graph(4,[(0,1),(1,2),(2,3),(3,0)]))


def test_triangle_not_bipartite():
    assert not is_any_placement_feasible(make_graph(3,[(0,1),(1,2),(2,0)]))


def test_disconnected():
    assert not is_any_placement_feasible(make_graph(5,[(0,1),(2,3),(3,4),(4,2)]))
