"""EPI 12.5: Find the nearest repeated entries in an array — printed page 167.

Educational reconstruction; not a verified verbatim textbook transcription.
Question: Find the nearest repeated entries in an array
Algorithm: Hash table remembers each word’s latest position, giving O(n) time and O(distinct words) space.
Read the corresponding `pg_167_exercise_...md` file for the extracted
book's problem, worked explanations and variants. OCR is unverified.

Run: python -m epi_python.chapter_12_hash_tables.pg_167_find_nearest_repetition
Test: python -m pytest tests/chapter_12_hash_tables/test_pg_167_find_nearest_repetition.py -v
"""

def find_nearest_repetition(words: list[str]) -> int:
    """Return shortest index gap between equal words; -1 if all distinct."""
    last_seen={}
    nearest=float('inf')
    for index,word in enumerate(words):
        if word in last_seen:
            nearest=min(nearest,index-last_seen[word])
        last_seen[word]=index
    return int(nearest) if nearest != float('inf') else -1


if __name__ == "__main__":
    # Demonstrations check representative input/output behavior.
    observed = find_nearest_repetition([])
    print("find_nearest_repetition:", observed)
    assert observed == -1
    observed = find_nearest_repetition(['a', 'b', 'a'])
    print("find_nearest_repetition:", observed)
    assert observed == 2
    observed = find_nearest_repetition(['a', 'a', 'b'])
    print("find_nearest_repetition:", observed)
    assert observed == 1
    observed = find_nearest_repetition(['a', 'b'])
    print("find_nearest_repetition:", observed)
    assert observed == -1
