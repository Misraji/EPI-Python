"""Parameterized tests for EPI exercise 4.4.

pytest documentation: https://docs.pytest.org/en/stable/how-to/parametrize.html
"""

# pytest is installed as a development dependency, not part of Python itself.
# Documentation: https://docs.pytest.org/en/stable/
import pytest

from epi_python.chapter_04_primitive_types.pg_028_closest_int_same_bit_count import closest_int_same_bit_count


@pytest.mark.parametrize(
    ("arguments", "expected"),
    [((6, 8), 5), ((7, 8), 11), ((8, 8), 4), ((10, 8), 9)],
)
def test_examples(arguments, expected):
    """Run book-inspired normal cases and explicitly selected edge cases."""
    observed = closest_int_same_bit_count(*arguments)
    assert observed == expected
