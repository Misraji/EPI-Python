"""Unit tests for EPI exercise 10.1."""

# pytest parametrization documentation:
# https://docs.pytest.org/en/stable/how-to/parametrize.html
import pytest

from epi_python.chapter_10_heaps.pg_134_merge_sorted_arrays import merge_sorted_arrays


@pytest.mark.parametrize(("arguments", "expected"), [(([],), []), (([[1, 3], [2, 4]],), [1, 2, 3, 4]), (([[], [1, 1], [0]],), [0, 1, 1])])
def test_cases(arguments, expected):
    assert merge_sorted_arrays(*arguments) == expected
