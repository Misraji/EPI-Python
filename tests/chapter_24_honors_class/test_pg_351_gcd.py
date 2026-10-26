"""Parameterized tests for EPI exercise 24.1.

pytest documentation: https://docs.pytest.org/en/stable/how-to/parametrize.html
"""

# pytest is installed as a development dependency, not part of Python itself.
# Documentation: https://docs.pytest.org/en/stable/
import pytest

from epi_python.chapter_24_honors_class.pg_351_gcd import gcd


@pytest.mark.parametrize(
    ("arguments", "expected"),
    [((0, 0), 0), ((20, 8), 4), ((17, 13), 1), ((-12, 18), 6), ((100, 10), 10)],
)
def test_examples(arguments, expected):
    """Run book-inspired normal cases and explicitly selected edge cases."""
    observed = gcd(*arguments)
    assert observed == expected
