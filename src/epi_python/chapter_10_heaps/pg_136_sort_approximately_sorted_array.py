"""EPI Python — Exercise 10.3: Sort an Almost-Sorted Array

Chapter 10: Heaps
Textbook: pages 136–137 (printed page numbers; the introduction starts at
the bottom of page 136, the problem, solution, program and complexity are
on page 137).

PROBLEM (from the textbook)
---------------------------
"Often data is almost-sorted—for example, a server receives timestamped
stock quotes and earlier quotes may arrive slightly after later quotes
because of differences in server loads and network routes. In this problem
we address efficient ways to sort such data.

Write a program which takes as input a very long sequence of numbers and
prints the numbers in sorted order. Each number is at most k away from its
correctly sorted position. (Such an array is sometimes referred to as being
k-sorted.) For example, no number in the sequence <3, -1, 2, 6, 4, 5, 8> is
more than 2 away from its final sorted position."

HINT (from the textbook)
------------------------
"How many numbers must you read after reading the ith number to be sure you
can place it in the correct location?"

SOLUTION DEVELOPMENT (following the textbook)
---------------------------------------------
Brute force: store the whole sequence in an array, sort it and print it:
O(n log n) time and O(n) space, where n is the length of the sequence.

Using the almost-sorted property: once k + 1 numbers have been read, the
smallest of them must be smaller than every number still to come (no later
number can move more than k places forward).

Book example (k = 2): after reading 3, -1, 2, the smallest, -1, must be the
global minimum, because every number is at most 2 places from its sorted
position and the minimum belongs at index 0. After reading 4 as well, the
second smallest number must be the minimum of 3, 2, 4, namely 2.

General case: keep k + 1 numbers, repeatedly extracting the minimum and
adding a new number, which is exactly what a min-heap supports. The book
first adds k numbers to a min-heap; then for each further number it adds
the number and extracts the minimum; when the input runs out, it simply
keeps extracting until the heap is empty.

The book's program is `sort_approximately_sorted_array(sequence, k)`; this
file's function of the same name follows the same idea (see the code
comparison at the end).

ADDITIONAL EXAMPLES (added for learning; not printed in this exercise)
---------------------------------------------------------------------
    ([], 0)         -> []
    ([2, 1, 3], 1)  -> [1, 2, 3]
    ([3, 1, 2], 2)  -> [1, 2, 3]
    ([1, 2, 3], 0)  -> [1, 2, 3]   (k = 0: already sorted)
"""

# Python standard library: heap queue (priority queue) algorithms on plain
# lists, where index 0 always holds the smallest item (a min-heap).
# Module documentation: https://docs.python.org/3/library/heapq.html
# heapify:     https://docs.python.org/3/library/heapq.html#heapq.heapify
# heappushpop: https://docs.python.org/3/library/heapq.html#heapq.heappushpop
# heappop:     https://docs.python.org/3/library/heapq.html#heapq.heappop
import heapq


def sort_approximately_sorted_array(values: list[int], k: int) -> list[int]:
    """Sort where every item lies at most k positions from its sorted place.

    Implements the textbook's `sort_approximately_sorted_array` min-heap
    algorithm (page 137), returning a list instead of a stream.
    """

    # The slice values[: k + 1] copies the first k + 1 items (or fewer if
    # the list is shorter; slicing never raises for out-of-range bounds).
    heap = values[: k + 1]

    # heapq.heapify(list) rearranges the list in place into heap order in
    # O(len) time, so heap[0] becomes the smallest item. This is faster than
    # pushing the items one by one (O(len log len)).
    # Documentation: https://docs.python.org/3/library/heapq.html#heapq.heapify
    heapq.heapify(heap)
    result = []

    # values[k + 1:] is every remaining item after the first k + 1.
    for value in values[k + 1:]:

        # heapq.heappushpop(heap, item) pushes item and then pops and returns
        # the smallest item, in one step that is more efficient than a
        # heappush followed by a heappop. If the new item is no larger than
        # the current minimum it is returned immediately. The returned value
        # is the smallest of k + 2 candidates, which by the k-sorted property
        # is the next value in sorted order.
        # Documentation: https://docs.python.org/3/library/heapq.html#heapq.heappushpop
        result.append(heapq.heappushpop(heap, value))

    # Input exhausted: the heap holds the largest remaining values; popping
    # them one at a time yields them in ascending order.
    while heap:

        # heapq.heappop(heap) removes and returns the smallest item.
        # Documentation: https://docs.python.org/3/library/heapq.html#heapq.heappop
        result.append(heapq.heappop(heap))
    return result


# TEXTBOOK POST-SOLUTION DISCUSSION (page 137)
# --------------------------------------------
# Time complexity O(n log k); space complexity O(k) (the heap never holds
# more than about k + 1 numbers).
#
# VARIANTS
# The textbook gives no variants for this exercise.


# TEXTBOOK CODE COMPARISON
# ------------------------
# Book: `def sort_approximately_sorted_array(sequence, k)` with `result =
# []` and `min_heap = []`; it pushes the first k elements with
# `for x in itertools.islice(sequence, k): heapq.heappush(min_heap, x)`
# (comment "Adds the first k elements into min_heap. Stop if there are fewer
# than k elements."), then `for x in sequence:` uses heappushpop (comment
# "For every new element, add it to min_heap and extract the smallest."),
# then pops the rest (comment "sequence is exhausted, iteratively extracts
# the remaining elements."). The book's version expects `sequence` to be an
# iterator (islice consumes the first k items, and the second loop continues
# from there), so it works on a stream without storing all of it.
# File: parameters `values: list[int], k: int` with `-> list[int]`; no
# `itertools` import; the heap is built from the slice `values[: k + 1]`
# with `heapq.heapify` (k + 1 items, not k pushed one at a time), and the
# loop runs over the slice `values[k + 1:]`. The heap therefore holds k + 1
# items between steps instead of the book's k. Same sorted output; the file
# requires a list (slicing) rather than an arbitrary stream.


# Python executes this block only when this source file is run directly.
# When pytest imports the file, this block is skipped automatically.
# Documentation: https://docs.python.org/3/library/__main__.html
if __name__ == "__main__":

    # Demonstrations check representative input/output behavior: empty
    # input, neighbours swapped (k = 1), the smallest item two places late
    # (k = 2), and an already sorted list with k = 0.
    #
    # `assert` stops the program with an AssertionError if the condition is
    # false; these are quick smoke checks, pytest does the thorough testing.
    observed = sort_approximately_sorted_array([], 0)
    print("sort_approximately_sorted_array:", observed)
    assert observed == []
    observed = sort_approximately_sorted_array([2, 1, 3], 1)
    print("sort_approximately_sorted_array:", observed)
    assert observed == [1, 2, 3]
    observed = sort_approximately_sorted_array([3, 1, 2], 2)
    print("sort_approximately_sorted_array:", observed)
    assert observed == [1, 2, 3]
    observed = sort_approximately_sorted_array([1, 2, 3], 0)
    print("sort_approximately_sorted_array:", observed)
    assert observed == [1, 2, 3]
