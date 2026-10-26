"""EPI Python — Exercise 24.8: Justify Text

Chapter 24: Honors Class
Textbook: pages 360–361 (printed page numbers; problem on 360, solution,
program and analysis on 361).

PROBLEM (from the textbook)
---------------------------
This problem is concerned with justifying text. It abstracts a problem
arising in typesetting. The input is specified as a sequence of words, and
the target line length. After justification, each individual line must
begin with a word, and each subsequent word must be separated from prior
words with at least one blank. If a line contains more than one word, it
should not end in a blank. The sequences of blanks within each line should
be as close to equal in length as possible, with the longer blank
sequences, if any, appearing at the initial part of the line. As an
exception, the very last line should use single blanks as separators, with
additional blanks appearing at its end.

For example, if A = <"The", "quick", "brown", "fox", "jumped", "over",
"the", "lazy", "dogs.">, and the line length L is 11, then the returned
result should be "The   quick", "brown   fox", "jumped over",
"the    lazy", "dogs.      ". (In the book a special symbol denotes each
blank; here blanks are written as spaces.)

Write a program which takes as input an array A of strings and a positive
integer L, and computes the justification of the text specified by A.

HINT (from the textbook)
------------------------
Solve it on a line-by-line basis, assuming a single blank between pairs of
words. Then figure out how to distribute excess blanks.

SOLUTION DEVELOPMENT (following the textbook)
---------------------------------------------
The difficulty is that the problem needs lookahead: the number of blanks
between the words of a line cannot be computed until the complete set of
words on that line is known.

So work line by line:
  1. Decide which words go on the line, assuming a single blank between
     words.
  2. Once the line's words are known, compute how many blanks the line
     needs and distribute them evenly among the gaps (extra blanks going to
     the earlier gaps).
  3. Special-case the final line: single blanks, padded at the end.

The book prints one program, `justify_text(words, L)`, implemented here.

ADDITIONAL EXAMPLES (added for learning; not printed in this exercise)
---------------------------------------------------------------------
    words=['The', 'quick', 'brown', 'fox'], line_length=11
        -> ['The   quick', 'brown fox  ']
    words=[] -> []   (file-only behaviour)
"""


def justify_text(words: list[str],line_length: int) -> list[str]:
    """Textbook implementation: greedy line filling, round-robin blanks.

    Type hints (`list[str]`, `int`, `-> list[str]`) are documentation only;
    Python does not enforce them.
    """

    # Tuple assignment initializes three variables at once:
    # total letters (not blanks) on the current line, the finished lines,
    # and the words of the line being built.
    current_line_length,result,current_line=0,[],[]
    for word in words:

        # Added guard (not in the book): a word longer than a line can never
        # be placed.
        if len(word)>line_length:
            raise ValueError('Word longer than line')

        # len(current_line) is the number of words already on the line,
        # which equals the number of single blanks needed if `word` is added
        # (one after each existing word). If the total would
        # exceed the line length, the current line is complete.
        if current_line_length+len(word)+len(current_line)>line_length:

            # Distribute equally between words in current_line.
            #
            # line_length - current_line_length is the number of blanks to
            # add. Blank number i is appended to word i % (gaps), cycling
            # round-robin from the left, so earlier gaps get the extras.
            # `len(current_line)-1 or 1`: `or` returns its left operand if
            # truthy, else its right one. For a one-word line there are 0
            # gaps, so 1 is used and all blanks go after that single word
            # (also avoiding `% 0`, which raises ZeroDivisionError).
            # `+=` on a list element rebinds that element to a new string
            # (strings are immutable).
            for i in range(line_length-current_line_length):
                current_line[i%(len(current_line)-1 or 1)]+=' '

            # ''.join(list_of_strings) concatenates the strings with the
            # empty separator (blanks were already attached to the words).
            # https://docs.python.org/3/library/stdtypes.html#str.join
            result.append(''.join(current_line))
            current_line,current_line_length=[],0
        current_line.append(word)
        current_line_length+=len(word)

    # Use ljust(L) to pad the last line with the appropriate number of
    # blanks.
    #
    # ' '.join(...) puts single blanks between the last line's words.
    # str.ljust(width) returns the string left-justified in a field of that
    # width, padded on the right with spaces (unchanged if already as long).
    # https://docs.python.org/3/library/stdtypes.html#str.ljust
    #
    # Conditional expression: `X if cond else Y` binds more loosely than
    # `+`, so this is (result + [last_line]) if words else []. The `else []`
    # is a file addition so that no input produces no lines.
    return result+[' '.join(current_line).ljust(line_length)] if words else []


# TEXTBOOK POST-SOLUTION DISCUSSION (page 361)
# --------------------------------------------
# Let n be the sum of the lengths of the strings in A. O(1) time is spent per
# character in the first pass (choosing words) as well as the second pass
# (building the padded line), so the time complexity is O(n).
#
# VARIANTS
# The book gives no variants for this exercise.


# TEXTBOOK CODE COMPARISON
# ------------------------
# book: `def justify_text(words, L)`; variables `curr_line_length`,
#   `curr_line`; no length check; final statement
#   `return result + [' '.join(curr_line).ljust(L)]` (so an empty `words`
#   gives one all-blank line of length L).
# file: parameters `words: list[str], line_length: int` with `-> list[str]`;
#   variables renamed `current_line_length` / `current_line`; added
#   `ValueError` for a word longer than the line; final return gains
#   `if words else []`, so empty input returns []. Same algorithm otherwise.


# Python executes this block only when this source file is run directly.
# When pytest imports the file, this block is skipped automatically.
# Documentation: https://docs.python.org/3/library/__main__.html
if __name__=='__main__':

    # The book's example (first four words, L = 11): the first line gets the
    # two extra blanks between its words; the last line uses single blanks
    # and is padded at the end.
    # `assert` raises AssertionError if the result differs; the tests/
    # folder holds the thorough pytest suite.
    lines=justify_text(['The','quick','brown','fox'],11)
    print('Justified lines:',lines)
    assert lines==['The   quick','brown fox  ']
