"""Pytest verification for EPI 13.2 (printed page 183)."""

# pytest parameterization lets one test cover many sets of arguments.
# Documentation: https://docs.pytest.org/en/stable/how-to/parametrize.html
import pytest

from epi_python.chapter_13_sorting.pg_183_merge_two_sorted_arrays import merge_two_sorted_arrays


@pytest.mark.parametrize(('a', 'm', 'b', 'expected'), [
    ([1, 4, None, None], 2, [2, 3], [1, 2, 3, 4]),
    ([None, None], 0, [1, 2], [1, 2]),
    ([1, 2], 2, [], [1, 2]),
    ([5, 6, None], 2, [1], [1, 5, 6]),
    ([1, 1, None, None], 2, [1, 1], [1, 1, 1, 1]),
])
def test_merge(a, m, b, expected):
    merge_two_sorted_arrays(a, m, b, len(b))
    assert a == expected


def test_capacity_check():
    with pytest.raises(ValueError):
        merge_two_sorted_arrays([1], 1, [2], 1)
