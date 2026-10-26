"""EPI 13.4: Smallest nonconstructible value — printed page 185.

Educational reconstruction; not a verified verbatim textbook transcription.
Question: Smallest nonconstructible value
Algorithm: If 1..x-1 are constructible, a coin ≤x extends the range; otherwise x is impossible.
Read the corresponding `pg_185_exercise_...md` file for the extracted
book's problem, worked explanations and variants. OCR is unverified.

Run: python -m epi_python.chapter_13_sorting.pg_185_smallest_nonconstructible_value
Test: python -m pytest tests/chapter_13_sorting/test_pg_185_smallest_nonconstructible_value.py -v
"""

def smallest_nonconstructible_value(coins: list[int]) -> int:
    """Smallest positive amount not formable from a subset of positive coins."""

    # sorted() returns a sorted copy, preserving the original list.
    # Documentation: https://docs.python.org/3/library/functions.html#sorted
    ordered=sorted(coins)
    smallest_missing=1
    for coin in ordered:
        if coin > smallest_missing:
            break
        smallest_missing += coin
    return smallest_missing


if __name__ == "__main__":
    # Demonstrations check representative input/output behavior.
    observed = smallest_nonconstructible_value([])
    print("smallest_nonconstructible_value:", observed)
    assert observed == 1
    observed = smallest_nonconstructible_value([1, 1, 3, 4])
    print("smallest_nonconstructible_value:", observed)
    assert observed == 10
    observed = smallest_nonconstructible_value([1, 2, 2])
    print("smallest_nonconstructible_value:", observed)
    assert observed == 6
    observed = smallest_nonconstructible_value([2, 3])
    print("smallest_nonconstructible_value:", observed)
    assert observed == 1
