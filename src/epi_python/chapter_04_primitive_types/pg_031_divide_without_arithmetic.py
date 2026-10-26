"""EPI exercise 4.6, printed page 31: Compute x divided by y.

EDUCATIONAL RECONSTRUCTION — not a verbatim verified code transcription.
Problem: Compute x divided by y.
Method/complexity: Repeatedly subtract largest doubled divisor; O(log² x) simple-shift worst case, O(1) auxiliary space.
For the book's original explanation and variants, see:
    pg_031_exercise_04_06_compute_x_divided_by_y.md

Run: python -m epi_python.chapter_04_primitive_types.pg_031_divide_without_arithmetic
Test: python -m pytest tests/chapter_04_primitive_types/test_pg_031_divide_without_arithmetic.py -v
"""

def divide(x: int, y: int) -> int:
    """Compute floor(x / y) for nonnegative x and positive y."""
    if x < 0 or y <= 0:
        raise ValueError("Expected x >= 0 and y > 0")
    quotient = 0
    while x >= y:
        multiple, factor = y, 1
        while (multiple << 1) <= x:
            multiple <<= 1
            factor <<= 1
        quotient += factor
        x -= multiple
    return quotient


if __name__ == "__main__":
    for a, b in [(17, 3), (6, 3), (0, 1)]:
        print(f"{a} // {b} = {divide(a, b)}")
        assert divide(a, b) == a // b
