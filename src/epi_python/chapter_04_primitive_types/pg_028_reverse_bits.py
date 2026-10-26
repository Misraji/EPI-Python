"""EPI 4.3: Reverse bits (printed page 28).

ORIGIN: Educational reconstruction based on the supplied EPI exercise.
NOT a verified line-for-line transcription of the textbook's Python snippet.

Question: Reverse bits
Method: Move the least significant input bit into the most significant available output position. Time O(width).

For the PDF text layer of the original problem, solution exposition, variants,
and complexity discussion, read the companion Markdown document:
    pg_028_exercise_04_03_reverse_bits.md

Run independently:
    python -m epi_python.chapter_04_primitive_types.pg_028_reverse_bits
Run thorough tests:
    python -m pytest tests/chapter_04_primitive_types/test_pg_028_reverse_bits.py -v
"""

def reverse_bits(x: int, width: int = 64) -> int:
    """Reverse the low `width` bits; the textbook considers 64-bit words."""
    result = 0
    for _ in range(width):
        result = (result << 1) | (x & 1)
        x >>= 1
    return result


if __name__ == "__main__":
    # Run a few self-contained examples before exploring the pytest suite.
    observed = reverse_bits(0, 8)
    print("reverse_bits:", observed)
    assert observed == 0
    observed = reverse_bits(1, 8)
    print("reverse_bits:", observed)
    assert observed == 128
    observed = reverse_bits(3, 4)
    print("reverse_bits:", observed)
    assert observed == 12
    observed = reverse_bits(5, 4)
    print("reverse_bits:", observed)
    assert observed == 10
    observed = reverse_bits(255, 8)
    print("reverse_bits:", observed)
    assert observed == 255
