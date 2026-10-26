# pytest documentation: https://docs.pytest.org/en/stable/
from epi_python.chapter_19_parallel_computing.pg_298_parallel_collatz import collatz_check,parallel_collatz,worker


def test_collatz():
    assert worker(1,100)
    assert collatz_check(27,set())
    assert parallel_collatz(40,max_workers=2,range_size=10)
    assert parallel_collatz(0)
