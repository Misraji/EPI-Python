"""EPI 11.3: Search a cyclically sorted array — printed page 147.

Educational reconstruction; not a verified verbatim textbook transcription.
Question: Search a cyclically sorted array
Algorithm: Search for the rotation boundary by comparing midpoint with the rightmost item.
Read the corresponding `pg_147_exercise_...md` file for the extracted
book's problem, worked explanations and variants. OCR is unverified.

Run: python -m epi_python.chapter_11_searching.pg_147_search_smallest
Test: python -m pytest tests/chapter_11_searching/test_pg_147_search_smallest.py -v
"""

def search_smallest(cyclic_sorted: list[int]) -> int:
    """Return index of the smallest entry in a rotated distinct sorted array."""
    if not cyclic_sorted:
        return -1
    left,right = 0,len(cyclic_sorted)-1
    while left < right:
        middle=(left+right)//2
        if cyclic_sorted[middle] > cyclic_sorted[right]:
            left = middle+1
        else:
            right = middle
    return left


if __name__ == "__main__":
    # Demonstrations check representative input/output behavior.
    observed = search_smallest([])
    print("search_smallest:", observed)
    assert observed == -1
    observed = search_smallest([4, 5, 1, 2, 3])
    print("search_smallest:", observed)
    assert observed == 2
    observed = search_smallest([1, 2, 3])
    print("search_smallest:", observed)
    assert observed == 0
    observed = search_smallest([2, 1])
    print("search_smallest:", observed)
    assert observed == 1
