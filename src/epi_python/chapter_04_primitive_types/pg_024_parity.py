"""EPI 4.1: Computing the parity of a word (printed page 24).

ORIGIN: Educational reconstruction based on the supplied EPI exercise.
NOT a verified line-for-line transcription of the textbook's Python snippet.

Question: Computing the parity of a word
Method: Repeatedly discard the low bit and toggle a parity accumulator. Time O(number of bits), extra space O(1).

For the PDF text layer of the original problem, solution exposition, variants,
and complexity discussion, read the companion Markdown document:
    pg_024_exercise_04_01_computing_the_parity_of_a_word.md

Run independently:
    python -m epi_python.chapter_04_primitive_types.pg_024_parity
Run thorough tests:
    python -m pytest tests/chapter_04_primitive_types/test_pg_024_parity.py -v
"""

def parity(x: int) -> int:
    """Return 1 for an odd number of set bits, otherwise 0."""
    result = 0
    while x:
        result ^= x & 1
        x >>= 1
    return result


if __name__ == "__main__":
    # Run a few self-contained examples before exploring the pytest suite.
    observed = parity(0)
    print("parity:", observed)
    assert observed == 0
    observed = parity(1)
    print("parity:", observed)
    assert observed == 1
    observed = parity(3)
    print("parity:", observed)
    assert observed == 0
    observed = parity(7)
    print("parity:", observed)
    assert observed == 1
    observed = parity(10)
    print("parity:", observed)
    assert observed == 0
