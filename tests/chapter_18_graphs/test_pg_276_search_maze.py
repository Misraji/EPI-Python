# pytest documentation: https://docs.pytest.org/en/stable/
from epi_python.chapter_18_graphs.pg_276_search_maze import Coordinate, search_maze


def test_path_found():
    g=[[1,1,0],[0,1,1],[1,0,1]]
    path=search_maze(g,Coordinate(0,0),Coordinate(2,2))
    assert path[0]==(0,0) and path[-1]==(2,2)
    assert all(abs(a.x-b.x)+abs(a.y-b.y)==1 for a,b in zip(path,path[1:]))


def test_no_path():
    assert search_maze([[1,0],[0,1]],Coordinate(0,0),Coordinate(1,1))==[]


def test_single_cell():
    assert search_maze([[1]],Coordinate(0,0),Coordinate(0,0))==[Coordinate(0,0)]
