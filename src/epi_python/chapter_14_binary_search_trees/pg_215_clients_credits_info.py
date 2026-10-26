"""EPI Python — Exercise 14.11: Add Credits

Chapter 14: Binary Search Trees
Textbook: pages 215–216 (printed page numbers; problem and solution start on 215).

PROBLEM (from the textbook)
---------------------------
"Consider a server that a large number of clients connect to. Each client is
identified by a string. Each client has a "credit", which is a nonnegative
integer value. The server needs to maintain a data structure to which
clients can be added, removed, queried, or updated. In addition, the server
needs to be able to add a specified number of credits to all clients
simultaneously."

"Design a data structure that implements the following methods:
 - Insert: add a client with specified credit, replacing any existing entry
   for the client.
 - Remove: delete the specified client.
 - Lookup: return the number of credits associated with the specified
   client.
 - Add-to-all: increment the credit count for all current clients by the
   specified amount.
 - Max: return a client with the highest number of credits."

HINT (from the textbook)
------------------------
"Use additional global state."

SOLUTION DEVELOPMENT (following the textbook)
---------------------------------------------
A hash table is natural here, but it supports neither an efficient max nor
an obvious way to increment everyone at once short of visiting every entry.
A BST has an efficient max but also no built-in global increment.

General principle: wrap the object and give the wrapper functions that add
behaviour before or after delegating to the object. Here: keep the clients
in a BST and let the wrapper track the total increment applied so far.

Example from the book: clients A, B, C with credits 1, 2, 3; adding 5 credits
to each just sets the wrapper's total increment to 5. A lookup on B finds 2
in the BST and adds 5 before returning. Adding 4 more to each simply makes
the total increment 9.

Pitfall: clients inserted AFTER an add-to-all. Continuing the example, if D
is now added with credit 6, a lookup would return 6 + 9, which is wrong.
Fix: subtract the current increment when inserting, i.e. store D with
6 - 9 = -3; a lookup then returns -3 + 9, the correct amount.

Concretely, the BST's keys are (offset-adjusted) credits and each value is
the set of clients with that credit, which makes max-queries fast. Since the
BST is ordered by credit, not client id, lookups and removes by client need
an additional hash table from clients to credits. Lookup is then trivial.
Remove looks up the credit in the hash table, searches the BST for that
credit's set of clients, and deletes the client from the set.

This file keeps the hash table and the global offset exactly as in the book,
but replaces the book's third-party `bintrees.RBTree` with a standard-library
`heapq` max-heap (by negating credits) whose stale entries are discarded
lazily (see the code comparison).

ADDITIONAL EXAMPLES (added for learning; not printed in this exercise)
---------------------------------------------------------------------
    insert A=4, B=8; add_all(3) -> max() == 'B', lookup('A') == 7
"""

# Python standard library: heap queue (priority queue) algorithms on lists.
# heapq keeps a MIN-heap (smallest item at index 0); this file stores
# negated credits so that the highest credit is the smallest heap item.
# Module documentation: https://docs.python.org/3/library/heapq.html
# heappush: https://docs.python.org/3/library/heapq.html#heapq.heappush
# heappop: https://docs.python.org/3/library/heapq.html#heapq.heappop
import heapq


