"""EPI Python — Exercise 6.1: Interconvert Strings and Integers

Chapter 6: Strings
Textbook: pages 68–69 (printed page numbers; problem and solution start on
68, the program is printed on 69).

PROBLEM (from the textbook)
---------------------------
A string is a sequence of characters. A string may encode an integer,
e.g., "123" encodes 123. In this problem, you are to implement methods that
take a string representing an integer and return the corresponding integer,
and vice versa. Your code should handle negative integers. You cannot use
library functions like int in Python.

Implement an integer to string conversion function, and a string to integer
conversison function. For example, if the input to the first function is
the integer 314, it should return the string "314" and if the input to the
second function is the string "314" it should return the integer 314.

(The spelling "conversison" is the book's own.)

HINT (from the textbook)
------------------------
Build the result one digit at a time.

SOLUTION DEVELOPMENT (following the textbook)
---------------------------------------------
Integer to string:

* A single-digit number (0 through 9) is trivial: the answer is the
  one-character string for that digit.
* For a number with several digits, work digit by digit. For a positive
  integer x, the least significant decimal digit is x mod 10, and the
  remaining (higher) digits are x / 10 (integer division).
* This produces the digits from right to left. Starting with 423: first
  digit 3, leaving 42; then 2, leaving 4; then 4, leaving nothing.
* Prepending each new digit to the front of the partial result would be the
  obvious approach, but inserting at the front of a string is expensive
  because every existing character must shift. It is faster to append each
  digit at the end and reverse the whole sequence once at the finish.
* A negative x: remember that it was negative, negate it, and add a '-'
  before the reversal (so the sign ends up in front).
* x == 0: a loop that stops as soon as x becomes 0 would write no digits
  at all, so a 0 must be produced explicitly. (The book's listing uses a
  `while True` loop with the test at the bottom, so it always writes at
  least one digit; this file's int_to_string handles 0 with an early
  return instead — see TEXTBOOK CODE COMPARISON.)

String to integer:

* Recall how positional notation works: a base-10 numeral d2 d1 d0 stands
  for 10^2 x d2 + 10^1 x d1 + d0.
* Brute force: start at the rightmost digit and keep adding 10^i x d_i to a
  running total. Each next power 10^(i+1) is obtained cheaply by
  multiplying the previous power 10^i by 10.
* More elegant: start at the leftmost digit; for each further digit,
  multiply the partial result by 10 and add the digit. Converting "314":
  begin with r = 0; after the first digit r = 3; after the second
  r = 3 x 10 + 1 = 31; after the third r = 31 x 10 + 4 = 314.
* Negative numbers: record the sign and negate the final result.

The book prints two functions: int_to_string(x) (append digits, then
reverse) and string_to_int(s) (a one-expression functools.reduce version of
the left-to-right method). In this file:

* int_to_string implements the book's integer-to-string algorithm.
* string_to_int_reduce is the book's functools.reduce string-to-integer
  program.
* string_to_int is an extra helper (not printed in the book) that performs
  the same left-to-right "multiply by 10 and add" method with an explicit
  loop and ord() arithmetic.

ADDITIONAL EXAMPLES (added for learning; not printed in this exercise)
---------------------------------------------------------------------
    int_to_string(0)       -> '0'
    int_to_string(-125)    -> '-125'
    int_to_string(2001)    -> '2001'   (interior zero digits are kept)
    string_to_int_reduce('-143') -> -143
"""

# Python standard library: higher-order functions and operations on callables.
# Module documentation: https://docs.python.org/3/library/functools.html
# reduce API: https://docs.python.org/3/library/functools.html#functools.reduce
import functools

# Python standard library: common string constants and operations.
# Module documentation: https://docs.python.org/3/library/string.html
# digits constant: https://docs.python.org/3/library/string.html#string.digits
import string


