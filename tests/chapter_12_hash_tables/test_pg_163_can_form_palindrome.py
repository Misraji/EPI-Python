"""Parameterized tests for EPI exercise 12.1.

pytest documentation: https://docs.pytest.org/en/stable/how-to/parametrize.html
"""

# pytest is installed as a development dependency, not part of Python itself.
# Documentation: https://docs.pytest.org/en/stable/
import pytest

from epi_python.chapter_12_hash_tables.pg_163_can_form_palindrome import can_form_palindrome


@pytest.mark.parametrize(
    ("arguments", "expected"),
    [(('edified',), True), (('aab',), True), (('abc',), False), (('',), True), (('a',), True)],
)
def test_examples(arguments, expected):
    """Run book-inspired normal cases and explicitly selected edge cases."""
    observed = can_form_palindrome(*arguments)
    assert observed == expected
