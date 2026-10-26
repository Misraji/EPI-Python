"""EPI Python — Exercise 12.3: Implement an ISBN Cache

Chapter 12: Hash Tables
Textbook: pages 165–166 (printed page numbers; problem, solution and the
start of the program on 165, rest of program and complexity on 166).

PROBLEM (from the textbook)
---------------------------
"The International Standard Book Number (ISBN) is a unique commercial book
identifier. It is a string of length 10. The first 9 characters are
digits; the last character is a check character. The check character is
the sum of the first 9 digits, mod 11, with 10 represented by 'X'. (Modern
ISBNs use 13 digits, and the check digit is taken mod 10; this problem is
concerned with 10-digit ISBNs.)

Create a cache for looking up prices of books identified by their ISBN. You
implement lookup, insert, and remove methods. Use the Least Recently Used
(LRU) policy for cache eviction. If an ISBN is already present, insert
should not change the price, but it should update that entry to be the most
recently used entry. Lookup should also update that entry to be the most
recently used entry."

HINT (from the textbook)
------------------------
"Amortize the cost of deletion. Alternatively, use an auxiliary data
structure."

SOLUTION DEVELOPMENT (following the textbook)
---------------------------------------------
Hash tables are ideal for fast lookups: use ISBNs as keys, and store as the
value both the price and the time of the most recent lookup of that key.

That gives O(1) lookups on cache hits, and O(1) inserts until the cache is
full. Once it is full, adding an entry requires finding the least recently
used entry to evict, which takes O(n) time for a cache of size n.

Option 1 -- lazy garbage collection (amortizing deletion): for a cache of
size n, do not delete anything until the table grows to 2n entries. Then
scan the whole table, find the median age of the items, and discard
everything older than the median. One such cleanup costs O(n) in the worst
case but happens at most once every n operations, so deletion is O(1)
amortized. Drawbacks: some lookups that miss on a full cache take O(n)
time, and memory use grows by O(n).

Option 2 -- an auxiliary queue of keys: keep a separate queue of keys, and
in the hash table store, for each key, a reference to its position in the
queue. Whenever an ISBN is looked up and found, move it to the front of the
queue. (This needs a linked-list queue, so that an item in the middle can
be moved to the head.) When a new element is added and the queue's length
exceeds n, delete the item at the tail of the queue from both the queue and
the hash table.

The book's program realises option 2 with collections.OrderedDict, a
dictionary that remembers the order of its keys. This file's LRUCache
class follows that program.

ADDITIONAL EXAMPLES (added for learning; not printed in this exercise)
---------------------------------------------------------------------
With capacity 2:
    put(1, 10), put(2, 20)  -> cache holds 1 and 2
    get(1)                  -> 10 (1 becomes most recently used)
    put(3, 30)              -> evicts 2, the least recently used
    get(2)                  -> -1 (no longer cached)
"""

# Python standard library: specialized container types.
# Module documentation: https://docs.python.org/3/library/collections.html
# OrderedDict API: https://docs.python.org/3/library/collections.html#collections.OrderedDict
#
# `from collections import OrderedDict` imports just that one name, so the
# code can write OrderedDict(...) instead of collections.OrderedDict(...).
from collections import OrderedDict


class LRUCache:
    """ISBN-to-price cache evicting the least recently accessed key.

    This is the textbook's LRUCache class (lookup / insert / erase built on
    an OrderedDict), with type hints, a capacity check, and
    OrderedDict.move_to_end used to refresh recency.
    """

    # __init__ is the constructor, run when LRUCache(capacity) is called.
    # `self` is the new object; attributes set on it persist between calls.
    # Type hints (`capacity: int`) are not enforced by Python.
    def __init__(self, capacity: int):

        # A cache that can hold nothing is rejected. (Check added in this
        # file; not in the book.)
        # ValueError: https://docs.python.org/3/library/exceptions.html#ValueError
        if capacity <= 0:
            raise ValueError("Capacity must be positive")
        self.capacity = capacity

        # OrderedDict is a dict subclass that keeps keys in an order that
        # can be changed cheaply: move_to_end() moves a key to either end,
        # and popitem(last=False) removes the key at the front. Here the
        # front is the least recently used ISBN and the end is the most
        # recently used -- the book's linked-list queue plus hash table in
        # one object, with O(1) operations.
        #
        # `self._prices: OrderedDict[int, int] = ...` is an annotated
        # assignment: it documents that keys (ISBNs) and values (prices) are
        # ints. The leading underscore is a convention meaning "internal;
        # not part of the public interface".
        self._prices: OrderedDict[int, int] = OrderedDict()

    def lookup(self, isbn: int) -> int:
        """Return the price for isbn (marking it most recent), or -1."""

        # `in` on a mapping tests whether the key is present (O(1) expected).
        if isbn not in self._prices:
            return -1
        # move_to_end marks this lookup as the most recent access.
        #
        # OrderedDict.move_to_end(key) moves an existing key to the end
        # (last=True is the default); it raises KeyError if the key is
        # missing, which cannot happen after the check above.
        # Documentation: https://docs.python.org/3/library/collections.html#collections.OrderedDict.move_to_end
        self._prices.move_to_end(isbn)
        return self._prices[isbn]

    def insert(self, isbn: int, price: int) -> None:
        """Add isbn -> price; an existing ISBN keeps its price but is refreshed.

        `-> None` means the method returns no useful value.
        """
        if isbn in self._prices:
            # EPI's cache leaves the existing price unchanged on a repeated insert.
            # (Book's comment: we add the value for key only if key is not
            # present -- we don't update existing values.) Only the recency
            # is refreshed, and the bare `return` leaves the method.
            self._prices.move_to_end(isbn)
            return

        # Assigning a NEW key to an OrderedDict appends it at the end, i.e.
        # as the most recently used entry.
        self._prices[isbn] = price
        if len(self._prices) > self.capacity:
            # popitem(last=False) removes the oldest entry, not the newest one.
            # It returns the removed (key, value) pair, which is ignored
            # here. With the default last=True it would remove the newest.
            # Documentation: https://docs.python.org/3/library/collections.html#collections.OrderedDict.popitem
            self._prices.popitem(last=False)

    def erase(self, isbn: int) -> bool:
        """Remove isbn; return True if it was present, else False."""

        # dict.pop(key, default) removes key and returns its value, or
        # returns default (None here) instead of raising KeyError when the
        # key is absent. `is not None` turns that into True/False. (Prices
        # are ints, never None, so this test is reliable.)
        # Documentation: https://docs.python.org/3/library/stdtypes.html#dict.pop
        return self._prices.pop(isbn, None) is not None


