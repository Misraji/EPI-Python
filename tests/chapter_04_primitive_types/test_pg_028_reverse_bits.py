"""Parameterized tests for EPI exercise 4.3.

pytest documentation: https://docs.pytest.org/en/stable/how-to/parametrize.html
"""

# pytest is installed as a development dependency, not part of Python itself.
# Documentation: https://docs.pytest.org/en/stable/
import pytest

from epi_python.chapter_04_primitive_types.pg_028_reverse_bits import reverse_bits


@pytest.mark.parametrize(
    ("arguments", "expected"),
    [((0, 8), 0), ((1, 8), 128), ((3, 4), 12), ((5, 4), 10), ((255, 8), 255)],
)
def test_examples(arguments, expected):
    """Run book-inspired normal cases and explicitly selected edge cases."""
    observed = reverse_bits(*arguments)
    assert observed == expected
