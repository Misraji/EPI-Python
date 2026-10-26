"""Unit tests for EPI exercise 6.3."""

# pytest parametrization documentation:
# https://docs.pytest.org/en/stable/how-to/parametrize.html
import pytest

from epi_python.chapter_06_strings.pg_070_ss_decode_col_id import ss_decode_col_id


@pytest.mark.parametrize(("arguments", "expected"), [(('A',), 1), (('Z',), 26), (('AA',), 27), (('AB',), 28), (('ZZ',), 702)])
def test_cases(arguments, expected):
    assert ss_decode_col_id(*arguments) == expected


def test_spreadsheet_col_reduce_version():
    from epi_python.chapter_06_strings.pg_070_ss_decode_col_id import ss_decode_col_id,ss_decode_col_id_reduce
    import itertools
    for k in range(1,4):
        for symbols in itertools.product('ABCDYZ', repeat=k):
            col=''.join(symbols)
            assert ss_decode_col_id_reduce(col) == ss_decode_col_id(col)
