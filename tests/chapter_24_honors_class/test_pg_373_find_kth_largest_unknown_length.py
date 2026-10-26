# pytest parameterization: https://docs.pytest.org/en/stable/how-to/parametrize.html
import pytest

from epi_python.chapter_24_honors_class.pg_373_find_kth_largest_unknown_length import find_kth_largest_unknown_length


@pytest.mark.parametrize('data',[[3,1,5,2,4],[1,1,1,1,1],list(range(20)),[5,5,7,3,7,1],[-3,-1,-7,-4]])
def test_ranks(data):
    for k in range(1,len(data)+1):
        assert find_kth_largest_unknown_length(iter(data),k)==sorted(data,reverse=True)[k-1]


def test_invalid():
    with pytest.raises(ValueError):
        find_kth_largest_unknown_length([],1)
