# pytest documentation: https://docs.pytest.org/en/stable/
from epi_python.chapter_18_graphs.pg_280_fill_surrounded_regions import fill_surrounded_regions


def test_enclosed():
    a=[list('BBBB'),list('BWWB'),list('BBWB'),list('BWBB')]
    fill_surrounded_regions(a)
    assert [''.join(row) for row in a]==['BBBB','BBBB','BBBB','BWBB']


def test_all_boundary_reachable():
    a=[list('WWW'),list('WBW'),list('WWW')]
    before=[row[:] for row in a]
    fill_surrounded_regions(a)
    assert a==before


def test_empty():
    a=[]
    fill_surrounded_regions(a)
    assert a==[]
