"""Parameterized tests for EPI exercise 17.4.

pytest documentation: https://docs.pytest.org/en/stable/how-to/parametrize.html
"""

# pytest is installed as a development dependency, not part of Python itself.
# Documentation: https://docs.pytest.org/en/stable/
import pytest

from epi_python.chapter_17_greedy_algorithms_and_invariants.pg_264_has_three_sum import has_three_sum


@pytest.mark.parametrize(
    ("arguments", "expected"),
    [(([], 0), False), (([1, 2, 3], 6), True), (([1, 2, 3], 9), True), (([1, 2, 3], 0), False), (([0], 0), True)],
)
def test_examples(arguments, expected):
    """Run book-inspired normal cases and explicitly selected edge cases."""
    observed = has_three_sum(*arguments)
    assert observed == expected
