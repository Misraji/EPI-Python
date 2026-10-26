"""EPI Python — Exercise 6.9: Convert from Roman to Decimal

Chapter 6: Strings
Textbook: pages 76–77 (printed page numbers; problem and solution start on
76; the program, complexity and variants are on 77).

PROBLEM (from the textbook)
---------------------------
The Roman numeral representation of positive integers uses the symbols
I, V, X, L, C, D, M. Each symbol represents a value, with I being 1, V
being 5, X being 10, L being 50, C being 100, D being 500, and M being
1000.

In this problem we give simplified rules for representing numbers in this
system. Specifically, define a string over the Roman number symbols to be a
valid Roman number string if symbols appear in nonincreasing order, with
the following exceptions allowed:
    * I can immediately precede V and X.
    * X can immediately precede L and C.
    * C can immediately precede D and M.
Back-to-back exceptions are not allowed, e.g., IXC is invalid, as is CDM.

A valid complex Roman number string represents the integer which is the
sum of the symbols that do not correspond to exceptions; for the
exceptions, add the difference of the larger symbol and the smaller
symbol.

For example, the strings "XXXXXIIIIIIIII", "LVIIII" and "LIX" are valid
Roman number strings representing 59. The shortest valid complex Roman
number string corresponding to the integer 59 is "LIX".

Write a program which takes as input a valid Roman number string s and
returns the integer it corresponds to.

HINT (from the textbook)
------------------------
Start by solving the problem assuming no exception cases.

SOLUTION DEVELOPMENT (following the textbook)
---------------------------------------------
Brute force: scan s from left to right, adding each symbol's value, except
when the following symbol has a higher value. In that case the pair is one
of the six exception cases, and the pair's value (larger minus smaller) is
added instead.

Slightly easier to code: scan from the right. If the symbol after the
current one is greater than it, subtract the current symbol; otherwise add
it. The book's program performs this right-to-left iteration.

The book points out that the program does not check that a smaller symbol
to the left of a larger one forms one of the six allowed exceptions, so on
invalid input it can give an answer anyway — e.g. it returns 99 for "IC".

In this file:
* roman_to_integer_right_to_left follows the book's right-to-left
  program (written with a loop instead of functools.reduce).
* roman_to_integer is an extra left-to-right helper (not printed in the
  book) that uses the same "subtract when a larger symbol follows" rule.

ADDITIONAL EXAMPLES (added for learning; not printed in this exercise)
---------------------------------------------------------------------
    roman_to_integer('IV')      -> 4
    roman_to_integer('XIV')     -> 14
    roman_to_integer('MCMXCIV') -> 1994  (1000 + 900 + 90 + 4)
(The book's "LIX" -> 59 is checked in the __main__ block as well.)
"""


# `roman: str` and `-> int` are type hints: they document the expected
# argument and return types. Python does not check or enforce them at run
# time; tools such as mypy can.
# Annotations: https://docs.python.org/3/glossary.html#term-annotation
def roman_to_integer(roman: str) -> int:
    """Convert a valid Roman numeral to an integer.

    Left-to-right helper added in this file (not printed in the book).
    Like the book's program, it does not validate the numeral.
    """
    # A dict literal mapping each symbol to its value; values[symbol]
    # looks a value up in O(1) average time and raises KeyError for an
    # unknown symbol.
    values = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    result = 0

    # enumerate(iterable) yields (index, item) pairs: (0, 'M'), (1, 'C'),
    # ... The pair is unpacked into `index` and `symbol`, giving both the
    # position (to look at the next symbol) and the character.
    # Docs: https://docs.python.org/3/library/functions.html#enumerate
    for index, symbol in enumerate(roman):
        value = values[symbol]

        # If a strictly larger symbol follows, this symbol is the smaller
        # half of an exception (e.g. the I in IX) and is subtracted. The
        # bound check comes first so roman[index + 1] is never read past
        # the end (`and` stops at the first false operand).
        if index + 1 < len(roman) and value < values[roman[index + 1]]:
            result -= value
        else:
            result += value
    return result


