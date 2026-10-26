"""Unit tests for EPI exercise 5.11."""

# pytest parametrization documentation:
# https://docs.pytest.org/en/stable/how-to/parametrize.html
import pytest

from epi_python.chapter_05_arrays.pg_052_next_permutation import next_permutation


@pytest.mark.parametrize(("arguments", "expected"), [(([],), []), (([1],), []), (([1, 2, 3],), [1, 3, 2]), (([3, 2, 1],), []), (([1, 1, 2],), [1, 2, 1])])
def test_cases(arguments, expected):
    assert next_permutation(*arguments) == expected
