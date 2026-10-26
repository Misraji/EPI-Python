# pytest documentation: https://docs.pytest.org/en/stable/
from epi_python.chapter_18_graphs.pg_282_clone_graph import GraphVertex, clone_graph


def test_cycle():
    a,b,c=GraphVertex(1),GraphVertex(2),GraphVertex(3)
    a.edges=[b,c,b];b.edges=[a];c.edges=[c]
    ca=clone_graph(a)
    assert ca is not a and ca.label==1
    assert ca.edges[0].edges[0] is ca
    assert ca.edges[1].edges[0] is ca.edges[1]
    assert ca.edges[0] is ca.edges[2]


def test_empty():
    assert clone_graph(None) is None
