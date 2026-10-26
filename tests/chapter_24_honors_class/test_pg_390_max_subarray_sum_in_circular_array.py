"""Parameterized checks of EPI 24.28 educational solution."""

# pytest API: https://docs.pytest.org/en/stable/how-to/parametrize.html
import pytest

from epi_python.chapter_24_honors_class.pg_390_max_subarray_sum_in_circular_array import max_subarray_sum_in_circular_array


@pytest.mark.parametrize(("arguments", "expected"), [(([],), 0), (([1, 2, -4, 3],), 6), (([-2, -1, -5],), -1), (([5, -3, 5],), 10)])
def test_examples(arguments, expected):
    assert max_subarray_sum_in_circular_array(*arguments) == expected
