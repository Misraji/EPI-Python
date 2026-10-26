"""Parameterized checks of EPI 7.1 educational solution."""

# pytest API: https://docs.pytest.org/en/stable/how-to/parametrize.html
import pytest

from epi_python.chapter_07_linked_lists.pg_084_merge_two_sorted_lists import merge_two_sorted_lists


@pytest.mark.parametrize(("arguments", "expected"), [(([1, 3, 5], [2, 4, 6]), [1, 2, 3, 4, 5, 6]), (([], [1]), [1]), (([1, 1], [1, 2]), [1, 1, 1, 2])])
def test_examples(arguments, expected):
    assert merge_two_sorted_lists(*arguments) == expected
