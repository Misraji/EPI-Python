"""EPI 16.4: Compute the binomial coefficients — printed page 244.

Educational reconstruction; not a verified verbatim textbook transcription.
Question: Compute the binomial coefficients
Algorithm: Build the row of Pascal’s triangle until row n, then read entry k.
Read the corresponding `pg_244_exercise_...md` file for the extracted
book's problem, worked explanations and variants. OCR is unverified.

Run: python -m epi_python.chapter_16_dynamic_programming.pg_244_compute_binomial_coefficients
Test: python -m pytest tests/chapter_16_dynamic_programming/test_pg_244_compute_binomial_coefficients.py -v
"""

def compute_binomial_coefficients(n: int, k: int) -> int:
    """Compute n choose k using Pascal's addition rule."""
    if k < 0 or k > n:
        return 0
    row=[1]
    for i in range(1,n+1):
        current=[1]*(i+1)
        for j in range(1,i):
            current[j]=row[j-1]+row[j]
        row=current
    return row[k]


if __name__ == "__main__":
    # Demonstrations check representative input/output behavior.
    observed = compute_binomial_coefficients(0, 0)
    print("compute_binomial_coefficients:", observed)
    assert observed == 1
    observed = compute_binomial_coefficients(5, 2)
    print("compute_binomial_coefficients:", observed)
    assert observed == 10
    observed = compute_binomial_coefficients(4, 4)
    print("compute_binomial_coefficients:", observed)
    assert observed == 1
    observed = compute_binomial_coefficients(4, 5)
    print("compute_binomial_coefficients:", observed)
    assert observed == 0
