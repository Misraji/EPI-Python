"""EPI Python — Exercise 6.8: The Look-and-Say Problem

Chapter 6: Strings
Textbook: pages 75–76 (printed page numbers; problem, solution and the
first program begin on 75; the end of the first program, the Pythonic
program and the complexity are on 76).

PROBLEM (from the textbook)
---------------------------
The look-and-say sequence starts with 1. Subsequent numbers are derived by
describing the previous number in terms of consecutive digits.
Specifically, to generate an entry of the sequence from the previous entry,
read off the digits of the previous entry, counting the number of digits in
groups of the same digit. For example, 1; one 1; two 1s; one 2 then one 1;
one 1, then one 2, then two 1s; three 1s, then two 2s, then one 1. The
first eight numbers in the look-and-say sequence are
<1, 11, 21, 1211, 111221, 312211, 13112221, 1113213211>.

Write a program that takes as input an integer n and returns the nth
integer in the look-and-say sequence. Return the result as a string.

HINT (from the textbook)
------------------------
You need to return the result as a string.

SOLUTION DEVELOPMENT (following the textbook)
---------------------------------------------
Compute the nth number by applying the "describe the previous number" rule
n - 1 times, starting from "1".

Because the rule is about counting digits, strings are the natural
representation for the terms. Going from the ith number to the (i + 1)th
means scanning the digits from most significant to least significant,
counting each run of consecutive equal digits, and writing out the count
followed by the digit.

The book gives two programs:
* look_and_say(n), with a nested next_number(s) helper that counts runs
  with explicit indices; this file's look_and_say implements the same
  method with the helper inlined.
* look_and_say_pythonic(n), a "Pythonic solution" using
  itertools.groupby(); this file's look_and_say_pythonic.

ADDITIONAL EXAMPLES (added for learning; not printed in this exercise)
---------------------------------------------------------------------
The __main__ block checks terms 1 to 6 ('1', '11', '21', '1211',
'111221', '312211'), which are the first six terms listed in the book's
problem statement.
"""

# Python standard library: functions creating iterators for efficient looping.
# Module documentation: https://docs.python.org/3/library/itertools.html
# groupby API: https://docs.python.org/3/library/itertools.html#itertools.groupby
import itertools


# `n: int` and `-> str` are type hints: they document the expected argument
# and return types. Python does not check or enforce them at run time;
# tools such as mypy can.
# Annotations: https://docs.python.org/3/glossary.html#term-annotation
def look_and_say(n: int) -> str:
    """Return the nth look-and-say sequence term, beginning with '1'.

    This is the textbook's first (explicit run-counting) implementation,
    with the next_number helper written inline.
    """
    term = '1'

    # range(1, n) runs n - 1 times (the rule is applied n - 1 times). The
    # name `_` is a convention for a loop variable whose value is unused.
    # For n <= 1 the loop does not run and '1' is returned.
    for _ in range(1,n):
        chunks = []
        i = 0
        while i < len(term):

            # Advance j past the run of digits equal to term[i]; the run
            # is term[i:j], of length j - i.
            j = i + 1
            while j < len(term) and term[j] == term[i]:
                j += 1

            # str(j - i) converts the run length to its decimal text, and
            # `+` concatenates it with the digit: a run "111" gives "31".
            # str: https://docs.python.org/3/library/stdtypes.html#str
            chunks.append(str(j - i) + term[i])
            i = j

        # Collect the pieces in a list and join once: str.join is the
        # efficient way to build a string because strings are immutable.
        # str.join: https://docs.python.org/3/library/stdtypes.html#str.join
        term = ''.join(chunks)
    return term


def look_and_say_pythonic(n: int) -> str:
    """Textbook's second program, look_and_say_pythonic (itertools.groupby).

    Pythonic solution uses the power of itertools.groupby() (book comment).
    """
    term = '1'

    # range(n - 1) also runs n - 1 times.
    for _ in range(n-1):

        # itertools.groupby(iterable) yields (key, group) pairs, one per
        # run of CONSECUTIVE equal items: groupby('1121') gives runs keyed
        # '1' (two items), '2' (one), '1' (one). It does not collect every
        # occurrence of a digit across the string — exactly what
        # look-and-say needs.
        # groupby: https://docs.python.org/3/library/itertools.html#itertools.groupby
        #
        # Each `group` is a lazy iterator over the run, with no len();
        # list(group) consumes it into a list so len() gives the run
        # length. The group must be used before groupby advances to the
        # next run, which the generator expression does.
        #
        # The argument to ''.join is a generator expression: it produces
        # "count + digit" strings one at a time for join to concatenate.
        # Generator expressions: https://docs.python.org/3/reference/expressions.html#generator-expressions
        term = ''.join(str(len(list(group)))+key
                       for key, group in itertools.groupby(term))
    return term


# TEXTBOOK POST-SOLUTION DISCUSSION (page 76)
# -------------------------------------------
# The exact time complexity depends on the lengths of the terms, which are
# extremely hard to analyze. A bound: each number can have at most twice
# as many digits as the one before (this happens when all its digits
# differ), so the longest term has length at most 2^n. There are n
# iterations, and each does work proportional to the length of the number
# it computes, so a simple bound on the time complexity is O(n 2^n).
#
# VARIANTS
# --------
# The book lists no variants for this exercise.


# TEXTBOOK CODE COMPARISON
# ------------------------
# look_and_say (file) vs look_and_say (book):
#   book: `def look_and_say(n)` with a nested `def next_number(s)` that
#   uses `result, i = [], 0`, a `count` variable, an inner loop
#   `while i + 1 < len(s) and s[i] == s[i + 1]` that advances i and
#   count, `result.append(str(count) + s[i])`, `i += 1`, and returns
#   `''.join(result)`; the outer code is `s = '1'`,
#   `for _ in range(1, n): s = next_number(s)`, `return s`.
#   file: `look_and_say(n: int) -> str` (type hints added); no nested
#   helper — the run-counting is written inline in the loop; the run is
#   measured with a second index `j` (length `j - i`) instead of a
#   `count` variable; names `term` and `chunks` instead of `s` and
#   `result`. Same algorithm and results.
# look_and_say_pythonic: book `def look_and_say_pythonic(n)` with variable
#   `s`; file adds type hints and names the variable `term`. Otherwise
#   the same expression.


# Python executes this block only when this source file is run directly.
# When pytest imports the file, this block is skipped automatically.
# Documentation: https://docs.python.org/3/library/__main__.html
if __name__ == "__main__":

    # The first four terms from the book's list. The comprehensive test
    # suite remains in the separate tests/ folder.
    observed = look_and_say(1)

    # print() with several arguments writes them separated by a space.
    print("look_and_say:", observed)

    # `assert` stops the program with an AssertionError if the condition
    # is false. These are quick smoke checks; pytest provides the more
    # thorough automated verification.
    assert observed == '1'
    observed = look_and_say(2)
    print("look_and_say:", observed)
    assert observed == '11'
    observed = look_and_say(3)
    print("look_and_say:", observed)
    assert observed == '21'
    observed = look_and_say(4)
    print("look_and_say:", observed)
    assert observed == '1211'

    # Both textbook programs must agree on terms 1 through 6
    # (range(1, 7) yields 1, 2, ..., 6).
    for n in range(1,7):
        result = look_and_say_pythonic(n)
        print("PDF groupby look-and-say", n, result)
        assert result == look_and_say(n)
