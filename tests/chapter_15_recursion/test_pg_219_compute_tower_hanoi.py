"""Parameterized tests for EPI exercise 15.1.

pytest documentation: https://docs.pytest.org/en/stable/how-to/parametrize.html
"""

# pytest is installed as a development dependency, not part of Python itself.
# Documentation: https://docs.pytest.org/en/stable/
import pytest

from epi_python.chapter_15_recursion.pg_219_compute_tower_hanoi import compute_tower_hanoi


@pytest.mark.parametrize(
    ("arguments", "expected"),
    [((0,), []), ((1,), [(0, 1)]), ((2,), [(0, 2), (0, 1), (2, 1)]), ((3,), [(0, 1), (0, 2), (1, 2), (0, 1), (2, 0), (2, 1), (0, 1)])],
)
def test_examples(arguments, expected):
    """Run book-inspired normal cases and explicitly selected edge cases."""
    observed = compute_tower_hanoi(*arguments)
    assert observed == expected
