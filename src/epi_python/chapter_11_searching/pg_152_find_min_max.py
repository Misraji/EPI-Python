"""EPI exercise 11.7, printed page 152: Find the min and max simultaneously.

EDUCATIONAL RECONSTRUCTION — not a verbatim verified code transcription.
Problem: Find the min and max simultaneously.
Method/complexity: Examine input pairs; O(n) time and O(1) space.
For the book's original explanation and variants, see:
    pg_152_exercise_11_07_find_the_min_and_max_simultaneously.md

Run: python -m epi_python.chapter_11_searching.pg_152_find_min_max
Test: python -m pytest tests/chapter_11_searching/test_pg_152_find_min_max.py -v
"""

def find_min_max(values: list[int]) -> tuple[int, int]:
    """Find both extrema with pairwise comparisons (~3n/2 compares)."""
    if not values:
        raise ValueError("Requires nonempty input")
    if len(values) % 2:
        low = high = values[0]
        start = 1
    else:
        low, high = sorted(values[:2])
        start = 2
    for i in range(start, len(values), 2):
        small, large = sorted((values[i], values[i+1]))
        low, high = min(low, small), max(high, large)
    return low, high


if __name__ == "__main__":
    print("min and max:", find_min_max([4, 1, 3, 2]))
    assert find_min_max([4, 1, 3, 2]) == (1, 4)
