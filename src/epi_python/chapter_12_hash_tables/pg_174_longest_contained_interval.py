"""EPI Python — Exercise 12.9: Find the Length of a Longest Contained Interval

Chapter 12: Hash Tables
Textbook: pages 174–175 (printed page numbers; problem, solution and the
start of the program on 174, end of program and complexity on 175).

PROBLEM (from the textbook)
---------------------------
"Write a program which takes as input a set of integers represented by an
array, and returns the size of a largest subset of integers in the array
having the property that if two integers are in the subset, then so are all
integers between them. For example, if the input is <3, -2, 7, 9, 8, 1, 2,
0, -1, 5, 8>, the largest such subset is {-2, -1, 0, 1, 2, 3}, so you
should return 6."

HINT (from the textbook)
------------------------
"Do you really need a total ordering on the input?"

SOLUTION DEVELOPMENT (following the textbook)
---------------------------------------------
Brute force: sort the array, then scan it, recording for each entry the
largest qualifying subset (run of consecutive values) ending at that entry.

Sorting is not actually essential. No total ordering is needed -- only
whether the integers next to a given value are present. That suggests a
hash table holding the entries. Then, for each array entry e that is still
in the hash table, compute the largest interval containing e whose values
are all in the table, by repeatedly looking up e + 1, e + 2, ... and
e - 1, e - 2, .... Afterwards, remove every entry of that interval from the
table, because they all belong to the same largest contained interval and
should not be processed again.

Book's worked example, A = <10, 5, 3, 11, 6, 100, 4>:
  * The hash table starts as {6, 10, 3, 11, 100, 4} plus 5, i.e. all
    entries.
  * First entry 10: expanding both ways gives {10, 11}, size 2. The table
    becomes {6, 3, 5, 100, 4}.
  * Next entry 5 is still in the table, so its interval has not been
    computed. Expanding finds 3, 4, 6 in the table, while 2 and 7 are
    absent, so the set is {3, 4, 5, 6}, size 4. The table becomes {100}.
  * The next three entries 3, 11, 6 are no longer in the table, so their
    intervals have already been computed.
  * 100 cannot be extended: {100}, size 1. The table becomes {}.
  * 4 is not in the table, so it is skipped.
  * The largest of the three sets is {3, 4, 5, 6}, so the answer is 4.

The implementation below, longest_contained_range, follows this idea.

ADDITIONAL EXAMPLES (added for learning; not printed in this exercise)
---------------------------------------------------------------------
    [3, -2, 7, 9, 8, 1, 2, 0, -1, 5, 8] -> 6 (the book's problem example)
    []                                  -> 0
"""


def longest_contained_range(values: list[int]) -> int:
    """Return the largest run of consecutive integers present, regardless of order.

    This is the textbook's longest_contained_range (the only implementation
    given), counting the interval length as it expands instead of
    computing it from the two bounds afterwards.

    Type hints: `list[int]` and `-> int` document the expected types; Python
    does not enforce them.
    """

    # Book's comment: the set records the existence of each entry in A.
    # set(iterable) builds a hash set (duplicates collapse to one entry),
    # giving O(1) expected membership tests and removals.
    # set: https://docs.python.org/3/library/stdtypes.html#set
    remaining = set(values)
    longest = 0

    # An empty set is falsy, so the loop runs until every value has been
    # processed.
    while remaining:

        # set.pop() removes and returns an ARBITRARY element (sets have no
        # order). Any unprocessed value works as the seed of its interval.
        # set.pop: https://docs.python.org/3/library/stdtypes.html#frozenset.pop
        current = remaining.pop()
        length = 1
        low, high = current - 1, current + 1

        # Book's comment: find the lower bound of the largest range
        # containing the seed. set.remove(x) deletes x (it would raise
        # KeyError if x were absent, but the `in` test guarantees it is
        # present). Removing values means no value is ever expanded twice.
        # set.remove: https://docs.python.org/3/library/stdtypes.html#frozenset.remove
        while low in remaining:
            remaining.remove(low)
            low -= 1
            length += 1

        # Book's comment: find the upper bound of the largest range.
        while high in remaining:
            remaining.remove(high)
            high += 1
            length += 1

        # max() returns the larger of its arguments.
        # max: https://docs.python.org/3/library/functions.html#max
        longest = max(longest, length)
    return longest


# TEXTBOOK POST-SOLUTION DISCUSSION (page 175)
# --------------------------------------------
# Time complexity O(n), where n is the array length, because every array
# element is added to and removed from the hash table at most once. The
# hash table uses O(n) space.
#
# VARIANTS
# --------
# The book gives no variants for this exercise.


# TEXTBOOK CODE COMPARISON
# ------------------------
# Book: `def longest_contained_range(A):` with
#   `unprocessed_entries = set(A)`, `max_interval_size = 0`,
#   `a = unprocessed_entries.pop()`, `lower_bound = a - 1` /
#   `upper_bound = a + 1` loops that remove entries, and
#   `max_interval_size = max(max_interval_size, upper_bound - lower_bound
#   - 1)`.
# File: parameter renamed `values: list[int]` with return hint `-> int`;
#   variables renamed (`remaining`, `longest`, `current`, `low`, `high`);
#   bounds initialised together with tuple unpacking; a separate `length`
#   counter is incremented during expansion instead of computing
#   `upper_bound - lower_bound - 1` (same value). Same algorithm.


# Python executes this block only when this source file is run directly.
# When pytest imports the file, this block is skipped automatically.
# Documentation: https://docs.python.org/3/library/__main__.html
if __name__ == "__main__":

    # The book's problem example: {-2, -1, 0, 1, 2, 3} is the longest
    # interval, so the answer is 6. The duplicate 8 is harmless because a
    # set stores it once.
    #
    # `assert` stops the program with an AssertionError if the condition is
    # false; this is a quick smoke check, while pytest provides the more
    # thorough automated verification.
    data=[3,-2,7,9,8,1,2,0,-1,5,8]
    print("consecutive interval length:", longest_contained_range(data))
    assert longest_contained_range(data) == 6
