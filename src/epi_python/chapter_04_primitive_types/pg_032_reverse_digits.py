"""EPI Python — Exercise 4.8: Reverse Digits

Chapter 4: Primitive Types
Textbook: pages 32–33 (printed page numbers; the problem and brute force are
at the bottom of 32, the improved solution, program and complexity on 33).

PROBLEM (from the textbook)
---------------------------
Write a program which takes an integer and returns the integer corresponding
to the digits of the input written in reverse order. For example, the
reverse of 42 is 24, and the reverse of -314 is -413.

HINT (from the textbook)
------------------------
How would you solve the same problem if the input is presented as a string?

SOLUTION DEVELOPMENT (following the textbook)
---------------------------------------------
Brute force: convert the integer to a string and build the reverse by
reading the string from back to front. The book's example: (1100)_2 is the
decimal number 12, and its answer comes from traversing the string "12" in
reverse order.

A closer look shows no string is needed. Take the input 1132. The first
digit of the result is 2, which is 1132 mod 10. The rest of the result is
the reverse of 1132/10 = 113 (integer division). In general, for an input
k >= 0, k mod 10 is the most significant digit of the result and the
remaining digits are the reverse of k/10. Continuing the example, the
(result, remaining input) pairs go: (2, 113), then (23, 11), then (231, 1),
then the result 2311.

For a general k, remember its sign, solve the problem for |k|, and put the
sign back on the result.

The book gives one program, implemented below as `reverse_digits`.

ADDITIONAL EXAMPLES (added for learning; not printed in this exercise)
---------------------------------------------------------------------
    0    -> 0
    123  -> 321
    120  -> 21  (the trailing zero becomes a leading zero, which vanishes)
    1    -> 1
(-314 -> -413 in the `__main__` block is the book's example.)
"""

# This file has no import statements: it uses only built-in operators and
# the built-in function abs().


# Type hints (`x: int`, `-> int`) document intended types; Python does not
# enforce them at runtime.
def reverse_digits(x: int) -> int:
    """Reverse base-10 digits, preserving the original sign.

    This is the textbook's numeric (no-string) implementation.
    """

    # Remember the sign as a bool (True/False).
    negative = x < 0

    # abs(x) returns the absolute value, so the loop works on |x| >= 0.
    # https://docs.python.org/3/library/functions.html#abs
    remaining = abs(x)
    result = 0

    # A nonzero int is truthy; the loop stops when all digits are consumed.
    while remaining:

        # `remaining % 10` is the rightmost decimal digit (the remainder on
        # division by 10). Multiplying `result` by 10 shifts its digits one
        # place left, and adding the new digit appends it on the right.
        result = result * 10 + remaining % 10

        # `//` is floor (integer) division: `remaining //= 10` drops the
        # digit just used. Because `remaining` is nonnegative, floor division
        # simply discards the remainder. (For negative numbers Python's `//`
        # and `%` round toward minus infinity, which is why the sign is
        # removed first.)
        remaining //= 10

    # Conditional expression `A if condition else B`: evaluates to A when the
    # condition is true, otherwise B. Here it puts the original sign back.
    return -result if negative else result


# TEXTBOOK POST-SOLUTION DISCUSSION (page 33)
# -------------------------------------------
# The time complexity is O(n), where n is the number of digits in k.
#
# VARIANTS
# --------
# The book gives no variants for this exercise.


# TEXTBOOK CODE COMPARISON
# ------------------------
# - Book: `def reverse(x)`; file: `reverse_digits(x: int) -> int` (renamed,
#   type hints added).
# - Book: `result, x_remaining = 0, abs(x)` and returns
#   `-result if x < 0 else result`. File: separate assignments, renames
#   `x_remaining` to `remaining`, and stores the sign in a variable
#   `negative` which the return uses instead of re-testing `x < 0`.
# - Loop body is the same as the book's.


# Python executes this block only when this source file is run directly.
# When pytest imports the file, this block is skipped automatically.
# Documentation: https://docs.python.org/3/library/__main__.html
if __name__ == "__main__":

    # Each tuple is (x, expected). (-314, -413) is the book's example; the
    # others are added (including 120, whose trailing zero disappears).
    for x,expected in ((0,0),(123,321),(-314,-413),(120,21),(1,1)):
        observed = reverse_digits(x)

        # f-string: each expression in {} is evaluated and inserted.
        # https://docs.python.org/3/reference/lexical_analysis.html#f-strings
        print(f"reverse digits {x}: {observed}")

        # `assert` stops the program with an AssertionError if the condition
        # is false. These are quick smoke checks; pytest does the thorough
        # testing in the separate tests/ folder.
        assert observed == expected
