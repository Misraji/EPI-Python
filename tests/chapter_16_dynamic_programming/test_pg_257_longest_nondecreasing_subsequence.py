"""Parameterized checks of EPI 16.12 educational solution."""

# pytest API: https://docs.pytest.org/en/stable/how-to/parametrize.html
import pytest

from epi_python.chapter_16_dynamic_programming.pg_257_longest_nondecreasing_subsequence import longest_nondecreasing_subsequence


@pytest.mark.parametrize(("arguments", "expected"), [(([],), 0), (([1],), 1), (([3, 1, 2, 2, 5],), 4), (([5, 4, 3],), 1), (([2, 2, 2],), 3)])
def test_examples(arguments, expected):
    assert longest_nondecreasing_subsequence(*arguments) == expected