def cache_lookup_history(capacity: int, operations: list[tuple]) -> list[int]:
    """Replay a list of operations on a new cache; return the lookup results.

    Helper added in this repository for demonstrations and tests; it is not
    part of the textbook. Each operation is a tuple: ('put', isbn, price),
    ('get', isbn) or ('erase', isbn). `list[tuple]` is a type hint meaning
    "a list of tuples"; Python does not enforce it.
    """
    cache = LRUCache(capacity)
    result = []
    for operation in operations:

        # operation[0] is the operation name; the remaining positions are
        # its arguments.
        if operation[0] == 'put':
            cache.insert(operation[1], operation[2])
        elif operation[0] == 'get':
            result.append(cache.lookup(operation[1]))
        elif operation[0] == 'erase':
            cache.erase(operation[1])
    return result


# TEXTBOOK POST-SOLUTION DISCUSSION (page 166)
# --------------------------------------------
# Each lookup costs O(1) for the hash table lookup and O(1) for updating the
# queue, i.e., O(1) overall. (Inserts and erases are likewise O(1); storage
# is O(capacity).)
#
# VARIANTS
# --------
# The book gives no variants for this exercise.


# TEXTBOOK CODE COMPARISON
# ------------------------
# Book: `class LRUCache:` with `__init__(self, capacity)` setting
#   `self._isbn_price_table = collections.OrderedDict()` and
#   `self._capacity = capacity`; `lookup` refreshes recency by
#   `price = self._isbn_price_table.pop(isbn)` followed by re-inserting
#   `self._isbn_price_table[isbn] = price`; `insert` pops an existing key
#   (keeping its old price) `elif self._capacity <= len(table)` evicts with
#   `popitem(last=False)` BEFORE inserting, then always assigns
#   `table[isbn] = price`; `erase` is
#   `return self._isbn_price_table.pop(isbn, None) is not None`.
# File: imports `from collections import OrderedDict` instead of
#   `import collections`; attributes renamed `capacity` (public, no
#   underscore) and `_prices` (annotated `OrderedDict[int, int]`); type
#   hints added on all methods; a ValueError for capacity <= 0 is added;
#   recency is refreshed with `move_to_end(isbn)` instead of pop and
#   re-insert; `insert` returns early for an existing key, and for a new key
#   inserts first and then evicts when the size exceeds capacity (book:
#   evicts first when full, then inserts -- same resulting contents).
#   `erase` matches. Extra helper `cache_lookup_history` is not in the book.


# Python executes this block only when this source file is run directly.
# When pytest imports the file, this block is skipped automatically.
# Documentation: https://docs.python.org/3/library/__main__.html
if __name__ == "__main__":

    # A capacity-2 cache: after get(1), ISBN 1 is the most recent, so
    # put(3, 30) evicts ISBN 2 and the final get(2) misses (-1). The list
    # of lookup results is therefore [10, -1].
    #
    # `assert` stops the program with an AssertionError if the condition is
    # false; this is a quick smoke check, while pytest provides the more
    # thorough automated verification.
    ops=[("put",1,10),("put",2,20),("get",1),("put",3,30),("get",2)]
    print("ISBN cache lookups:", cache_lookup_history(2, ops))
    assert cache_lookup_history(2, ops) == [10,-1]
