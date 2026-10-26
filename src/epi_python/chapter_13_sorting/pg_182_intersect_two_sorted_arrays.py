"""EPI 13.1: Compute the intersection of two sorted arrays (printed page 182).

ORIGIN: Educational reconstruction based on the supplied EPI exercise.
NOT a verified line-for-line transcription of the textbook's Python snippet.

Question: Compute the intersection of two sorted arrays
Method: Walk the two sorted arrays with monotonic indices and skip duplicate matches. O(n+m) time.

For the PDF text layer of the original problem, solution exposition, variants,
and complexity discussion, read the companion Markdown document:
    pg_182_exercise_13_01_compute_the_intersection_of_two_sorted_arrays.md

Run independently:
    python -m epi_python.chapter_13_sorting.pg_182_intersect_two_sorted_arrays
Run thorough tests:
    python -m pytest tests/chapter_13_sorting/test_pg_182_intersect_two_sorted_arrays.py -v
"""

def intersect_two_sorted_arrays(a: list[int], b: list[int]) -> list[int]:
    """Sorted intersection with each shared value appearing once."""
    result: list[int] = []
    i = j = 0
    while i < len(a) and j < len(b):
        if a[i] == b[j]:
            if not result or result[-1] != a[i]:
                result.append(a[i])
            i += 1
            j += 1
        elif a[i] < b[j]:
            i += 1
        else:
            j += 1
    return result


if __name__ == "__main__":
    # Run a few self-contained examples before exploring the pytest suite.
    observed = intersect_two_sorted_arrays([], [])
    print("intersect_two_sorted_arrays:", observed)
    assert observed == []
    observed = intersect_two_sorted_arrays([1, 2, 2, 3], [2, 2, 3, 4])
    print("intersect_two_sorted_arrays:", observed)
    assert observed == [2, 3]
    observed = intersect_two_sorted_arrays([1, 3], [2, 4])
    print("intersect_two_sorted_arrays:", observed)
    assert observed == []
    observed = intersect_two_sorted_arrays([1, 1], [1])
    print("intersect_two_sorted_arrays:", observed)
    assert observed == [1]
