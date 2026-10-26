# pytest documentation: https://docs.pytest.org/en/stable/
from epi_python.chapter_19_parallel_computing.pg_294_thread_pool_server import process_requests


def test_thread_pool():
    assert process_requests(range(100),lambda n:n*n,max_workers=3)==[n*n for n in range(100)]
    assert process_requests([],str)==[]
