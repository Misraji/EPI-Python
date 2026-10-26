"""Unit tests for EPI exercise 6.10."""

# pytest parametrization documentation:
# https://docs.pytest.org/en/stable/how-to/parametrize.html
import pytest

from epi_python.chapter_06_strings.pg_077_get_valid_ip_addresses import get_valid_ip_addresses


@pytest.mark.parametrize(("arguments", "expected"), [(('0000',), ['0.0.0.0']), (('1111',), ['1.1.1.1']), (('123',), []), (('9999',), ['9.9.9.9'])])
def test_cases(arguments, expected):
    assert get_valid_ip_addresses(*arguments) == expected
