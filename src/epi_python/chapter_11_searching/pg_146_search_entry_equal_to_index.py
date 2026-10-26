"""EPI 11.2: Search a sorted array for entry equal to its index — printed page 146.

Educational reconstruction; not a verified verbatim textbook transcription.
Question: Search a sorted array for entry equal to its index
Algorithm: Binary search on a[i]-i, monotonic for strictly increasing sorted integers.
Read the corresponding `pg_146_exercise_...md` file for the extracted
book's problem, worked explanations and variants. OCR is unverified.

Run: python -m epi_python.chapter_11_searching.pg_146_search_entry_equal_to_index
Test: python -m pytest tests/chapter_11_searching/test_pg_146_search_entry_equal_to_index.py -v
"""

def search_entry_equal_to_index(sorted_distinct: list[int]) -> int:
    """Find any index i with a[i] == i, or return -1."""
    left,right = 0,len(sorted_distinct)-1
    while left <= right:
        middle=(left+right)//2
        if sorted_distinct[middle] == middle:
            return middle
        if sorted_distinct[middle] > middle:
            right = middle-1
        else:
            left = middle+1
    return -1


if __name__ == "__main__":
    # Demonstrations check representative input/output behavior.
    observed = search_entry_equal_to_index([-2, 0, 2, 5])
    print("search_entry_equal_to_index:", observed)
    assert observed == 2
    observed = search_entry_equal_to_index([1, 2, 3])
    print("search_entry_equal_to_index:", observed)
    assert observed == -1
    observed = search_entry_equal_to_index([])
    print("search_entry_equal_to_index:", observed)
    assert observed == -1
    observed = search_entry_equal_to_index([0])
    print("search_entry_equal_to_index:", observed)
    assert observed == 0