class ClientsCreditsInfo:
    """Credit map with O(1) add-to-all and lazy max-heap cleanup.

    This corresponds to the textbook's `ClientsCreditsInfo` class.
    EPI uses bintrees.RBTree. A lazy heap plus dict uses only standard Python.
    """

    # `__init__` is the constructor, run by `ClientsCreditsInfo()`. Names
    # starting with an underscore (`_offset`, ...) are, by convention,
    # internal attributes not meant to be used from outside the class.
    # `name: type = value` on an attribute is a variable annotation:
    # `dict[str,int]` maps client-id strings to int credits, and
    # `list[tuple[int,str]]` is a list of (negated credit, client) pairs.
    # Annotations are not enforced at run time.
    def __init__(self):
        self._offset=0
        self._client_to_credit:dict[str,int]={}
        self._credit_heap:list[tuple[int,str]]=[]

    def insert(self, client_id: str, credits: int) -> None:
        """Insert or replace a client (textbook `insert`)."""

        # Store the credit relative to the current global offset, so that a
        # later lookup (stored value + offset) returns exactly `credits`.
        # Assigning to the dict key replaces any existing entry.
        adjusted=credits-self._offset
        self._client_to_credit[client_id]=adjusted

        # heapq.heappush(heap, item) adds an item in O(log n) time while
        # keeping the heap property. The tuple (-adjusted, client_id) makes
        # the LARGEST credit the SMALLEST item; tuples compare element by
        # element, so equal credits are ordered by client id. Any older heap
        # entry for this client is left in place and ignored later by max().
        # Documentation: https://docs.python.org/3/library/heapq.html#heapq.heappush
        heapq.heappush(self._credit_heap,(-adjusted,client_id))

    def remove(self, client_id: str) -> bool:
        """Delete a client; True if it was present (textbook `remove`)."""

        # dict.pop(key, default) removes the key and returns its value, or
        # returns `default` (None) without error if the key is absent.
        # The client's heap entries become stale and are skipped by max().
        # Documentation: https://docs.python.org/3/library/stdtypes.html#dict.pop
        return self._client_to_credit.pop(client_id,None) is not None

    def lookup(self, client_id: str) -> int:
        """Return a client's credits, or -1 if absent (textbook `lookup`)."""

        # dict.get(key) returns None when the key is absent (no KeyError).
        # Documentation: https://docs.python.org/3/library/stdtypes.html#dict.get
        credit=self._client_to_credit.get(client_id)

        # Conditional expression `X if cond else Y`: undo the offset
        # adjustment made at insertion time.
        return -1 if credit is None else credit+self._offset

    def add_all(self, credits: int) -> None:
        """Add `credits` to every client in O(1) (textbook `add_all`)."""
        self._offset+=credits

    def max(self) -> str:
        """Return a client with the most credits, or '' (textbook `max`).

        Naming a method `max` does not affect the built-in max() elsewhere;
        inside the class it is reached as `self.max`.
        """

        # Lazy deletion: the top entry is valid only if the dictionary still
        # maps that client to that same adjusted credit. Otherwise the entry
        # is stale (client removed or re-inserted with another credit).
        while self._credit_heap:

            # heap[0] is always the smallest item: here, the highest credit.
            # Tuple unpacking splits it into its two parts.
            negative,client=self._credit_heap[0]
            if self._client_to_credit.get(client)==-negative:
                return client

            # heapq.heappop(heap) removes and returns the smallest item in
            # O(log n) time; here it discards the stale top entry.
            # Documentation: https://docs.python.org/3/library/heapq.html#heapq.heappop
            heapq.heappop(self._credit_heap)
        return ''


# TEXTBOOK POST-SOLUTION DISCUSSION (page 216)
# --------------------------------------------
# With the book's BST: insert and remove are dominated by the BST, O(log n),
# n being the number of clients. Lookup and add-to-all touch only the hash
# table and are O(1). Library BST implementations use caching to make max
# O(1).
#
# (For this file's heap version: insert is O(log n); remove, lookup and
# add_all are O(1); max is amortized O(log n), since each stale entry is
# popped at most once. The heap may hold stale entries, so its size can
# exceed the number of clients.)
#
# VARIANTS
# --------
# The textbook gives no variants for this exercise.


# TEXTBOOK CODE COMPARISON
# ------------------------
# - DIFFERENT LIBRARY. Book: `self._credit_to_clients = bintrees.RBTree()`
#   (third-party red-black BST) mapping adjusted credit -> set of client ids,
#   updated with `setdefault(c - self._offset, set()).add(client_id)`;
#   `max` returns `next(iter(...max_item()[1]))` (any client in the
#   top-credit set). File: `self._credit_heap`, a standard-library `heapq`
#   list of `(-adjusted_credit, client_id)` tuples with lazy removal of stale
#   entries in `max`; ties go to the lexicographically smallest client id.
# - Book `insert(self, client_id, c)` first calls `self.remove(client_id)`;
#   the file's `insert(self, client_id, credits)` does not (the dict
#   assignment replaces the entry and the old heap entry becomes stale).
# - Book `remove` deletes the client from the BST's set (and the set's key
#   when it becomes empty) and from the dict, returning True/False. File:
#   `dict.pop(client_id, None) is not None`, touching only the dict.
# - Book `add_all(self, C)`; file `add_all(self, credits)`.
# - `lookup` matches the book. `__init__` matches except the BST attribute
#   is replaced by the heap list and type annotations are added.
# - Type hints added to all methods.


# Python executes this block only when this source file is run directly.
# When pytest imports the file, this block is skipped automatically.
# Documentation: https://docs.python.org/3/library/__main__.html
if __name__ == '__main__':

    # An added example (not from the book). Semicolons put two statements
    # on one line. After add_all(3), A has 7 and B has 11 credits.
    info=ClientsCreditsInfo()
    info.insert('A',4); info.insert('B',8)
    info.add_all(3)
    print('Top client and adjusted credits:',info.max(),info.lookup(info.max()))

    # `assert` stops the program with an AssertionError if the condition is
    # false; a quick smoke check, with full tests in the tests/ folder.
    assert info.max()=='B' and info.lookup('A')==7
