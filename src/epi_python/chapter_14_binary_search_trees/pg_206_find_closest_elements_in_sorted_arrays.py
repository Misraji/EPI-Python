"""EPI Python — Exercise 14.6: Find the Closest Entries in Three Sorted Arrays

Chapter 14: Binary Search Trees
Textbook: pages 206–207 (printed page numbers; problem and solution start on 206).

PROBLEM (from the textbook)
---------------------------
"Design an algorithm that takes three sorted arrays and returns one entry
from each such that the minimum interval containing these three entries is
as small as possible. For example, if the three arrays are <5,10,15>,
<3,6,9,12,15>, and <8,16,24>, then 15,15,16 lie in the smallest possible
interval."

HINT (from the textbook)
------------------------
"How would you proceed if you needed to pick three entries in a single
sorted array?"

SOLUTION DEVELOPMENT (following the textbook)
---------------------------------------------
Brute force: try every triple, e.g. with three nested loops. The length of
the smallest interval containing a triple is its maximum minus its minimum.
Time O(lmn), where l, m, n are the three array lengths.

This ignores the sortedness. In the example, the smallest intervals
containing (5,3,16) and (5,3,24) must be larger than the one containing
(5,3,8), since 8 is the maximum of 5,3,8 and 8 < 16 < 24.

Start with the triple of the smallest entries of each array. Let s be its
minimum and t its maximum. The smallest interval with left endpoint s that
contains an element of each array must be [s, t], because the other two
values are as small as possible.

Now remove s from the triple and bring in the next element of the array s
came from. Let s' and t' be the new minimum and maximum. [s', t'] is the
smallest interval whose left endpoint is s': the other two values are the
smallest entries of their arrays that are >= s'. By repeatedly examining
and removing the smallest element of the triple, we compute the minimum
interval starting at each such element. Since the overall minimum interval
must start at an element of SOME array, it is guaranteed to be encountered.

Worked example from the book: begin with (5,3,8). The smallest interval with
left endpoint 3 has length 8 - 3 = 5. Next after 3 is 6: triple (5,6,8),
smallest interval from 5 has length 8 - 5 = 3. Next after 5 is 10: triple
(10,6,8), interval from 6 has length 10 - 6 = 4. Next after 6 is 9: triple
(10,9,8). Continuing gives the triples (10,9,16), (10,12,16), (15,12,16),
(15,15,16). Of all these, the one in the minimum-length interval is
(15,15,16).

The book then writes a general function for k sorted arrays. Since it must
repeatedly insert, delete, find the minimum and find the maximum among k
elements, a BST is the natural choice; the book uses `bintrees.RBTree`, a
third-party balanced-BST package (its chapter introduction explains that
`sortedcontainers` would be equally acceptable).

This file implements the same "advance the minimum" algorithm with the
standard-library `heapq` module instead of `bintrees` (see the code
comparison below).
"""

# Python standard library: heap queue (priority queue) algorithms on lists.
# A heap is a list arranged so that heap[0] is always the smallest item.
# Module documentation: https://docs.python.org/3/library/heapq.html
# heapify: https://docs.python.org/3/library/heapq.html#heapq.heapify
# heappop: https://docs.python.org/3/library/heapq.html#heapq.heappop
# heappush: https://docs.python.org/3/library/heapq.html#heapq.heappush
import heapq


