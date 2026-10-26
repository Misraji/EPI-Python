"""Unit tests for EPI exercise 15.4."""

# pytest parametrization documentation:
# https://docs.pytest.org/en/stable/how-to/parametrize.html
import pytest

from epi_python.chapter_15_recursion.pg_224_generate_power_set import generate_power_set


@pytest.mark.parametrize(("arguments", "expected"), [(([],), [[]]), (([1],), [[], [1]]), (([1, 2],), [[], [1], [2], [1, 2]])])
def test_cases(arguments, expected):
    assert generate_power_set(*arguments) == expected
