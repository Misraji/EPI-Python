# pytest documentation: https://docs.pytest.org/en/stable/
from epi_python.chapter_19_parallel_computing.pg_295_account_transfer import Account


def test_transfers_concurrently():
    a,b=Account(1000),Account(1000)
    jobs=[Account.transfer(a,b,1) for _ in range(100)]+[Account.transfer(b,a,1) for _ in range(100)]
    for job in jobs:
        job.join(timeout=2)
        assert not job.is_alive()
    assert a.get_balance()==1000
    assert b.get_balance()==1000
