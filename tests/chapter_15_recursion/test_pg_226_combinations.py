"""Unit tests for EPI exercise 15.5."""

# pytest parametrization documentation:
# https://docs.pytest.org/en/stable/how-to/parametrize.html
import pytest

from epi_python.chapter_15_recursion.pg_226_combinations import combinations


@pytest.mark.parametrize(("arguments", "expected"), [((0, 0), [[]]), ((3, 0), [[]]), ((3, 2), [[1, 2], [1, 3], [2, 3]]), ((2, 3), [])])
def test_cases(arguments, expected):
    assert combinations(*arguments) == expected
