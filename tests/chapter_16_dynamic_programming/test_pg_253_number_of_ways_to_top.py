"""Unit tests for EPI exercise 16.10."""

# pytest parametrization documentation:
# https://docs.pytest.org/en/stable/how-to/parametrize.html
import pytest

from epi_python.chapter_16_dynamic_programming.pg_253_number_of_ways_to_top import number_of_ways_to_top


@pytest.mark.parametrize(("arguments", "expected"), [((0, 2), 1), ((1, 2), 1), ((2, 2), 2), ((3, 2), 3), ((4, 2), 5)])
def test_cases(arguments, expected):
    assert number_of_ways_to_top(*arguments) == expected
