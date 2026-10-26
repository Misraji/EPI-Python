"""EPI 5.8: Computing an alternation — printed page 48.

Educational reconstruction; not a verified verbatim textbook transcription.
Question: Computing an alternation
Algorithm: A single pass locally swaps neighbors until <=,>=,<= alternation holds.
Read the corresponding `pg_048_exercise_...md` file for the extracted
book's problem, worked explanations and variants. OCR is unverified.

Run: python -m epi_python.chapter_05_arrays.pg_048_rearrange_alternation
Test: python -m pytest tests/chapter_05_arrays/test_pg_048_rearrange_alternation.py -v
"""

def rearrange_alternation(values: list[int]) -> list[int]:
    """Return alternating <= and >= neighbors starting with <=."""
    result = values.copy()
    for i in range(len(result) - 1):
        if (i % 2 == 0 and result[i] > result[i + 1]) or (i % 2 and result[i] < result[i + 1]):
            result[i], result[i + 1] = result[i + 1], result[i]
    return result


if __name__ == "__main__":
    # Demonstrations check representative input/output behavior.
    observed = rearrange_alternation([])
    print("rearrange_alternation:", observed)
    assert observed == []
    observed = rearrange_alternation([3, 2])
    print("rearrange_alternation:", observed)
    assert observed == [2, 3]
    observed = rearrange_alternation([1, 2, 3, 4])
    print("rearrange_alternation:", observed)
    assert observed == [1, 3, 2, 4]
    observed = rearrange_alternation([4, 3, 2, 1])
    print("rearrange_alternation:", observed)
    assert observed == [3, 4, 1, 2]
