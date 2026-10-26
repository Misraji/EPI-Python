"""EPI Python — Exercise 13.6: Merging Intervals

Chapter 13: Sorting
Textbook: pages 188–189 (printed page numbers; problem and solution start on 188).

PROBLEM (from the textbook)
---------------------------
"Suppose the time during the day that a person is busy is stored as a set
of disjoint time intervals. If an event is added to the person's calendar,
the set of busy times may need to be updated."

"In the abstract, we want a way to add an interval to a set of disjoint
intervals and represent the new set as a set of disjoint intervals. For
example, if the initial set of intervals is [-4,-1],[0,2],[3,6],[7,9],
[11,12],[14,17], and the added interval is [1,8], the result is
[-4,-1],[0,9],[11,12],[14,17]."

"Write a program which takes as input an array of disjoint closed intervals
with integer endpoints, sorted by increasing order of left endpoint, and an
interval to be added, and returns the union of the intervals in the array
and the added interval. Your result should be expressed as a union of
disjoint intervals sorted by left endpoint."

HINT (from the textbook)
------------------------
"What is the union of two closed intervals?"

SOLUTION DEVELOPMENT (following the textbook)
---------------------------------------------
Brute force: find the smallest left endpoint and the largest right endpoint
over all the intervals (including the added one), then test every integer
between them for membership in some interval, building the result. This is
O(Dn), where D is the difference between those two extreme values and n is
the number of intervals. D can be far larger than n: for the array
<[0,1],[999999,1000000]> and added interval [10,20], the brute force
iterates over every integer from 0 to 1000000.

The brute force wastes effort on non-endpoints: an integer p that is not an
endpoint must lie in the same interval as p - 1. Focus on endpoints instead,
and use the sorted order to process the array quickly, in three stages:

1. Iterate over intervals lying completely before the interval to be added;
   append each directly to the result.
2. On reaching an interval that intersects the added interval, form their
   union, which is itself an interval. Keep absorbing subsequent intervals
   as long as they intersect the union being formed. Append that single
   union to the result.
3. Iterate over the remaining intervals. Because the array is sorted, none
   of them can intersect the added interval, so append them all.

Worked example from the book: array [-4,-1],[0,2],[3,6],[7,9],[11,12],
[14,17], added interval [1,8].
- Stage 1: [-4,-1] does not intersect [1,8]; add it to the result.
- [0,2] intersects [1,8]: Stage 2 begins; their union is [0,8].
- [3,6] lies completely inside [0,8]; continue.
- [7,9] intersects but is not contained, so the union grows to [0,9]. (The
  printed text says the most recently added interval changes "[1,8] to
  [0,9]"; from the preceding step it is [0,8] that becomes [0,9].)
- [11,12] does not intersect [0,9]: Stage 3; it and all later intervals are
  added, giving [-4,-1],[0,9],[11,12],[14,17].
The algorithm works "locally": sortedness guarantees no combination of
intervals is missed.

The function below follows the book's single implementation, using plain
(left, right) tuples instead of an Interval namedtuple.

ADDITIONAL EXAMPLES (added for learning; not printed in this exercise)
---------------------------------------------------------------------
    [(0,2), (3,5), (7,9)] + (4,8) -> [(0,2), (3,9)]
"""


# Type hints: `list[tuple[int,int]]` describes a list of 2-tuples of ints,
# i.e. (left, right) closed intervals. Python records but does not enforce
# these annotations.
# Documentation: https://docs.python.org/3/library/typing.html
def add_interval(disjoint_intervals: list[tuple[int,int]], new_interval: tuple[int,int]) -> list[tuple[int,int]]:
    """Merge a new closed interval into already sorted disjoint closed intervals.

    This is the textbook's three-stage implementation.
    """
    result = []

    # Tuple unpacking: split the (left, right) pair into two names.
    new_start, new_end = new_interval

    # Added input check (not in the book): reject an interval whose left end
    # exceeds its right end by raising ValueError.
    if new_start > new_end:
        raise ValueError('Reversed interval')
    i = 0

    # Stage 1: intervals ending strictly before the new interval starts
    # (`[i][1]` is the right endpoint) cannot overlap it; copy them.
    while i < len(disjoint_intervals) and disjoint_intervals[i][1] < new_start:
        result.append(disjoint_intervals[i])
        i += 1

    # Stage 2: while the current interval starts no later than the union's
    # right end, they overlap. The union of [a, b] and [c, d] is
    # [min(a, c), max(b, d)]. Built-ins min() and max() return the smaller
    # / larger of their arguments.
    # Documentation: https://docs.python.org/3/library/functions.html#min
    while i < len(disjoint_intervals) and disjoint_intervals[i][0] <= new_end:
        new_start = min(new_start, disjoint_intervals[i][0])
        new_end = max(new_end, disjoint_intervals[i][1])
        i += 1
    result.append((new_start, new_end))

    # Stage 3: `disjoint_intervals[i:]` is a slice (a new list) of every
    # interval not yet processed; list.extend() appends each of its items
    # to `result` in order.
    # Documentation: https://docs.python.org/3/tutorial/datastructures.html#more-on-lists
    result.extend(disjoint_intervals[i:])
    return result


# TEXTBOOK POST-SOLUTION DISCUSSION (page 189)
# --------------------------------------------
# The program spends O(1) time per entry, so the time complexity is O(n).
#
# VARIANTS
# --------
# The textbook gives no variants for this exercise.


# TEXTBOOK CODE COMPARISON
# ------------------------
# - Book defines `Interval = collections.namedtuple('Interval', ('left',
#   'right'))`; the file has no Interval type and uses plain tuples, reading
#   endpoints as `[0]` and `[1]`.
# - Book: `def add_interval(disjoint_intervals, new_interval):` with
#   `i, result = 0, []`, updates `new_interval = Interval(min(...), max(...))`
#   in Stage 2, and ends with `return result + [new_interval] +
#   disjoint_intervals[i:]`. Its loop conditions are
#   `new_interval.left > disjoint_intervals[i].right` and
#   `new_interval.right >= disjoint_intervals[i].left`. Book comments:
#   "Processes intervals in disjoint_intervals which come before /
#   overlap with / come after new_interval." and "If [a, b] and [c, d]
#   overlap, union is [min(a, c), max(b, d)]."
# - File: type hints added; endpoints unpacked into `new_start`/`new_end`;
#   added ValueError check for a reversed interval; Stage 2 updates the two
#   variables instead of building a namedtuple; the result is built with
#   `append` and `extend` instead of list concatenation. Same results.


# Python executes this block only when this source file is run directly.
# When pytest imports the file, this block is skipped automatically.
# Documentation: https://docs.python.org/3/library/__main__.html
if __name__ == "__main__":

    # An added example (not from the book): (4, 8) overlaps (3, 5) and
    # (7, 9), which merge into (3, 9); (0, 2) lies entirely before it.
    result = add_interval([(0, 2), (3, 5), (7, 9)], (4, 8))
    print('Intervals after insert:', result)

    # `assert` stops the program with an AssertionError if the condition is
    # false; a quick smoke check, with full tests in the tests/ folder.
    assert result == [(0, 2), (3, 9)]
