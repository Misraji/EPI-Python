"""EPI 4.9: Check if a decimal integer is a palindrome (printed page 33).

ORIGIN: Educational reconstruction based on the supplied EPI exercise.
NOT a verified line-for-line transcription of the textbook's Python snippet.

Question: Check if a decimal integer is a palindrome
Method: Reverse only half the digits to avoid converting to text. Time O(digits), extra space O(1).

For the PDF text layer of the original problem, solution exposition, variants,
and complexity discussion, read the companion Markdown document:
    pg_033_exercise_04_09_check_if_a_decimal_integer_is_a_palindrome.md

Run independently:
    python -m epi_python.chapter_04_primitive_types.pg_033_is_number_palindromic
Run thorough tests:
    python -m pytest tests/chapter_04_primitive_types/test_pg_033_is_number_palindromic.py -v
"""

def is_number_palindromic(x: int) -> bool:
    """Check an integer palindrome without converting it to a string."""
    if x < 0:
        return False
    if x == 0:
        return True
    if x % 10 == 0:
        return False
    remaining = x
    reversed_digits = 0
    while remaining > reversed_digits:
        reversed_digits = reversed_digits * 10 + remaining % 10
        remaining //= 10
    return remaining == reversed_digits or remaining == reversed_digits // 10


if __name__ == "__main__":
    # Run a few self-contained examples before exploring the pytest suite.
    observed = is_number_palindromic(0)
    print("is_number_palindromic:", observed)
    assert observed == True
    observed = is_number_palindromic(7)
    print("is_number_palindromic:", observed)
    assert observed == True
    observed = is_number_palindromic(121)
    print("is_number_palindromic:", observed)
    assert observed == True
    observed = is_number_palindromic(1221)
    print("is_number_palindromic:", observed)
    assert observed == True
    observed = is_number_palindromic(123)
    print("is_number_palindromic:", observed)
    assert observed == False
