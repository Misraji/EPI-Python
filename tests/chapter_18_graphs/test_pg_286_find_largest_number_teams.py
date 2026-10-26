# pytest documentation: https://docs.pytest.org/en/stable/
from epi_python.chapter_18_graphs.pg_286_find_largest_number_teams import GraphVertex,find_largest_number_teams


def graph(n,edges):
    v=[GraphVertex() for _ in range(n)]
    for a,b in edges:v[a].edges.append(v[b])
    return v


def test_dag():
    assert find_largest_number_teams(graph(5,[(0,1),(1,2),(0,3),(3,4),(4,2)]))==4


def test_empty_and_isolated():
    assert find_largest_number_teams([])==0
    assert find_largest_number_teams(graph(3,[]))==1
