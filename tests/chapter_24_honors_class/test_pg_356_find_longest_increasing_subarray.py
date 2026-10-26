# pytest parameterization: https://docs.pytest.org/en/stable/how-to/parametrize.html
import pytest

from epi_python.chapter_24_honors_class.pg_356_find_longest_increasing_subarray import find_longest_increasing_subarray


@pytest.mark.parametrize('a',[[],[1],[1,2,3],[3,2,1],[1,1,2,3,0,2],[1,2,3,1,4,6,7],[3,4,1,2,3,4]])
def test_longest(a):
    result=find_longest_increasing_subarray(a)
    length=max((e-s+1 for s in range(len(a)) for e in range(s,len(a)) if all(a[k-1]<a[k] for k in range(s+1,e+1))),default=0)
    assert result.end-result.start+1==length
    assert all(a[k-1]<a[k] for k in range(result.start+1,result.end+1))
