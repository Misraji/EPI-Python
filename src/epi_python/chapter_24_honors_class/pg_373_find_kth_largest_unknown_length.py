"""EPI Python — Exercise 24.17: Find the kth Largest Element—Large n, Small k

Chapter 24: Honors Class
Textbook: pages 373–374 (printed page numbers; problem, solution and program
on 373, the complexity analysis and space-time discussion on 374).

PROBLEM (from the textbook)
---------------------------
The goal of this problem is to design an algorithm for computing the kth
largest element in a sequence of elements that is presented one element at
a time. The length of the sequence is not known in advance, and could be
very large.

Design an algorithm for computing the kth largest element in a sequence of
elements.

HINT (from the textbook)
------------------------
Track the k largest elements, but don't update the collection immediately
after each new element is read.

SOLUTION DEVELOPMENT (following the textbook)
---------------------------------------------
Natural approach: keep a min-heap of the k largest elements seen so far,
as in Solution 10.4 on Page 138. After the last element is read, the
answer is at the root of the min-heap. Time: O(n log k), with n the total
number of elements.

Faster: there is a very fast algorithm for the kth largest element of a
fixed-size array (Solution 11.8 on Page 153), but applying it directly
would need O(n) space to hold the whole sequence. Instead, break the input
into fixed-size arrays and run Solution 11.8 on each one to eliminate all
but its k largest elements; those survivors are carried over into the next
array.

The book's program `find_kth_largest_unknown_length(stream, k)`:
  * append each element to a candidates array;
  * when it holds 2k - 1 elements, run the selection algorithm, which
    reorders elements about the median with the larger elements first,
    then resize to keep just the k largest seen so far;
  * at the end, find the kth largest among the candidates.

This file follows that plan but must adapt the "keep the k largest" step,
because the repository's Chapter 11 `find_kth_largest` does not reorder the
list (see the comments in the code and TEXTBOOK CODE COMPARISON).

ADDITIONAL EXAMPLES (added for learning; not printed in this exercise)
---------------------------------------------------------------------
    stream=iter([3, 1, 5, 2, 4]), k=3 -> 3
"""

# Local project import (not the standard library): the repository's
# Chapter 11 selection function, Solution 11.8 "Find the kth largest element"
# (printed page 153), in
# src/epi_python/chapter_11_searching/pg_153_kth_largest_element.py.
# `find_kth_largest(k, values)` returns the kth largest value (k is 1-based)
# and does NOT modify `values` (it partitions a copy).
# `from package.module import name` makes `name` available directly.
# Import system reference: https://docs.python.org/3/reference/import.html
# Import statement: https://docs.python.org/3/reference/simple_stmts.html#the-import-statement
from epi_python.chapter_11_searching.pg_153_kth_largest_element import find_kth_largest


def find_kth_largest_unknown_length(stream,k: int) -> int:
    """Kth largest of an iterable read once, keeping O(k) candidates.

    Follows the textbook's batch-of-(2k - 1) idea; the pruning step is
    adapted because the selection helper returns a value instead of
    reordering the list. `stream` can be any iterable (list, iterator,
    generator); it is consumed in a single pass. Type hints are not enforced.
    """

    # Added validation (not in the book). The body follows the colon on the
    # same line, which is allowed for a single simple statement.
    if k<=0:raise ValueError('k must be positive')
    candidates=[]

    # A for loop pulls items from the iterable one at a time, so the whole
    # stream never needs to be in memory at once.
    for x in stream:
        candidates.append(x)

        # Batch is full: prune it down to the k largest values.
        if len(candidates)>=2*k-1:
            # The book's selection algorithm partitions in place, keeping k largest first.
            # Our Chapter 11 helper returns a value without reordering the supplied list,
            # so use the pivot threshold to retain exactly k values, including duplicates.
            #
            # cutoff is the kth largest value in the batch.
            cutoff=find_kth_largest(k,candidates)

            # List comprehension: a new list of every value strictly greater
            # than the cutoff (at most k - 1 of them).
            larger=[v for v in candidates if v>cutoff]

            # `[cutoff] * m` is a list of m copies of cutoff; it pads the
            # strictly-larger values with enough copies of the cutoff to keep
            # exactly k values, so duplicates of the cutoff are preserved.
            candidates=larger+[cutoff]*(k-len(larger))

    # Added validation (not in the book): a stream shorter than k has no
    # kth largest element.
    if len(candidates)<k:
        raise ValueError('Fewer than k elements in stream')

    # Finds the k-th largest element in candidates.
    return find_kth_largest(k,candidates)


# TEXTBOOK POST-SOLUTION DISCUSSION (page 374)
# --------------------------------------------
# With an array of size 2k - 1, each selection call is almost certainly
# O(k), and it runs once every k - 1 elements, so the total time is O(n).
#
# Less storage would also work, e.g. an array of length 3k/2, still giving
# O(n) time; but the actual run time is higher, because each selection call
# then discards only k/2 elements. This is a classic space-time trade-off.
# With a 4k-long array, each call to Solution 11.8 discards 3k elements.
# Since Solution 11.8 runs in time proportional to the array length, a
# length-4k array versus a length-3k/2 array gives a speed-up of
# (3/2) / ((1/2) / (4/3)) = 2.25. More storage means faster run times (in the
# extreme, read all n elements and make a single call to Solution 11.8), so
# there is a trade-off in how much storage to use.
#
# VARIANTS
# The book gives no variants for this exercise.


# TEXTBOOK CODE COMPARISON
# ------------------------
# book: `def find_kth_largest_unknown_length(stream, k)`; when
#   `len(candidates) >= 2 * k - 1` it calls `find_kth_largest(k, candidates)`
#   (Solution 11.8, which reorders the list about the kth element with
#   larger elements first) and then `del candidates[k:]`; at the end it
#   calls `find_kth_largest(k, candidates)` again and returns
#   `candidates[k - 1]`.
# file: same name, `k: int` and `-> int` hints added; imports the
#   repository's `find_kth_largest`, which returns the value without
#   reordering, so pruning is rewritten as `cutoff = find_kth_largest(...)`,
#   a comprehension of values above the cutoff, and padding with copies of
#   the cutoff; the final answer is the helper's return value. Added
#   ValueError checks for k <= 0 and for a stream shorter than k.


# Python executes this block only when this source file is run directly.
# When pytest imports the file, this block is skipped automatically.
# Documentation: https://docs.python.org/3/library/__main__.html
if __name__=='__main__':

    # iter(list) produces a one-pass iterator, imitating a stream whose
    # length is not known in advance. The 3rd largest of 3, 1, 5, 2, 4 is 3.
    # A fresh iterator is created for the assert because the first one has
    # been consumed. `assert` raises AssertionError on mismatch; the tests/
    # folder holds the thorough pytest suite.
    print('Third largest:',find_kth_largest_unknown_length(iter([3,1,5,2,4]),3))
    assert find_kth_largest_unknown_length(iter([3,1,5,2,4]),3)==3
