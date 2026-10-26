"""EPI 18.7: Transform one string to another — printed page 284.

Educational reconstruction; not a verified verbatim textbook transcription.
Question: Transform one string to another
Algorithm: Breadth-first search guarantees minimum mutation count when every edge has equal cost.
Read the corresponding `pg_284_exercise_...md` file for the extracted
book's problem, worked explanations and variants. OCR is unverified.

Run: python -m epi_python.chapter_18_graphs.pg_284_transform_string
Test: python -m pytest tests/chapter_18_graphs/test_pg_284_transform_string.py -v
"""

# collections.deque supports efficient queue operations from both ends.
# Documentation: https://docs.python.org/3/library/collections.html#collections.deque
from collections import deque


def transform_string(start: str, target: str, dictionary: set[str]) -> int:
    """Minimum single-character substitutions through supplied dictionary words."""
    if start == target:
        return 0
    if target not in dictionary:
        return -1
    queue=deque([(start,0)])
    visited={start}
    while queue:
        word,distance=queue.popleft()
        for index in range(len(word)):
            for letter in 'abcdefghijklmnopqrstuvwxyz':
                candidate=word[:index]+letter+word[index+1:]
                if candidate == target:
                    return distance+1
                if candidate in dictionary and candidate not in visited:
                    visited.add(candidate)
                    queue.append((candidate,distance+1))
    return -1


if __name__ == "__main__":
    # Demonstrations check representative input/output behavior.
    observed = transform_string('cat', 'dog', {'cat', 'cog', 'cot', 'dog'})
    print("transform_string:", observed)
    assert observed == 3
    observed = transform_string('cat', 'cat', set())
    print("transform_string:", observed)
    assert observed == 0
    observed = transform_string('cat', 'dog', {'dog'})
    print("transform_string:", observed)
    assert observed == -1
