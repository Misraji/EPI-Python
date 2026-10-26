"""EPI exercise 11.10, printed page 157: Find the duplicate and missing elements.

EDUCATIONAL RECONSTRUCTION — not a verbatim verified code transcription.
Problem: Find the duplicate and missing elements.
Method/complexity: XOR over array and expected positions; O(n) time, O(1) auxiliary space.
For the book's original explanation and variants, see:
    pg_157_exercise_11_10_find_the_duplicate_and_missing_elements.md

Run: python -m epi_python.chapter_11_searching.pg_157_find_duplicate_missing
Test: python -m pytest tests/chapter_11_searching/test_pg_157_find_duplicate_missing.py -v
"""

def find_duplicate_missing(values: list[int]) -> tuple[int, int]:
    """Return (duplicate, missing) among indices 0..n-1 using XOR partition."""
    n = len(values)
    if n < 2:
        raise ValueError("Need at least two positions")
    difference = 0
    for i, value in enumerate(values):
        difference ^= i ^ value
    bit = difference & -difference
    if bit == 0:
        raise ValueError("Expected exactly one duplicate and missing entry")
    candidate = 0
    for i, value in enumerate(values):
        if i & bit:
            candidate ^= i
        if value & bit:
            candidate ^= value
    if values.count(candidate) == 2:
        return candidate, candidate ^ difference
    return candidate ^ difference, candidate


if __name__ == "__main__":
    print("duplicate, missing:", find_duplicate_missing([0, 1, 1, 3]))
    assert find_duplicate_missing([0,1,1,3]) == (1,2)
