"""EPI 24.2: Find the first missing positive entry — printed page 352.

Educational reconstruction; not a verified verbatim textbook transcription.
Question: Find the first missing positive entry
Algorithm: Place value v at index v-1 if possible; the first incorrect position is missing.
Read the corresponding `pg_352_exercise_...md` file for the extracted
book's problem, worked explanations and variants. OCR is unverified.

Run: python -m epi_python.chapter_24_honors_class.pg_352_first_missing_positive
Test: python -m pytest tests/chapter_24_honors_class/test_pg_352_first_missing_positive.py -v
"""

def first_missing_positive(values: list[int]) -> int:
    """Smallest missing positive integer (in-place cyclic-placement strategy)."""
    data=values.copy()
    n=len(data)
    for i in range(n):
        while 1<=data[i]<=n and data[data[i]-1] != data[i]:
            target=data[i]-1
            data[i],data[target]=data[target],data[i]
    for index,value in enumerate(data):
        if value != index+1:
            return index+1
    return n+1


if __name__ == "__main__":
    # Demonstrations check representative input/output behavior.
    observed = first_missing_positive([])
    print("first_missing_positive:", observed)
    assert observed == 1
    observed = first_missing_positive([1, 2, 3])
    print("first_missing_positive:", observed)
    assert observed == 4
    observed = first_missing_positive([3, 4, -1, 1])
    print("first_missing_positive:", observed)
    assert observed == 2
    observed = first_missing_positive([1, 1])
    print("first_missing_positive:", observed)
    assert observed == 2
