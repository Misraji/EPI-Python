"""EPI Python — Exercise 10.2: Sort an Increasing-Decreasing Array

Chapter 10: Heaps
Textbook: pages 135–136 (printed page numbers; problem and Figure 10.2 on
page 135, hint, solution, programs and complexity on page 136).

PROBLEM (from the textbook)
---------------------------
"An array is said to be k-increasing-decreasing if elements repeatedly
increase up to a certain index after which they decrease, then again
increase, a total of k times. This is illustrated in Figure 10.2."

Figure 10.2 ("A 4-increasing-decreasing array"):
    A[0..9] = 57, 131, 493, 294, 221, 339, 418, 452, 442, 190
    (up 57 -> 493, down 493 -> 221, up 221 -> 452, down 452 -> 190)

"Design an efficient algorithm for sorting a k-increasing-decreasing array."

HINT (from the textbook)
------------------------
"Can you cast this in terms of combining k sorted arrays?"

SOLUTION DEVELOPMENT (following the textbook)
---------------------------------------------
Brute force: sort the array with a general sorting algorithm, ignoring the
k-increasing-decreasing structure: O(n log n) time for an array of length n.

When k is much smaller than n, one can do better. For k = 2 the array is an
increasing subarray followed by a decreasing one; reversing the second gives
two sorted arrays, and merging two sorted arrays is easy in O(n) time.

In general: reverse each decreasing subarray, so the array decomposes into k
sorted arrays, then merge them with the technique of Exercise 10.1 (a
min-heap merge). For Figure 10.2 the decomposition is <57, 131, 493>,
<221, 294>, <339, 418, 452> and <190, 442>.

The book gives two programs: `sort_k_increasing_decreasing_array(A)`, which
scans for direction changes explicitly, and
`sort_k_increasing_decreasing_array_pythonic(A)`, which finds the runs with
itertools.groupby and a stateful callable object. Both merge with the
`merge_sorted_arrays` function of Exercise 10.1. This file implements only
the explicit-scan idea (merging with heapq.merge); see the code comparison
at the end.

ADDITIONAL EXAMPLES (added for learning; not printed in this exercise)
---------------------------------------------------------------------
    [1, 3, 5, 4, 2, 6, 9] -> runs [1, 3, 5], [2, 4] (reversed), [6, 9]
                          -> [1, 2, 3, 4, 5, 6, 9]
    []                    -> []
"""

# Python standard library: heap queue (priority queue) algorithms.
# Module documentation: https://docs.python.org/3/library/heapq.html
# merge API: https://docs.python.org/3/library/heapq.html#heapq.merge
import heapq


# Type hints (not enforced by Python): takes a list of ints and returns a
# new sorted list of ints.
def sort_k_increasing_decreasing_array(values: list[int]) -> list[int]:
    """Merge monotone runs of alternating directions into ascending order.

    Implements the idea of the textbook's first program,
    `sort_k_increasing_decreasing_array` (page 136), restructured.
    """

    # An empty list is falsy; there is nothing to split or merge.
    if not values:
        return []

    # `runs` collects the sorted (ascending) pieces; `start` is the index
    # where the current run begins; `increasing` is the current direction.
    runs = []
    start = 0
    increasing = True
    for i in range(1, len(values)):

        # The current run ends at a direction change: a drop while
        # increasing, or a rise while decreasing. Equal neighbours stay in
        # the current run (both a non-decreasing run and a reversed
        # non-increasing run are still sorted). `and` / `or` combine the
        # two cases; parentheses make the grouping explicit.
        ended = (increasing and values[i] < values[i-1]) or (not increasing and values[i] > values[i-1])
        if ended:

            # Slicing values[start:i] copies the elements from index start
            # up to but not including i. A decreasing run is reversed with
            # the slice [::-1] (step -1), which makes it ascending. The
            # conditional expression `A if condition else B` chooses which.
            run = values[start:i]
            runs.append(run if increasing else run[::-1])

            # Tuple assignment updates both names at once: the next run
            # starts at i and goes in the opposite direction.
            start, increasing = i, not increasing

    # The last run extends to the end of the list (values[start:] omits the
    # stop index).
    run = values[start:]
    runs.append(run if increasing else run[::-1])

    # heapq.merge(*iterables) merges already-sorted inputs lazily, using a
    # small heap holding one pending value per run, so merging n values
    # from k runs takes O(n log k) time. The `*` unpacks the list of runs
    # into separate arguments, and list(...) collects the merged values.
    # Documentation: https://docs.python.org/3/library/heapq.html#heapq.merge
    return list(heapq.merge(*runs))


# TEXTBOOK POST-SOLUTION DISCUSSION (page 136)
# --------------------------------------------
# As in Exercise 10.1, merging the k sorted subarrays takes O(n log k) time.
#
# VARIANTS
# The textbook gives no variants for this exercise.


# TEXTBOOK CODE COMPARISON
# ------------------------
# Book program 1: `def sort_k_increasing_decreasing_array(A)` (comment
# "Decomposes A into a set of sorted arrays.") uses `sorted_subarrays`,
# constants `INCREASING, DECREASING = range(2)`, `subarray_type`, and
# `start_idx`; it loops `for i in range(1, len(A) + 1)` and closes a
# subarray when `i == len(A)` (comment "A is ended. Adds the last
# subarray.") or when `A[i - 1] < A[i]` while DECREASING or `A[i - 1] >=
# A[i]` while INCREASING; a decreasing subarray is taken reversed with the
# slice `A[i - 1:start_idx - 1:-1]`; it finishes with
# `merge_sorted_arrays(sorted_subarrays)` from Solution 10.1.
# File: parameter renamed `values: list[int]` with `-> list[int]`; an
# explicit empty-input check; a boolean `increasing` instead of the
# INCREASING/DECREASING constants; the loop stops at len(values) - 1 and the
# last run is appended after the loop; reversal uses `run[::-1]` on a copied
# slice; an increasing run is ended only by a strict drop (`<`), whereas the
# book also ends it on equal neighbours (`>=`). Both produce sorted runs, so
# the result is the same sorted list. Merging uses `heapq.merge` directly
# instead of the book's `merge_sorted_arrays` (no import from the 10.1 file).
#
# Book program 2, MISSING from the file:
# `sort_k_increasing_decreasing_array_pythonic(A)` (comment "Pythonic
# solution, uses a stateful object to trace the monotonic subarrays.")
# defines a nested class `Monotonic` with `_last = float('-inf')` and a
# `__call__(self, curr)` returning whether `curr < self._last`, then merges
# `[list(group)[::-1 if is_decreasing else 1] for is_decreasing, group in
# itertools.groupby(A, Monotonic())]` with `merge_sorted_arrays`.


# Python executes this block only when this source file is run directly.
# When pytest imports the file, this block is skipped automatically.
# Documentation: https://docs.python.org/3/library/__main__.html
if __name__ == "__main__":

    # [1, 3, 5, 4, 2, 6, 9] has an increasing run, a decreasing run, and an
    # increasing run; sorted it is [1, 2, 3, 4, 5, 6, 9], written here as
    # list(range(1, 7)) + [9] (range(1, 7) is 1..6; `+` joins lists).
    # `assert` stops the program with an AssertionError if the result
    # differs; pytest provides the thorough automated verification.
    print("sorted monotone runs:", sort_k_increasing_decreasing_array([1,3,5,4,2,6,9]))
    assert sort_k_increasing_decreasing_array([1,3,5,4,2,6,9]) == list(range(1,7)) + [9]
