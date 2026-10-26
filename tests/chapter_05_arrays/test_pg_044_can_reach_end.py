"""Parameterized tests for EPI exercise 5.4.

pytest documentation: https://docs.pytest.org/en/stable/how-to/parametrize.html
"""

# pytest is installed as a development dependency, not part of Python itself.
# Documentation: https://docs.pytest.org/en/stable/
import pytest

from epi_python.chapter_05_arrays.pg_044_can_reach_end import can_reach_end


@pytest.mark.parametrize(
    ("arguments", "expected"),
    [(([3, 3, 1, 0, 2, 0, 1],), True), (([3, 2, 0, 0, 2, 0, 1],), False), (([0],), True), (([],), True), (([0, 1],), False)],
)
def test_examples(arguments, expected):
    """Run book-inspired normal cases and explicitly selected edge cases."""
    observed = can_reach_end(*arguments)
    assert observed == expected


def test_reachable_in_one_jump():
    assert can_reach_end([10, 0, 0, 0])
