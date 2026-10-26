"""EPI Python — Exercise 13.7: Compute the Union of Intervals

Chapter 13: Sorting
Textbook: pages 189–191 (printed page numbers; problem starts on 189,
solution on 190).

PROBLEM (from the textbook)
---------------------------
"In this problem we consider sets of intervals with integer endpoints; the
intervals may be open or closed at either end. We want to compute the union
of the intervals in such sets. A concrete example is given in Figure 13.2."

Figure 13.2 ("A set of intervals and their union"), as drawn on page 189:
    intervals: (0,3), [1,1], [2,4], [3,4), [5,7), [7,8), [8,11), (9,11],
               [12,14], (12,16], (13,15), (16,17)
    union:     (0,4], [5,11], [12,17)

"Design an algorithm that takes as input a set of intervals, and outputs
their union expressed as a set of disjoint intervals."

HINT (from the textbook)
------------------------
"Do a case analysis."

SOLUTION DEVELOPMENT (following the textbook)
---------------------------------------------
Brute force: the approach from the start of Solution 13.6 (page 188), which
examines every number from the minimum left endpoint to the maximum right
endpoint, also works here. Its time is O(Dn), where D is the difference
between the two extreme values and n the number of intervals; that is
unacceptable when D is large.

Working with intervals instead of individual values: repeatedly pick any
interval and find every interval it intersects. If it intersects none,
remove it from the set and add it to the result. Otherwise, take the union
of it and everything it intersects (that union is itself an interval),
remove all of those intervals, and put the union back into the set. Each
round removes at least one interval and costs O(n) for the intersection
tests and unions, so this is O(n^2).

Faster: process the intervals in sorted order so attention can be limited to
a subset of them. Sort by left endpoint; then intervals entirely to the left
of the current one never need to be revisited.

Terminology: an interval that does not include its left endpoint is
"left-open"; left-closed, right-open and right-closed are defined likewise.
When two intervals have the same left endpoint, the left-closed one is
placed first; other ties are broken arbitrarily.

Iterating over the sorted intervals, compare the current interval with the
interval most recently added to the result:
- They do not intersect, and the result interval's right endpoint does not
  equal the current interval's left endpoint: append the current interval
  to the result as a new interval.
- They intersect: replace the most recent result interval with its union
  with the current interval.
- The result interval's right endpoint equals the current interval's left
  endpoint and at least one of these two endpoints is closed: likewise,
  replace the most recent result interval with the union.

Worked example from the book (Figure 13.2): the result array evolves as
    <(0,3)>
    <(0,4]>
    <(0,4], [5,7)>
    <(0,4], [5,8)>
    <(0,4], [5,11)>
    <(0,4], [5,11]>
    <(0,4], [5,11], [12,14]>
    <(0,4], [5,11], [12,16]>
    <(0,4], [5,11], [12,17)>

The function `union_of_intervals` below follows the book's single
implementation. `closed` is a helper added in this file (not in the book).

ADDITIONAL EXAMPLES (added for learning; not printed in this exercise)
---------------------------------------------------------------------
    [1,3], [2,7], [9,10]  ->  [1,7], [9,10]
"""

# Python standard library: automatic generation of special methods for
# simple record-like classes.
# Module documentation: https://docs.python.org/3/library/dataclasses.html
# dataclass decorator: https://docs.python.org/3/library/dataclasses.html#dataclasses.dataclass
from dataclasses import dataclass


# `@dataclass(frozen=True)` is a class decorator. From the annotated fields
# it generates `__init__` (so `Endpoint(3, True)` works), a readable
# `__repr__`, and an `__eq__` comparing all fields (used by the `assert`
# below). `frozen=True` makes instances immutable: assigning to a field
# after construction raises an error. That is why the function below builds
# a NEW Interval when it extends one, instead of changing it in place.
# Annotations such as `value: int` declare field types; they are not enforced.
# Documentation: https://docs.python.org/3/library/dataclasses.html#dataclasses.dataclass
@dataclass(frozen=True)
class Endpoint:
    value: int
    is_closed: bool


# Same decorator: an immutable record holding two Endpoint objects.
# Documentation: https://docs.python.org/3/library/dataclasses.html#dataclasses.dataclass
@dataclass(frozen=True)
class Interval:
    left: Endpoint
    right: Endpoint


