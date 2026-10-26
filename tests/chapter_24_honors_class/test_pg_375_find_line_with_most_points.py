# pytest parameterization: https://docs.pytest.org/en/stable/how-to/parametrize.html
import pytest

from epi_python.chapter_24_honors_class.pg_375_find_line_with_most_points import Point,find_line_with_most_points


@pytest.mark.parametrize(('pts','expected'),[([],0),([(0,0)],1),([(0,0),(1,1),(2,2),(0,1)],3),([(1,1),(1,2),(1,3)],3),([(0,0),(0,0),(1,1),(2,2)],4),([(0,0),(1,0),(2,0),(0,1)],3)])
def test_lines(pts,expected):
    assert find_line_with_most_points([Point(*p) for p in pts])==expected
