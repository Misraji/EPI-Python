"""EPI 16.2: Compute the Levenshtein distance (printed page 239).

ORIGIN: Educational reconstruction based on the supplied EPI exercise.
NOT a verified line-for-line transcription of the textbook's Python snippet.

Question: Compute the Levenshtein distance
Method: Dynamic programming over string prefixes; memory reduced to one previous row. Time O(mn), space O(n).

For the PDF text layer of the original problem, solution exposition, variants,
and complexity discussion, read the companion Markdown document:
    pg_239_exercise_16_02_compute_the_levenshtein_distance.md

Run independently:
    python -m epi_python.chapter_16_dynamic_programming.pg_239_levenshtein_distance
Run thorough tests:
    python -m pytest tests/chapter_16_dynamic_programming/test_pg_239_levenshtein_distance.py -v
"""

def levenshtein_distance(first: str, second: str) -> int:
    """Minimum insertions, deletions, or substitutions to transform a string."""
    previous = list(range(len(second) + 1))
    for row, left_character in enumerate(first, start=1):
        current = [row] + [0] * len(second)
        for column, right_character in enumerate(second, start=1):
            substitution = 0 if left_character == right_character else 1
            current[column] = min(
                previous[column] + 1,
                current[column - 1] + 1,
                previous[column - 1] + substitution,
            )
        previous = current
    return previous[-1]


if __name__ == "__main__":
    # Run a few self-contained examples before exploring the pytest suite.
    observed = levenshtein_distance('', '')
    print("levenshtein_distance:", observed)
    assert observed == 0
    observed = levenshtein_distance('cat', 'cat')
    print("levenshtein_distance:", observed)
    assert observed == 0
    observed = levenshtein_distance('cat', 'cut')
    print("levenshtein_distance:", observed)
    assert observed == 1
    observed = levenshtein_distance('kitten', 'sitting')
    print("levenshtein_distance:", observed)
    assert observed == 3
    observed = levenshtein_distance('a', '')
    print("levenshtein_distance:", observed)
    assert observed == 1
