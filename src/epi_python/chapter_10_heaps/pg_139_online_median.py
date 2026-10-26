"""EPI Python — Exercise 10.5: Compute the Median of Online Data

Chapter 10: Heaps
Textbook: pages 139–140 (printed page numbers; problem, solution, worked
example and most of the program on page 139, the program's last lines and
the complexity at the top of page 140).

PROBLEM (from the textbook)
---------------------------
"You want to compute the running median of a sequence of numbers. The
sequence is presented to you in a streaming fashion—you cannot back up to
read an earlier value, and you need to output the median after reading in
each new element. For example, if the input is 1, 0, 3, 5, 2, 0, 1 the
output is 1, 0.5, 1, 2, 2, 1.5, 1.

Design an algorithm for computing the running median of a sequence."

HINT (from the textbook)
------------------------
"Avoid looking at all values each time you read a new value."

SOLUTION DEVELOPMENT (following the textbook)
---------------------------------------------
Brute force: keep every element read so far in an array and find the median
each time, e.g. with the kth-smallest selection algorithm of Solution 11.8
(page 153). Computing the running median for the first n elements this way
costs O(n^2) time.

Its weakness is that it is not incremental: nothing from the previous step
is reused. The median splits the collection into two equal halves. Adding one
element changes the halves by at most one element, and the element that may
need to move is either the largest of the smaller half or the smallest of
the larger half.

So use two heaps: a max-heap for the smaller half (its largest element is
quickly available) and a min-heap for the larger half (its smallest element
is quickly available), and keep their sizes balanced.

Worked example from the book, input 1, 0, 3, 5, 2, 0, 1. The book writes L
for the min-heap (larger half) and H for the max-heap (smaller half):
    (1) read 1: L = [1],          H = [],        median 1
    (2) read 0: L = [1],          H = [0],       median (1 + 0)/2 = 0.5
    (3) read 3: L = [1, 3],       H = [0],       median 1
    (4) read 5: L = [3, 5],       H = [1, 0],    median (3 + 1)/2 = 2
    (5) read 2: L = [2, 3, 5],    H = [1, 0],    median 2
    (6) read 0: L = [2, 3, 5],    H = [1, 0, 0], median (2 + 1)/2 = 1.5
    (7) read 1: L = [1, 2, 3, 5], H = [1, 0, 0], median 1
In the book's scheme the min-heap (larger half) holds the extra element when
an odd number of values has been read.

The book's program is `online_median(sequence)`. This file's function of the
same name follows the same two-heap idea but lets the smaller half hold the
extra element (see the code comparison at the end).

ADDITIONAL EXAMPLES (added for learning; not printed in this exercise)
---------------------------------------------------------------------
    []               -> []
    [1]              -> [1.0]
    [1, 2]           -> [1.0, 1.5]
    [1, 0, 3, 5, 2]  -> [1.0, 0.5, 1.0, 2.0, 2.0]  (first five book outputs)
"""

# Python standard library: heap queue (priority queue) algorithms on plain
# lists. heapq only provides MIN-heaps (smallest item at index 0); a
# max-heap is emulated by storing negated values.
# Module documentation: https://docs.python.org/3/library/heapq.html
# heappush: https://docs.python.org/3/library/heapq.html#heapq.heappush
# heappop:  https://docs.python.org/3/library/heapq.html#heapq.heappop
import heapq


# Type hints (not enforced by Python): a list of ints in, a list of floats
# (one median per prefix) out.
def online_median(values: list[int]) -> list[float]:
    """Return median after each newly observed input value.

    Implements the textbook's two-heap `online_median` idea (page 139),
    with the smaller half holding the extra element.
    """

    # `smaller` is the lower half as a max-heap: values are stored negated,
    # so the min-heap's smallest entry, smaller[0], is minus the largest
    # value in the lower half. `larger` is the upper half as a min-heap.
    smaller=[]  # negatives: Python min-heap emulates max-heap
    larger=[]
    result=[]
    for number in values:

        # Step 1: put the new number into the lower half.
        # heapq.heappush(heap, item) inserts while keeping heap order,
        # O(log n). The minus sign stores the value negated.
        heapq.heappush(smaller,-number)

        # Step 2: move the largest value of the lower half to the upper half.
        # heapq.heappop(smaller) removes the smallest stored entry, i.e. the
        # negation of the lower half's maximum; negating again restores the
        # value before pushing it onto `larger`. This guarantees every value
        # in `smaller` is <= every value in `larger`.
        heapq.heappush(larger,-heapq.heappop(smaller))

        # Step 3: rebalance so that `smaller` has the same size as `larger`
        # or exactly one more element: if the upper half became bigger, move
        # its minimum back (negated) into the lower half.
        if len(larger)>len(smaller):
            heapq.heappush(smaller,-heapq.heappop(larger))

        # Even count: the median is the average of the two middle values,
        # the lower half's maximum (-smaller[0]) and the upper half's minimum
        # (larger[0]). `/` is true division and always returns a float.
        if len(smaller)==len(larger):
            result.append((-smaller[0]+larger[0])/2)

        # Odd count: the extra element sits in `smaller`, so its maximum is
        # the median; float(...) converts the int to a float for a
        # consistent result type.
        else:
            result.append(float(-smaller[0]))
    return result

# TEXTBOOK POST-SOLUTION DISCUSSION (page 140)
# --------------------------------------------
# Each new entry costs O(log n) time, for the heap insertions and
# extractions.
#
# VARIANTS
# The textbook gives no variants for this exercise.


# TEXTBOOK CODE COMPARISON
# ------------------------
# Book: `def online_median(sequence)` with `min_heap` (comment: stores the
# larger half), `max_heap` (comment: stores the smaller half; values are
# negative) and `result`. For each x it does `heapq.heappush(max_heap,
# -heapq.heappushpop(min_heap, x))`, i.e. x goes through the MIN-heap first
# and the min-heap's smallest moves to the max-heap; then, if the max-heap is
# larger, it moves the max-heap's top back to the min-heap (comment: if an
# odd number has been read, min_heap must have one more element). It appends
# `0.5 * (min_heap[0] + (-max_heap[0]))` for an even count, else
# `min_heap[0]`.
# File: parameter `values: list[int]` with `-> list[float]`; heaps renamed
# `smaller` (negated max-heap) and `larger`; the new number goes into the
# lower half first (heappush then heappop instead of heappushpop), and the
# LOWER half keeps the extra element, so the odd-count median is
# `float(-smaller[0])` instead of `min_heap[0]`. The even-count median uses
# `/2` instead of `0.5 *`. Same median values; the file always returns
# floats, whereas the book returns the stored int for odd counts.


# Python executes this block only when this source file is run directly.
# When pytest imports the file, this block is skipped automatically.
# Documentation: https://docs.python.org/3/library/__main__.html
if __name__ == "__main__":

    # Executable demonstration cases; pytest has the full set.
    # They cover an empty stream, one value, an even count, and the first
    # five values of the book's example (medians 1, 0.5, 1, 2, 2).
    # `assert` stops the program with an AssertionError if the result
    # differs from the expected list.
    result=online_median([])
    print('online_median', result)
    assert result == []
    result=online_median([1])
    print('online_median', result)
    assert result == [1.0]
    result=online_median([1, 2])
    print('online_median', result)
    assert result == [1.0, 1.5]
    result=online_median([1, 0, 3, 5, 2])
    print('online_median', result)
    assert result == [1.0, 0.5, 1.0, 2.0, 2.0]
