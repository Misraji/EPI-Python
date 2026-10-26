"""EPI Python — Exercise 16.11: The Pretty Printing Problem

Chapter 16: Dynamic Programming
Textbook: pages 254–256 (printed page numbers; problem starts on 254, solution on 255).

PROBLEM (from the textbook)
---------------------------
"Consider the problem of laying out text using a fixed width font. Each
line can hold no more than a fixed number of characters. Words on a line
are to be separated by exactly one blank. Therefore, we may be left with
whitespace at the end of a line (since the next word will not fit in the
remaining space). This whitespace is visually unappealing.

Define the messiness of the end-of-line whitespace as follows. The
messiness of a single line ending with b blank characters is b^2. The total
messiness of a sequence of lines is the sum of the messinesses of all the
lines. A sequence of words can be split across lines in different ways with
different messiness, as illustrated in Figure 16.12 on the next page."

Figure 16.12 lays out the same text ("I have inserted a large number of new
examples from the papers for the Mathematical Tripos during the last twenty
years, which should be useful to Cambridge students.") with line length
L = 36 in two ways: (a) messiness 3^2 + 0^2 + 1^2 + 0^2 + 14^2 = 206;
(b) messiness 6^2 + 5^2 + 2^2 + 1^2 + 4^2 = 82.

"Given text, i.e., a string of words separated by single blanks, decompose
the text into lines such that no word is split across lines and the
messiness of the decomposition is minimized. Each line can hold no more
than a specified number of characters."

HINT (from the textbook)
------------------------
"Focus on the last word and the last line."

SOLUTION DEVELOPMENT (following the textbook)
---------------------------------------------
Greedy (fit as many words as possible on each line) is suboptimal; it does
not spread words evenly, and adding a word can require moving earlier
words. Figure 16.13: for the text "a b c d" and line length 5, greedy puts
"a b c" / "d" (messiness 0^2 + 4^2 = 16) while the optimum is "a b" / "c d"
(messiness 2^2 + 2^2 = 8).

So the optimal placement of the first i words cannot simply be extended
from the optimal placement of the first i - 1 words (removing word i from
an optimum for i words need not leave an optimum for i - 1 words). What IS
true: if, in an optimum placement of the first i words, the last line holds
words j, j+1, ..., i, then the first j - 1 words are placed optimally.

In an optimum placement of the first i words the last line is some group of
words ending at word i, and everything before it is placed optimally. This
gives the recurrence for M(i), the minimum messiness of placing the first i
words:

    M(i) = min over j <= i of f(j, i) + M(j - 1),

where f(j, i) is the messiness of one line holding words j..i.

Figure 16.14 (line length 11) works through "aaa bbb c d ee ff ggggggg"
(the caption prints "aaa bb c d ee ff ggggggg"; the grids show "bbb"):
* (a) optimum for "aaa bbb c d ee": "aaa bbb" / "c d ee";
* (b) optimum for "aaa bbb c d ee ff": "aaa bbb" / "c d ee ff".
* For the full text there are two cases for the last line: "ff ggggggg" or
  "ggggggg" ("ee ff ggggggg" cannot fit on one line). If the last line is
  "ff ggggggg", the words before it must be placed as in (a); if it is
  "ggggggg", the words before it must be placed as in (b). The figure shows
  both layouts — "aaa bbb" / "c d ee ff" / "ggggggg" and "aaa bbb" /
  "c d ee" / "ff ggggggg" — and the one ending with "ggggggg" has the
  lower messiness (4^2 + 2^2 + 4^2 = 36 versus 4^2 + 5^2 + 1^2 = 42), so
  it is optimum. (The book's text and the sub-figure captions (c)/(d)
  assign these two layouts to the letters in opposite orders.)

Computed directly, the recursion is exponential because it revisits the
same subproblems; caching the values of M fixes that. The book's program
minimum_messiness(words, line_length) does this iteratively with a list
min_messiness; this file implements the same program.

ADDITIONAL EXAMPLES (added for learning; not printed in this exercise)
---------------------------------------------------------------------
    words ['a', 'b', 'c', 'd'], line_length 5 -> 8
        (the book's Figure 16.13 example: "a b" / "c d")
"""