# `x: int` and `-> str` are type hints (annotations). They document that the
# parameter is expected to be an int and that a str is returned. Python
# itself does not check or enforce them at run time; tools such as mypy can.
# Annotations: https://docs.python.org/3/glossary.html#term-annotation
def int_to_string(x: int) -> str:
    """Convert an integer to decimal characters without calling str(x).

    This is the textbook's int_to_string algorithm (append the digits in
    reverse order, then reverse once). The zero and sign handling are
    arranged slightly differently from the printed listing.
    """
    # Zero is handled up front: the `while x:` loop below stops as soon as
    # x is 0, so for an input of 0 it would never produce any digit.
    if x == 0:
        return '0'
    negative = x < 0

    # abs(x) is a built-in that returns the absolute value. Working with a
    # non-negative number makes `%` and `//` produce ordinary decimal
    # digits (for negative x, Python's `%` result takes the sign of the
    # divisor, so -7 % 10 == 3, which would give wrong digits here).
    # Docs: https://docs.python.org/3/library/functions.html#abs
    x = abs(x)
    digits = []

    # `while x:` relies on truthiness: a nonzero int is true, 0 is false.
    while x:

        # x % 10 is the least significant decimal digit (0..9).
        # ord(c) gives the integer code point of a one-character string,
        # and chr(n) does the reverse. Digit characters '0'..'9' have
        # consecutive code points, so chr(ord('0') + d) is the character
        # for digit d, e.g. chr(ord('0') + 7) == '7'. This avoids calling
        # str(), which the problem forbids.
        # ord: https://docs.python.org/3/library/functions.html#ord
        # chr: https://docs.python.org/3/library/functions.html#chr
        digits.append(chr(ord('0') + x % 10))

        # `//=` is floor-division assignment: it drops the digit just
        # recorded (423 // 10 == 42). x is non-negative here, so floor
        # division is the same as truncating division.
        x //= 10
    if negative:

        # The digits are stored right-to-left, so appending '-' now puts
        # the sign at the front once the list is reversed.
        digits.append('-')

    # reversed(seq) returns a lazy iterator that yields the items of the
    # sequence from last to first, without copying the list.
    # str.join(iterable) concatenates the strings in the iterable, placing
    # the separator ('' here, i.e. nothing) between them. Building a list
    # and joining once is the efficient alternative to repeated string
    # concatenation, because Python strings are immutable.
    # reversed: https://docs.python.org/3/library/functions.html#reversed
    # str.join: https://docs.python.org/3/library/stdtypes.html#str.join
    return ''.join(reversed(digits))


def string_to_int(text: str) -> int:
    """Convert an optional leading minus and decimal digits to an integer.

    Helper added in this file (not printed in the book). It carries out the
    textbook's left-to-right "multiply by 10 and add the digit" method with
    an explicit loop. Input is assumed to be well formed.
    """
    # str.startswith(prefix) returns True if the string begins with prefix.
    # Docs: https://docs.python.org/3/library/stdtypes.html#str.startswith
    negative = text.startswith('-')
    result = 0

    # bool is a subclass of int, so int(True) == 1 and int(False) == 0.
    # text[int(negative):] therefore skips the first character exactly
    # when it is a minus sign, and otherwise slices the whole string.
    # bool: https://docs.python.org/3/library/functions.html#bool
    for digit in text[int(negative):]:

        # ord(digit) - ord('0') turns a digit character into its value
        # (e.g. ord('4') - ord('0') == 4), because '0'..'9' have
        # consecutive code points. Shifting the old result one decimal
        # place left (* 10) and adding the new digit is the textbook's
        # left-to-right method: "314" -> 3 -> 31 -> 314.
        # ord: https://docs.python.org/3/library/functions.html#ord
        result = result * 10 + ord(digit) - ord('0')

    # `A if condition else B` is a conditional expression: it evaluates to
    # A when the condition is true and to B otherwise.
    # Docs: https://docs.python.org/3/reference/expressions.html#conditional-expressions
    return -result if negative else result


def string_to_int_reduce(text: str) -> int:
    """Textbook's idiomatic string_to_int based on functools.reduce.

    Same algorithm as the book's string_to_int(s); this version adds an
    explicit check for empty input or a lone '-' sign.
    """
    # `raise` signals an error. ValueError is the conventional built-in
    # exception for an argument of the right type but an unacceptable
    # value. Without this check, text[0] would raise IndexError on '' and
    # a lone '-' would silently return 0.
    # ValueError: https://docs.python.org/3/library/exceptions.html#ValueError
    if not text or text == '-':
        raise ValueError('Expected decimal digits')

    # functools.reduce(function, iterable, initial) repeatedly applies a
    # two-argument function: it starts with `initial` (0 here), then calls
    # function(running_value, next_item) for each item and returns the
    # final running value. For "314": f(0,'3')=3, f(3,'1')=31,
    # f(31,'4')=314 — exactly the textbook's left-to-right method.
    # reduce: https://docs.python.org/3/library/functools.html#functools.reduce
    #
    # `lambda total, char: ...` creates a small anonymous function whose
    # body is a single expression (here, the "multiply by 10 and add"
    # step).
    # lambda: https://docs.python.org/3/reference/expressions.html#lambda
    #
    # string.digits is the constant '0123456789'. str.index(char) returns
    # the position of char in that string, which is the digit's value
    # ('7' is at index 7). It raises ValueError for a non-digit
    # character, which gives basic input validation for free.
    # string.digits: https://docs.python.org/3/library/string.html#string.digits
    # str.index: https://docs.python.org/3/library/stdtypes.html#str.index
    #
    # The iterable is a conditional expression: text[1:] (everything after
    # the sign) when the first character is '-', otherwise the whole text.
    accumulated = functools.reduce(
        lambda total, char: total*10 + string.digits.index(char),
        text[1:] if text[0] == '-' else text, 0)

    # Restore the sign recorded in text[0] with a conditional expression.
    return -accumulated if text[0] == '-' else accumulated


