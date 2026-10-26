"""Independent tests for EPI 12.3.

pytest parameterization: https://docs.pytest.org/en/stable/how-to/parametrize.html
"""

# pytest enables one test function to run over several examples.
# Documentation: https://docs.pytest.org/en/stable/
import pytest

# Standard library: copies mutable inputs so tests do not share state.
# Documentation: https://docs.python.org/3/library/copy.html
import copy

from epi_python.chapter_12_hash_tables.pg_165_isbn_lru_cache import cache_lookup_history

@pytest.mark.parametrize(("args", "expected"), [
    ((2, [("put",1,10),("put",2,20),("get",1),("put",3,30),("get",2),("get",3)]), [10,-1,30]),
    ((1, [("put",1,10),("put",2,20),("get",1)]), [-1]),
    ((1, [("put",1,10),("put",1,99),("get",1)]), [10]),
])
def test_examples(args, expected):
    """Verify representative and boundary conditions independently."""
    assert cache_lookup_history(*copy.deepcopy(args)) == expected

from epi_python.chapter_12_hash_tables.pg_165_isbn_lru_cache import LRUCache


def test_erase_removes_key():
    cache = LRUCache(2)
    cache.insert(7, 99)
    assert cache.erase(7)
    assert not cache.erase(7)
    assert cache.lookup(7) == -1
