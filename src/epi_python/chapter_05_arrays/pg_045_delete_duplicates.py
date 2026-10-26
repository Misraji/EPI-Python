"""EPI 5.5: Delete duplicates from a sorted array (printed page 45).

ORIGIN: Educational reconstruction based on the supplied EPI exercise.
NOT a verified line-for-line transcription of the textbook's Python snippet.

Question: Delete duplicates from a sorted array
Method: Two indices compact adjacent duplicates without extra array allocation. Return the new logical length.

For the PDF text layer of the original problem, solution exposition, variants,
and complexity discussion, read the companion Markdown document:
    pg_045_exercise_05_05_delete_duplicates_from_a_sorted_array.md

Run independently:
    python -m epi_python.chapter_05_arrays.pg_045_delete_duplicates
Run thorough tests:
    python -m pytest tests/chapter_05_arrays/test_pg_045_delete_duplicates.py -v
"""

def delete_duplicates(sorted_array: list[int]) -> int:
    """Compact unique values in place; return length of meaningful prefix."""
    if not sorted_array:
        return 0
    write = 1
    for read in range(1, len(sorted_array)):
        if sorted_array[read] != sorted_array[write - 1]:
            sorted_array[write] = sorted_array[read]
            write += 1
    return write


if __name__ == "__main__":
    # The returned length identifies the meaningful prefix, not a new list.
    values = [1, 1, 2, 2, 3]
    length = delete_duplicates(values)
    print("Unique sorted prefix:", values[:length])
    assert values[:length] == [1, 2, 3]
