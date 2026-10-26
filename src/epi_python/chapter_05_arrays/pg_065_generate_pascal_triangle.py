"""EPI 5.20: Compute rows in Pascal's Triangle (printed page 65).

ORIGIN: Educational reconstruction based on the supplied EPI exercise.
NOT a verified line-for-line transcription of the textbook's Python snippet.

Question: Compute rows in Pascal's Triangle
Method: Each interior entry is the sum of the two entries above it. Time and space O(n²).

For the PDF text layer of the original problem, solution exposition, variants,
and complexity discussion, read the companion Markdown document:
    pg_065_exercise_05_20_compute_rows_in_pascal_s_triangle.md

Run independently:
    python -m epi_python.chapter_05_arrays.pg_065_generate_pascal_triangle
Run thorough tests:
    python -m pytest tests/chapter_05_arrays/test_pg_065_generate_pascal_triangle.py -v
"""

def generate_pascal_triangle(n: int) -> list[list[int]]:
    """Construct the first n rows of Pascal's triangle."""
    triangle = []
    for row_index in range(n):
        row = [1] * (row_index + 1)
        for column in range(1, row_index):
            row[column] = triangle[-1][column - 1] + triangle[-1][column]
        triangle.append(row)
    return triangle


if __name__ == "__main__":
    # Run a few self-contained examples before exploring the pytest suite.
    observed = generate_pascal_triangle(0)
    print("generate_pascal_triangle:", observed)
    assert observed == []
    observed = generate_pascal_triangle(1)
    print("generate_pascal_triangle:", observed)
    assert observed == [[1]]
    observed = generate_pascal_triangle(3)
    print("generate_pascal_triangle:", observed)
    assert observed == [[1], [1, 1], [1, 2, 1]]
    observed = generate_pascal_triangle(5)
    print("generate_pascal_triangle:", observed)
    assert observed == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
