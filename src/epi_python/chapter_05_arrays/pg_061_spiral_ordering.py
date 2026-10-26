"""EPI exercise 5.18, printed page 61: Compute the spiral ordering of a 2D array.

EDUCATIONAL RECONSTRUCTION — not a verbatim verified code transcription.
Problem: Compute the spiral ordering of a 2D array.
Method/complexity: Perimeter walk with moving boundaries; O(mn) time and O(mn) output memory.
For the book's original explanation and variants, see:
    pg_061_exercise_05_18_compute_the_spiral_ordering_of_a_2d_array.md

Run: python -m epi_python.chapter_05_arrays.pg_061_spiral_ordering
Test: python -m pytest tests/chapter_05_arrays/test_pg_061_spiral_ordering.py -v
"""

def matrix_in_spiral_order(matrix: list[list[int]]) -> list[int]:
    """Return clockwise perimeter rings from a rectangular matrix."""
    if not matrix:
        return []
    if any(len(row) != len(matrix[0]) for row in matrix):
        raise ValueError("All matrix rows must be same length")
    result: list[int] = []
    top, bottom = 0, len(matrix) - 1
    left, right = 0, len(matrix[0]) - 1
    while top <= bottom and left <= right:
        result.extend(matrix[top][left:right + 1])
        top += 1
        for r in range(top, bottom + 1):
            result.append(matrix[r][right])
        right -= 1
        if top <= bottom:
            result.extend(reversed(matrix[bottom][left:right + 1]))
            bottom -= 1
        if left <= right:
            for r in range(bottom, top - 1, -1):
                result.append(matrix[r][left])
            left += 1
    return result


if __name__ == "__main__":
    m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print("spiral order:", matrix_in_spiral_order(m))
    assert matrix_in_spiral_order(m) == [1, 2, 3, 6, 9, 8, 7, 4, 5]