# Type hints: `list[Interval]` in and out; not enforced at run time.
def union_of_intervals(intervals: list[Interval]) -> list[Interval]:
    """Union intervals accounting for open and closed endpoints.

    This is the textbook's implementation (sort by left endpoint, then merge
    with a three-case analysis).
    """

    # Empty input: an empty list is falsy, so return no intervals.
    if not intervals:
        return []

    # sorted(iterable, key=...) returns a NEW sorted list, leaving the
    # caller's list unchanged. The key function returns a tuple; tuples
    # compare element by element. First the left coordinate; then, for equal
    # coordinates, `not x.left.is_closed` is False (sorts first, since
    # False < True) for a closed left end and True for an open one. So
    # left-closed intervals precede left-open ones at the same coordinate,
    # matching the book's tie rule.
    # Documentation: https://docs.python.org/3/library/functions.html#sorted
    ordered = sorted(intervals, key=lambda x: (x.left.value, not x.left.is_closed))

    # A variable annotation documenting the result type (not enforced).
    result: list[Interval] = []

    # `current` plays the role of the book's "interval most recently added
    # to the result"; it is appended once it can no longer grow.
    current = ordered[0]

    # `ordered[1:]` is a slice (new list) of every interval after the first.
    for nxt in ordered[1:]:

        # Tuple unpacking: the right end of the growing interval and the
        # left end of the next interval.
        right, left = current.right, nxt.left

        # They must be merged if they overlap (next starts before current
        # ends) or touch at one coordinate where at least one of the two
        # endpoints is closed (book cases 2 and 3). The parentheses let the
        # boolean expression span several lines.
        overlap = (left.value < right.value or
                   (left.value == right.value and (left.is_closed or right.is_closed)))
        if overlap:

            # Extend only if `nxt` reaches further right, or ends at the same
            # coordinate but closed where the current end is open.
            if (nxt.right.value > right.value or
                    (nxt.right.value == right.value and nxt.right.is_closed and not right.is_closed)):
                current = Interval(current.left, nxt.right)
        else:

            # Book case 1: disjoint and not touching; finalize `current`.
            result.append(current)
            current = nxt
    result.append(current)
    return result


def closed(left: int, right: int) -> Interval:
    """Convenience constructor used in demonstrations and tests.

    Helper added in this file (not in the textbook): builds the closed
    interval [left, right].
    """
    return Interval(Endpoint(left, True), Endpoint(right, True))


# TEXTBOOK POST-SOLUTION DISCUSSION (page 191)
# --------------------------------------------
# The time complexity is dominated by the sort step, i.e. O(n log n).
#
# VARIANTS
# --------
# The textbook gives no variants for this exercise.


# TEXTBOOK CODE COMPARISON
# ------------------------
# - Book: `Endpoint = collections.namedtuple('Endpoint', ('is_closed',
#   'val'))`. File: `@dataclass(frozen=True) class Endpoint` with fields in
#   the opposite order, `value` (renamed from `val`) then `is_closed`.
# - Book: `class Interval` with a hand-written `__init__(self, left, right)`
#   and `__lt__` (compare `left.val`; on a tie, closed-left first; book
#   comment "Left endpoints are equal, so now see if one is closed and the
#   other open - closed intervals should appear first."). File: frozen
#   dataclass `Interval` with no `__lt__`; the ordering is provided instead
#   by `sorted(..., key=lambda x: (x.left.value, not x.left.is_closed))`.
# - Book: `union_of_intervals(intervals)` sorts the caller's list in place
#   (`intervals.sort()`), seeds `result = [intervals[0]]`, loops over ALL
#   intervals (including the first), and mutates `result[-1].right = i.right`.
#   Its extension test for equal right values is `i.right.is_closed` alone.
#   Book comments "Empty input." and "Sort intervals according to left
#   endpoints of intervals." File: type hints; sorts a copy; keeps the
#   growing interval in a separate variable `current` and appends it when it
#   is finished; builds a new `Interval` instead of mutating (required by
#   frozen=True); extension test adds `and not right.is_closed` (no effect
#   on the result); intermediate names `right`, `left`, `overlap`, `nxt`.
# - File adds the helper `closed(left, right)`, not in the book.


# Python executes this block only when this source file is run directly.
# When pytest imports the file, this block is skipped automatically.
# Documentation: https://docs.python.org/3/library/__main__.html
if __name__ == '__main__':

    # An added example (not from the book) with closed intervals: [1,3] and
    # [2,7] overlap and merge to [1,7]; [9,10] stays separate.
    answer = union_of_intervals([closed(1, 3), closed(2, 7), closed(9, 10)])
    print('Union:', answer)

    # `assert` stops the program with an AssertionError if the condition is
    # false. The dataclass-generated `__eq__` compares the fields, so equal
    # intervals compare equal. Full tests live in the tests/ folder.
    assert answer == [closed(1, 7), closed(9, 10)]
