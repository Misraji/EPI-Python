# pytest parameterization: https://docs.pytest.org/en/stable/how-to/parametrize.html
import pytest

from epi_python.chapter_24_honors_class.pg_385_count_inversions import count_inversions


@pytest.mark.parametrize('data',[[],[1],[2,1],[3,6,4,2,5,1],[1,2,3],[3,2,1],[2,2,1,1]])
def test_inversions(data):
    oracle=sum(data[i]>data[j] for i in range(len(data)) for j in range(i+1,len(data)))
    a=data[:]
    assert count_inversions(a)==oracle
    assert a==sorted(data)
