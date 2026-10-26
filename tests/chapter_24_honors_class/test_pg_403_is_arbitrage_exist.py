# pytest documentation: https://docs.pytest.org/en/stable/
from epi_python.chapter_24_honors_class.pg_403_is_arbitrage_exist import is_arbitrage_exist


def test_arbitrage():
    assert is_arbitrage_exist([[1,2,1],[0.5,1,2],[0.3,0.5,1]])
    assert not is_arbitrage_exist([[1,2,4],[0.5,1,2],[0.25,0.5,1]])
    assert not is_arbitrage_exist([[1]])
    assert not is_arbitrage_exist([])
