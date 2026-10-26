"""Unit tests for EPI exercise 5.7."""

# pytest parametrization documentation:
# https://docs.pytest.org/en/stable/how-to/parametrize.html
import pytest

from epi_python.chapter_05_arrays.pg_047_buy_and_sell_stock_twice import buy_and_sell_stock_twice


@pytest.mark.parametrize(("arguments", "expected"), [(([],), 0.0), (([1, 5],), 4.0), (([1, 5, 2, 10],), 12.0), (([5, 4, 3, 2],), 0.0)])
def test_cases(arguments, expected):
    assert buy_and_sell_stock_twice(*arguments) == expected


def test_two_stock_transactions_against_bruteforce():
    from epi_python.chapter_05_arrays.pg_047_buy_and_sell_stock_twice import buy_and_sell_stock_twice
    import random
    r=random.Random(5707)
    for _ in range(500):
        data=[r.randrange(1,25) for _ in range(r.randrange(12))]
        want=0.0
        for split in range(len(data)+1):
            left=max([data[j]-data[i] for i in range(split) for j in range(i+1,split)]+[0])
            right=max([data[j]-data[i] for i in range(split,len(data)) for j in range(i+1,len(data))]+[0])
            want=max(want,left+right)
        assert buy_and_sell_stock_twice(data)==want
