"""EPI exercise 11.5, printed page 149: Compute the real square root.

EDUCATIONAL RECONSTRUCTION — not a verbatim verified code transcription.
Problem: Compute the real square root.
Method/complexity: Binary search across real interval; O(log(range/tolerance)) iterations, O(1) space.
For the book's original explanation and variants, see:
    pg_149_exercise_11_05_compute_the_real_square_root.md

Run: python -m epi_python.chapter_11_searching.pg_149_real_square_root
Test: python -m pytest tests/chapter_11_searching/test_pg_149_real_square_root.py -v
"""

def square_root(x: float, tolerance: float = 1e-12) -> float:
    """Approximate real sqrt(x) by binary search over a range that brackets it."""
    if x < 0:
        raise ValueError("Square root of negative real is undefined")
    if x == 0 or x == 1:
        return x
    left, right = (x, 1.0) if x < 1 else (1.0, x)
    while right - left > tolerance * max(1.0, right):
        middle = (left + right) / 2
        if middle * middle > x:
            right = middle
        else:
            left = middle
    return (left + right) / 2


if __name__ == "__main__":
    for x in (2., 0.25, 100.):
        approximation = square_root(x)
        print("sqrt:", x, approximation)
        assert abs(approximation ** 2 - x) < 1e-7
