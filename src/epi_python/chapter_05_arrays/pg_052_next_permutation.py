"""EPI 5.11: Compute the next permutation — printed page 52.

Educational reconstruction; not a verified verbatim textbook transcription.
Question: Compute the next permutation
Algorithm: Find rightmost ascent, swap with the smallest larger suffix value, reverse the suffix.
Read the corresponding `pg_052_exercise_...md` file for the extracted
book's problem, worked explanations and variants. OCR is unverified.

Run: python -m epi_python.chapter_05_arrays.pg_052_next_permutation
Test: python -m pytest tests/chapter_05_arrays/test_pg_052_next_permutation.py -v
"""

def next_permutation(values: list[int]) -> list[int]:
    """Lexicographically next permutation, or [] if this is the last."""
    result = values.copy()
    pivot = len(result) - 2
    while pivot >= 0 and result[pivot] >= result[pivot + 1]:
        pivot -= 1
    if pivot < 0:
        return []
    swap = len(result) - 1
    while result[swap] <= result[pivot]:
        swap -= 1
    result[pivot], result[swap] = result[swap], result[pivot]

    # list.reverse() reverses the mutable suffix in-place; a slice copies it.
    # Documentation: https://docs.python.org/3/library/stdtypes.html#mutable-sequence-types
    result[pivot + 1:] = reversed(result[pivot + 1:])
    return result


if __name__ == "__main__":
    # Demonstrations check representative input/output behavior.
    observed = next_permutation([])
    print("next_permutation:", observed)
    assert observed == []
    observed = next_permutation([1])
    print("next_permutation:", observed)
    assert observed == []
    observed = next_permutation([1, 2, 3])
    print("next_permutation:", observed)
    assert observed == [1, 3, 2]
    observed = next_permutation([3, 2, 1])
    print("next_permutation:", observed)
    assert observed == []
