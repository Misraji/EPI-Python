"""Parameterized tests for EPI exercise 4.9.

pytest documentation: https://docs.pytest.org/en/stable/how-to/parametrize.html
"""

# pytest is installed as a development dependency, not part of Python itself.
# Documentation: https://docs.pytest.org/en/stable/
import pytest

from epi_python.chapter_04_primitive_types.pg_033_is_number_palindromic import is_number_palindromic


@pytest.mark.parametrize(
    ("arguments", "expected"),
    [((0,), True), ((7,), True), ((121,), True), ((1221,), True), ((123,), False), ((-121,), False), ((10,), False)],
)
def test_examples(arguments, expected):
    """Run book-inspired normal cases and explicitly selected edge cases."""
    observed = is_number_palindromic(*arguments)
    assert observed == expected
