"""EPI Python — Exercise 6.2: Base Conversion

Chapter 6: Strings
Textbook: pages 69–70 (printed page numbers; problem and solution start on
69, the program and complexity analysis are on 70).

PROBLEM (from the textbook)
---------------------------
In the decimal number system, the position of a digit is used to signify
the power of 10 that digit is to be multiplied with. For example, "314"
denotes the number 3 x 100 + 1 x 10 + 4 x 1. The base b number system
generalizes the decimal number system: the string "a_{k-1} a_{k-2} ... a_1
a_0", where 0 <= a_i < b, denotes in base-b the integer
a_0 x b^0 + a_1 x b^1 + a_2 x b^2 + ... + a_{k-1} x b^{k-1}.

Write a program that performs base conversion. The input is a string, an
integer b1, and another integer b2. The string represents an integer in
base b1. The output should be the string representing the integer in base
b2. Assume 2 <= b1, b2 <= 16. Use "A" to represent 10, "B" for 11, ..., and
"F" for 15. (For example, if the string is "615", b1 is 7 and b2 is 13,
then the result should be "1A7", since
6 x 7^2 + 1 x 7 + 5 = 1 x 13^2 + 10 x 13 + 7.)

HINT (from the textbook)
------------------------
What base can you easily convert to and from?

SOLUTION DEVELOPMENT (following the textbook)
---------------------------------------------
Brute force: convert the input to unary (a row of 1s) and then group the
1s into multiples of b2, b2^2, b2^3, and so on. The book's example:
(102)_3 = (11111111111)_1, i.e. eleven 1s. Converting that to base 4 gives two groups of 4 with three
1s left over, so the answer is (23)_4. This is awkward to implement and has
terrible time and space complexity.

Key insight: every programming language has an integer type supporting
multiply, add, divide and modulus, and these make the conversion easy.
Use the integer as the intermediate form:

1. Convert the base-b1 string to an integer with a sequence of
   multiply-and-add steps (as in the string-to-integer part of 6.1).
2. Convert that integer to a base-b2 string with a sequence of modulus and
   division steps (as in the integer-to-string part of 6.1).

Worked example from the book: "615" with b1 = 7, b2 = 13.
    * The integer value, in decimal, is 306.
    * 306 mod 13 = 7 is the least significant output digit; continue
      with 306 / 13 = 23.
    * 23 mod 13 = 10, written 'A'; continue with 23 / 13 = 1.
    * 1 mod 13 = 1 and 1 / 13 = 0, so the final (most significant) digit
      is 1. The result is "1A7".
The book remarks that the design nicely illustrates reduction (reducing
the problem to integer conversion).

Because the output step is naturally expressed in terms of a smaller
instance of the same problem (convert value // base, then append the last
digit), the book implements it with recursion.

In this file:
* convert_base_recursive follows the book's program convert_base(...):
  functools.reduce for parsing and a recursive helper for output.
* convert_base is an extra iterative implementation (not printed in the
  book) of the same two-step algorithm, using divmod and a loop.

ADDITIONAL EXAMPLES (added for learning; not printed in this exercise)
---------------------------------------------------------------------
    convert_base("FF", 16, 10)    -> "255"
    convert_base("101", 2, 16)    -> "5"
    convert_base("-1A7", 13, 10)  -> "-306"  (the book's example reversed,
                                               with a sign)
"""

# Python standard library: higher-order functions and operations on callables.
# Module documentation: https://docs.python.org/3/library/functools.html
# reduce API: https://docs.python.org/3/library/functools.html#functools.reduce
import functools

# Python standard library: common string constants and operations.
# Module documentation: https://docs.python.org/3/library/string.html
# hexdigits constant: https://docs.python.org/3/library/string.html#string.hexdigits
import string


# Digit symbols for bases up to 16: the symbol at index d stands for the
# value d (so DIGITS[10] == 'A'). An upper-case module-level name is the
# Python convention for a constant (the language does not enforce it).
DIGITS = "0123456789ABCDEF"


