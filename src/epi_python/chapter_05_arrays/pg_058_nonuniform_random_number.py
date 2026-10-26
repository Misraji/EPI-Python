"""EPI exercise 5.16, printed page 58: Generate nonuniform random numbers.

EDUCATIONAL RECONSTRUCTION — not a verbatim verified code transcription.
Problem: Generate nonuniform random numbers.
Method/complexity: Prefix sums O(n) plus O(log n) binary search per sample; O(n) extra space.
For the book's original explanation and variants, see:
    pg_058_exercise_05_16_generate_nonuniform_random_numbers.md

Run: python -m epi_python.chapter_05_arrays.pg_058_nonuniform_random_number
Test: python -m pytest tests/chapter_05_arrays/test_pg_058_nonuniform_random_number.py -v
"""

# bisect_left finds the insertion point in a sorted sequence in logarithmic time.
# Documentation: https://docs.python.org/3/library/bisect.html#bisect.bisect_left
import bisect

# itertools.accumulate yields running sums for cumulative probabilities.
# Documentation: https://docs.python.org/3/library/itertools.html#itertools.accumulate
import itertools

# random.random draws a uniform floating point value in [0, 1).
# Documentation: https://docs.python.org/3/library/random.html#random.random
import random


def nonuniform_random_number(values: list[int], probabilities: list[float], rng=None) -> int:
    """Draw values with prescribed nonnegative weights."""
    if len(values) != len(probabilities) or not values:
        raise ValueError("Expected nonempty equally sized value/weight arrays")
    if any(weight < 0 for weight in probabilities) or sum(probabilities) <= 0:
        raise ValueError("Weights must be nonnegative and not all zero")
    rng = random if rng is None else rng

    # accumulate([0.2, 0.3, 0.5]) produces 0.2, 0.5, 1.0.
    cumulative = list(itertools.accumulate(probabilities))
    choice = rng.random() * cumulative[-1]

    # bisect_right places an exact boundary in the following bucket.
    index = bisect.bisect_right(cumulative, choice)
    return values[min(index, len(values) - 1)]


if __name__ == "__main__":
    value = nonuniform_random_number(["red", "blue"], [1, 3], random.Random(2))
    print("weighted choice:", value)
    assert value in ("red", "blue")
