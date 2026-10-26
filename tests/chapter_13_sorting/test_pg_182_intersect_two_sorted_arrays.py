"""Parameterized tests for EPI exercise 13.1.

pytest documentation: https://docs.pytest.org/en/stable/how-to/parametrize.html
"""

# pytest is installed as a development dependency, not part of Python itself.
# Documentation: https://docs.pytest.org/en/stable/
import pytest

from epi_python.chapter_13_sorting.pg_182_intersect_two_sorted_arrays import intersect_two_sorted_arrays


@pytest.mark.parametrize(
    ("arguments", "expected"),
    [(([], []), []), (([1, 2, 2, 3], [2, 2, 3, 4]), [2, 3]), (([1, 3], [2, 4]), []), (([1, 1], [1]), [1])],
)
def test_examples(arguments, expected):
    """Run book-inspired normal cases and explicitly selected edge cases."""
    observed = intersect_two_sorted_arrays(*arguments)
    assert observed == expected
