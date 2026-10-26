"""EPI exercise 12.10, printed page 175: Compute all string decompositions.

EDUCATIONAL RECONSTRUCTION — not a verbatim verified code transcription.
Problem: Compute all string decompositions.
Method/complexity: Brute sliding start, Counter over k tokens each: O(n*k) expected time, O(k) memory.
For the book's original explanation and variants, see:
    pg_175_exercise_12_10_compute_all_string_decompositions.md

Run: python -m epi_python.chapter_12_hash_tables.pg_175_string_decompositions
Test: python -m pytest tests/chapter_12_hash_tables/test_pg_175_string_decompositions.py -v
"""

# Counter compares the multiset of dictionary words used by a candidate window.
# Documentation: https://docs.python.org/3/library/collections.html#collections.Counter
from collections import Counter


def find_all_substrings(s: str, words: list[str]) -> list[int]:
    """Return starts where equal-length dictionary words concatenate in any order."""
    if not words or not words[0]:
        return []
    width = len(words[0])
    if any(len(word) != width for word in words):
        raise ValueError("All dictionary words must have equal length")
    target = Counter(words)
    span = width * len(words)
    found = []
    for start in range(len(s) - span + 1):
        pieces = [s[i:i+width] for i in range(start,start+span,width)]
        if Counter(pieces) == target:
            found.append(start)
    return found


if __name__ == "__main__":
    print("word concatenations:", find_all_substrings("barfoothefoobarman",["foo","bar"]))
    assert find_all_substrings("barfoothefoobarman",["foo","bar"]) == [0,9]
