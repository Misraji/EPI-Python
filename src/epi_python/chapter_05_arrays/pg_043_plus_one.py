"""EPI 5.2: Increment an arbitrary-precision integer (printed page 43).

ORIGIN: Educational reconstruction based on the supplied EPI exercise.
NOT a verified line-for-line transcription of the textbook's Python snippet.

Question: Increment an arbitrary-precision integer
Method: Propagate carry right-to-left; create a new leading digit if necessary. Time O(n), O(n) output space.

For the PDF text layer of the original problem, solution exposition, variants,
and complexity discussion, read the companion Markdown document:
    pg_043_exercise_05_02_increment_an_arbitrary_precision_integer.md

Run independently:
    python -m epi_python.chapter_05_arrays.pg_043_plus_one
Run thorough tests:
    python -m pytest tests/chapter_05_arrays/test_pg_043_plus_one.py -v
"""

def plus_one(digits: list[int]) -> list[int]:
    """Increment an unsigned decimal number represented as digit entries."""
    if not digits:
        return [1]
    result = digits.copy()
    result[-1] += 1
    for i in range(len(result) - 1, 0, -1):
        if result[i] < 10:
            break
        result[i] = 0
        result[i - 1] += 1
    if result[0] == 10:
        result[0] = 0
        result.insert(0, 1)
    return result


if __name__ == "__main__":
    # Run a few self-contained examples before exploring the pytest suite.
    observed = plus_one([1, 2, 9])
    print("plus_one:", observed)
    assert observed == [1, 3, 0]
    observed = plus_one([9, 9])
    print("plus_one:", observed)
    assert observed == [1, 0, 0]
    observed = plus_one([0])
    print("plus_one:", observed)
    assert observed == [1]
    observed = plus_one([2, 3])
    print("plus_one:", observed)
    assert observed == [2, 4]
    observed = plus_one([])
    print("plus_one:", observed)
    assert observed == [1]
