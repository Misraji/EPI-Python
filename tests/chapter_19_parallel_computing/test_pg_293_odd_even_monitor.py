# pytest documentation: https://docs.pytest.org/en/stable/
import pytest

from epi_python.chapter_19_parallel_computing.pg_293_odd_even_monitor import print_in_order


@pytest.mark.parametrize('n',[2,4,6,10,20,100])
def test_thread_order(n):
    assert print_in_order(n)==list(range(1,n+1))
