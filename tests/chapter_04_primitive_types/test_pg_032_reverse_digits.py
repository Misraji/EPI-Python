"""Parameterized tests for EPI exercise 4.8.

pytest documentation: https://docs.pytest.org/en/stable/how-to/parametrize.html
"""

# pytest is installed as a development dependency, not part of Python itself.
# Documentation: https://docs.pytest.org/en/stable/
import pytest

from epi_python.chapter_04_primitive_types.pg_032_reverse_digits import reverse_digits


@pytest.mark.parametrize(
    ("arguments", "expected"),
    [((0,), 0), ((123,), 321), ((-123,), -321), ((120,), 21), ((1,), 1)],
)
def test_examples(arguments, expected):
    """Run book-inspired normal cases and explicitly selected edge cases."""
    observed = reverse_digits(*arguments)
    assert observed == expected
