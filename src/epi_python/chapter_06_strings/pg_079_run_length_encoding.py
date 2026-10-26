"""EPI Python — Exercise 6.12: Implement Run-Length Encoding

Chapter 6: Strings
Textbook: page 79 (printed page number; problem, solution, both programs
and complexity are all on 79).

PROBLEM (from the textbook)
---------------------------
Run-length encoding (RLE) compression offers a fast way to do efficient
on-the-fly compression and decompression of strings. The idea is
simple—encode successive repeated characters by the repetition count and
the character. For example, the RLE of "aaaabcccaa" is "4a1b3c2a". The
decoding of "3e4f2e" returns "eeeffffee".

Implement run-length encoding and decoding functions. Assume the string to
be encoded consists of letters of the alphabet, with no digits, and the
string to be decoded is a valid encoding.

HINT (from the textbook)
------------------------
This is similar to converting between binary and string representations.

SOLUTION DEVELOPMENT (following the textbook)
---------------------------------------------
Decoding first. Every encoded string is a sequence of blocks, each being a
string of digits followed by one character. The digits are the decimal
representation of a positive integer (the repetition count, which may have
several digits). To decode, convert each digit string into its integer
value and then write the following character that many times; repeat for
every character.

Encoding needs the opposite conversion: turning an integer (the repetition
count) into a string.

The book prints two programs, decoding(s) and encoding(s); this file's
decoding and encoding implement them.

ADDITIONAL EXAMPLES (added for learning; not printed in this exercise)
---------------------------------------------------------------------
    encoding('')    -> ''
    encoding('a')   -> '1a'
    encoding('ab')  -> '1a1b'
(The book's "aaaabcccaa" -> "4a1b3c2a" is also checked in __main__.)
"""


# `text: str` and `-> str` are type hints: they document the expected
# argument and return types. Python does not check or enforce them at run
# time; tools such as mypy can.
# Annotations: https://docs.python.org/3/glossary.html#term-annotation
def encoding(text: str) -> str:
    """Run-length encode a text string as count + symbol segments.

    This is the textbook's encoding function, restructured to measure each
    run with a second index.
    """
    # `parts: list[str] = []` is an annotated assignment: the variable is
    # declared to hold a list of strings. Like all annotations it is not
    # enforced at run time. (`list[str]` needs Python 3.9 or later.)
    # Annotated assignments: https://docs.python.org/3/reference/simple_stmts.html#annotated-assignment-statements
    parts: list[str] = []
    index = 0
    while index < len(text):

        # Advance `end` past the run of characters equal to text[index];
        # the run is text[index:end], of length end - index.
        end = index + 1
        while end < len(text) and text[end] == text[index]:
            end += 1

        # str(n) converts the count to decimal text (it may have several
        # digits, e.g. '12'), followed by the repeated character.
        # str: https://docs.python.org/3/library/stdtypes.html#str
        parts.append(str(end - index) + text[index])
        index = end

    # str.join() assembles a list of strings, with no separator here.
    # Building a list and joining once is efficient because strings are
    # immutable.
    # Documentation: https://docs.python.org/3/library/stdtypes.html#str.join
    return "".join(parts)


def decoding(text: str) -> str:
    """Decode count + symbol segments (assumes symbol is not a digit).

    This is the textbook's decoding function.
    """
    pieces: list[str] = []
    count = 0
    for symbol in text:

        # str.isdigit() returns True if all characters are digits (and the
        # string is non-empty). Note: it also accepts some non-ASCII
        # digit characters, which a valid encoding will not contain.
        # Documentation: https://docs.python.org/3/library/stdtypes.html#str.isdigit
        if symbol.isdigit():

            # Accumulate a multi-digit count left to right ("12" -> 1 ->
            # 12): shift the previous count one decimal place and add the
            # new digit. int(symbol) converts the digit character to its
            # value. This is the string-to-integer method of Exercise 6.1.
            # int: https://docs.python.org/3/library/functions.html#int
            count = count * 10 + int(symbol)
        else:

            # symbol is a letter of the alphabet (book comment).
            # str * int repeats the string: 'e' * 3 == 'eee'. This
            # appends count copies of the letter to the result (book
            # comment), then resets the count for the next block.
            # Sequence repetition: https://docs.python.org/3/library/stdtypes.html#common-sequence-operations
            pieces.append(symbol * count)
            count = 0
    return "".join(pieces)


# TEXTBOOK POST-SOLUTION DISCUSSION (page 79)
# -------------------------------------------
# The time complexity is O(n), where n is the length of the string.
#
# VARIANTS
# --------
# The book lists no variants for this exercise.


# TEXTBOOK CODE COMPARISON
# ------------------------
# decoding:
#   book: `def decoding(s)` with `count, result = 0, []`; loop `for c in s`;
#   `if c.isdigit(): count = count * 10 + int(c)`; else
#   `result.append(c * count)` and `count = 0`; returns
#   `''.join(result)`.
#   file: `decoding(text: str) -> str` (type hints added); the list is
#   named `pieces` and declared with the annotation `list[str]`; loop
#   variable `symbol`. Same algorithm.
# encoding:
#   book: `def encoding(s)` with `result, count = [], 1`; a single loop
#   `for i in range(1, len(s) + 1)`: when `i == len(s) or s[i] != s[i - 1]`
#   (book comment: "Found new character so write the count of previous
#   character.") it appends `str(count) + s[i - 1]` and resets count to 1;
#   otherwise (`s[i] == s[i - 1]`) it increments count.
#   file: `encoding(text: str) -> str` (type hints added); restructured as
#   a `while` loop over run starts (`index`) with an inner loop advancing
#   `end` to the end of the run, appending `str(end - index) +
#   text[index]`; no `count` variable; list named `parts` with a
#   `list[str]` annotation. Same results (including '' for empty input).


# Python executes this block only when this source file is run directly.
# When pytest imports the file, this block is skipped automatically.
# Documentation: https://docs.python.org/3/library/__main__.html
if __name__ == "__main__":

    # Added examples (empty string, one letter, two different letters)
    # plus the book's "aaaabcccaa" example. The comprehensive test suite
    # remains in the separate tests/ folder.
    observed = encoding('')

    # print() with several arguments writes them separated by a space.
    print("encoding:", observed)

    # `assert` stops the program with an AssertionError if the condition
    # is false. These are quick smoke checks; pytest provides the more
    # thorough automated verification.
    assert observed == ''
    observed = encoding('a')
    print("encoding:", observed)
    assert observed == '1a'
    observed = encoding('aaaabcccaa')
    print("encoding:", observed)
    assert observed == '4a1b3c2a'
    observed = encoding('ab')
    print("encoding:", observed)
    assert observed == '1a1b'
