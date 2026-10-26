"""Pytest verification for EPI 13.7 (printed page 189)."""

# pytest parameterization: https://docs.pytest.org/en/stable/how-to/parametrize.html
import pytest

from epi_python.chapter_13_sorting.pg_189_union_of_intervals import Interval, Endpoint, closed, union_of_intervals


@pytest.mark.parametrize(('pairs','expected'), [
    ([], []),
    ([(1,2)], [(1,2)]),
    ([(1,3),(2,4),(8,9)], [(1,4),(8,9)]),
    ([(2,3),(1,2)], [(1,3)]),
])
def test_closed_intervals(pairs,expected):
    assert union_of_intervals([closed(*v) for v in pairs]) == [closed(*v) for v in expected]


def test_touching_open_intervals_do_not_merge():
    a = Interval(Endpoint(1,True),Endpoint(2,False))
    b = Interval(Endpoint(2,False),Endpoint(3,True))
    assert union_of_intervals([b,a]) == [a,b]


def test_touching_with_at_least_one_closed_merges():
    a = Interval(Endpoint(1,True),Endpoint(2,True))
    b = Interval(Endpoint(2,False),Endpoint(3,True))
    assert union_of_intervals([b,a]) == [closed(1,3)]
