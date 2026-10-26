"""EPI exercise 5.14, printed page 56: Compute a random permutation.

EDUCATIONAL RECONSTRUCTION — not a verbatim verified code transcription.
Problem: Compute a random permutation.
Method/complexity: Fisher–Yates shuffle; O(n) time and O(n) output memory.
For the book's original explanation and variants, see:
    pg_056_exercise_05_14_compute_a_random_permutation.md

Run: python -m epi_python.chapter_05_arrays.pg_056_compute_random_permutation
Test: python -m pytest tests/chapter_05_arrays/test_pg_056_compute_random_permutation.py -v
"""

# The random module implements unbiased integer selection for Fisher–Yates.
# Documentation: https://docs.python.org/3/library/random.html
import random


def compute_random_permutation(n: int, rng=None) -> list[int]:
    """Construct a random permutation of integers from zero through n-1."""
    if n < 0:
        raise ValueError("n must be nonnegative")
    rng = random if rng is None else rng
    permutation = list(range(n))
    for i in range(n):
        j = rng.randrange(i, n)
        permutation[i], permutation[j] = permutation[j], permutation[i]
    return permutation


if __name__ == "__main__":
    permutation = compute_random_permutation(8, random.Random(42))
    print("permutation:", permutation)
    assert sorted(permutation) == list(range(8))