# Type hints: a list of sorted int lists in, an int (the minimum interval
# length) out. Python does not enforce annotations at run time.
def find_closest_elements_in_sorted_arrays(sorted_arrays: list[list[int]]) -> int:
    """Return minimum (maximum - minimum) across one value per sorted array.

    The textbook's general k-array implementation of the same algorithm.
    The textbook uses an ordered BST from the third-party bintrees package.
    This self-contained adaptation uses the standard-library heapq instead.
    """

    # Added input check (not in the book): every array needs at least one
    # entry. `any(not row for row in sorted_arrays)` is True if some row is
    # empty (an empty list is falsy).
    # Documentation: https://docs.python.org/3/library/functions.html#any
    if not sorted_arrays or any(not row for row in sorted_arrays):
        raise ValueError('Every input sorted array must contain at least one item')

    # One entry per array: (current value, array number, position in array).
    # enumerate yields (index, row) pairs. Tuples compare element by element,
    # so the heap orders entries by value, breaking ties by array number,
    # just like the book's RBTree keys (value, idx).
    # Documentation: https://docs.python.org/3/library/functions.html#enumerate
    heap = [(row[0], i, 0) for i,row in enumerate(sorted_arrays)]

    # heapq.heapify(list) rearranges the list IN PLACE into a min-heap in
    # linear time; afterwards heap[0] is the smallest entry.
    # Documentation: https://docs.python.org/3/library/heapq.html#heapq.heapify
    heapq.heapify(heap)

    # A heap gives fast access only to its minimum, not its maximum, so the
    # maximum of the current triple is tracked separately. max() over a
    # generator expression; `value,_,_` unpacks each tuple, `_` naming the
    # ignored fields.
    current_max = max(value for value,_,_ in heap)

    # float('inf') is positive infinity: larger than any real distance.
    min_distance = float('inf')
    while True:

        # heapq.heappop(heap) removes and returns the smallest entry in
        # O(log k) time, keeping the heap property. This is the book's
        # `iters.pop_min()` (and its `min_key()`).
        # Documentation: https://docs.python.org/3/library/heapq.html#heapq.heappop
        minimum, source, index = heapq.heappop(heap)

        # [minimum, current_max] is the smallest interval starting at
        # `minimum` that holds one entry from each array.
        min_distance = min(min_distance, current_max - minimum)

        # Return if the array providing the minimum has no remaining
        # elements: no later interval can include an entry from it. int()
        # converts the result to an int (it is already an integer value).
        if index+1 == len(sorted_arrays[source]):
            return int(min_distance)
        next_value = sorted_arrays[source][index+1]

        # Entries only grow, so the new maximum is the larger of the old one
        # and the newly added value.
        current_max = max(current_max, next_value)

        # heapq.heappush(heap, item) adds an item in O(log k) time while
        # preserving the heap property (book: `iters.insert(...)`).
        # Documentation: https://docs.python.org/3/library/heapq.html#heapq.heappush
        heapq.heappush(heap,(next_value,source,index+1))


# TEXTBOOK POST-SOLUTION DISCUSSION (page 207)
# --------------------------------------------
# Time O(n log k), where n is the total number of elements in the k arrays.
# For the special case k = 3 in the problem statement, this is
# O(n log 3) = O(n).
#
# VARIANTS
# --------
# The textbook gives no variants for this exercise.


# TEXTBOOK CODE COMPARISON
# ------------------------
# - DIFFERENT LIBRARY. The book uses the third-party `bintrees` package:
#   `iters = bintrees.RBTree()` (comment "Stores array iterators in each
#   entry."), a red-black BST whose keys are `(value, idx)` and whose values
#   are Python iterators over each array. It uses `iters.insert(key, it)`,
#   `iters.min_key()`, `iters.max_key()[0]` and `iters.pop_min()[1]`, all
#   O(log k). A BST gives both the minimum and the maximum directly.
#   The file uses the standard-library `heapq` min-heap of tuples
#   `(value, array_index, position)`. A heap only gives the minimum, so the
#   file keeps the maximum in `current_max` (valid because each array is
#   sorted, so values entering the heap never decrease per array). The
#   asymptotic cost is the same, O(n log k). `bintrees` is not part of the
#   standard library and is not used here, so the file runs without extra
#   packages.
# - Book: positions are advanced with `iter()`/`next(it, None)` and an
#   empty array is simply skipped (`if first_min is not None`); the loop
#   ends with `return min_distance_so_far` when `next_min is None`
#   (comment "Return if some array has no remaining elements.").
#   File: explicit indices instead of iterators; raises ValueError if any
#   array (or the list of arrays) is empty; returns `int(min_distance)`.
# - Names: book `min_distance_so_far`, `min_value`, `min_idx`, `max_value`,
#   `next_min`; file `min_distance`, `minimum`, `source`, `current_max`,
#   `next_value`. Type hints added.


# Python executes this block only when this source file is run directly.
# When pytest imports the file, this block is skipped automatically.
# Documentation: https://docs.python.org/3/library/__main__.html
if __name__ == '__main__':

    # The book's example arrays; the best triple is (15, 15, 16), whose
    # interval [15, 16] has length 1.
    example=[[5,10,15],[3,6,9,12,15],[8,16,24]]
    result=find_closest_elements_in_sorted_arrays(example)
    print('Shortest covering interval width:',result)

    # `assert` stops the program with an AssertionError if the condition is
    # false; a quick smoke check, with full tests in the tests/ folder.
    assert result==1