def minimum_messiness(words: list[str], line_length: int) -> int:
    """Return the minimum total messiness (sum of squared trailing blanks).

    This is the textbook's DP implementation. Unlike the book, an empty word
    list returns 0, a word longer than a line raises ValueError, and the
    result is converted to int.
    """

    # Type hints such as `list[str]` document intended types only.
    if not words:
        return 0

    # `any(...)` over a generator expression is True if some word is too
    # long. `raise ValueError(...)` stops with an exception describing the
    # bad input (otherwise the answer would stay infinite).
    if any(len(word) > line_length for word in words):
        raise ValueError('A word cannot fit on any line')
    num_remaining_blanks = line_length - len(words[0])

    # min_messiness[i] is the minimum messiness when placing words[0:i + 1].
    # Word 0 alone gives (remaining blanks)**2 (`**` is exponentiation).
    # float('inf') is positive infinity: larger than every number, so the
    # first real candidate always replaces it in min(). `[x] * k` repeats
    # the list item k times.
    min_messiness = [num_remaining_blanks ** 2] + [float('inf')] * (len(words)-1)
    for i in range(1,len(words)):

        # Candidate 1: word i alone on a new last line.
        num_remaining_blanks = line_length - len(words[i])
        min_messiness[i] = min_messiness[i-1] + num_remaining_blanks ** 2

        # Try adding words[i - 1], words[i - 2], ... to the last line.
        # reversed(range(i)) yields i-1, i-2, ..., 0 lazily.
        for j in reversed(range(i)):

            # Each extra word uses its length plus one separating blank.
            num_remaining_blanks -= len(words[j]) + 1

            # Not enough space to add more words.
            if num_remaining_blanks < 0:
                break

            # Messiness of placing words[0:j] optimally (0 if the last line
            # starts at word 0, i.e. there is no earlier line), plus this
            # last line's messiness.
            first_j_messiness = 0 if j == 0 else min_messiness[j-1]
            current_line_messiness = num_remaining_blanks ** 2
            min_messiness[i] = min(min_messiness[i], first_j_messiness + current_line_messiness)

    # All entries are ints here (each was replaced by an int sum), and
    # int(...) guarantees an int result type.
    return int(min_messiness[-1])


# TEXTBOOK POST-SOLUTION DISCUSSION (page 256)
# --------------------------------------------
# Let L be the line length. A line can hold at most L words, so the work for
# each word is O(L). With n words the time is O(nL). The space is O(n) for
# the cache.
#
# VARIANTS (each stated in the book; no solution given)
# ----------------------------------------------------
# 1. Solve the same problem when the messiness is the sum of the
#    messinesses of all but the last line.
# 2. Suppose the messiness of a line ending with b blank characters is
#    defined to be b. Can you solve the messiness minimization problem in
#    O(n) time and O(1) space?


# TEXTBOOK CODE COMPARISON
# ------------------------
# * File adds `if not words: return 0` (book would raise IndexError at
#   `words[0]`) and a ValueError check for words longer than the line (book
#   would return inf). Type hints added.
# * Book `first_j_messiness = 0 if j - 1 < 0 else ...`; file `0 if j == 0
#   else ...` (same meaning for j >= 0).
# * Book returns `min_messiness[-1]`; file returns `int(min_messiness[-1])`.
# * Otherwise the code matches the book's listing; the book's comments are
#   reproduced above.


# Python executes this block only when this source file is run directly.
# When pytest imports the file, this block is skipped automatically.
# Documentation: https://docs.python.org/3/library/__main__.html
if __name__ == '__main__':

    # The book's Figure 16.13 example: "a b c d" with line length 5 has
    # optimum "a b" / "c d", messiness 2**2 + 2**2 = 8 (greedy gives 16).
    # `assert` stops the program with an AssertionError if the condition is
    # false; this is a quick smoke check, the pytest suite is thorough.
    result=minimum_messiness(['a','b','c','d'],5)
    print('Minimum messiness:',result)
    assert result==8
