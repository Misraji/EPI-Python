"""EPI 4.2: Swap bits (printed page 27).

ORIGIN: Educational reconstruction based on the supplied EPI exercise.
NOT a verified line-for-line transcription of the textbook's Python snippet.

Question: Swap bits
Method: Only toggle the positions if the original bits differ. Time O(1) for fixed-width integers.

For the PDF text layer of the original problem, solution exposition, variants,
and complexity discussion, read the companion Markdown document:
    pg_027_exercise_04_02_swap_bits.md

Run independently:
    python -m epi_python.chapter_04_primitive_types.pg_027_swap_bits
Run thorough tests:
    python -m pytest tests/chapter_04_primitive_types/test_pg_027_swap_bits.py -v
"""

def swap_bits(x: int, i: int, j: int) -> int:
    """Exchange two bit positions of the nonnegative integer x."""
    if ((x >> i) & 1) != ((x >> j) & 1):
        x ^= (1 << i) | (1 << j)
    return x


if __name__ == "__main__":
    # Run a few self-contained examples before exploring the pytest suite.
    observed = swap_bits(8, 0, 3)
    print("swap_bits:", observed)
    assert observed == 1
    observed = swap_bits(9, 0, 3)
    print("swap_bits:", observed)
    assert observed == 9
    observed = swap_bits(0, 1, 2)
    print("swap_bits:", observed)
    assert observed == 0
    observed = swap_bits(1, 0, 0)
    print("swap_bits:", observed)
    assert observed == 1
