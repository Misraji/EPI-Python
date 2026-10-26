# pytest parameterization: https://docs.pytest.org/en/stable/how-to/parametrize.html
import pytest

from epi_python.chapter_24_honors_class.pg_393_max_rectangle_submatrix import max_rectangle_submatrix,max_square_submatrix


@pytest.mark.parametrize(('g','r','s'), [([],0,0),([[0]],0,0),([[1]],1,1),([[1,1,0],[1,1,1],[1,1,1]],6,4),([[1,1,1],[0,0,0]],3,1)])
def test_both_shapes(g,r,s):
    assert max_rectangle_submatrix(g)==r
    assert max_square_submatrix(g)==s
