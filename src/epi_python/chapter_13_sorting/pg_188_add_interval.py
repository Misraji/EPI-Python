"""EPI 13.6, printed page 188: Merging intervals.

Problem: Merging intervals. See pg_188_exercise_13_06_merging_intervals.md for the full
original problem, hint, development, and variants from the PDF text layer.

Approach and complexity: O(n) single pass, O(n) output; compare left and right endpoints.

EDUCATIONAL RECONSTRUCTION: source and comments are not claimed verbatim.
Run directly: python -m epi_python.chapter_13_sorting.pg_188_add_interval
Test: python -m pytest tests/chapter_13_sorting/test_pg_188_add_interval.py -v
"""

# TEXTBOOK PROBLEM (exercise 13.6, printed page 188):
# Insert an interval into a sorted set of disjoint intervals, merging overlaps.
# HINT: Merge every interval that intersects the new interval.

def add_interval(disjoint_intervals: list[tuple[int,int]], new_interval: tuple[int,int]) -> list[tuple[int,int]]:
    """Merge a new closed interval into already sorted disjoint closed intervals."""
    result = []
    new_start, new_end = new_interval
    if new_start > new_end:
        raise ValueError('Reversed interval')
    i = 0
    while i < len(disjoint_intervals) and disjoint_intervals[i][1] < new_start:
        result.append(disjoint_intervals[i])
        i += 1
    while i < len(disjoint_intervals) and disjoint_intervals[i][0] <= new_end:
        new_start = min(new_start, disjoint_intervals[i][0])
        new_end = max(new_end, disjoint_intervals[i][1])
        i += 1
    result.append((new_start, new_end))
    result.extend(disjoint_intervals[i:])
    return result


if __name__ == "__main__":
    result = add_interval([(0, 2), (3, 5), (7, 9)], (4, 8))
    print('Intervals after insert:', result)
    assert result == [(0, 2), (3, 9)]
