"""Unit tests for EPI exercise 6.3."""

# pytest parametrization documentation:
# https://docs.pytest.org/en/stable/how-to/parametrize.html
import pytest

from epi_python.chapter_06_strings.pg_070_ss_decode_col_id import ss_decode_col_id


@pytest.mark.parametrize(("arguments", "expected"), [(('A',), 1), (('Z',), 26), (('AA',), 27), (('AB',), 28), (('ZZ',), 702)])
def test_cases(arguments, expected):
    assert ss_decode_col_id(*arguments) == expected
