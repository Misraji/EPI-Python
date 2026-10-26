"""EPI 11.4: Compute the integer square root — printed page 148.

Educational reconstruction; not a verified verbatim textbook transcription.
Question: Compute the integer square root
Algorithm: Binary search for largest integer whose square does not exceed k.
Read the corresponding `pg_148_exercise_...md` file for the extracted
book's problem, worked explanations and variants. OCR is unverified.

Run: python -m epi_python.chapter_11_searching.pg_148_square_root
Test: python -m pytest tests/chapter_11_searching/test_pg_148_square_root.py -v
"""

def square_root(k: int) -> int:
    """Floor of the integer square root of nonnegative k."""
    if k < 0:
        raise ValueError('negative input')
    left,right = 0,k
    result=0
    while left <= right:
        middle=(left+right)//2
        if middle*middle <= k:
            result=middle
            left=middle+1
        else:
            right=middle-1
    return result


if __name__ == "__main__":
    # Demonstrations check representative input/output behavior.
    observed = square_root(0)
    print("square_root:", observed)
    assert observed == 0
    observed = square_root(1)
    print("square_root:", observed)
    assert observed == 1
    observed = square_root(2)
    print("square_root:", observed)
    assert observed == 1
    observed = square_root(15)
    print("square_root:", observed)
    assert observed == 3
