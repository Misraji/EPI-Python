"""EPI 13.7, printed page 189: Compute the union of intervals.

Problem: Compute the union of intervals. See pg_189_exercise_13_07_compute_the_union_of_intervals.md for the full
original problem, hint, development, and variants from the PDF text layer.

Approach and complexity: O(n log n) sorting; preserve closed/open endpoint semantics and O(n) output.

EDUCATIONAL RECONSTRUCTION: source and comments are not claimed verbatim.
Run directly: python -m epi_python.chapter_13_sorting.pg_189_union_of_intervals
Test: python -m pytest tests/chapter_13_sorting/test_pg_189_union_of_intervals.py -v
"""

# TEXTBOOK PROBLEM (exercise 13.7, printed page 189):
# Compute the union of intervals, including correct open and closed endpoints.
# HINT: Sort endpoints and merge touching or overlapping intervals appropriately.

# dataclass provides a compact representation of named interval endpoints.
# Documentation: https://docs.python.org/3/library/dataclasses.html
from dataclasses import dataclass


@dataclass(frozen=True)
class Endpoint:
    value: int
    is_closed: bool


@dataclass(frozen=True)
class Interval:
    left: Endpoint
    right: Endpoint


def union_of_intervals(intervals: list[Interval]) -> list[Interval]:
    """Union intervals accounting for open and closed endpoints."""
    if not intervals:
        return []

    # Earlier closed starts precede open starts at the same coordinate.
    # Documentation: https://docs.python.org/3/library/functions.html#sorted
    ordered = sorted(intervals, key=lambda x: (x.left.value, not x.left.is_closed))
    result: list[Interval] = []
    current = ordered[0]
    for nxt in ordered[1:]:
        right, left = current.right, nxt.left
        overlap = (left.value < right.value or
                   (left.value == right.value and (left.is_closed or right.is_closed)))
        if overlap:
            if (nxt.right.value > right.value or
                    (nxt.right.value == right.value and nxt.right.is_closed and not right.is_closed)):
                current = Interval(current.left, nxt.right)
        else:
            result.append(current)
            current = nxt
    result.append(current)
    return result


def closed(left: int, right: int) -> Interval:
    """Convenience constructor used in demonstrations and tests."""
    return Interval(Endpoint(left, True), Endpoint(right, True))


if __name__ == '__main__':
    answer = union_of_intervals([closed(1, 3), closed(2, 7), closed(9, 10)])
    print('Union:', answer)
    assert answer == [closed(1, 7), closed(9, 10)]
