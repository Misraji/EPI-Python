"""EPI Python — Exercise 12.2: Is an Anonymous Letter Constructible?

Chapter 12: Hash Tables
Textbook: pages 164–165 (printed page numbers; solution starts on 164).

PROBLEM (from the textbook)
---------------------------
Write a program which takes text for an anonymous letter and text for a
magazine and determines if it is possible to write the anonymous letter
using the magazine. The anonymous letter can be written using the magazine
if for each character in the anonymous letter, the number of times it
appears in the anonymous letter is no more than the number of times it
appears in the magazine.

HINT (from the textbook)
------------------------
Count the number of distinct characters appearing in the letter.

SOLUTION DEVELOPMENT (following the textbook)
---------------------------------------------
A brute-force approach counts, for *every* character in the character set,
how many times it occurs in the letter and the magazine. This may scan
characters that occur in neither string, and may repeatedly scan the inputs.

A better solution counts only the characters required by the letter:

1. Build a hash table recording the number of copies of each character
   needed to construct the letter.
2. Scan the magazine one character at a time. When a character is needed,
   decrement its count in the hash table.
3. Remove a character once all its required copies have been found.
4. If the hash table becomes empty, the letter can be constructed. If
   magazine characters run out first, the remaining requirements cannot
   be satisfied.

The textbook also supplies a shorter, Pythonic solution using the
subtraction behavior of collections.Counter. Both original algorithms
appear below as separate functions and are tested independently.

ADDITIONAL EXAMPLES (added for learning; not printed in this exercise)
---------------------------------------------------------------------
    letter='aab', magazine='baa'    -> True
    letter='aab', magazine='ab'     -> False (only one 'a')
    letter='',    magazine='abc'    -> True  (nothing is required)
    letter='A',   magazine='a'      -> False (case matters)

Characters are treated literally: spaces, punctuation, and case count.
"""

# Python standard library: specialized container types.
# Module documentation: https://docs.python.org/3/library/collections.html
# Counter API: https://docs.python.org/3/library/collections.html#collections.Counter
import collections


def is_letter_constructible_from_magazine(letter_text, magazine_text):
    """Test constructibility by consuming the letter's character counts.

    This is the textbook's first, explicit hash-table implementation.
    The input strings are not modified.
    """

    # collections is a Python standard-library module containing several
    # specialized container types, including Counter.
    #
    # collections.Counter(iterable) constructs a dictionary-like object:
    # each distinct item is a key, and its value is the item's frequency.
    # For example, Counter('aab') behaves like {'a': 2, 'b': 1}.
    # We use it to represent the letters we still need to find.
    char_frequency_for_letter = collections.Counter(letter_text)

    # Scan each available magazine character exactly once. The `in`
    # operation asks whether this character still has an outstanding
    # requirement in our Counter (a dictionary-like container).
    for c in magazine_text:
        if c in char_frequency_for_letter:
            char_frequency_for_letter[c] -= 1
            if char_frequency_for_letter[c] == 0:

                # `del mapping[key]` removes a key from a mapping.
                # Unlike assigning the value 0, deleting the key ensures
                # that an empty Counter really means no characters remain.
                del char_frequency_for_letter[c]

                # Empty collections are falsy in Python. Therefore,
                # `not char_frequency_for_letter` is True precisely when
                # no characters remain to be matched.
                if not char_frequency_for_letter:
                    return True

    # If magazine_text ends first, all required characters were present
    # exactly when the remaining-frequency mapping is empty.
    return not char_frequency_for_letter


def is_letter_constructible_from_magazine_pythonic(letter_text, magazine_text):
    """Test constructibility using Counter subtraction (textbook version)."""

    # Counter subtraction differs from ordinary arithmetic on dictionary
    # values: `Counter('aab') - Counter('ab')` keeps only {'a': 1}.
    # Entries with zero or negative results are omitted entirely.
    #
    # Here the first Counter counts characters needed by the letter;
    # the second counts characters supplied by the magazine. If their
    # difference is empty, every needed character was supplied.
    #
    # `not` converts that empty/nonempty Counter result to True/False.
    # Parentheses make explicit the precedence that the textbook relies on.
    return not (
        collections.Counter(letter_text) - collections.Counter(magazine_text)
    )


# TEXTBOOK POST-SOLUTION DISCUSSION (pages 164–165)
# -------------------------------------------------
# In the worst case, the letter cannot be constructed, or the last magazine
# character is needed. The explicit algorithm scans both strings once.
#
# Time: O(m + n), where m is the length of the letter and n the magazine.
# Extra space for the explicit version: O(L), where L is the number of
# distinct characters in the letter.
#
# The Counter-subtraction solution also builds a Counter for the magazine,
# so its additional storage depends on the distinct magazine characters.
#
# The textbook notes an alternative for ASCII input: instead of a hash
# table, use a fixed array of 256 integer counts, indexed by character.


# Python executes this block only when this source file is run directly.
# When pytest imports the file, this block is skipped automatically.
# Documentation: https://docs.python.org/3/library/__main__.html
if __name__ == "__main__":

    # Each example is (letter, magazine, expected_result).
    # These small, hand-selected examples show ordinary inputs, too few
    # copies of a letter, empty input, and case-sensitive characters.
    # The comprehensive test suite remains in the separate tests/ folder.
    examples = (
        ("aab", "baa", True),
        ("aab", "ab", False),
        ("", "abc", True),
        ("A", "a", False),
        ("a b", "b a", True),
    )

    for letter, magazine, expected in examples:

        # Call both versions so you can see that they produce the same
        # answer on each example. `!r` prints quotes around strings,
        # making spaces and empty strings easier to recognize.
        explicit_result = is_letter_constructible_from_magazine(letter, magazine)
        pythonic_result = is_letter_constructible_from_magazine_pythonic(
            letter, magazine
        )
        print(
            f"letter={letter!r}, magazine={magazine!r}, "
            f"explicit={explicit_result}, pythonic={pythonic_result}"
        )

        # `assert` stops the program with an AssertionError if a result is
        # different from the expected value. These are quick smoke checks;
        # pytest provides the more thorough automated verification.
        assert explicit_result is expected
        assert pythonic_result is expected

    print("All five standalone examples passed.")
