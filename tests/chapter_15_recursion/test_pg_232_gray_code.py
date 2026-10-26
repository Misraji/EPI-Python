# pytest documentation: https://docs.pytest.org/en/stable/
import pytest

from epi_python.chapter_15_recursion.pg_232_gray_code import gray_code, gray_code_backtracking


def one_bit(a,b):
    diff=a^b
    return diff>0 and diff&(diff-1)==0


@pytest.mark.parametrize('n', [1,2,3,4])
def test_gray_cycles(n):
    for fn in (gray_code, gray_code_backtracking):
        values=fn(n)
        assert set(values)==set(range(1<<n))
        assert all(one_bit(a,b) for a,b in zip(values,values[1:]+values[:1]))
