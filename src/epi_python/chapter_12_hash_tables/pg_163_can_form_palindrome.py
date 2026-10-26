"""EPI 12.1: Test for palindromic permutations (printed page 163).

ORIGIN: Educational reconstruction based on the supplied EPI exercise.
NOT a verified line-for-line transcription of the textbook's Python snippet.

Question: Test for palindromic permutations
Method: At most one character may have an odd frequency; others form mirrored pairs. Time O(n).

For the PDF text layer of the original problem, solution exposition, variants,
and complexity discussion, read the companion Markdown document:
    pg_163_exercise_12_01_test_for_palindromic_permutations.md

Run independently:
    python -m epi_python.chapter_12_hash_tables.pg_163_can_form_palindrome
Run thorough tests:
    python -m pytest tests/chapter_12_hash_tables/test_pg_163_can_form_palindrome.py -v
"""

# Counter is a dictionary subclass for counting hashable values.
# Documentation: https://docs.python.org/3/library/collections.html#collections.Counter
import collections


def can_form_palindrome(text: str) -> bool:
    """Whether some permutation of text can form a palindrome."""

    # Counter(text) computes occurrences of each distinct character.
    counts = collections.Counter(text)

    # sum() totals boolean conditions; in Python True behaves as integer 1.
    # Documentation: https://docs.python.org/3/library/functions.html#sum
    return sum(count % 2 for count in counts.values()) <= 1


if __name__ == "__main__":
    # Run a few self-contained examples before exploring the pytest suite.
    observed = can_form_palindrome('edified')
    print("can_form_palindrome:", observed)
    assert observed == True
    observed = can_form_palindrome('aab')
    print("can_form_palindrome:", observed)
    assert observed == True
    observed = can_form_palindrome('abc')
    print("can_form_palindrome:", observed)
    assert observed == False
    observed = can_form_palindrome('')
    print("can_form_palindrome:", observed)
    assert observed == True
    observed = can_form_palindrome('a')
    print("can_form_palindrome:", observed)
    assert observed == True
