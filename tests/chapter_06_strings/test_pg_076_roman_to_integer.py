"""Parameterized tests for EPI exercise 6.9.

pytest documentation: https://docs.pytest.org/en/stable/how-to/parametrize.html
"""

# pytest is installed as a development dependency, not part of Python itself.
# Documentation: https://docs.pytest.org/en/stable/
import pytest

from epi_python.chapter_06_strings.pg_076_roman_to_integer import roman_to_integer


@pytest.mark.parametrize(
    ("arguments", "expected"),
    [(('I',), 1), (('IV',), 4), (('IX',), 9), (('XIV',), 14), (('MCMXCIV',), 1994), (('',), 0)],
)
def test_examples(arguments, expected):
    """Run book-inspired normal cases and explicitly selected edge cases."""
    observed = roman_to_integer(*arguments)
    assert observed == expected
