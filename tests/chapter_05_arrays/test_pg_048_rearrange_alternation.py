"""Unit tests for EPI exercise 5.8."""

# pytest parametrization documentation:
# https://docs.pytest.org/en/stable/how-to/parametrize.html
import pytest

from epi_python.chapter_05_arrays.pg_048_rearrange_alternation import rearrange_alternation


@pytest.mark.parametrize(("arguments", "expected"), [(([],), []), (([3, 2],), [2, 3]), (([1, 2, 3, 4],), [1, 3, 2, 4]), (([4, 3, 2, 1],), [3, 4, 1, 2])])
def test_cases(arguments, expected):
    assert rearrange_alternation(*arguments) == expected
