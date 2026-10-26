"""EPI exercise 4.10, printed page 34: Generate uniform random numbers.

EDUCATIONAL RECONSTRUCTION — not a verbatim verified code transcription.
Problem: Generate uniform random numbers.
Method/complexity: Rejection sampling; expected O(log(range_size)) calls to an unbiased bit source.
For the book's original explanation and variants, see:
    pg_034_exercise_04_10_generate_uniform_random_numbers.md

Run: python -m epi_python.chapter_04_primitive_types.pg_034_uniform_random
Test: python -m pytest tests/chapter_04_primitive_types/test_pg_034_uniform_random.py -v
"""

# The random module supplies a source of pseudorandom bits.
# Documentation: https://docs.python.org/3/library/random.html
import random


def uniform_random(lower_bound: int, upper_bound: int, bit_source=None) -> int:
    """Sample an inclusive integer interval using only unbiased random bits."""
    if lower_bound > upper_bound:
        raise ValueError("Lower bound must not exceed upper bound")
    if bit_source is None:
        # getrandbits(1) returns either zero or one with equal probability.
        bit_source = lambda: random.getrandbits(1)
    n = upper_bound - lower_bound + 1
    while True:
        result = 0
        for _ in range((n - 1).bit_length()):
            result = (result << 1) | bit_source()
        # Rejection sampling removes modulo bias when n is not a power of two.
        if result < n:
            return lower_bound + result


if __name__ == "__main__":
    rng = random.Random(42)
    for _ in range(3):
        value = uniform_random(4, 9, lambda: rng.getrandbits(1))
        print("uniform_random(4, 9):", value)
        assert 4 <= value <= 9
