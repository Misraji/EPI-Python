"""Unit tests for EPI exercise 11.2."""

# pytest parametrization documentation:
# https://docs.pytest.org/en/stable/how-to/parametrize.html
import pytest

from epi_python.chapter_11_searching.pg_146_search_entry_equal_to_index import search_entry_equal_to_index


@pytest.mark.parametrize(("arguments", "expected"), [(([-2, 0, 2, 5],), 2), (([1, 2, 3],), -1), (([],), -1), (([0],), 0)])
def test_cases(arguments, expected):
    assert search_entry_equal_to_index(*arguments) == expected
