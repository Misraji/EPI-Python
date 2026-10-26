# pytest parameterization: https://docs.pytest.org/en/stable/how-to/parametrize.html
import pytest

from epi_python.chapter_16_dynamic_programming.pg_245_is_pattern_contained_in_grid import is_pattern_contained_in_grid


@pytest.mark.parametrize(('pattern','expected'), [([],True),([1],True),([1,2,5],True),([1,2,5,8],True),([1,1],False),([1,4,5,6],True),([9,5,1],False)])
def test_pattern(pattern, expected):
    g=[[1,2,3],[4,5,6],[7,8,9]]
    assert is_pattern_contained_in_grid(g,pattern) is expected


def test_revisiting_cell_allowed():
    assert is_pattern_contained_in_grid([[1,2]],[1,2,1])
