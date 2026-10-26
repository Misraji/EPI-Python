"""EPI 11.6: Search in a 2D sorted array — printed page 150.

Educational reconstruction; not a verified verbatim textbook transcription.
Question: Search in a 2D sorted array
Algorithm: Start in the upper-right; discard a row or column with each comparison.
Read the corresponding `pg_150_exercise_...md` file for the extracted
book's problem, worked explanations and variants. OCR is unverified.

Run: python -m epi_python.chapter_11_searching.pg_150_matrix_search
Test: python -m pytest tests/chapter_11_searching/test_pg_150_matrix_search.py -v
"""

def matrix_search(matrix: list[list[int]], target: int) -> bool:
    """Search a matrix with sorted rows and columns."""
    if not matrix or not matrix[0]:
        return False
    row,col=0,len(matrix[0])-1
    while row < len(matrix) and col >= 0:
        value=matrix[row][col]
        if value == target:
            return True
        if value > target:
            col-=1
        else:
            row+=1
    return False


if __name__ == "__main__":
    # Demonstrations check representative input/output behavior.
    observed = matrix_search([[1, 3, 5], [2, 4, 6]], 4)
    print("matrix_search:", observed)
    assert observed == True
    observed = matrix_search([[1, 3, 5], [2, 4, 6]], 7)
    print("matrix_search:", observed)
    assert observed == False
    observed = matrix_search([], 2)
    print("matrix_search:", observed)
    assert observed == False
