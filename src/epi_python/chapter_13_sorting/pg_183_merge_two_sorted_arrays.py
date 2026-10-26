"""EPI 13.2, printed page 183: Merge two sorted arrays.

Problem: Merge two sorted arrays. See pg_183_exercise_13_02_merge_two_sorted_arrays.md for the full
original problem, hint, development, and variants from the PDF text layer.

Approach and complexity: O(m+n) time, O(1) auxiliary memory; fill the target from right to left.

EDUCATIONAL RECONSTRUCTION: source and comments are not claimed verbatim.
Run directly: python -m epi_python.chapter_13_sorting.pg_183_merge_two_sorted_arrays
Test: python -m pytest tests/chapter_13_sorting/test_pg_183_merge_two_sorted_arrays.py -v
"""

# TEXTBOOK PROBLEM (exercise 13.2, printed page 183):
# Merge two sorted arrays into the first array, which has sufficient empty slots at the end.
# HINT: Avoid repeatedly moving entries.

def merge_two_sorted_arrays(A: list[int | None], m: int,
                            B: list[int], n: int) -> None:
    """Merge the first m elements of A and first n elements of B into A.

    The four-argument signature is retained from the textbook's printed
    listing on page 184. A must have at least m + n slots.
    """
    if m < 0 or n < 0 or m + n > len(A) or n > len(B):
        raise ValueError("Invalid element counts or insufficient target capacity")
    a, b, write_idx = m - 1, n - 1, m + n - 1
    while a >= 0 and b >= 0:
        if A[a] > B[b]:
            A[write_idx] = A[a]
            a -= 1
        else:
            A[write_idx] = B[b]
            b -= 1
        write_idx -= 1
    while b >= 0:
        A[write_idx] = B[b]
        write_idx, b = write_idx - 1, b - 1


if __name__ == "__main__":
    values = [5, 13, 17, None, None, None, None]
    merge_two_sorted_arrays(values, 3, [3, 7, 11, 19], 4)
    print("Merged:", values)
    assert values == [3, 5, 7, 11, 13, 17, 19]
