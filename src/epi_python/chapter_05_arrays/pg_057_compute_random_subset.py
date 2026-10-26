"""EPI exercise 5.15, printed page 57: Compute a random subset.

EDUCATIONAL RECONSTRUCTION — not a verbatim verified code transcription.
Problem: Compute a random subset.
Method/complexity: Sparse Fisher–Yates shuffle; expected O(k) time and O(k) space.
For the book's original explanation and variants, see:
    pg_057_exercise_05_15_compute_a_random_subset.md

Run: python -m epi_python.chapter_05_arrays.pg_057_compute_random_subset
Test: python -m pytest tests/chapter_05_arrays/test_pg_057_compute_random_subset.py -v
"""

# Random supplies a bounded unbiased integer selection.
# Documentation: https://docs.python.org/3/library/random.html#random.randrange
import random


def random_subset(n: int, k: int, rng=None) -> list[int]:
    """Select k distinct members of range(n) using a sparse virtual shuffle."""
    if not 0 <= k <= n:
        raise ValueError("Expected 0 <= k <= n")
    rng = random if rng is None else rng
    changed: dict[int, int] = {}
    for i in range(k):
        r = rng.randrange(i, n)
        x, y = changed.get(i, i), changed.get(r, r)
        changed[i], changed[r] = y, x
    return [changed[i] for i in range(k)]


if __name__ == "__main__":
    sample = random_subset(100, 5, random.Random(12))
    print("random subset:", sample)
    assert len(set(sample)) == 5 and all(0 <= x < 100 for x in sample)
