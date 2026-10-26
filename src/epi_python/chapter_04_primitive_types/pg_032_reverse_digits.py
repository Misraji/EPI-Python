"""EPI 4.8: Reverse digits (printed page 32).

ORIGIN: Educational reconstruction based on the supplied EPI exercise.
NOT a verified line-for-line transcription of the textbook's Python snippet.

Question: Reverse digits
Method: Peel off rightmost decimal digits using remainder and integer division. Time O(number of digits).

For the PDF text layer of the original problem, solution exposition, variants,
and complexity discussion, read the companion Markdown document:
    pg_032_exercise_04_08_reverse_digits.md

Run independently:
    python -m epi_python.chapter_04_primitive_types.pg_032_reverse_digits
Run thorough tests:
    python -m pytest tests/chapter_04_primitive_types/test_pg_032_reverse_digits.py -v
"""

def reverse_digits(x: int) -> int:
    """Reverse base-10 digits, preserving the sign."""
    negative = x < 0
    remaining = abs(x)
    result = 0
    while remaining:
        result = result * 10 + remaining % 10
        remaining //= 10
    return -result if negative else result


if __name__ == "__main__":
    # Run a few self-contained examples before exploring the pytest suite.
    observed = reverse_digits(0)
    print("reverse_digits:", observed)
    assert observed == 0
    observed = reverse_digits(123)
    print("reverse_digits:", observed)
    assert observed == 321
    observed = reverse_digits(-123)
    print("reverse_digits:", observed)
    assert observed == -321
    observed = reverse_digits(120)
    print("reverse_digits:", observed)
    assert observed == 21
    observed = reverse_digits(1)
    print("reverse_digits:", observed)
    assert observed == 1
