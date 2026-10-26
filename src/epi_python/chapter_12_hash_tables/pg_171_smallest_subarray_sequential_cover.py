"""EPI exercise 12.7, printed page 171: Find smallest subarray sequentially covering all values.

EDUCATIONAL RECONSTRUCTION — not a verbatim verified code transcription.
Problem: Find smallest subarray sequentially covering all values.
Method/complexity: Single scan with last positions and shortest prefix matches; O(n) time, O(query_size) memory.
For the book's original explanation and variants, see:
    pg_171_exercise_12_07_find_smallest_subarray_sequentially_covering_all_values.md

Run: python -m epi_python.chapter_12_hash_tables.pg_171_smallest_subarray_sequential_cover
Test: python -m pytest tests/chapter_12_hash_tables/test_pg_171_smallest_subarray_sequential_cover.py -v
"""

def find_smallest_sequentially_covering_subset(values: list[str], query: list[str]) -> tuple[int, int] | None:
    """Find shortest subarray containing query words in order, with gaps allowed."""
    if not query:
        return (0, -1)
    if len(set(query)) != len(query):
        raise ValueError("This educational version expects distinct query words")
    query_index = {word: i for i, word in enumerate(query)}
    latest = [-1] * len(query)
    shortest = [float('inf')] * len(query)
    result = None
    for i, word in enumerate(values):
        j = query_index.get(word)
        if j is None:
            continue
        if j == 0:
            shortest[j] = 1
        elif shortest[j - 1] != float('inf'):
            shortest[j] = shortest[j - 1] + i - latest[j - 1]
        latest[j] = i
        if j == len(query) - 1 and shortest[j] != float('inf'):
            start = i - int(shortest[j]) + 1
            if result is None or i - start < result[1] - result[0]:
                result = (start, i)
    return result


if __name__ == "__main__":
    words=["a","b","x","c","a","b","c"]
    print("ordered cover:", find_smallest_sequentially_covering_subset(words,["a","b","c"]))
    assert find_smallest_sequentially_covering_subset(words,["a","b","c"]) == (4,6)