# `number: str`, `source_base: int`, `-> str` are type hints. They document
# the expected types; Python does not check or enforce them at run time.
# Annotations: https://docs.python.org/3/glossary.html#term-annotation
def convert_base(number: str, source_base: int, target_base: int) -> str:
    """Convert a signed integer string between bases 2 through 16.

    Iterative implementation added in this file (not printed in the book)
    of the textbook's algorithm: parse to an integer, then emit digits with
    repeated division. Also validates bases and digits.
    """
    # `2 <= source_base <= 16` is a chained comparison: Python evaluates
    # it as `2 <= source_base and source_base <= 16`.
    # Docs: https://docs.python.org/3/reference/expressions.html#comparisons
    #
    # `raise ValueError(...)` signals an argument with an unacceptable
    # value. ValueError: https://docs.python.org/3/library/exceptions.html#ValueError
    if not 2 <= source_base <= 16 or not 2 <= target_base <= 16:
        raise ValueError("Only bases 2 through 16 are supported")
    if not number or number == '-':
        raise ValueError("Missing digits")

    # `A if condition else B` is a conditional expression: A when the
    # condition is true, otherwise B.
    # Docs: https://docs.python.org/3/reference/expressions.html#conditional-expressions
    sign = -1 if number[0] == '-' else 1

    # str.lstrip('-') returns a copy with all leading '-' characters
    # removed (note: all of them, not just one). str.upper() returns an
    # upper-case copy, so 'ff' and 'FF' are both accepted. Strings are
    # immutable, so both methods return new strings.
    # lstrip: https://docs.python.org/3/library/stdtypes.html#str.lstrip
    # upper: https://docs.python.org/3/library/stdtypes.html#str.upper
    abs_text = number.lstrip('-').upper()
    decimal_value = 0
    for digit in abs_text:

        # str.find(sub) returns the lowest index of sub, or -1 if it is
        # absent (unlike str.index, which raises ValueError). The index
        # in DIGITS is the digit's numeric value.
        # Docs: https://docs.python.org/3/library/stdtypes.html#str.find
        value = DIGITS.find(digit)

        # A digit is valid only if 0 <= value < source_base; this also
        # rejects -1 (symbol not found).
        if not 0 <= value < source_base:
            raise ValueError("Digit is not valid in source base")

        # Step 1 of the textbook algorithm: multiply-and-add parsing.
        decimal_value = decimal_value * source_base + value

    # The loop below writes no digits for 0, so handle it explicitly.
    if decimal_value == 0:
        return "0"
    symbols = []
    while decimal_value:

        # divmod(a, b) returns the pair (a // b, a % b) in one call. Tuple
        # unpacking assigns the quotient back to decimal_value and the
        # remainder (the next least significant base-b2 digit) to
        # remainder. Step 2 of the textbook algorithm.
        # Docs: https://docs.python.org/3/library/functions.html#divmod
        decimal_value, remainder = divmod(decimal_value, target_base)
        symbols.append(DIGITS[remainder])

    # Digits were produced least significant first. reversed(list) yields
    # them from last to first (a lazy iterator), and ''.join concatenates
    # them into one string; the sign is prefixed with a conditional
    # expression.
    # reversed: https://docs.python.org/3/library/functions.html#reversed
    # str.join: https://docs.python.org/3/library/stdtypes.html#str.join
    return ('-' if sign < 0 else '') + ''.join(reversed(symbols))


