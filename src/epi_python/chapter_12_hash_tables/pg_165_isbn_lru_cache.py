"""EPI exercise 12.3, printed page 165: Implement an ISBN cache.

EDUCATIONAL RECONSTRUCTION — not a verbatim verified code transcription.
Problem: Implement an ISBN cache.
Method/complexity: OrderedDict LRU; expected O(1) lookup/insert/erase, O(capacity) memory.
For the book's original explanation and variants, see:
    pg_165_exercise_12_03_implement_an_isbn_cache.md

Run: python -m epi_python.chapter_12_hash_tables.pg_165_isbn_lru_cache
Test: python -m pytest tests/chapter_12_hash_tables/test_pg_165_isbn_lru_cache.py -v
"""

# OrderedDict preserves insertion order and supports move_to_end/popitem.
# Documentation: https://docs.python.org/3/library/collections.html#collections.OrderedDict
from collections import OrderedDict


class LRUCache:
    """ISBN-to-price cache evicting the least recently accessed key."""
    def __init__(self, capacity: int):
        if capacity <= 0:
            raise ValueError("Capacity must be positive")
        self.capacity = capacity
        self._prices: OrderedDict[int, int] = OrderedDict()

    def lookup(self, isbn: int) -> int:
        if isbn not in self._prices:
            return -1
        # move_to_end marks this lookup as the most recent access.
        self._prices.move_to_end(isbn)
        return self._prices[isbn]

    def insert(self, isbn: int, price: int) -> None:
        if isbn in self._prices:
            # EPI's cache leaves the existing price unchanged on a repeated insert.
            self._prices.move_to_end(isbn)
            return
        self._prices[isbn] = price
        if len(self._prices) > self.capacity:
            # popitem(last=False) removes the oldest entry, not the newest one.
            self._prices.popitem(last=False)

    def erase(self, isbn: int) -> bool:
        return self._prices.pop(isbn, None) is not None


def cache_lookup_history(capacity: int, operations: list[tuple]) -> list[int]:
    cache = LRUCache(capacity)
    result = []
    for operation in operations:
        if operation[0] == 'put':
            cache.insert(operation[1], operation[2])
        elif operation[0] == 'get':
            result.append(cache.lookup(operation[1]))
        elif operation[0] == 'erase':
            cache.erase(operation[1])
    return result


if __name__ == "__main__":
    ops=[("put",1,10),("put",2,20),("get",1),("put",3,30),("get",2)]
    print("ISBN cache lookups:", cache_lookup_history(2, ops))
    assert cache_lookup_history(2, ops) == [10,-1]
