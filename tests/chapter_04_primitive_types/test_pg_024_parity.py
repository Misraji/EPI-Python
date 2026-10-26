"""Parameterized tests for EPI exercise 4.1.

pytest documentation: https://docs.pytest.org/en/stable/how-to/parametrize.html
"""

# pytest is installed as a development dependency, not part of Python itself.
# Documentation: https://docs.pytest.org/en/stable/
import pytest

from epi_python.chapter_04_primitive_types.pg_024_parity import parity


@pytest.mark.parametrize(
    ("arguments", "expected"),
    [((0,), 0), ((1,), 1), ((3,), 0), ((7,), 1), ((10,), 0), ((15,), 0)],
)
def test_examples(arguments, expected):
    """Run book-inspired normal cases and explicitly selected edge cases."""
    observed = parity(*arguments)
    assert observed == expected
