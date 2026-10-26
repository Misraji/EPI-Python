"""Parameterized tests for EPI exercise 6.12.

pytest documentation: https://docs.pytest.org/en/stable/how-to/parametrize.html
"""

# pytest is installed as a development dependency, not part of Python itself.
# Documentation: https://docs.pytest.org/en/stable/
import pytest

from epi_python.chapter_06_strings.pg_079_run_length_encoding import encoding


@pytest.mark.parametrize(
    ("arguments", "expected"),
    [(('',), ''), (('a',), '1a'), (('aaaabcccaa',), '4a1b3c2a'), (('ab',), '1a1b')],
)
def test_examples(arguments, expected):
    """Run book-inspired normal cases and explicitly selected edge cases."""
    observed = encoding(*arguments)
    assert observed == expected


@pytest.mark.parametrize("text", ["", "a", "aabbbcc", "zzzzzz", "aabbccdd"])
def test_round_trip(text):
    from epi_python.chapter_06_strings.pg_079_run_length_encoding import decoding
    assert decoding(encoding(text)) == text
