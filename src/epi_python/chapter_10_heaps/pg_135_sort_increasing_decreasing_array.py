"""EPI exercise 10.2, printed page 135: Sort an increasing-decreasing array.

EDUCATIONAL RECONSTRUCTION — not a verbatim verified code transcription.
Problem: Sort an increasing-decreasing array.
Method/complexity: Identify k monotonic runs O(n), merge with heap O(n log k), space O(n).
For the book's original explanation and variants, see:
    pg_135_exercise_10_02_sort_an_increasing_decreasing_array.md

Run: python -m epi_python.chapter_10_heaps.pg_135_sort_increasing_decreasing_array
Test: python -m pytest tests/chapter_10_heaps/test_pg_135_sort_increasing_decreasing_array.py -v
"""

# heapq.merge produces sorted output lazily from sorted input iterables.
# Documentation: https://docs.python.org/3/library/heapq.html#heapq.merge
import heapq


def sort_k_increasing_decreasing_array(values: list[int]) -> list[int]:
    """Merge monotone runs of alternating directions into ascending order."""
    if not values:
        return []
    runs = []
    start = 0
    increasing = True
    for i in range(1, len(values)):
        ended = (increasing and values[i] < values[i-1]) or (not increasing and values[i] > values[i-1])
        if ended:
            run = values[start:i]
            runs.append(run if increasing else run[::-1])
            start, increasing = i, not increasing
    run = values[start:]
    runs.append(run if increasing else run[::-1])
    return list(heapq.merge(*runs))


if __name__ == "__main__":
    print("sorted monotone runs:", sort_k_increasing_decreasing_array([1,3,5,4,2,6,9]))
    assert sort_k_increasing_decreasing_array([1,3,5,4,2,6,9]) == list(range(1,7)) + [9]
