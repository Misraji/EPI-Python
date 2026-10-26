# pytest parameterization: https://docs.pytest.org/en/stable/how-to/parametrize.html
import pytest

from epi_python.chapter_24_honors_class.pg_380_is_match import is_match


@pytest.mark.parametrize(('regex','s','expected'), [('', 'abc',True),('abc','zabcx',True),('^abc$','abc',True),('^abc$','abcd',False),('a.c','zzabc',True),('ab*c','ac',True),('ab*c','abbbc',True),('ab*c','abbd',False),('^a.*z$','abcz',True),('^a.*z$','za',False),('^$','',True)])
def test_regular_expression(regex,s,expected):
    assert is_match(regex,s) is expected
