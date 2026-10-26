# pytest parameterization: https://docs.pytest.org/en/stable/how-to/parametrize.html
import pytest

from epi_python.chapter_16_dynamic_programming.pg_252_maximum_revenue import maximum_revenue


@pytest.mark.parametrize(('coins','expected'), [([],0),([7],7),([5,25,10,1],26),([10,25,5,1,10,5],31),([4,4],4)])
def test_revenue(coins,expected):
    assert maximum_revenue(coins)==expected
