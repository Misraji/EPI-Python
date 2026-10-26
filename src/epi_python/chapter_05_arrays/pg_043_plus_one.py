"""EPI Python — Exercise 5.2: Increment an Arbitrary-Precision Integer

Chapter 5: Arrays
Textbook: page 43 (printed page number; problem, solution and variant all
appear on page 43).

PROBLEM (from the textbook)
---------------------------
"Write a program which takes as input an array of digits encoding a
nonnegative decimal integer D and updates the array to represent the
integer D + 1. For example, if the input is <1,2,9> then you should update
the array to <1,3,0>. Your algorithm should work even if it is implemented
in a language that has finite-precision arithmetic."

HINT (from the textbook)
------------------------
"Experiment with concrete examples."

SOLUTION DEVELOPMENT (following the textbook)
---------------------------------------------
Brute force: turn the digit array into the integer it encodes, add one,
and split the result back into digits. For <1,2,9> that means forming
129, computing 130, and extracting <1,3,0>. In a language whose integer
type has a bounded range, this breaks on inputs that encode numbers
outside that range.

Overflow is avoided by working on the digits themselves, imitating the
grade-school addition method: add starting at the least significant digit
and pass carries leftward. One complication: the result may need one more
digit than the input has. For example, 99 + 1 = 100 requires three digits
while the input only has two, so the array must grow.

Worked example from the book: for <1,2,9>, the 9 becomes 0 with a carry
out of 1; the carry turns the 2 into 3; there is no further carry, so the
process stops and the result is <1,3,0>.

The book prints one program, implemented here as `plus_one`.

ADDITIONAL EXAMPLES (added for learning; not printed in this exercise)
---------------------------------------------------------------------
    [9, 9, 9] -> [1, 0, 0, 0]   (carry runs through every digit; array grows)
    [0]       -> [1]
The list passed in is modified in place and the same list object is
returned.
"""


# `digits: list[int]` and `-> list[int]` are type hints: they document that
# the function takes and returns a list of ints. Python does not enforce
# annotations at run time. `list[int]` requires Python 3.9 or newer.
# Documentation: https://docs.python.org/3/library/typing.html
def plus_one(digits: list[int]) -> list[int]:
    """Add one to a mutable decimal digit array, preserving its identity.

    This is the textbook's `plus_one(A)` program. The list is updated in
    place and the same list object is returned.
    """

    # An empty list is falsy, so `not digits` is True for []. This guard
    # was added in this repository (the book assumes at least one digit);
    # ValueError is the built-in exception for an unacceptable value.
    # Documentation: https://docs.python.org/3/library/exceptions.html#ValueError
    if not digits:
        raise ValueError("The textbook requires at least one decimal digit")

    # Index -1 means "last element" in Python: negative indices count from
    # the end. Adding one to the least significant digit starts the
    # grade-school addition. The digit may now be 10, a pending carry.
    digits[-1] += 1

    # `reversed(range(1, n))` yields n-1, n-2, ..., 1. reversed() returns
    # an iterator that walks the range backwards without building an
    # extra list. Index 0 is excluded because there is no position to its
    # left to carry into; it is handled after the loop.
    # Documentation: https://docs.python.org/3/library/functions.html#reversed
    for index in reversed(range(1, len(digits))):

        # A digit other than 10 means no carry-out: everything to the left
        # is unchanged, so stop early.
        if digits[index] != 10:
            break

        # Replace the 10 with 0 and carry 1 into the next more significant
        # digit.
        digits[index] = 0
        digits[index - 1] += 1
    if digits[0] == 10:

        # Book comments: "There is a carry-out, so we need one more digit
        # to store the result. A slick way to do this is to append a 0 at
        # the end of the array, and update the first entry to 1."
        # This works because a carry out of the first digit only happens
        # when every digit was 9, so the answer is 1 followed by zeros.
        digits[0] = 1

        # `append` extends the existing list at its right-hand side.
        # Documentation: https://docs.python.org/3/tutorial/datastructures.html
        digits.append(0)
    return digits


# TEXTBOOK POST-SOLUTION DISCUSSION (page 43)
# ------------------------------------------
# The time complexity is O(n), where n is the length of the array: in the
# worst case (all nines) the carry travels through every digit.
#
# VARIANTS
# --------
# Variant (stated in the book; no solution given): Write a program which
# takes as input two strings s and t of bits encoding binary numbers B_s
# and B_t, respectively, and returns a new string of bits representing the
# number B_s + B_t.


# TEXTBOOK CODE COMPARISON
# ------------------------
# - Book: `def plus_one(A)`; file: parameter renamed `digits`, with type
#   hints `list[int]` added.
# - The file adds an empty-input guard (`raise ValueError`) that the book
#   does not have.
# - Loop variable renamed from `i` to `index`. Otherwise the statements
#   (increment last digit, reversed carry loop with break, the
#   `A[0] = 1; A.append(0)` trick, `return A`) match the book's listing.


# Python executes this block only when this source file is run directly.
# When pytest imports the file, this block is skipped automatically.
# Documentation: https://docs.python.org/3/library/__main__.html
if __name__ == "__main__":

    # Each example is (input digits as a tuple, expected list). The first
    # is the book's <1,2,9>; the others are added for learning (carry
    # through every digit, and a single digit).
    for original, expected in (((1, 2, 9), [1, 3, 0]),
                               ((9, 9, 9), [1, 0, 0, 0]),
                               ((0,), [1])):

        # `list(original)` builds a new, mutable list from the tuple,
        # because plus_one modifies its argument and tuples are immutable.
        digits = list(original)

        # id() returns an integer identifying an object for its lifetime.
        # Comparing ids below shows that plus_one returned the very same
        # list it was given (in-place update), not a new list.
        # Documentation: https://docs.python.org/3/library/functions.html#id
        original_identity = id(digits)
        result = plus_one(digits)

        # An f-string (prefix f) evaluates the expressions in {} and inserts
        # their text into the string.
        # Documentation: https://docs.python.org/3/tutorial/inputoutput.html#formatted-string-literals
        print(f"{original} + 1 = {result}")

        # `assert` stops the program with an AssertionError if a condition
        # is false. These are quick smoke checks; pytest provides the more
        # thorough automated verification.
        assert result == expected
        assert id(result) == original_identity
    print("Textbook in-place increment examples passed.")
