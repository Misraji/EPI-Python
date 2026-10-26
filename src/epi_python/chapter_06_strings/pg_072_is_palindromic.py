"""EPI Python — Exercise 6.5: Test Palindromicity

Chapter 6: Strings
Textbook: pages 72–73 (printed page numbers; problem and solution start on
72, the program and complexity are on 73).

PROBLEM (from the textbook)
---------------------------
For the purpose of this problem, define a palindromic string to be a string
which when all the nonalphanumeric are removed it reads the same front to
back ignoring case. For example, "A man, a plan, a canal, Panama." and
"Able was I, ere I saw Elba!" are palindromic, but "Ray a Ray" is not.

Implement a function which takes as input a string s and returns true if s
is a palindromic string.

HINT (from the textbook)
------------------------
Use two indices.

SOLUTION DEVELOPMENT (following the textbook)
---------------------------------------------
Naive approach: build a reversed copy of s and compare it with s, skipping
nonalphanumeric characters. This needs extra space proportional to the
length of s.

The reversed copy is unnecessary: traversing s from right to left gives the
same effect as reading its reverse. So use two indices, one moving forward
from the start and one moving backward from the end:

1. Each index skips over nonalphanumeric characters.
2. Compare the two alphanumeric characters case-insensitively.
3. Return false as soon as there is a mismatch.
4. If the indices meet or cross, palindromicity has been verified.

The book prints one program, is_palindrome(s); this file's
is_palindromic(text) implements it.

ADDITIONAL EXAMPLES (added for learning; not printed in this exercise)
---------------------------------------------------------------------
    is_palindromic('abc')    -> False
    is_palindromic('')       -> True   (nothing to compare)
    is_palindromic('12321')  -> True   (digits are alphanumeric)
"""


# `text: str` and `-> bool` are type hints: they document the expected
# argument and return types. Python does not check or enforce them at run
# time; tools such as mypy can.
# Annotations: https://docs.python.org/3/glossary.html#term-annotation
def is_palindromic(text: str) -> bool:
    """Ignore punctuation/case when determining palindrome status.

    This is the textbook's is_palindrome two-index implementation.
    """
    # Tuple assignment sets both indices at once: `left` moves forward
    # from the start, `right` moves backward from the end. For an empty
    # string right is -1, so the loop below never runs and the result is
    # True.
    left, right = 0, len(text) - 1
    while left < right:

        # str.isalnum() returns True if all characters in the string are
        # alphanumeric (letters or digits, including Unicode letters and
        # digits) and the string is non-empty. Here it is called on a
        # single character to decide whether to skip it.
        # The `left < right` test comes first so the skipping stops when
        # the indices meet (e.g. a string of only punctuation). The book
        # writes the two conditions in the opposite order; because i < j
        # always holds inside the loop, both orders stay within bounds.
        # Documentation: https://docs.python.org/3/library/stdtypes.html#str.isalnum
        while left < right and not text[left].isalnum():
            left += 1
        while left < right and not text[right].isalnum():
            right -= 1

        # str.lower() returns a lower-case copy of the string, so 'A' and
        # 'a' compare equal; this gives the case-insensitive comparison
        # the problem requires.
        # Documentation: https://docs.python.org/3/library/stdtypes.html#str.lower
        if text[left].lower() != text[right].lower():
            return False
        left += 1
        right -= 1
    return True


# TEXTBOOK POST-SOLUTION DISCUSSION (page 73)
# -------------------------------------------
# O(1) work is spent per character, so the time complexity is O(n), where
# n is the length of s. (The two indices replace the reversed copy, so no
# extra space proportional to n is used.)
#
# VARIANTS
# --------
# The book lists no variants for this exercise.


# TEXTBOOK CODE COMPARISON
# ------------------------
# book: `def is_palindrome(s)` with indices `i, j`; the inner loops are
#   `while not s[i].isalnum() and i < j:` (condition order: character
#   test first); the indices advance with `i, j = i + 1, j - 1`.
# file: renamed `is_palindromic(text: str) -> bool` (type hints added);
#   indices renamed `left, right`; the inner-loop conditions are written
#   `left < right and not ...` (bound test first); the indices advance
#   with two separate statements. Same algorithm and results.


# Python executes this block only when this source file is run directly.
# When pytest imports the file, this block is skipped automatically.
# Documentation: https://docs.python.org/3/library/__main__.html
if __name__ == "__main__":

    # The first two examples are the book's palindromes (the first without
    # its final period). The rest are added: a non-palindrome, the empty
    # string, and digits. The comprehensive test suite remains in the
    # separate tests/ folder.
    observed = is_palindromic('A man, a plan, a canal, Panama')

    # print() with several arguments writes them separated by a space.
    print("is_palindromic:", observed)

    # `assert` stops the program with an AssertionError if the condition
    # is false. These are quick smoke checks; pytest provides the more
    # thorough automated verification.
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
