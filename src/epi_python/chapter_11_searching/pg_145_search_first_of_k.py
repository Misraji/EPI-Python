"""EPI 11.1: Search a sorted array for first occurrence of k (printed page 145).

ORIGIN: Educational reconstruction based on the supplied EPI exercise.
NOT a verified line-for-line transcription of the textbook's Python snippet.

Question: Search a sorted array for first occurrence of k
Method: A lower-bound binary search remembers equality but keeps searching to the left. Time O(log n), space O(1).

For the PDF text layer of the original problem, solution exposition, variants,
and complexity discussion, read the companion Markdown document:
    pg_145_exercise_11_01_search_a_sorted_array_for_first_occurrence_of_k.md

Run independently:
    python -m epi_python.chapter_11_searching.pg_145_search_first_of_k
Run thorough tests:
    python -m pytest tests/chapter_11_searching/test_pg_145_search_first_of_k.py -v
"""

def search_first_of_k(sorted_array: list[int], key: int) -> int:
    """Return index of first key occurrence, or -1."""
    left, right = 0, len(sorted_array) - 1
    result = -1
    while left <= right:
        middle = (left + right) // 2
        if sorted_array[middle] >= key:
            if sorted_array[middle] == key:
                result = middle
            right = middle - 1
        else:
            left = middle + 1
    return result


if __name__ == "__main__":
    # Run a few self-contained examples before exploring the pytest suite.
    observed = search_first_of_k([], 5)
    print("search_first_of_k:", observed)
    assert observed == -1
    observed = search_first_of_k([1, 2, 2, 2, 3], 2)
    print("search_first_of_k:", observed)
    assert observed == 1
    observed = search_first_of_k([1, 2, 3], 1)
    print("search_first_of_k:", observed)
    assert observed == 0
    observed = search_first_of_k([1, 2, 3], 9)
    print("search_first_of_k:", observed)
    assert observed == -1
    observed = search_first_of_k([3, 3, 3], 3)
    print("search_first_of_k:", observed)
    assert observed == 0
