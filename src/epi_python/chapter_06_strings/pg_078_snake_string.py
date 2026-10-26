"""EPI Python — Exercise 6.11: Write a String Sinusoidally

Chapter 6: Strings
Textbook: pages 78–79 (printed page numbers; problem, solution and both
programs on 78; the complexity sentence is at the top of 79).

PROBLEM (from the textbook)
---------------------------
We illustrate what it means to write a string in sinusoidal fashion by
means of an example. The string "Hello_World!" written in sinusoidal
fashion is

        e       _       l
    H   l   o   W   r   d
          l       o       !

(Here _ denotes a blank.)

[The diagram above is redrawn in plain text: in the book the characters
form a three-row wave, the top row holding e, _, l, the middle row H, l,
o, W, r, d and the bottom row l, o, !, each character in its own column.]

Define the snakestring of s to be the left-right top-to-bottom sequence in
which characters appear when s is written in sinusoidal fashion. For
example, the snakestring string for "Hello_World!" is "e_lHloWrdlo!".

Write a program which takes as input a string s and returns the
snakestring of s.

HINT (from the textbook)
------------------------
Try concrete examples, and look for periodicity.

SOLUTION DEVELOPMENT (following the textbook)
---------------------------------------------
Brute force: fill a 3 x n two-dimensional array of characters, initially
all null; write the string into it in the sinusoidal pattern; then read out
the non-null characters row by row (row-major order).

Observation: the answer always starts with s[1], s[5], s[9], ... (the top
row), followed by s[0], s[2], s[4], ... (the middle row), and then s[3],
s[7], s[11], ... (the bottom row). So the snakestring can be produced
directly with three passes over s, without the 2D array.

The book prints two programs:
* snake_string(s): three loops, one per row; this file's
  snake_string_three_pass.
* snake_string_pythonic(s): "Python solution uses slicing with right
  steps"; this file's snake_string.

ADDITIONAL EXAMPLES (added for learning; not printed in this exercise)
---------------------------------------------------------------------
    snake_string('')     -> ''
    snake_string('abc')  -> 'bac'   (top 'b', middle 'a','c', bottom none)
The __main__ block also uses the book's "Hello World!" example.
"""


# `text: str` and `-> str` are type hints: they document the expected
# argument and return types. Python does not check or enforce them at run
# time; tools such as mypy can.
# Annotations: https://docs.python.org/3/glossary.html#term-annotation
def snake_string(text: str) -> str:
    """Read 3-row sinusoidally placed characters row by row.

    This is the textbook's snake_string_pythonic (slicing with steps).
    """
    # Extended slicing text[start::step] takes every step-th character
    # beginning at index start, up to the end of the string; it yields ''
    # when start is past the end (no IndexError).
    #   text[1::4] -> positions 1, 5, 9, ...  (top row)
    #   text[0::2] -> positions 0, 2, 4, ...  (middle row)
    #   text[3::4] -> positions 3, 7, 11, ... (bottom row)
    # `+` concatenates the three new strings in row order.
    # Slicing: https://docs.python.org/3/library/stdtypes.html#common-sequence-operations
    return text[1::4] + text[0::2] + text[3::4]


def snake_string_three_pass(text: str) -> str:
    """Textbook's snake_string: three range-based loops, one per row."""
    result=[]

    # range(start, stop, step) yields start, start+step, ... below stop.
    # Outputs the first row, i.e., s[1], s[5], s[9], ... (book comment).
    # range: https://docs.python.org/3/library/stdtypes.html#range
    for i in range(1,len(text),4):
        result.append(text[i])

    # Outputs the second row, i.e., s[0], s[2], s[4], ... (book comment).
    for i in range(0,len(text),2):
        result.append(text[i])

    # Outputs the third row, i.e., s[3], s[7], s[11], ... (book comment).
    for i in range(3,len(text),4):
        result.append(text[i])

    # str.join concatenates the collected characters with no delimiter;
    # collecting into a list and joining once avoids building many
    # intermediate immutable strings.
    # Documentation: https://docs.python.org/3/library/stdtypes.html#str.join
    return ''.join(result)


# TEXTBOOK POST-SOLUTION DISCUSSION (page 79)
# -------------------------------------------
# Let n be the length of s. Each of the three iterations takes O(n) time,
# so the time complexity is O(n).
#
# VARIANTS
# --------
# The book lists no variants for this exercise.


# TEXTBOOK CODE COMPARISON
# ------------------------
# snake_string_three_pass (file) vs snake_string (book):
#   book: `def snake_string(s)` with `result = []` and three loops
#   `for i in range(1, len(s), 4)`, `range(0, len(s), 2)`,
#   `range(3, len(s), 4)` appending `s[i]`, then `return ''.join(result)`.
#   file: renamed `snake_string_three_pass(text: str) -> str` (type hints
#   added), parameter `text`. Otherwise the same.
# snake_string (file) vs snake_string_pythonic (book):
#   book: `def snake_string_pythonic(s)` returning
#   `s[1::4] + s[::2] + s[3::4]`.
#   file: named `snake_string(text: str) -> str` (type hints added); the
#   middle slice is written `text[0::2]` instead of `s[::2]` (identical
#   meaning). Note that the file's name `snake_string` refers to the
#   book's Pythonic version, while the book's `snake_string` is the
#   three-loop version.


# Python executes this block only when this source file is run directly.
# When pytest imports the file, this block is skipped automatically.
# Documentation: https://docs.python.org/3/library/__main__.html
if __name__ == "__main__":

    # The book's example "Hello World!", whose snakestring is
    # "e lHloWrdlo!". The comprehensive test suite remains in the
    # separate tests/ folder.
    sample = "Hello World!"

    # print() with several arguments writes them separated by a space.
    print("snake string:", snake_string(sample))

    # `assert` stops the program with an AssertionError if the condition
    # is false. sorted(string) returns a list of its characters in sorted
    # order, so comparing sorted lists checks that the snakestring is a
    # rearrangement of the input (same characters, same counts).
    # sorted: https://docs.python.org/3/library/functions.html#sorted
    assert sorted(snake_string(sample)) == sorted(sample)

    # Both textbook programs must agree, including on the empty string
    # and strings whose length is not a multiple of 4.
    for candidate in ("Hello World!", "", "abc", "abcdefghijkl"):
        assert snake_string_three_pass(candidate) == snake_string(candidate)
