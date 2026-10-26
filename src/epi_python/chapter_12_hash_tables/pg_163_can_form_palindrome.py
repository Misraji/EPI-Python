"""EPI Python — Exercise 12.1: Test for Palindromic Permutations

Chapter 12: Hash Tables
Textbook: pages 163–164 (printed page numbers; problem, solution and
program on 163, complexity on 164).

PROBLEM (from the textbook)
---------------------------
"A palindrome is a string that reads the same forwards and backwards,
e.g., "level", "rotator", and "foobaraboof".

Write a program to test whether the letters forming a string can be
permuted to form a palindrome. For example, "edified" can be permuted to
form "deified"."

HINT (from the textbook)
------------------------
"Find a simple characterization of strings that can be permuted to form a
palindrome."

SOLUTION DEVELOPMENT (following the textbook)
---------------------------------------------
Brute force: generate every permutation of the string and test each one
for being a palindrome. The time complexity is very high.

A first refinement: if a candidate palindrome starts with, say, 'a', it
must also end with 'a', so only permutations ending in 'a' need to be
considered. That prunes the permutation search.

The more powerful conclusion: for a string to be rearrangeable into a
palindrome, its characters must occur in pairs, with one exception when the
length is odd (the middle character). Book's example: "edified" has odd
length 7 and contains two 'e's, two 'd's, two 'i's and one 'f' -- enough to
guarantee a palindromic permutation.

Stated precisely:
  * even length: necessary and sufficient that every character appears an
    even number of times;
  * odd length: all but one character must appear an even number of times.
Both cases are covered by the single test "at most one character has an odd
count", which a hash table from characters to frequencies can check.

The implementation below, can_form_palindrome, follows this test.

ADDITIONAL EXAMPLES (added for learning; not printed in this exercise)
---------------------------------------------------------------------
    'edified' -> True  (the book's example)
    'aab'     -> True  ('aba')
    'abc'     -> False (three characters with odd counts)
    ''        -> True  (the empty string is a palindrome)
    'a'       -> True
"""

# Python standard library: specialized container types.
# Module documentation: https://docs.python.org/3/library/collections.html
# Counter API: https://docs.python.org/3/library/collections.html#collections.Counter
import collections


def can_form_palindrome(text: str) -> bool:
    """Whether some permutation of text can form a palindrome.

    This is the textbook's can_form_palindrome (the only implementation
    given), with the Counter stored in a separate variable.

    Type hints: `text: str` and `-> bool` document the expected argument and
    return types; Python does not enforce them.
    """

    # collections.Counter(iterable) builds a dictionary-like object mapping
    # each distinct item to how many times it occurs. Iterating over a
    # string yields its characters, so Counter('aab') behaves like
    # {'a': 2, 'b': 1}. This is the hash table of character frequencies the
    # book describes. Characters are counted literally (case, spaces and
    # punctuation all count).
    counts = collections.Counter(text)

    # Book's comment: a string can be permuted to form a palindrome if and
    # only if the number of chars whose frequency is odd is at most 1.
    #
    # counts.values() gives the frequencies. `count % 2` is 1 for an odd
    # count and 0 for an even one, so the generator expression
    # `(count % 2 for count in ...)` yields a 1 per odd-count character, and
    # sum() adds them up to the number of odd counts. (For an empty string
    # there are no values and sum() returns 0.)
    # sum: https://docs.python.org/3/library/functions.html#sum
    # dict.values: https://docs.python.org/3/library/stdtypes.html#dict.values
    return sum(count % 2 for count in counts.values()) <= 1


# TEXTBOOK POST-SOLUTION DISCUSSION (page 164)
# --------------------------------------------
# Time complexity O(n), where n is the length of the string. Space
# complexity O(c), where c is the number of distinct characters appearing in
# the string (the size of the Counter).
#
# VARIANTS
# --------
# The book gives no variants for this exercise.


# TEXTBOOK CODE COMPARISON
# ------------------------
# Book: `def can_form_palindrome(s):` with a one-line
#   `return sum(v % 2 for v in collections.Counter(s).values()) <= 1`.
# File: parameter renamed `text: str`, return hint `-> bool` added; the
#   Counter is split out into a separate variable `counts`; the generator
#   variable is named `count` instead of `v`. Same algorithm.


# Python executes this block only when this source file is run directly.
# When pytest imports the file, this block is skipped automatically.
# Documentation: https://docs.python.org/3/library/__main__.html
if __name__ == "__main__":
    # Run a few self-contained examples before exploring the pytest suite:
    # the book's 'edified', a short rearrangeable word, a word that cannot
    # be rearranged, the empty string, and a single character.
    #
    # `assert` stops the program with an AssertionError if a result is
    # different from the expected value. These are quick smoke checks;
    # pytest provides the more thorough automated verification.
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