# TEXTBOOK POST-SOLUTION DISCUSSION (page 69)
# -------------------------------------------
# The book gives no complexity analysis or further discussion after the
# program for this exercise. (For reference only, not from the book: each
# function does a constant amount of work per digit, so it runs in time
# proportional to the number of digits.)
#
# VARIANTS
# --------
# The book lists no variants for this exercise.


# TEXTBOOK CODE COMPARISON
# ------------------------
# int_to_string:
#   book: `def int_to_string(x)`; sets `is_negative`, and if x < 0 does
#   `x, is_negative = -x, True`; then a `while True:` loop that appends
#   `chr(ord('0') + x % 10)`, does `x //= 10`, and breaks when x == 0 (so
#   0 yields '0' without a special case); finally
#   `return ('-' if is_negative else '') + ''.join(reversed(s))`.
#   file: `def int_to_string(x: int) -> str` (type hints added); an early
#   `if x == 0: return '0'`; the sign is recorded as `negative = x < 0`
#   and `x = abs(x)` replaces the tuple assignment; the loop is
#   `while x:`; the list is named `digits`; the '-' is appended to the
#   list before reversing instead of being concatenated in front of the
#   joined string. Same results for all integers.
# string_to_int (book) vs string_to_int_reduce (file):
#   book: `def string_to_int(s)`, a single return expression
#   `functools.reduce(lambda running_sum, c: running_sum * 10 +
#   string.digits.index(c), s[s[0] == '-':], 0) * (-1 if s[0] == '-' else 1)`.
#   file: renamed `string_to_int_reduce(text: str) -> int`; adds a
#   ValueError check for empty text or a lone '-'; lambda parameters
#   renamed `total, char`; the book's `s[s[0] == '-':]` (bool used as a
#   slice index) is replaced by the conditional expression
#   `text[1:] if text[0] == '-' else text`; the result is stored in
#   `accumulated` and the sign is applied with a conditional expression
#   instead of multiplying by -1 or 1.
# string_to_int (file): a helper not in the book; an explicit-loop version
#   of the same left-to-right algorithm using `ord(digit) - ord('0')`.
#   Note that the file's name `string_to_int` therefore refers to this
#   helper, not to the book's reduce-based function of that name.


# Python executes this block only when this source file is run directly.
# When pytest imports the file, this block is skipped automatically.
# Documentation: https://docs.python.org/3/library/__main__.html
if __name__ == "__main__":

    # These small, hand-selected examples show zero, a single digit, a
    # negative number, and a number with interior zeros. The book's own
    # example (314 <-> "314") follows the same pattern. The comprehensive
    # test suite remains in the separate tests/ folder.
    observed = int_to_string(0)

    # print() with several arguments writes them separated by a space.
    print("int_to_string:", observed)

    # `assert` stops the program with an AssertionError if the condition
    # is false. These are quick smoke checks; pytest provides the more
    # thorough automated verification.
    assert observed == '0'
    observed = int_to_string(3)
    print("int_to_string:", observed)
    assert observed == '3'
    observed = int_to_string(-125)
    print("int_to_string:", observed)
    assert observed == '-125'
    observed = int_to_string(2001)
    print("int_to_string:", observed)
    assert observed == '2001'

    # Round trip: converting an integer to text and back with the book's
    # reduce-based parser must give the original integer.
    for number in (-143, 0, 709):
        decimal_text = int_to_string(number)
        print("reduce parser:", decimal_text, string_to_int_reduce(decimal_text))
        assert string_to_int_reduce(decimal_text) == number
