"""Parameterized tests for EPI exercise 11.1.

pytest documentation: https://docs.pytest.org/en/stable/how-to/parametrize.html
"""

# pytest is installed as a development dependency, not part of Python itself.
# Documentation: https://docs.pytest.org/en/stable/
import pytest

from epi_python.chapter_11_searching.pg_145_search_first_of_k import search_first_of_k


@pytest.mark.parametrize(
    ("arguments", "expected"),
    [(([], 5), -1), (([1, 2, 2, 2, 3], 2), 1), (([1, 2, 3], 1), 0), (([1, 2, 3], 9), -1), (([3, 3, 3], 3), 0)],
)
def test_examples(arguments, expected):
    """Run book-inspired normal cases and explicitly selected edge cases."""
    observed = search_first_of_k(*arguments)
    assert observed == expected
