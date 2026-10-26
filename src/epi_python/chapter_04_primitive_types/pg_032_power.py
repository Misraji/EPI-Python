"""EPI exercise 4.7, printed page 32: Compute x to the power y.

EDUCATIONAL RECONSTRUCTION — not a verbatim verified code transcription.
Problem: Compute x to the power y.
Method/complexity: Binary exponentiation; O(log |y|) multiplications, O(1) auxiliary space.
For the book's original explanation and variants, see:
    pg_032_exercise_04_07_compute_x_to_the_power_y.md

Run: python -m epi_python.chapter_04_primitive_types.pg_032_power
Test: python -m pytest tests/chapter_04_primitive_types/test_pg_032_power.py -v
"""

def power(x: float, y: int) -> float:
    """Exponentiation by squaring; supports negative integer powers."""
    if y < 0:
        if x == 0:
            raise ZeroDivisionError("0 cannot be raised to a negative power")
        x, y = 1.0 / x, -y
    result = 1.0
    while y:
        if y & 1:
            result *= x
        x *= x
        y >>= 1
    return result


if __name__ == "__main__":
    for x, y in [(2.0, 10), (2.0, -2), (-2.0, 3)]:
        print(f"{x} ** {y} = {power(x, y)}")
        assert power(x, y) == x ** y
