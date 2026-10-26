"""Parameterized checks of EPI 17.8 educational solution."""

# pytest API: https://docs.pytest.org/en/stable/how-to/parametrize.html
import pytest

from epi_python.chapter_17_greedy_algorithms_and_invariants.pg_270_largest_rectangle_under_skyline import largest_rectangle_under_skyline


@pytest.mark.parametrize(("arguments", "expected"), [(([],), 0), (([1],), 1), (([2, 1, 5, 6, 2, 3],), 10), (([2, 2, 2],), 6)])
def test_examples(arguments, expected):
    assert largest_rectangle_under_skyline(*arguments) == expected
