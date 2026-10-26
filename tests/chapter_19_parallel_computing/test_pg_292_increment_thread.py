# pytest documentation: https://docs.pytest.org/en/stable/
from epi_python.chapter_19_parallel_computing.pg_292_increment_thread import run_unsynchronized_increments


def test_counter_non_determinism_not_assumed():
    assert run_unsynchronized_increments(0)==0
    for n in [1,10,100]:
        assert 1<=run_unsynchronized_increments(n)<=2*n
