# pytest parameterization: https://docs.pytest.org/en/stable/how-to/parametrize.html
import pytest

from epi_python.chapter_24_honors_class.pg_370_binary_search_unknown_length import binary_search_unknown_length


@pytest.mark.parametrize('a',[[],[1],[1,2,4,6,10],[0,0,0,1,1,5],list(range(26))])
def test_unknown_length(a):
    for val in set(a):
        result=binary_search_unknown_length(a,val)
        assert 0<=result<len(a) and a[result]==val
    assert binary_search_unknown_length(a,999)==-1
    assert binary_search_unknown_length(a,-999)==-1
