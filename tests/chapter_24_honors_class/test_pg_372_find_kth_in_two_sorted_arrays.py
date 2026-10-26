# pytest parameterization: https://docs.pytest.org/en/stable/how-to/parametrize.html
import pytest

from epi_python.chapter_24_honors_class.pg_372_find_kth_in_two_sorted_arrays import find_kth_in_two_sorted_arrays


@pytest.mark.parametrize(('a','b'),[([1,3,6],[2,4,5]),([],[1,2]),([1,1,3],[1,2]),([1,2,3],[]),([1],[2]),([-5,-1],[0,5,11])])
def test_all_ranks(a,b):
    expected=sorted(a+b)
    for k,value in enumerate(expected,1):
        assert find_kth_in_two_sorted_arrays(a,b,k)==value


def test_invalid_rank():
    with pytest.raises(ValueError):
        find_kth_in_two_sorted_arrays([],[],1)
