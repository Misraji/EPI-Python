"""EPI Python — Exercise 6.3: Compute the Spreadsheet Column Encoding

Chapter 6: Strings
Textbook: pages 70–71 (printed page numbers; problem, solution and program
on 70, variants at the top of 71).

PROBLEM (from the textbook)
---------------------------
Spreadsheets often use an alphabetical encoding of the successive columns.
Specifically, columns are identified by "A", "B", "C", ..., "X", "Y", "Z",
"AA", "AB", ..., "ZZ", "AAA", "AAB", ....

Implement a function that converts a spreadsheet column id to the
corresponding integer, with "A" corresponding to 1. For example, you should
return 4 for "D", 27 for "AA", 702 for "ZZ", etc. How would you test your
code?

HINT (from the textbook)
------------------------
There are 26 characters in ["A", "Z"], and each can be mapped to an integer.

SOLUTION DEVELOPMENT (following the textbook)
---------------------------------------------
Brute force: enumerate the column ids in order ("A", "B", ...), stopping
when the current id equals the input. Computing the successor of ids such
as "Z" or "AZ" takes some care, but the bigger problem is time: reaching
"ZZZZZZ" takes 26^6 steps, and in general the time is O(26^n) for a string
of length n.

Better: take bigger jumps. The problem is essentially converting a string
that represents a base-26 number into an integer, except that "A" stands
for 1 rather than 0. So the string-to-integer method of Solution 6.1
(page 68) applies: scan left to right, multiply the running result by 26
and add the value of the next letter.

Worked example from the book: for "ZZ", start with result 0; add 26 (for
the first 'Z'); multiply by 26; add 26 again. The id is 26^2 + 26 = 702.

Testing (the book's answer to "How would you test your code?"): good test
cases are the boundaries, e.g. "A", "B", "Y", "Z", "AA", "AB", "ZY", "ZZ",
plus some random strings such as "M", "BZ", "CCC".

The book prints one program, ss_decode_col_id(col), using
functools.reduce. In this file:
* ss_decode_col_id_reduce is the book's reduce-based program.
* ss_decode_col_id is an extra explicit-loop version (not printed in the
  book) of the same computation.

ADDITIONAL EXAMPLES (added for learning; not printed in this exercise)
---------------------------------------------------------------------
    ss_decode_col_id('A')  -> 1
    ss_decode_col_id('Z')  -> 26
    ss_decode_col_id('AB') -> 28   (1 x 26 + 2)
(The book's own examples "D" -> 4, "AA" -> 27, "ZZ" -> 702 also hold.)
"""

# Python standard library: higher-order functions and operations on callables.
# Module documentation: https://docs.python.org/3/library/functools.html
# reduce API: https://docs.python.org/3/library/functools.html#functools.reduce
import functools


# `column: str` and `-> int` are type hints: they document the expected
# argument and return types. Python does not check or enforce them at run
# time; external tools such as mypy can.
# Annotations: https://docs.python.org/3/glossary.html#term-annotation
def ss_decode_col_id(column: str) -> int:
    """Spreadsheet column label to 1-indexed column number.

    Explicit-loop helper added in this file (not printed in the book); it
    performs the same computation as the textbook's reduce version.
    Expects upper-case letters 'A'..'Z'.
    """
    result = 0
    for character in column:

        # ord(c) returns the integer code point of a one-character string.
        # 'A'..'Z' have consecutive code points, so
        # ord(character) - ord('A') + 1 maps 'A' -> 1, ..., 'Z' -> 26
        # (the "+ 1" is what makes 'A' mean 1 rather than 0).
        # Multiplying the previous result by 26 shifts it one base-26
        # place left before the new letter is added.
        # ord: https://docs.python.org/3/library/functions.html#ord
        result = result * 26 + ord(character) - ord('A') + 1
    return result


def ss_decode_col_id_reduce(col: str) -> int:
    """Textbook's ss_decode_col_id: reduce letters into a base-26 integer."""

    # functools.reduce(function, iterable, initial) starts with `initial`
    # (0) and calls function(running_value, next_item) for each letter of
    # col, returning the final running value. For "ZZ":
    # f(0, 'Z') = 26, then f(26, 'Z') = 26*26 + 26 = 702.
    # reduce: https://docs.python.org/3/library/functools.html#functools.reduce
    #
    # `lambda result, c: ...` defines a small anonymous two-argument
    # function whose body is a single expression: multiply the running
    # result by 26 and add the letter's value (ord(c) - ord('A') + 1, so
    # 'A' -> 1). The initial value 0 also makes an empty string give 0.
    # lambda: https://docs.python.org/3/reference/expressions.html#lambda
    # ord: https://docs.python.org/3/library/functions.html#ord
    return functools.reduce(lambda result, c: result*26 + ord(c)-ord('A')+1, col, 0)


# TEXTBOOK POST-SOLUTION DISCUSSION (pages 70–71)
# -----------------------------------------------
# The time complexity is O(n), where n is the length of the column id
# (one constant-time multiply-and-add per letter).
#
# VARIANTS
# --------
# Variant 1: Solve the same problem with "A" corresponding to 0.
#            (stated in the book; no solution given)
# Variant 2: Implement a function that converts an integer to the
#            spreadsheet column id. For example, return "D" for 4, "AA"
#            for 27, and "ZZ" for 702.
#            (stated in the book; no solution given)


# TEXTBOOK CODE COMPARISON
# ------------------------
# ss_decode_col_id_reduce (file) vs ss_decode_col_id (book):
#   book: `def ss_decode_col_id(col)` returning
#   `functools.reduce(lambda result, c: result * 26 + ord(c) - ord('A') + 1,
#   col, 0)`.
#   file: renamed `ss_decode_col_id_reduce(col: str) -> int` (type hints
#   added); the body is the same expression (only spacing differs).
# ss_decode_col_id (file): an extra explicit-loop version not printed in
#   the book, with parameter `column: str`. Note that the file's name
#   `ss_decode_col_id` refers to this helper, not to the book's reduce
#   program of that name.


# Python executes this block only when this source file is run directly.
# When pytest imports the file, this block is skipped automatically.
# Documentation: https://docs.python.org/3/library/__main__.html
if __name__ == "__main__":

    # Boundary examples from the book's testing advice ("A", "Z", "AA",
    # "AB"). The comprehensive test suite remains in the separate tests/
    # folder.
    observed = ss_decode_col_id('A')

    # print() with several arguments writes them separated by a space.
    print("ss_decode_col_id:", observed)

    # `assert` stops the program with an AssertionError if the condition
    # is false. These are quick smoke checks; pytest provides the more
    # thorough automated verification.
    assert observed == 1
    observed = ss_decode_col_id('Z')
    print("ss_decode_col_id:", observed)
    assert observed == 26
    observed = ss_decode_col_id('AA')
    print("ss_decode_col_id:", observed)
    assert observed == 27
    observed = ss_decode_col_id('AB')
    print("ss_decode_col_id:", observed)
    assert observed == 28

    # The book's reduce program must agree with the loop version
    # (including the book's "ZZ" -> 702 example).
    for label in ("A", "AA", "ZZ"):
        assert ss_decode_col_id_reduce(label) == ss_decode_col_id(label)
        print("reduce spreadsheet column:", label, ss_decode_col_id_reduce(label))
