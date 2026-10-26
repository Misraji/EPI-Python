"""Unit tests for EPI exercise 10.3."""

# pytest parametrization documentation:
# https://docs.pytest.org/en/stable/how-to/parametrize.html
import pytest

from epi_python.chapter_10_heaps.pg_136_sort_approximately_sorted_array import sort_approximately_sorted_array


@pytest.mark.parametrize(("arguments", "expected"), [(([], 0), []), (([2, 1, 3], 1), [1, 2, 3]), (([3, 1, 2], 2), [1, 2, 3]), (([1, 2, 3], 0), [1, 2, 3])])
def test_cases(arguments, expected):
    assert sort_approximately_sorted_array(*arguments) == expected
