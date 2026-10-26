"""Pytest verification for EPI 13.6 (printed page 188)."""

# pytest parameterization: https://docs.pytest.org/en/stable/how-to/parametrize.html
import pytest

from epi_python.chapter_13_sorting.pg_188_add_interval import add_interval


@pytest.mark.parametrize(('existing','added','expected'), [
    ([], (3,5), [(3,5)]),
    ([(1,2),(4,5)], (3,3), [(1,2),(3,3),(4,5)]),
    ([(1,2),(5,7)], (2,6), [(1,7)]),
    ([(3,4)], (1,2), [(1,2),(3,4)]),
    ([(1,2)], (4,5), [(1,2),(4,5)]),
    ([(1,2),(4,5),(7,8)], (0,9), [(0,9)]),
])
def test_intervals(existing, added, expected):
    assert add_interval(existing, added) == expected
