# math.comb is a test reference: https://docs.python.org/3/library/math.html#math.comb
from math import comb

# pytest parameterization: https://docs.pytest.org/en/stable/how-to/parametrize.html
import pytest

from epi_python.chapter_16_dynamic_programming.pg_242_number_of_ways import number_of_ways


@pytest.mark.parametrize(('n','m'), [(1,1),(1,7),(7,1),(2,2),(3,4),(5,5),(10,6)])
def test_number_of_ways(n,m):
    assert number_of_ways(n,m)==comb(n+m-2,n-1)
