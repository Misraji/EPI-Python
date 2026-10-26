"""Unit tests for EPI exercise 10.1."""

# pytest parametrization documentation:
# https://docs.pytest.org/en/stable/how-to/parametrize.html
import pytest

from epi_python.chapter_10_heaps.pg_134_merge_sorted_arrays import merge_sorted_arrays


@pytest.mark.parametrize(("arguments", "expected"), [(([],), []), (([[1, 3], [2, 4]],), [1, 2, 3, 4]), (([[], [1, 1], [0]],), [0, 1, 1])])
def test_cases(arguments, expected):
    assert merge_sorted_arrays(*arguments) == expected


def test_both_textbook_kway_merge_implementations():
    """Both variants must match an independent concatenate/sort reference."""
    from random import Random
    from epi_python.chapter_10_heaps.pg_134_merge_sorted_arrays import merge_sorted_arrays_pythonic

    rng = Random(10101)
    for _ in range(500):
        arrays = [sorted(rng.choices(range(-8, 9), k=rng.randrange(11)))
                  for _ in range(rng.randrange(8))]
        expected = sorted(value for array in arrays for value in array)
        assert merge_sorted_arrays(arrays) == expected
        assert merge_sorted_arrays_pythonic(arrays) == expected
