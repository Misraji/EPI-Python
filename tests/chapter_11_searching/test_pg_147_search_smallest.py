"""Unit tests for EPI exercise 11.3."""

# pytest parametrization documentation:
# https://docs.pytest.org/en/stable/how-to/parametrize.html
import pytest

from epi_python.chapter_11_searching.pg_147_search_smallest import search_smallest


@pytest.mark.parametrize(("arguments", "expected"), [(([],), -1), (([4, 5, 1, 2, 3],), 2), (([1, 2, 3],), 0), (([2, 1],), 1)])
def test_cases(arguments, expected):
    assert search_smallest(*arguments) == expected
