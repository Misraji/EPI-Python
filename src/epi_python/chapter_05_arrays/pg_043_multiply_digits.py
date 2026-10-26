"""EPI exercise 5.3, printed page 43: Multiply two arbitrary-precision integers.

EDUCATIONAL RECONSTRUCTION — not a verbatim verified code transcription.
Problem: Multiply two arbitrary-precision integers.
Method/complexity: Grade-school digit-by-digit multiplication; O(mn) time, O(m+n) result space.
For the book's original explanation and variants, see:
    pg_043_exercise_05_03_multiply_two_arbitrary_precision_integers.md

Run: python -m epi_python.chapter_05_arrays.pg_043_multiply_digits
Test: python -m pytest tests/chapter_05_arrays/test_pg_043_multiply_digits.py -v
"""

def multiply_digits(num1: list[int], num2: list[int]) -> list[int]:
    """Multiply signed arbitrary-precision decimal digit arrays."""
    if not num1 or not num2:
        raise ValueError("Both operands require at least one digit")
    sign = -1 if (num1[0] < 0) != (num2[0] < 0) else 1
    a, b = [abs(x) for x in num1], [abs(x) for x in num2]
    product = [0] * (len(a) + len(b))
    for i in range(len(a) - 1, -1, -1):
        for j in range(len(b) - 1, -1, -1):
            product[i + j + 1] += a[i] * b[j]
            product[i + j] += product[i + j + 1] // 10
            product[i + j + 1] %= 10
    start = 0
    while start < len(product) - 1 and product[start] == 0:
        start += 1
    result = product[start:]
    if result != [0]:
        result[0] *= sign
    return result


if __name__ == "__main__":
    for a, b in [([1, 2, 3], [4, 5]), ([-2], [3])]:
        print(f"{a} × {b} = {multiply_digits(a, b)}")
