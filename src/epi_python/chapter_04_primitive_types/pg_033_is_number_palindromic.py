"""EPI Python — Exercise 4.9: Check if a Decimal Integer Is a Palindrome

Chapter 4: Primitive Types
Textbook: pages 33–34 (printed page numbers; problem, solution and the start
of the program are on 33; the rest of the program and the complexity remark
are at the top of 34).

PROBLEM (from the textbook)
---------------------------
A palindromic string is one which reads the same forwards and backwards,
e.g., "redivider". In this problem, you are to write a program which
determines if the decimal representation of an integer is a palindromic
string. For example, your program should return true for the inputs 0, 1,
7, 11, 121, 333, and 2147447412, and false for the inputs -1, 12, 100, and
2147483647.

Write a program that takes an integer and determines if that integer's
representation as a decimal string is a palindrome.

HINT (from the textbook)
------------------------
It's easy to come up with a simple expression that extracts the least
significant digit. Can you find a simple expression for the most significant
digit?

SOLUTION DEVELOPMENT (following the textbook)
---------------------------------------------
A negative input can never be palindromic, because its decimal string starts
with a minus sign.

Brute force: convert the integer to a string and compare digits in pairs,
starting with the least and most significant digits and moving inward,
stopping at the first mismatch. Time and space are both O(n), where n is the
number of digits.

The O(n) space for the string can be avoided by pulling digits straight out
of the number. The number of digits is n = floor(log10(x)) + 1. So the least
significant digit is x mod 10 and the most significant digit is
x / 10**(n - 1) (integer division). The program repeatedly compares the most
and least significant digits and then removes both from the number.

Book's examples:
- 151751: compare 1 and 1 (equal), leaving 5175; compare 5 and 5 (equal),
  leaving 17; 1 and 7 differ, so return false.
- 157751: the same steps end by comparing 7 with 7, so return true.

The book's program is `is_palindrome_number(x)`. This file contains:
- `is_number_palindromic`: compares the leading and trailing digits and
  strips both each round, like the book, but finds the leading-digit
  divisor with a loop instead of math.log10 (see TEXTBOOK CODE COMPARISON).
- `is_number_palindromic_half_reverse`: an added alternative that is NOT
  printed in the book.

ADDITIONAL EXAMPLES (added for learning; not printed in this exercise)
---------------------------------------------------------------------
    1221 -> True
    123  -> False
    -112 -> False (negative)
(0, 7, 121, 100 and 2147447412 in the `__main__` block are from the book's
list.)
"""

# This file has no import statements (the book's version imports math for
# math.floor and math.log10; this file's code does not use them).


# Type hints: `x: int` and `-> bool` say the input is an int and the result
# a bool (True/False). Python does not enforce hints.
def is_number_palindromic(x: int) -> bool:
    """Compare highest and lowest remaining decimal digits (textbook method).

    Repository variant of the book's `is_palindrome_number`; the leading
    digit's divisor is found by a loop instead of with math.log10.
    """

    # Negative numbers start with '-', so they cannot be palindromes.
    if x < 0:
        return False
    if x == 0:
        return True

    # Find the largest power of ten that is <= x: this is the book's
    # msd_mask = 10**(num_digits - 1). `//` is floor (integer) division.
    divisor = 1
    while x // divisor >= 10:
        divisor *= 10

    # A nonzero int is truthy; stop once all digits have been removed.
    while x:

        # `x // divisor` is the most significant digit; `x % 10` is the least
        # significant digit (remainder on division by 10).
        if x // divisor != x % 10:
            return False

        # Remove the highest digit (`x % divisor` keeps everything below it),
        # then the lowest digit (`// 10`). Two digits are gone, so the
        # divisor shrinks by a factor of 100.
        x = (x % divisor) // 10
        divisor //= 100
    return True


def is_number_palindromic_half_reverse(x: int) -> bool:
    """Alternative added in this repository (not printed in the textbook).

    Reverses the lower half of the digits numerically and compares it with
    the upper half.
    """
    if x < 0:
        return False
    if x == 0:
        return True

    # A number ending in 0 (other than 0 itself) would need to start with 0,
    # which decimal numbers never do.
    if x % 10 == 0:
        return False

    # Simultaneous assignment of two names on one line.
    remaining, reversed_digits = x, 0

    # Move digits from the end of `remaining` onto `reversed_digits` until
    # the reversed part is at least as large, i.e. about half the digits.
    while remaining > reversed_digits:
        reversed_digits = reversed_digits * 10 + remaining % 10
        remaining //= 10

    # Even digit count: the halves must match exactly. Odd digit count: the
    # middle digit sits at the end of reversed_digits; `// 10` drops it.
    return remaining == reversed_digits or remaining == reversed_digits // 10


# TEXTBOOK POST-SOLUTION DISCUSSION (page 34)
# -------------------------------------------
# The time complexity is O(n) and the space complexity is O(1).
#
# Alternatively, Solution 4.8 (reverse digits, page 32) could be used to
# reverse the number and check whether it is unchanged.
#
# VARIANTS
# --------
# The book gives no variants for this exercise.


# TEXTBOOK CODE COMPARISON
# ------------------------
# - Book: `def is_palindrome_number(x)`; file: `is_number_palindromic(x: int)
#   -> bool` (renamed, type hints added).
# - Book: `if x <= 0: return x == 0`; file: two separate tests
#   (`x < 0` -> False, `x == 0` -> True), same results.
# - Book computes `num_digits = math.floor(math.log10(x)) + 1` and
#   `msd_mask = 10**(num_digits - 1)` (requires `import math`), then runs
#   `for i in range(num_digits // 2)`, removing digits with
#   `x %= msd_mask` and `x //= 10` and shrinking `msd_mask //= 100`.
#   File: no math import; finds `divisor` with a `while x // divisor >= 10`
#   loop, loops `while x:` instead of a fixed num_digits // 2 iterations,
#   and removes both digits in one statement `x = (x % divisor) // 10`.
#   Because the stopping rule differs, the two loops are not step-for-step
#   identical (e.g. when inner zeros make x shrink faster); recorded for
#   review only.
# - `is_number_palindromic_half_reverse` is an extra helper not in the book.
# - The book's comments ("Remove the most/least significant digit of x.")
#   are paraphrased in the file's comment above the removal statement.


# Python executes this block only when this source file is run directly.
# When pytest imports the file, this block is skipped automatically.
# Documentation: https://docs.python.org/3/library/__main__.html
if __name__ == "__main__":

    # Each tuple is (x, expected). 0, 7, 121, 100 and 2147447412 come from
    # the book's example list; 1221, 123 and -112 are added.
    for x, expected in ((0,True),(7,True),(121,True),(1221,True),(123,False),
                        (-112,False),(100,False),(2147447412,True)):

        # Functions are objects, so a tuple of them can be looped over and
        # each one called in turn on the same input.
        for algorithm in (is_number_palindromic,
                          is_number_palindromic_half_reverse):
            observed = algorithm(x)

            # f-string: each expression in {} is evaluated and inserted.
            # `algorithm.__name__` is the function's name as a string.
            # https://docs.python.org/3/reference/lexical_analysis.html#f-strings
            print(f"{algorithm.__name__}({x})={observed}")

            # `assert` stops the program with an AssertionError if the
            # condition is false. `is` checks identity: True and False are
            # single objects, so `observed is expected` also confirms the
            # result is a real bool. Quick smoke checks; pytest does more.
            assert observed is expected
