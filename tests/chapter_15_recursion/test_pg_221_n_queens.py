# pytest parameterization: https://docs.pytest.org/en/stable/how-to/parametrize.html
import pytest
from epi_python.chapter_15_recursion.pg_221_n_queens import n_queens


@pytest.mark.parametrize(('size','count'),[(1,1),(2,0),(3,0),(4,2),(5,10),(6,4),(7,40)])
def test_n_queens(size,count):
    solutions=n_queens(size)
    assert len(solutions)==count
    for placement in solutions:
        assert sorted(placement)==list(range(size))
        assert len({r-c for r,c in enumerate(placement)})==size
        assert len({r+c for r,c in enumerate(placement)})==size
