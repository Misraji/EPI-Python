"""EPI exercise 5.13, printed page 55: Sample online data.

EDUCATIONAL RECONSTRUCTION — not a verbatim verified code transcription.
Problem: Sample online data.
Method/complexity: Reservoir sampling; O(n) time and O(k) space, for streaming inputs.
For the book's original explanation and variants, see:
    pg_055_exercise_05_13_sample_online_data.md

Run: python -m epi_python.chapter_05_arrays.pg_055_online_random_sampling
Test: python -m pytest tests/chapter_05_arrays/test_pg_055_online_random_sampling.py -v
"""

# itertools.islice lazily takes at most k entries without consuming the whole stream.
# Documentation: https://docs.python.org/3/library/itertools.html#itertools.islice
import itertools

# The random module provides uniform integer selection for reservoir replacement.
# Documentation: https://docs.python.org/3/library/random.html#random.randrange
import random


def online_random_sample(stream, k: int, rng=None) -> list:
    """Reservoir-sample k elements from a one-pass iterable."""
    if k < 0:
        raise ValueError("k must be nonnegative")
    rng = random if rng is None else rng

    # islice(stream, k) obtains the first k elements and stops immediately.
    # It works for generators and iterators, not just lists.
    iterator = iter(stream)
    reservoir = list(itertools.islice(iterator, k))
    if len(reservoir) != k:
        raise ValueError("Expected at least k input elements")
    for count, element in enumerate(iterator, start=k + 1):
        slot = rng.randrange(count)
        if slot < k:
            reservoir[slot] = element
    return reservoir


if __name__ == "__main__":
    selected = online_random_sample(iter(range(10)), 3, random.Random(42))
    print("online sample:", selected)
    assert len(selected) == 3 and len(set(selected)) == 3
