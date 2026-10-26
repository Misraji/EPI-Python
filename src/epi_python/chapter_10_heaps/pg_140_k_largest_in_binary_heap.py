"""EPI exercise 10.6, printed page 140: Compute the k largest elements in a max-heap.

EDUCATIONAL RECONSTRUCTION — not a verbatim verified code transcription.
Problem: Compute the k largest elements in a max-heap.
Method/complexity: Pop max candidate and add its children; O(k log k) time and O(k) candidate storage.
For the book's original explanation and variants, see:
    pg_140_exercise_10_06_compute_the_k_largest_elements_in_a_max_heap.md

Run: python -m epi_python.chapter_10_heaps.pg_140_k_largest_in_binary_heap
Test: python -m pytest tests/chapter_10_heaps/test_pg_140_k_largest_in_binary_heap.py -v
"""

# Python heapq is a min-heap; negative values simulate max-priority.
# Documentation: https://docs.python.org/3/library/heapq.html
import heapq


def k_largest_in_binary_heap(max_heap: list[int], k: int) -> list[int]:
    """Find k largest keys in a binary max-heap without modifying the heap."""
    if not 0 <= k <= len(max_heap):
        raise ValueError("k must lie between zero and size")
    if not k:
        return []
    candidates = [(-max_heap[0], 0)]
    answer = []
    for _ in range(k):
        neg_value, index = heapq.heappop(candidates)
        answer.append(-neg_value)
        for child in (2 * index + 1, 2 * index + 2):
            if child < len(max_heap):
                heapq.heappush(candidates, (-max_heap[child], child))
    return answer


if __name__ == "__main__":
    heap = [10,9,8,3,4,1,2]
    print("top 3 heap:", k_largest_in_binary_heap(heap, 3))
    assert k_largest_in_binary_heap(heap, 3) == [10,9,8]
