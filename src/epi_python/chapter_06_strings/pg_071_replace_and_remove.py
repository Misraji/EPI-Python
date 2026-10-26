"""EPI exercise 6.4, printed page 71: Replace and remove.

EDUCATIONAL RECONSTRUCTION — not a verbatim verified code transcription.
Problem: Replace and remove.
Method/complexity: Forward compaction + backward expansion; O(n) time, O(1) workspace given sufficient input capacity.
For the book's original explanation and variants, see:
    pg_071_exercise_06_04_replace_and_remove.md

Run: python -m epi_python.chapter_06_strings.pg_071_replace_and_remove
Test: python -m pytest tests/chapter_06_strings/test_pg_071_replace_and_remove.py -v
"""

def replace_and_remove(size: int, letters: list[str]) -> list[str]:
    """In-place: erase b and replace each a with two d entries."""
    if not 0 <= size <= len(letters):
        raise ValueError("size outside list")
    write = 0
    count_a = 0
    for read in range(size):
        if letters[read] != 'b':
            letters[write] = letters[read]
            write += 1
        if letters[read] == 'a':
            count_a += 1
    new_size = write + count_a
    if len(letters) < new_size:
        letters.extend([''] * (new_size - len(letters)))
    cursor = write - 1
    final = new_size - 1
    while cursor >= 0:
        if letters[cursor] == 'a':
            letters[final - 1:final + 1] = ['d', 'd']
            final -= 2
        else:
            letters[final] = letters[cursor]
            final -= 1
        cursor -= 1
    return letters[:new_size]


if __name__ == "__main__":
    letters = list("abac") + ["", ""]
    result = replace_and_remove(4, letters)
    print("replace_and_remove:", result)
    assert result == list("ddddc")
