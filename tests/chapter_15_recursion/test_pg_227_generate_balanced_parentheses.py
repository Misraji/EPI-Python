"""Unit tests for EPI exercise 15.6."""

# pytest parametrization documentation:
# https://docs.pytest.org/en/stable/how-to/parametrize.html
import pytest

from epi_python.chapter_15_recursion.pg_227_generate_balanced_parentheses import generate_balanced_parentheses


@pytest.mark.parametrize(("arguments", "expected"), [((0,), ['']), ((1,), ['()']), ((2,), ['(())', '()()'])])
def test_cases(arguments, expected):
    assert generate_balanced_parentheses(*arguments) == expected
