"""Parameterized tests for EPI exercise 6.5.

pytest documentation: https://docs.pytest.org/en/stable/how-to/parametrize.html
"""

# pytest is installed as a development dependency, not part of Python itself.
# Documentation: https://docs.pytest.org/en/stable/
import pytest

from epi_python.chapter_06_strings.pg_072_is_palindromic import is_palindromic


@pytest.mark.parametrize(
    ("arguments", "expected"),
    [(('A man, a plan, a canal, Panama',), True), (('Able was I, ere I saw Elba!',), True), (('abc',), False), (('',), True), (('12321',), True)],
)
def test_examples(arguments, expected):
    """Run book-inspired normal cases and explicitly selected edge cases."""
    observed = is_palindromic(*arguments)
    assert observed == expected
