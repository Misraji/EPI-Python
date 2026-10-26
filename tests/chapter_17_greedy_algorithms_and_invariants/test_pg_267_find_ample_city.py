# pytest parameterization: https://docs.pytest.org/en/stable/how-to/parametrize.html
import pytest

from epi_python.chapter_17_greedy_algorithms_and_invariants.pg_267_find_ample_city import find_ample_city


def is_ample(g,d,first):
    fuel=0
    for i in range(len(g)):
        city=(first+i)%len(g)
        fuel+=g[city]-d[city]//20
        if fuel<0:return False
    return True


@pytest.mark.parametrize(('g','d'), [([2,0,3],[20,40,40]),([1,1,1],[20,20,20]),([0,0,5],[20,20,60]),([3],[60])])
def test_ample_city(g,d):
    assert is_ample(g,d,find_ample_city(g,d))


def test_invalid():
    with pytest.raises(ValueError):
        find_ample_city([],[])
