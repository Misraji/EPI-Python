"""Pytest verification for EPI 13.5 (printed page 186)."""

# pytest parameterization is the canonical way to share one check among cases.
# Documentation: https://docs.pytest.org/en/stable/how-to/parametrize.html
import pytest

from epi_python.chapter_13_sorting.pg_186_find_max_simultaneous_events import Event, find_max_simultaneous_events


@pytest.mark.parametrize(('pairs','expected'), [
    ([], 0), ([(1,2)], 1), ([(1,2),(2,3)],2),
    ([(1,4),(2,5),(3,6)],3), ([(1,2),(3,4)],1),
    ([(1,1),(1,1)],2),
])
def test_concurrency(pairs,expected):
    assert find_max_simultaneous_events([Event(*pair) for pair in pairs]) == expected


def test_bad_interval():
    with pytest.raises(ValueError):
        find_max_simultaneous_events([Event(5,4)])
