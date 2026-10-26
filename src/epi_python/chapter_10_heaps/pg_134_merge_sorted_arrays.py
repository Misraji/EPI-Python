"""EPI Python — Exercise 10.1: Merge Sorted Files

Chapter 10: Heaps
Textbook: pages 134–135 (printed page numbers; problem, solution and worked
example on page 134, programs and complexity discussion on page 135).

PROBLEM (from the textbook)
---------------------------
Motivating scenario (summarised): there are 500 files, one per S&P 500
company, each holding that company's stock trades, one per line, in the
format "1232111,AAPL,30,456.12" (time in milliseconds since the start of
the day's trading, stock symbol, number of shares, price). Each file is
sorted by increasing time. The task is to produce one file with all the
trades from the 500 files sorted by increasing time. Each input file is
roughly 5–100 megabytes; the combined file is roughly five gigabytes.

"Write a program that takes as input a set of sorted sequences and computes
the union of these sequences as a sorted sequence. For example, if the input
is <3, 5, 7>, <0, 6>, and <0, 6, 28>, then the output is
<0, 0, 3, 5, 6, 6, 7, 28>."

HINT (from the textbook)
------------------------
"Which part of each sequence is significant as the algorithm executes?"

SOLUTION DEVELOPMENT (following the textbook)
---------------------------------------------
Brute force: concatenate all the sequences into one array and sort it:
O(n log n) time for n elements in total. It ignores the fact that each
sequence is already sorted.

Using the sortedness: only the first remaining element of each sequence can
be the next output. So repeatedly take the smallest among the first
remaining elements of all the sequences. A min-heap is the ideal structure
for a collection to which arbitrary values are added and from which the
smallest is repeatedly extracted.

For ease of explanation the book merges arrays rather than files. In
practice each heap entry must also record which array it came from and its
position in that array. (With files, no explicit position is needed: the
file I/O library remembers the first unread entry.)

Worked example: merge <3, 5, 7>, <0, 6>, <0, 6, 28> (heap contents shown
as values only):
  * Start: heap {3, 0, 0} (first entry of each array).
  * Extract 0 -> output <0>; add 6 (the book arbitrarily took the 0 of the
    third array; taking the second array's 0 would be equally fine);
    heap {3, 0, 6}.
  * Extract 0 -> output <0, 0>; add 6; heap {3, 6, 6}.
  * Extract 3 -> output <0, 0, 3>; add 5; heap {5, 6, 6}.
  * Extract 5 -> output <0, 0, 3, 5>; add 7; heap {7, 6, 6}.
  * Extract 6 -> output <0, 0, 3, 5, 6>; assuming this 6 came from the
    second array, which is now empty, nothing is added; heap {7, 6}.
  * Extract 6 -> output <0, 0, 3, 5, 6, 6>; add 28; heap {7, 28}.
  * Extract 7 -> output <0, 0, 3, 5, 6, 6, 7>; heap {28}.
  * Extract 28 -> output <0, 0, 3, 5, 6, 6, 7, 28>; everything has been
    processed and the output is sorted.

The book gives two programs: an explicit heap of (value, array index)
pairs driven by iterators, `merge_sorted_arrays`, and a one-line
"Pythonic" version using heapq.merge, `merge_sorted_arrays_pythonic`. Both
are implemented below under the same names.

ADDITIONAL EXAMPLES (added for learning; not printed in this exercise)
---------------------------------------------------------------------
    []                        -> []
    [[1, 1], [], [-1, 3]]     -> [-1, 1, 1, 3]  (an empty input list is fine)
"""

# Python standard library: heap queue (priority queue) algorithms on plain
# lists, where the smallest item is always at index 0 (a min-heap).
# Module documentation: https://docs.python.org/3/library/heapq.html
# heappush: https://docs.python.org/3/library/heapq.html#heapq.heappush
# heappop:  https://docs.python.org/3/library/heapq.html#heapq.heappop
# merge:    https://docs.python.org/3/library/heapq.html#heapq.merge
import heapq


# Type hints (not enforced by Python): `list[list[int]]` is a list of
# lists of ints; the function returns one list of ints.
def merge_sorted_arrays(sorted_lists: list[list[int]]) -> list[int]:
    """Textbook's explicit heap-of-iterators implementation (page 135)."""

    # The built-in iter(seq) returns an iterator over the sequence: an
    # object that remembers the position of the next unread element (like
    # the "first unread entry" of a file) without copying the data.
    # Documentation: https://docs.python.org/3/library/functions.html#iter
    iterators = [iter(items) for items in sorted_lists]

    # The heap is an ordinary list kept in heap order by heapq functions.
    # `tuple[int, int]` hints that items are (value, source index) pairs.
    min_heap: list[tuple[int, int]] = []

    # The built-in enumerate() yields (position, item) pairs: 0 with the
    # first iterator, 1 with the second, and so on. The position i records
    # which input list a heap entry came from, so after extracting it we
    # know which iterator to read next.
    # Documentation: https://docs.python.org/3/library/functions.html#enumerate
    for i, iterator in enumerate(iterators):

        # next(iterator, default) consumes and returns the next value, or
        # returns `default` (here None) instead of raising StopIteration
        # when the iterator is exhausted, e.g. for an empty input list.
        # (This relies on None never being a real data value.)
        # Documentation: https://docs.python.org/3/library/functions.html#next
        first = next(iterator, None)
        if first is not None:

            # heapq.heappush(heap, item) adds item while keeping the heap
            # property, in O(log k) time for k items. Tuples compare
            # component by component, left to right: the value decides the
            # order, and the index only breaks ties between equal values.
            # Documentation: https://docs.python.org/3/library/heapq.html#heapq.heappush
            heapq.heappush(min_heap, (first, i))

    result: list[int] = []

    # An empty list is falsy: loop until every input is exhausted.
    while min_heap:

        # heapq.heappop(heap) removes and returns the smallest item in
        # O(log k) time (IndexError if the heap is empty). The pair is
        # unpacked into two names in one assignment.
        # Documentation: https://docs.python.org/3/library/heapq.html#heapq.heappop
        smallest, source_index = heapq.heappop(min_heap)
        result.append(smallest)

        # Replace the extracted value with the next value from the same
        # input list, if it has one left.
        upcoming = next(iterators[source_index], None)
        if upcoming is not None:

            # Push the replacement; the heap again holds at most one entry
            # per input list, so it never exceeds k items.
            heapq.heappush(min_heap, (upcoming, source_index))
    return result


