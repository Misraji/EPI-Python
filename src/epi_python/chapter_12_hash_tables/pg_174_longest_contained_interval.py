"""EPI exercise 12.9, printed page 174: Find the length of a longest contained interval.

EDUCATIONAL RECONSTRUCTION — not a verbatim verified code transcription.
Problem: Find the length of a longest contained interval.
Method/complexity: Hash-set expansion at most once per distinct element; expected O(n) time, O(n) space.
For the book's original explanation and variants, see:
    pg_174_exercise_12_09_find_the_length_of_a_longest_contained_interval.md

Run: python -m epi_python.chapter_12_hash_tables.pg_174_longest_contained_interval
Test: python -m pytest tests/chapter_12_hash_tables/test_pg_174_longest_contained_interval.py -v
"""

def longest_contained_range(values: list[int]) -> int:
    """Return the largest run of consecutive integers present, regardless of order."""
    remaining = set(values)
    longest = 0
    while remaining:
        current = remaining.pop()
        length = 1
        low, high = current - 1, current + 1
        while low in remaining:
            remaining.remove(low)
            low -= 1
            length += 1
        while high in remaining:
            remaining.remove(high)
            high += 1
            length += 1
        longest = max(longest, length)
    return longest


if __name__ == "__main__":
    data=[3,-2,7,9,8,1,2,0,-1,5,8]
    print("consecutive interval length:", longest_contained_range(data))
    assert longest_contained_range(data) == 6
