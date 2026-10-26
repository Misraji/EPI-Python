# pytest parameterization: https://docs.pytest.org/en/stable/how-to/parametrize.html
import pytest

from epi_python.chapter_17_greedy_algorithms_and_invariants.pg_262_find_minimum_visits import Interval, find_minimum_visits


@pytest.mark.parametrize(('pairs','expected'), [([],0),([(1,2)],1),([(1,3),(2,5),(3,7)],1),([(0,3),(2,6),(3,4),(6,9)],2),([(1,2),(3,4),(5,6)],3),([(1,1),(1,1)],1)])
def test_visits(pairs,expected):
    assert find_minimum_visits([Interval(*x) for x in pairs])==expected
