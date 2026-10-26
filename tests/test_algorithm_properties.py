"""Small deterministic experiments comparing fast code with simple oracles.

These examples teach independent reference testing. Randomness is explicitly
seeded, so CI repeats exactly the same experiments on every run.
"""

# Python's itertools and random modules are both in the standard library.
# Documentation: https://docs.python.org/3/library/itertools.html
import itertools

# Documentation: https://docs.python.org/3/library/random.html
import random

# Documentation: https://docs.python.org/3/library/math.html#math.isqrt
import math

# Documentation: https://docs.python.org/3/library/statistics.html#statistics.median
import statistics

from epi_python.chapter_05_arrays.pg_043_plus_one import plus_one
from epi_python.chapter_05_arrays.pg_052_next_permutation import next_permutation
from epi_python.chapter_06_strings.pg_079_rabin_karp import rabin_karp
from epi_python.chapter_10_heaps.pg_139_online_median import online_median
from epi_python.chapter_11_searching.pg_148_square_root import square_root
from epi_python.chapter_12_hash_tables.pg_173_longest_subarray_with_distinct_entries import (
    longest_subarray_with_distinct_entries,
)
from epi_python.chapter_16_dynamic_programming.pg_257_longest_nondecreasing_subsequence import (
    longest_nondecreasing_subsequence,
)
from epi_python.chapter_17_greedy_algorithms_and_invariants.pg_264_has_three_sum import has_three_sum
from epi_python.chapter_24_honors_class.pg_365_max_of_sliding_window import max_of_sliding_window
from epi_python.chapter_24_honors_class.pg_390_max_subarray_sum_in_circular_array import (
    max_subarray_sum_in_circular_array,
)


def test_plus_one_against_integer_arithmetic():
    """Compare decimal digit arithmetic with an independent Python integer."""
    for value in range(0, 300):
        digits = [int(char) for char in str(value)]
        expected = [int(char) for char in str(value + 1)]
        assert plus_one(digits) == expected


def test_next_permutation_against_itertools():
    """Compare the algorithm to lexicographically sorted permutations."""
    for n in range(1, 5):
        sequence = list(itertools.permutations(range(n)))
        for index, item in enumerate(sequence):
            expected = list(sequence[index + 1]) if index + 1 < len(sequence) else []
            assert next_permutation(list(item)) == expected


def test_rabin_karp_against_str_find():
    rng = random.Random(47)
    for _ in range(250):
        text = "".join(rng.choices("abc", k=rng.randrange(20)))
        pattern = "".join(rng.choices("abc", k=rng.randrange(6)))
        assert rabin_karp(text, pattern) == text.find(pattern)


def test_online_median_against_statistics():
    rng = random.Random(9)
    for _ in range(30):
        values = [rng.randrange(-30, 31) for _ in range(18)]
        expected = [statistics.median(values[: i + 1]) for i in range(len(values))]
        assert online_median(values) == expected


def test_integer_square_root_against_python_math():
    for value in range(0, 1000):
        assert square_root(value) == math.isqrt(value)
    for value in [10**10, 10**20, 10**30]:
        assert square_root(value) == math.isqrt(value)


def test_distinct_window_against_brute_force():
    rng = random.Random(8)
    for _ in range(300):
        values = [rng.randrange(4) for _ in range(rng.randrange(9))]
        brute = 0
        for i in range(len(values)):
            for j in range(i + 1, len(values) + 1):
                if len(set(values[i:j])) == j - i:
                    brute = max(brute, j - i)
        assert longest_subarray_with_distinct_entries(values) == brute


def test_lnds_against_brute_force_subsets():
    rng = random.Random(13)
    for _ in range(90):
        values = [rng.randrange(5) for _ in range(rng.randrange(9))]
        best = 0
        for mask in range(1 << len(values)):
            subset = [value for i, value in enumerate(values) if mask & (1 << i)]
            if all(a <= b for a, b in zip(subset, subset[1:])):
                best = max(best, len(subset))
        assert longest_nondecreasing_subsequence(values) == best


def test_three_sum_against_brute_force_with_repetition():
    rng = random.Random(16)
    for _ in range(120):
        values = [rng.randrange(-5, 6) for _ in range(rng.randrange(8))]
        target = rng.randrange(-10, 11)
        expected = any(a + b + c == target for a in values for b in values for c in values)
        assert has_three_sum(values, target) == expected


def test_sliding_window_against_built_in_max():
    rng = random.Random(21)
    for _ in range(100):
        values = [rng.randrange(-10, 11) for _ in range(rng.randrange(12))]
        k = rng.randrange(1, 14)
        expected = [max(values[i : i + k]) for i in range(max(0, len(values) - k + 1))]
        assert max_of_sliding_window(values, k) == expected


def test_circular_sum_against_all_circular_segments():
    rng = random.Random(29)
    for _ in range(180):
        values = [rng.randrange(-8, 9) for _ in range(rng.randrange(1, 9))]
        n = len(values)
        expected = max(
            sum(values[(start + j) % n] for j in range(length))
            for start in range(n)
            for length in range(1, n + 1)
        )
        assert max_subarray_sum_in_circular_array(values) == expected
