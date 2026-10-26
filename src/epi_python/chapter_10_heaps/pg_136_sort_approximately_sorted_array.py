"""EPI 10.3: Sort an almost-sorted array — printed page 136.

Educational reconstruction; not a verified verbatim textbook transcription.
Question: Sort an almost-sorted array
Algorithm: Maintain a min-heap of the k+1 possible next values, yielding O(n log(k+1)).
Read the corresponding `pg_136_exercise_...md` file for the extracted
book's problem, worked explanations and variants. OCR is unverified.

Run: python -m epi_python.chapter_10_heaps.pg_136_sort_approximately_sorted_array
Test: python -m pytest tests/chapter_10_heaps/test_pg_136_sort_approximately_sorted_array.py -v
"""

# heapq supports push/pop operations on a binary min-heap.
# Documentation: https://docs.python.org/3/library/heapq.html
import heapq


def sort_approximately_sorted_array(values: list[int], k: int) -> list[int]:
    """Sort where every item lies at most k positions from its sorted place."""
    heap = values[: k + 1]
    heapq.heapify(heap)
    result = []
    for value in values[k + 1:]:
        result.append(heapq.heappushpop(heap, value))
    while heap:
        result.append(heapq.heappop(heap))
    return result


if __name__ == "__main__":
    # Demonstrations check representative input/output behavior.
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
