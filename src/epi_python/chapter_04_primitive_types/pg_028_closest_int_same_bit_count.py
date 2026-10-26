"""EPI 4.4: Find a closest integer with the same weight (printed page 28).

ORIGIN: Educational reconstruction based on the supplied EPI exercise.
NOT a verified line-for-line transcription of the textbook's Python snippet.

Question: Find a closest integer with the same weight
Method: Swapping the lowest adjacent unequal bits produces the nearest integer with equal bit weight. Time O(width).

For the PDF text layer of the original problem, solution exposition, variants,
and complexity discussion, read the companion Markdown document:
    pg_028_exercise_04_04_find_a_closest_integer_with_the_same_weight.md

Run independently:
    python -m epi_python.chapter_04_primitive_types.pg_028_closest_int_same_bit_count
Run thorough tests:
    python -m pytest tests/chapter_04_primitive_types/test_pg_028_closest_int_same_bit_count.py -v
"""

def closest_int_same_bit_count(x: int, width: int = 64) -> int:
    """Closest distinct fixed-width unsigned integer with equal popcount."""
    for i in range(width - 1):
        if ((x >> i) & 1) != ((x >> (i + 1)) & 1):
            return x ^ ((1 << i) | (1 << (i + 1)))
    raise ValueError("No distinct number of this width has the same popcount")


if __name__ == "__main__":
    # Run a few self-contained examples before exploring the pytest suite.
    observed = closest_int_same_bit_count(6, 8)
    print("closest_int_same_bit_count:", observed)
    assert observed == 5
    observed = closest_int_same_bit_count(7, 8)
    print("closest_int_same_bit_count:", observed)
    assert observed == 11
    observed = closest_int_same_bit_count(8, 8)
    print("closest_int_same_bit_count:", observed)
    assert observed == 4
    observed = closest_int_same_bit_count(10, 8)
    print("closest_int_same_bit_count:", observed)
    assert observed == 9