def merge_sorted_arrays_pythonic(sorted_lists: list[list[int]]) -> list[int]:
    """Textbook's one-line alternative using heapq.merge() (page 135)."""

    # heapq.merge(*iterables) merges already-sorted inputs into one sorted
    # stream. It is lazy: it returns an iterator that produces values on
    # demand, keeping only one pending value per input internally.
    # The `*` in the call unpacks the outer list, passing each inner list as
    # a separate positional argument: merge(*[[1], [2]]) == merge([1], [2]).
    # list(...) consumes the iterator and collects every merged value.
    # Documentation: https://docs.python.org/3/library/heapq.html#heapq.merge
    # Unpacking argument lists: https://docs.python.org/3/tutorial/controlflow.html#unpacking-argument-lists
    return list(heapq.merge(*sorted_lists))


# TEXTBOOK POST-SOLUTION DISCUSSION (page 135)
# --------------------------------------------
# Let k be the number of input sequences. The min-heap never holds more than
# k elements, so each extract-min and each insert costs O(log k), and the
# whole merge takes O(n log k) time. Extra space is O(k) beyond the space
# for the final result; in particular, when reading from files and writing
# to a file (rather than arrays), only O(k) additional storage is needed.
#
# Alternative: merge the k files recursively, two at a time, with the merge
# step of merge sort: k files become k/2, then k/4, and so on. There are
# log k stages, each costing O(n), so the time is also O(n log k), the same
# as the heap approach. But any reasonable merge-sort implementation needs
# O(n) space, which is much worse than the heap approach when k << n.
#
# VARIANTS
# The textbook gives no variants for this exercise.


# TEXTBOOK CODE COMPARISON
# ------------------------
# Book program 1: `def merge_sorted_arrays(sorted_arrays)` with
# `min_heap = []`, `sorted_arrays_iters = [iter(x) for x in sorted_arrays]`
# (comment "Builds a list of iterators for each array in sorted_arrays."),
# a loop `for i, it in enumerate(sorted_arrays_iters)` with `first_element`
# (comment "Puts first element from each iterator in min_heap."), and a
# main loop using `smallest_entry, smallest_array_i`, a separate local
# `smallest_array_iter`, and `next_element`.
# File: parameter renamed `sorted_lists: list[list[int]]` with `-> list[int]`;
# locals renamed (`iterators`, `iterator`, `first`, `smallest`,
# `source_index`, `upcoming`); the iterator is indexed directly in the
# `next(...)` call instead of a separate local; type hints on `min_heap`
# and `result`; the book's comments are not reproduced. Same algorithm.
#
# Book program 2: `def merge_sorted_arrays_pythonic(sorted_arrays)` returning
# `list(heapq.merge(*sorted_arrays))` (comment "Pythonic solution, uses the
# heapq.merge() method which takes multiple inputs."). File: same body;
# parameter renamed `sorted_lists` with type hints.


# Python executes this block only when this source file is run directly.
# When pytest imports the file, this block is skipped automatically.
# Documentation: https://docs.python.org/3/library/__main__.html
if __name__ == "__main__":

    # Each example is (input lists, expected merged list): no input lists,
    # the book's example, and an input including an empty list and
    # negative/duplicate values.
    examples = (
        ([], []),
        ([[3, 5, 7], [0, 6], [0, 6, 28]], [0, 0, 3, 5, 6, 6, 7, 28]),
        ([[1, 1], [], [-1, 3]], [-1, 1, 1, 3]),
    )
    for sorted_runs, expected in examples:

        # Functions are objects, so both implementations can be placed in a
        # tuple and called in turn. `algorithm.__name__` is the function's
        # name as a string; the f-string inserts it and the result.
        for algorithm in (merge_sorted_arrays, merge_sorted_arrays_pythonic):
            observed = algorithm(sorted_runs)
            print(f"{algorithm.__name__}: {observed}")

            # `assert` stops the program with an AssertionError if the result
            # differs; pytest provides the thorough automated verification.
            assert observed == expected
    print("Both textbook merge implementations passed.")
