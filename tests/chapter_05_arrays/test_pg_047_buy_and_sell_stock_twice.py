"""Unit tests for EPI exercise 5.7."""

# pytest parametrization documentation:
# https://docs.pytest.org/en/stable/how-to/parametrize.html
import pytest

from epi_python.chapter_05_arrays.pg_047_buy_and_sell_stock_twice import buy_and_sell_stock_twice


@pytest.mark.parametrize(("arguments", "expected"), [(([],), 0.0), (([1, 5],), 4.0), (([1, 5, 2, 10],), 12.0), (([5, 4, 3, 2],), 0.0)])
def test_cases(arguments, expected):
    assert buy_and_sell_stock_twice(*arguments) == expected
