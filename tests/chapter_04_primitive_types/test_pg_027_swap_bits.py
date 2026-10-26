"""Parameterized tests for EPI exercise 4.2.

pytest documentation: https://docs.pytest.org/en/stable/how-to/parametrize.html
"""

# pytest is installed as a development dependency, not part of Python itself.
# Documentation: https://docs.pytest.org/en/stable/
import pytest

from epi_python.chapter_04_primitive_types.pg_027_swap_bits import swap_bits


@pytest.mark.parametrize(
    ("arguments", "expected"),
    [((8, 0, 3), 1), ((9, 0, 3), 9), ((0, 1, 2), 0), ((1, 0, 0), 1)],
)
def test_examples(arguments, expected):
    """Run book-inspired normal cases and explicitly selected edge cases."""
    observed = swap_bits(*arguments)
    assert observed == expected
