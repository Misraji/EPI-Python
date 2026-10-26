# pytest parameterization: https://docs.pytest.org/en/stable/how-to/parametrize.html
import pytest

from epi_python.chapter_24_honors_class.pg_353_buy_and_sell_stock_k_times import buy_and_sell_stock_k_times


@pytest.mark.parametrize(('prices','k','expected'), [
    ([],2,0),([5],2,0),([3,2,6,5,0,3],2,7),([1,2,3,4,5],2,4),([7,6,4,3,1],5,0),([1,2],0,0),([2,4,1],2,2)])
def test_profit(prices,k,expected):
    assert buy_and_sell_stock_k_times(prices,k)==expected