def convert_base_recursive(number: str, b1: int, b2: int) -> str:
    """Textbook's convert_base: reduce-based parsing, recursive output.

    Follows the book's program, with added validation of the bases, of
    empty input and of each digit, and no '-' for an input of "-0".
    """
    if not 2 <= b1 <= 16 or not 2 <= b2 <= 16:
        raise ValueError('Bases must be between 2 and 16')
    if not number or number == '-':
        raise ValueError('No source-base digits')
    negative = number[0] == '-'

    # A nested function: defined inside convert_base_recursive, it can
    # read the enclosing function's variable b1 (a closure).
    def digit_value(symbol):

        # string.hexdigits is the constant '0123456789abcdefABCDEF'.
        # str.lower() maps 'A'..'F' to 'a'..'f', and str.index(sub)
        # returns the first position of sub, which for lower-case symbols
        # equals the digit value ('a' -> 10). str.index raises ValueError
        # if the symbol is not a hex digit at all.
        # hexdigits: https://docs.python.org/3/library/string.html#string.hexdigits
        # str.index: https://docs.python.org/3/library/stdtypes.html#str.index
        digit = string.hexdigits.index(symbol.lower())
        if digit >= b1:
            raise ValueError('Input contains a digit not valid in source base')
        return digit

    # functools.reduce(function, iterable, initial) starts from `initial`
    # (0) and calls function(running_value, next_item) for each character,
    # returning the final running value. Here each call shifts the total
    # one base-b1 place left and adds the next digit — the textbook's
    # multiply-and-add parsing step. `lambda total, ch: ...` is a small
    # anonymous function whose body is one expression.
    # reduce: https://docs.python.org/3/library/functools.html#functools.reduce
    # lambda: https://docs.python.org/3/reference/expressions.html#lambda
    #
    # The iterable skips a leading '-' via a conditional expression.
    parsed = functools.reduce(
        lambda total, ch: total*b1 + digit_value(ch),
        number[1:] if negative else number, 0)

    # Recursive output construction (the textbook's construct_from_base):
    # the base-b2 string of `value` is the string of value // b2 followed
    # by the symbol for value % b2. The recursion stops at 0, which
    # contributes the empty string. Recursion depth equals the number of
    # output digits, far below Python's default recursion limit here.
    def emit(value):
        if value == 0:
            return ''

        # string.hexdigits[d] is the lower-case symbol for d < 16, so
        # .upper() turns 'a'..'f' into the required 'A'..'F'.
        return emit(value//b2) + string.hexdigits[value % b2].upper()

    # emit(0) would give '', so zero is mapped to '0' explicitly; the '-'
    # is emitted only for a negative, nonzero value (avoids "-0").
    return ('-' if negative and parsed else '') + (emit(parsed) if parsed else '0')


# TEXTBOOK POST-SOLUTION DISCUSSION (page 70)
# -------------------------------------------
# Time complexity: O(n(1 + log_{b2} b1)), where n is the length of the
# input string s. Reasoning, as given in the book:
#   * Parsing takes n multiply-and-add steps to obtain the integer x from s.
#   * Producing the output takes log_{b2} x multiply-and-add style steps
#     (one per output digit).
#   * x is at most b1^n, and log_{b2}(b1^n) = n log_{b2} b1.
# Adding the two parts gives n + n log_{b2} b1 = n(1 + log_{b2} b1).
#
# VARIANTS
# --------
# The book lists no variants for this exercise.


# TEXTBOOK CODE COMPARISON
# ------------------------
# convert_base_recursive (file) vs convert_base (book):
#   book: `def convert_base(num_as_string, b1, b2)` with a nested
#   `construct_from_base(num_as_int, base)` written as one conditional
#   return expression; `is_negative = num_as_string[0] == '-'`;
#   `num_as_int = functools.reduce(lambda x, c: x * b1 +
#   string.hexdigits.index(c.lower()), num_as_string[is_negative:], 0)`
#   (a bool used as the slice start); then
#   `return ('-' if is_negative else '') + ('0' if num_as_int == 0 else
#   construct_from_base(num_as_int, b2))`.
#   file: renamed `convert_base_recursive(number: str, b1: int, b2: int)
#   -> str` (type hints added); adds ValueError checks for bases outside
#   2..16, empty input or a lone '-', and digits not valid in base b1
#   (the book does no validation); the digit lookup is moved into a nested
#   `digit_value` helper; the slice `num_as_string[is_negative:]` becomes
#   the conditional expression `number[1:] if negative else number`; the
#   nested output helper is renamed `emit(value)`, takes no base
#   parameter (it uses b2 from the enclosing scope), and is written with
#   an if-statement instead of a conditional expression; the sign is
#   emitted only when `negative and parsed`, so "-0" gives "0" where the
#   book's code would give "-0".
# convert_base (file): an extra iterative implementation not in the book
#   (DIGITS constant, str.find, divmod loop, reversed/join), with input
#   validation. Note the file's name `convert_base` refers to this
#   helper, not to the book's recursive program of that name.
# DIGITS: module-level constant not in the book.


# Python executes this block only when this source file is run directly.
# When pytest imports the file, this block is skipped automatically.
# Documentation: https://docs.python.org/3/library/__main__.html
if __name__ == "__main__":

    # Each example is (input string, source base, target base). These are
    # added examples: hexadecimal and binary to decimal. The comprehensive
    # test suite remains in the separate tests/ folder.
    for text, b1, b2 in [("FF", 16, 10), ("101", 2, 10)]:

        # An f-string (prefix f) evaluates the expressions inside {...}
        # and inserts their values into the text, here including the
        # result of a function call.
        # Docs: https://docs.python.org/3/tutorial/inputoutput.html#formatted-string-literals
        print(f"{text} (base {b1}) -> {convert_base(text, b1, b2)} (base {b2})")

    # `assert` stops the program with an AssertionError if the condition
    # is false. These are quick smoke checks; pytest provides the more
    # thorough automated verification.
    assert convert_base("FF", 16, 10) == "255"

    # Check that the textbook-style recursive version agrees with the
    # iterative version, including a negative input that is the book's
    # "1A7" (base 13) example.
    for number, source, target in (("FF", 16, 10), ("101", 2, 16), ("-1A7", 13, 10)):
        assert convert_base_recursive(number, source, target) == convert_base(number, source, target)
        print("recursive base conversion:", number, convert_base_recursive(number, source, target))
