"""EPI 10.1: Merge sorted files — printed page 134.

Educational reconstruction; not a verified verbatim textbook transcription.
Question: Merge sorted files
Algorithm: Heap-based k-way merge; `heapq.merge` returns a lazy iterator of sorted output elements.
Read the corresponding `pg_134_exercise_...md` file for the extracted
book's problem, worked explanations and variants. OCR is unverified.

Run: python -m epi_python.chapter_10_heaps.pg_134_merge_sorted_arrays
Test: python -m pytest tests/chapter_10_heaps/test_pg_134_merge_sorted_arrays.py -v
"""

# heapq exposes a binary heap priority queue and k-way merge generator.
# Documentation: https://docs.python.org/3/library/heapq.html#heapq.merge
import heapq


def merge_sorted_arrays(sorted_lists: list[list[int]]) -> list[int]:
    """Merge sorted input runs into one sorted list."""

    # heapq.merge(*iterables) lazily merges multiple already-sorted inputs.
    # Converting to list materializes its stream of results for this exercise.
    return list(heapq.merge(*sorted_lists))


if __name__ == "__main__":
    # Demonstrations check representative input/output behavior.
    observed = merge_sorted_arrays([])
    print("merge_sorted_arrays:", observed)
    assert observed == []
    observed = merge_sorted_arrays([[1, 3], [2, 4]])
    print("merge_sorted_arrays:", observed)
    assert observed == [1, 2, 3, 4]
    observed = merge_sorted_arrays([[], [1, 1], [0]])
    print("merge_sorted_arrays:", observed)
    assert observed == [0, 1, 1]
