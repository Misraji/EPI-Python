"""Parameterized checks of EPI 7.8 educational solution."""

# pytest API: https://docs.pytest.org/en/stable/how-to/parametrize.html
import pytest

from epi_python.chapter_07_linked_lists.pg_091_remove_duplicates_sorted_list import remove_duplicates_sorted_list


@pytest.mark.parametrize(("arguments", "expected"), [(([],), []), (([1, 1, 2, 2, 3],), [1, 2, 3]), (([1, 2, 3],), [1, 2, 3]), (([4, 4, 4],), [4])])
def test_examples(arguments, expected):
    assert remove_duplicates_sorted_list(*arguments) == expected
