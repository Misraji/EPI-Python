"""Parameterized tests for EPI exercise 16.2.

pytest documentation: https://docs.pytest.org/en/stable/how-to/parametrize.html
"""

# pytest is installed as a development dependency, not part of Python itself.
# Documentation: https://docs.pytest.org/en/stable/
import pytest

from epi_python.chapter_16_dynamic_programming.pg_239_levenshtein_distance import levenshtein_distance


@pytest.mark.parametrize(
    ("arguments", "expected"),
    [(('', ''), 0), (('cat', 'cat'), 0), (('cat', 'cut'), 1), (('kitten', 'sitting'), 3), (('a', ''), 1)],
)
def test_examples(arguments, expected):
    """Run book-inspired normal cases and explicitly selected edge cases."""
    observed = levenshtein_distance(*arguments)
    assert observed == expected
