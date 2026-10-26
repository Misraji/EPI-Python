"""Parameterized tests for EPI exercise 5.20.

pytest documentation: https://docs.pytest.org/en/stable/how-to/parametrize.html
"""

# pytest is installed as a development dependency, not part of Python itself.
# Documentation: https://docs.pytest.org/en/stable/
import pytest

from epi_python.chapter_05_arrays.pg_065_generate_pascal_triangle import generate_pascal_triangle


@pytest.mark.parametrize(
    ("arguments", "expected"),
    [((0,), []), ((1,), [[1]]), ((3,), [[1], [1, 1], [1, 2, 1]]), ((5,), [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]])],
)
def test_examples(arguments, expected):
    """Run book-inspired normal cases and explicitly selected edge cases."""
    observed = generate_pascal_triangle(*arguments)
    assert observed == expected
