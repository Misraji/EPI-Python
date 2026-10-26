"""Unit tests for EPI exercise 11.6."""

# pytest parametrization documentation:
# https://docs.pytest.org/en/stable/how-to/parametrize.html
import pytest

from epi_python.chapter_11_searching.pg_150_matrix_search import matrix_search


@pytest.mark.parametrize(("arguments", "expected"), [(([[1, 3, 5], [2, 4, 6]], 4), True), (([[1, 3, 5], [2, 4, 6]], 7), False), (([], 2), False)])
def test_cases(arguments, expected):
    assert matrix_search(*arguments) == expected
