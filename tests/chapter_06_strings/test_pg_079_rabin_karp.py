"""Unit tests for EPI exercise 6.13."""

# pytest parametrization documentation:
# https://docs.pytest.org/en/stable/how-to/parametrize.html
import pytest

from epi_python.chapter_06_strings.pg_079_rabin_karp import rabin_karp


@pytest.mark.parametrize(("arguments", "expected"), [(('hello world', 'world'), 6), (('abcabc', 'cab'), 2), (('abc', 'z'), -1), (('abc', ''), 0)])
def test_cases(arguments, expected):
    assert rabin_karp(*arguments) == expected
