"""EPI exercise 4.5, printed page 29: Compute x times y without arithmetical operators.

EDUCATIONAL RECONSTRUCTION — not a verbatim verified code transcription.
Problem: Compute x times y without arithmetical operators.
Method/complexity: Repeated shift/add; O(bit_length(x) * bit_length(product)) bit operations; constant-size local state.
For the book's original explanation and variants, see:
    pg_029_exercise_04_05_compute_x_times_y_without_arithmetical_operators.md

Run: python -m epi_python.chapter_04_primitive_types.pg_029_multiply_without_arithmetic
Test: python -m pytest tests/chapter_04_primitive_types/test_pg_029_multiply_without_arithmetic.py -v
"""

def add_bits(a: int, b: int) -> int:
    """Add two nonnegative integers using only Boolean bit operations."""
    while b:
        # XOR produces the sum bits; AND and shift compute carries.
        a, b = a ^ b, (a & b) << 1
    return a


def multiply(x: int, y: int) -> int:
    """Multiply nonnegative integers without + or * inside the algorithm."""
    if x < 0 or y < 0:
        raise ValueError("This problem works with nonnegative integers")
    result = 0
    while x:
        if x & 1:
            result = add_bits(result, y)
        x >>= 1
        y <<= 1
    return result


if __name__ == "__main__":
    for x, y in [(7, 6), (13, 9), (0, 5)]:
        print(f"{x} * {y} = {multiply(x, y)}")
        assert multiply(x, y) == x * y
