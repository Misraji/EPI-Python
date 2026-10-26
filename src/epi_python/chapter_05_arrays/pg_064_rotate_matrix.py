"""EPI exercise 5.19, printed page 64: Rotate a 2D array.

EDUCATIONAL RECONSTRUCTION — not a verbatim verified code transcription.
Problem: Rotate a 2D array.
Method/complexity: In-place four-way swaps per ring; O(n²) time and O(1) extra space.
For the book's original explanation and variants, see:
    pg_064_exercise_05_19_rotate_a_2d_array.md

Run: python -m epi_python.chapter_05_arrays.pg_064_rotate_matrix
Test: python -m pytest tests/chapter_05_arrays/test_pg_064_rotate_matrix.py -v
"""

def rotate_matrix(matrix: list[list[int]]) -> list[list[int]]:
    """Rotate a square image matrix 90 degrees clockwise, in place."""
    n = len(matrix)
    if any(len(row) != n for row in matrix):
        raise ValueError("Rotation requires an n x n square matrix")
    for layer in range(n // 2):
        lo, hi = layer, n - 1 - layer
        for j in range(hi - lo):
            top = matrix[lo][lo + j]
            matrix[lo][lo + j] = matrix[hi - j][lo]
            matrix[hi - j][lo] = matrix[hi][hi - j]
            matrix[hi][hi - j] = matrix[lo + j][hi]
            matrix[lo + j][hi] = top
    return matrix


if __name__ == "__main__":
    m = [[1, 2], [3, 4]]
    print("rotated matrix:", rotate_matrix(m))
    assert m == [[3, 1], [4, 2]]
