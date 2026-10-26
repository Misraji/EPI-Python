# pytest parameterization: https://docs.pytest.org/en/stable/how-to/parametrize.html
import pytest

from epi_python.chapter_24_honors_class.pg_364_longest_matching_parentheses import longest_matching_parentheses


@pytest.mark.parametrize(('s','length'),[('',0),('(()',2),(')()())',4),('()(())',6),('(()())',6),('(((',0),(')))',0),('())(())',4)])
def test_parentheses(s,length):
    assert longest_matching_parentheses(s)==length
