"""EPI exercise 11.8, printed page 153: Find the kth largest element.

EDUCATIONAL RECONSTRUCTION — not a verbatim verified code transcription.
Problem: Find the kth largest element.
Method/complexity: Partition-based selection; O(n) average time, O(n²) worst-case if pivots poor; O(n) defensive input copy.
For the book's original explanation and variants, see:
    pg_153_exercise_11_08_find_the_kth_largest_element.md

Run: python -m epi_python.chapter_11_searching.pg_153_kth_largest_element
Test: python -m pytest tests/chapter_11_searching/test_pg_153_kth_largest_element.py -v
"""

def find_kth_largest(k: int, values: list[int]) -> int:
    """Quickselect: find kth largest element (1-based), without full sorting."""
    if not 1 <= k <= len(values):
        raise ValueError("k out of bounds")
    values = values[:]
    target = k - 1
    left, right = 0, len(values) - 1
    while left <= right:
        pivot_value = values[(left + right) // 2]
        i, j = left, right
        while i <= j:
            while values[i] > pivot_value:
                i += 1
            while values[j] < pivot_value:
                j -= 1
            if i <= j:
                values[i], values[j] = values[j], values[i]
                i += 1
                j -= 1
        if target <= j:
            right = j
        elif target >= i:
            left = i
        else:
            return values[target]
    raise RuntimeError("Quickselect partition invariant failed")


if __name__ == "__main__":
    print("third largest:", find_kth_largest(3, [3,1,5,2,4]))
    assert find_kth_largest(3, [3,1,5,2,4]) == 3
