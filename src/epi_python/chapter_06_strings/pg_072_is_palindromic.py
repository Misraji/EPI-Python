"""EPI 6.5: Test palindromicity (printed page 72).

ORIGIN: Educational reconstruction based on the supplied EPI exercise.
NOT a verified line-for-line transcription of the textbook's Python snippet.

Question: Test palindromicity
Method: Two inward-facing indices skip nonalphanumeric characters and compare case-insensitively. O(n) time, O(1) space.

For the PDF text layer of the original problem, solution exposition, variants,
and complexity discussion, read the companion Markdown document:
    pg_072_exercise_06_05_test_palindromicity.md

Run independently:
    python -m epi_python.chapter_06_strings.pg_072_is_palindromic
Run thorough tests:
    python -m pytest tests/chapter_06_strings/test_pg_072_is_palindromic.py -v
"""

def is_palindromic(text: str) -> bool:
    """Ignore punctuation/case when determining palindrome status."""
    left, right = 0, len(text) - 1
    while left < right:
        # str.isalnum() tests whether a character is a letter or digit.
        # Documentation: https://docs.python.org/3/library/stdtypes.html#str.isalnum
        while left < right and not text[left].isalnum():
            left += 1
        while left < right and not text[right].isalnum():
            right -= 1

        # str.lower() produces a lowercase version for comparison.
        # Documentation: https://docs.python.org/3/library/stdtypes.html#str.lower
        if text[left].lower() != text[right].lower():
            return False
        left += 1
        right -= 1
    return True


if __name__ == "__main__":
    # Run a few self-contained examples before exploring the pytest suite.
    observed = is_palindromic('A man, a plan, a canal, Panama')
    print("is_palindromic:", observed)
    assert observed == True
    observed = is_palindromic('Able was I, ere I saw Elba!')
    print("is_palindromic:", observed)
    assert observed == True
    observed = is_palindromic('abc')
    print("is_palindromic:", observed)
    assert observed == False
    observed = is_palindromic('')
    print("is_palindromic:", observed)
    assert observed == True
    observed = is_palindromic('12321')
    print("is_palindromic:", observed)
    assert observed == True
