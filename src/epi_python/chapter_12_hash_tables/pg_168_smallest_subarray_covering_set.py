"""EPI exercise 12.6, printed page 168: Find the smallest subarray covering all values.

EDUCATIONAL RECONSTRUCTION — not a verbatim verified code transcription.
Problem: Find the smallest subarray covering all values.
Method/complexity: Sliding window with required-count map; O(n) time and O(|required|) space.
For the book's original explanation and variants, see:
    pg_168_exercise_12_06_find_the_smallest_subarray_covering_all_values.md

Run: python -m epi_python.chapter_12_hash_tables.pg_168_smallest_subarray_covering_set
Test: python -m pytest tests/chapter_12_hash_tables/test_pg_168_smallest_subarray_covering_set.py -v
"""

# Counter keeps a frequency count of values required in the window.
# Documentation: https://docs.python.org/3/library/collections.html#collections.Counter
from collections import Counter


def smallest_subarray_covering_set(values: list[str], required: set[str]) -> tuple[int, int] | None:
    """Return inclusive (start,end) of shortest window containing all required keys."""
    if not required:
        return (0, -1)
    need = Counter(required)
    still_missing = len(required)
    left = 0
    best = None
    for right, value in enumerate(values):
        if value in need:
            if need[value] > 0:
                still_missing -= 1
            need[value] -= 1
        while still_missing == 0:
            if best is None or right - left < best[1] - best[0]:
                best = (left, right)
            outgoing = values[left]
            if outgoing in need:
                need[outgoing] += 1
                if need[outgoing] > 0:
                    still_missing += 1
            left += 1
    return best


if __name__ == "__main__":
    words=["a","x","b","a","c","b"]
    print("covering window:", smallest_subarray_covering_set(words,{"a","b","c"}))
    assert smallest_subarray_covering_set(words,{"a","b","c"}) == (2,4)