def roman_to_integer_right_to_left(roman: str) -> int:
    """Textbook's roman_to_integer: right-to-left scan.

    Same computation as the book's functools.reduce program, written as an
    explicit loop, plus a guard that returns 0 for an empty string.
    """
    values={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}

    # An empty string is falsy. Without this guard, roman[-1] below would
    # raise IndexError.
    if not roman:
        return 0

    # A negative index counts from the end: roman[-1] is the last symbol,
    # which is always added (nothing follows it).
    result=values[roman[-1]]

    # range(start, stop, step) with step -1 counts down: from
    # len(roman) - 2 (the second-to-last position) to 0 inclusive (the
    # stop value -1 is excluded).
    # range: https://docs.python.org/3/library/stdtypes.html#range
    for i in range(len(roman)-2,-1,-1):
        current=values[roman[i]]

        # Conditional expression `A if condition else B`: add -current
        # (i.e. subtract) when the symbol to the right is larger,
        # otherwise add current.
        # Docs: https://docs.python.org/3/reference/expressions.html#conditional-expressions
        result += -current if current<values[roman[i+1]] else current
    return result


# TEXTBOOK POST-SOLUTION DISCUSSION (page 77)
# -------------------------------------------
# Each character of s is processed in O(1) time, so the overall time
# complexity is O(n), where n is the length of s.
#
# VARIANTS
# --------
# Variant 1: Write a program that takes as input a string of Roman number
#            symbols and checks whether that string is valid.
#            (stated in the book; no solution given)
# Variant 2: Write a program that takes as input a positive integer n and
#            returns a shortest valid simple Roman number string
#            representing n.
#            (stated in the book; no solution given)


# TEXTBOOK CODE COMPARISON
# ------------------------
# roman_to_integer_right_to_left (file) vs roman_to_integer (book):
#   book: `def roman_to_integer(s)` with the table named `T`, returning
#   `functools.reduce(lambda val, i: val + (-T[s[i]] if T[s[i]] <
#   T[s[i + 1]] else T[s[i]]), reversed(range(len(s) - 1)), T[s[-1]])`
#   (reduce over indices len(s)-2 down to 0, starting from the last
#   symbol's value). The book imports functools for this.
#   file: renamed `roman_to_integer_right_to_left(roman: str) -> int`
#   (type hints added); table named `values`; the reduce call is
#   replaced by an explicit `for i in range(len(roman)-2,-1,-1)` loop
#   with `result +=` a conditional expression; adds an `if not roman:
#   return 0` guard (the book's code raises IndexError on ''). The file
#   does not import functools. Same results for non-empty input.
# roman_to_integer (file): a left-to-right helper using enumerate, not
#   printed in the book. Note the file's name `roman_to_integer` refers
#   to this helper, not to the book's right-to-left program of that name.


# Python executes this block only when this source file is run directly.
# When pytest imports the file, this block is skipped automatically.
# Documentation: https://docs.python.org/3/library/__main__.html
if __name__ == "__main__":

    # Added examples: a single symbol, two subtractive pairs, a mixed
    # case, and a longer numeral. The comprehensive test suite remains in
    # the separate tests/ folder.
    observed = roman_to_integer('I')

    # print() with several arguments writes them separated by a space.
    print("roman_to_integer:", observed)

    # `assert` stops the program with an AssertionError if the condition
    # is false. These are quick smoke checks; pytest provides the more
    # thorough automated verification.
    assert observed == 1
    observed = roman_to_integer('IV')
    print("roman_to_integer:", observed)
    assert observed == 4
    observed = roman_to_integer('IX')
    print("roman_to_integer:", observed)
    assert observed == 9
    observed = roman_to_integer('XIV')
    print("roman_to_integer:", observed)
    assert observed == 14
    observed = roman_to_integer('MCMXCIV')
    print("roman_to_integer:", observed)
    assert observed == 1994

    # The textbook's right-to-left version must agree, including on the
    # book's "LIX" (59) example.
    for numeral in ("IV", "LIX", "MCMXCIV"):
        assert roman_to_integer_right_to_left(numeral) == roman_to_integer(numeral)
