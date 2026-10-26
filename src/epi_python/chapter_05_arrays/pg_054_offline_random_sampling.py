"""EPI exercise 5.12, printed page 54: Sample offline data.

EDUCATIONAL RECONSTRUCTION — not a verbatim verified code transcription.
Problem: Sample offline data.
Method/complexity: Partial Fisher–Yates in-place shuffle; O(k) time, O(1) additional space excluding returned slice.
For the book's original explanation and variants, see:
    pg_054_exercise_05_12_sample_offline_data.md

Run: python -m epi_python.chapter_05_arrays.pg_054_offline_random_sampling
Test: python -m pytest tests/chapter_05_arrays/test_pg_054_offline_random_sampling.py -v
"""

# Python's random module supplies randint for an inclusive random index.
# Documentation: https://docs.python.org/3/library/random.html#random.randint
import random


def random_sampling(k: int, values: list[int], rng=None) -> list[int]:
    """Uniformly choose k array elements using partial Fisher–Yates shuffle."""
    if not 0 <= k <= len(values):
        raise ValueError("k must be between zero and len(values)")
    rng = random if rng is None else rng
    for i in range(k):
        j = rng.randint(i, len(values) - 1)
        values[i], values[j] = values[j], values[i]
    return values[:k]


if __name__ == "__main__":
    seeded = random.Random(11)
    values = list(range(6))
    selected = random_sampling(3, values, seeded)
    print("offline sample:", selected)
    assert len(selected) == 3 and len(set(selected)) == 3
