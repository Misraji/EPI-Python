"""Parameterized tests for EPI exercise 5.5.

pytest documentation: https://docs.pytest.org/en/stable/how-to/parametrize.html
"""

# pytest is installed as a development dependency, not part of Python itself.
# Documentation: https://docs.pytest.org/en/stable/
import pytest

from epi_python.chapter_05_arrays.pg_045_delete_duplicates import delete_duplicates


@pytest.mark.parametrize(
    ("arguments", "expected"),
    [(([1, 1, 2, 2, 3],), [1, 2, 3]), (([1, 2, 3],), [1, 2, 3]), (([],), []), (([1, 1, 1],), [1])],
)
def test_examples(arguments, expected):
    """Run book-inspired normal cases and explicitly selected edge cases."""
    observed = delete_duplicates(*arguments)
    assert arguments[0][:observed] == expected
