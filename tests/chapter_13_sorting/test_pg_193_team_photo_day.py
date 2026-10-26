"""Pytest verification for EPI 13.9 (printed page 193)."""

# pytest parameterization: https://docs.pytest.org/en/stable/how-to/parametrize.html
import pytest

from epi_python.chapter_13_sorting.pg_193_team_photo_day import valid_placement_exists


@pytest.mark.parametrize(('a','b','expected'), [
    ([1,3,5],[2,4,6],True),
    ([2,4,6],[1,3,5],True),
    ([1,4],[2,3],False),
    ([1,2],[1,3],False),
    ([],[],True),
    ([1],[1,2],False),
])
def test_valid_placement(a,b,expected):
    assert valid_placement_exists(a,b) is expected
