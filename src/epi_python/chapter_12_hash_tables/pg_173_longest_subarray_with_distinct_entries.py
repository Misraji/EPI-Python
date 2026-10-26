"""EPI 12.8: Find the longest subarray with distinct entries — printed page 173.

Educational reconstruction; not a verified verbatim textbook transcription.
Question: Find the longest subarray with distinct entries
Algorithm: Sliding window whose left boundary jumps past the prior occurrence of each duplicate.
Read the corresponding `pg_173_exercise_...md` file for the extracted
book's problem, worked explanations and variants. OCR is unverified.

Run: python -m epi_python.chapter_12_hash_tables.pg_173_longest_subarray_with_distinct_entries
Test: python -m pytest tests/chapter_12_hash_tables/test_pg_173_longest_subarray_with_distinct_entries.py -v
"""

def longest_subarray_with_distinct_entries(values: list[int]) -> int:
    """Length of the longest contiguous subarray with no repeated values."""
    last_seen={}
    begin=0
    best=0
    for end,value in enumerate(values):
        if value in last_seen:
            begin=max(begin,last_seen[value]+1)
        last_seen[value]=end
        best=max(best,end-begin+1)
    return best


if __name__ == "__main__":
    # Demonstrations check representative input/output behavior.
    observed = longest_subarray_with_distinct_entries([])
    print("longest_subarray_with_distinct_entries:", observed)
    assert observed == 0
    observed = longest_subarray_with_distinct_entries([1, 2, 3])
    print("longest_subarray_with_distinct_entries:", observed)
    assert observed == 3
    observed = longest_subarray_with_distinct_entries([1, 2, 1, 3, 4])
    print("longest_subarray_with_distinct_entries:", observed)
    assert observed == 4
    observed = longest_subarray_with_distinct_entries([1, 1, 1])
    print("longest_subarray_with_distinct_entries:", observed)
    assert observed == 1
