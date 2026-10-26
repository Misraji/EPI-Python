"""EPI exercise 6.11, printed page 78: Write a string sinusoidally.

EDUCATIONAL RECONSTRUCTION — not a verbatim verified code transcription.
Problem: Write a string sinusoidally.
Method/complexity: Three Python slices; O(n) time and O(n) output memory.
For the book's original explanation and variants, see:
    pg_078_exercise_06_11_write_a_string_sinusoidally.md

Run: python -m epi_python.chapter_06_strings.pg_078_snake_string
Test: python -m pytest tests/chapter_06_strings/test_pg_078_snake_string.py -v
"""

def snake_string(text: str) -> str:
    """Read 3-row sinusoidally placed characters row by row."""
    # Top row holds positions 1,5,9,...; middle row 0,2,4,...;
    # bottom row positions 3,7,11,... of the original string.
    return text[1::4] + text[0::2] + text[3::4]


if __name__ == "__main__":
    sample = "Hello World!"
    print("snake string:", snake_string(sample))
    assert sorted(snake_string(sample)) == sorted(sample)
