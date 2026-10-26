"""EPI Python — Exercise 5.3: Multiply Two Arbitrary-Precision Integers

Chapter 5: Arrays
Textbook: pages 43–44 (printed page numbers; the exercise is introduced at
the bottom of page 43 and the problem and solution are on page 44).

PROBLEM (from the textbook)
---------------------------
Context: "Certain applications require arbitrary precision arithmetic. One
way to achieve this is to use arrays to represent integers, e.g., with one
digit per array entry with the most significant digit appearing first, and
a negative leading digit denoting a negative integer. For example,
<1,9,3,7,0,7,7,2,1> represents 193707721 and <-7,6,1,8,3,8,2,5,7,2,8,7>
represents -761838257287."

"Write a program that takes two arrays representing integers, and returns
an integer representing their product. For example, since
193707721 x -761838257287 = -147573952589676412927, if the inputs are
<1,9,3,7,0,7,7,2,1> and <-7,6,1,8,3,8,2,5,7,2,8,7>, your function should
return <-1,4,7,5,7,3,9,5,2,5,8,9,6,7,6,4,1,2,9,2,7>."

HINT (from the textbook)
------------------------
"Use arrays to simulate the grade-school multiplication algorithm."

SOLUTION DEVELOPMENT (following the textbook)
---------------------------------------------
As in Exercise 5.2 (incrementing a digit array), converting to a native
integer type is ruled out because it could overflow in a language with
fixed-size integers.

Instead, use the grade-school multiplication method: multiply the first
number by each digit of the second number and add up all of those partial
products.

To save space, the book accumulates each partial product into the running
total as it goes, rather than computing every partial product separately
and summing them at the end. A product of an n-digit and an m-digit number
has at most n + m digits, so a result array of length n + m is enough.

Worked example from the book, multiplying 123 by 987:
  - 7 x 123 = 861;
  - 8 x 123 x 10 = 9840, added to 861 gives 10701;
  - 9 x 123 x 100 = 110700, added to 10701 gives the final 121401.
(The book notes that all of these numbers are held as digit arrays.)

The sign is handled separately: the product is negative exactly when one,
but not both, of the inputs is negative; the digit work is done on the
absolute values, and the sign is applied to the leading digit at the end.

The book prints one program, implemented here as `multiply_digits`.

ADDITIONAL EXAMPLES (added for learning; not printed in this exercise)
---------------------------------------------------------------------
    [1, 2, 3] x [4, 5]  -> [5, 5, 3, 5]   (123 x 45 = 5535)
    [-2] x [3]          -> [-6]
    [0] x [1, 2]        -> [0]            (leading zeros removed; no sign)
"""


# `num1: list[int]` etc. are type hints. They document intent (lists of
# ints in, a list of ints out) but Python does not enforce them at run
# time. `list[int]` requires Python 3.9 or newer.
# Documentation: https://docs.python.org/3/library/typing.html
def multiply_digits(num1: list[int], num2: list[int]) -> list[int]:
    """Multiply signed arbitrary-precision decimal digit arrays.

    This is the textbook's `multiply(num1, num2)` program. Unlike the book,
    it does not modify the caller's arrays (see TEXTBOOK CODE COMPARISON).
    """

    # Guard added in this repository (not in the book): empty lists are
    # falsy, so this rejects an operand with no digits.
    # Documentation: https://docs.python.org/3/library/exceptions.html#ValueError
    if not num1 or not num2:
        raise ValueError("Both operands require at least one digit")

    # In this textbook representation, a negative first element signifies a
    # negative whole number. `(num1[0] < 0) != (num2[0] < 0)` is True when
    # exactly one operand is negative (an exclusive-or of the two booleans;
    # the book writes it with the `^` operator), and then the product is
    # negative.
    # `X if condition else Y` is a conditional expression: it evaluates to
    # X when the condition is true and to Y otherwise.
    # Documentation: https://docs.python.org/3/reference/expressions.html#conditional-expressions
    sign = -1 if (num1[0] < 0) != (num2[0] < 0) else 1

    # A list comprehension makes fresh nonnegative digit arrays, so the
    # caller's input arrays remain intact. abs() returns the absolute
    # value; only the leading digit can actually be negative.
    # Documentation: https://docs.python.org/3/library/functions.html#abs
    # The line also uses tuple unpacking to assign `a` and `b` at once.
    a, b = [abs(x) for x in num1], [abs(x) for x in num2]

    # `[0] * k` builds a list of k zeros. The product of an n-digit and an
    # m-digit number has at most n + m digits.
    product = [0] * (len(a) + len(b))

    # `range(len(a) - 1, -1, -1)` counts down from the last index to 0
    # (start, stop exclusive, step -1); the book writes
    # `reversed(range(len(num1)))`, which yields the same indices.
    #
    # Digit a[i] times digit b[j] contributes to output position i + j + 1
    # (positions count from the most significant end, with one extra slot
    # at the front for a possible final carry).
    # `//` is floor division and `%` is remainder: for nonnegative values,
    # x // 10 is the carry and x % 10 is the digit that stays.
    for i in range(len(a) - 1, -1, -1):
        for j in range(len(b) - 1, -1, -1):
            product[i + j + 1] += a[i] * b[j]
            product[i + j] += product[i + j + 1] // 10
            product[i + j + 1] %= 10

    # Book comment: "Remove the leading zeroes." Skip zeros at the front,
    # but always keep at least one digit, so a zero product stays [0].
    start = 0
    while start < len(product) - 1 and product[start] == 0:
        start += 1

    # `product[start:]` is a slice: a new list holding the elements from
    # index `start` to the end.
    result = product[start:]

    # Apply the sign to the leading digit, except for zero, which has no
    # sign in this representation.
    if result != [0]:
        result[0] *= sign
    return result


# TEXTBOOK POST-SOLUTION DISCUSSION (page 44)
# ------------------------------------------
# There are m partial products (one per digit of the second number), each
# with at most n + 1 digits. Each digit of each partial product costs O(1)
# work, so the time complexity is O(nm).
#
# VARIANTS
# --------
# The book gives no variants for this exercise.


# TEXTBOOK CODE COMPARISON
# ------------------------
# - Book: `def multiply(num1, num2)`; file: function renamed
#   `multiply_digits`, type hints added.
# - The file adds an empty-operand guard (`raise ValueError`); not in book.
# - Sign: book `sign = -1 if (num1[0] < 0) ^ (num2[0] < 0) else 1`; file
#   uses `!=` instead of `^` (same truth table for booleans).
# - Book overwrites the callers' leading digits in place:
#   `num1[0], num2[0] = abs(num1[0]), abs(num2[0])`. File instead builds
#   new lists `a` and `b` with abs() applied to every digit, leaving the
#   inputs untouched.
# - Book's result array is named `result`; file calls it `product`.
#   Book loops `for i in reversed(range(len(num1)))`; file uses
#   `range(len(a) - 1, -1, -1)`. The three loop-body statements match.
# - Leading-zero removal: book uses a one-liner
#   `result = result[next((i for i, x in enumerate(result) if x != 0),
#   len(result)):] or [0]` (a generator expression with next() and
#   enumerate()); file uses an explicit `while` loop that stops one short
#   of the end, then slices.
# - Final sign: book `return [sign * result[0]] + result[1:]`; file
#   multiplies `result[0]` in place, skipping the zero result, and returns
#   `result`.


# Python executes this block only when this source file is run directly.
# When pytest imports the file, this block is skipped automatically.
# Documentation: https://docs.python.org/3/library/__main__.html
if __name__ == "__main__":

    # Each example is (left digits, right digits, expected product digits).
    # These are added for learning: an ordinary multiplication, a negative
    # operand, and a zero result.
    for left, right, expected in (([1, 2, 3], [4, 5], [5, 5, 3, 5]),
                                  ([-2], [3], [-6]),
                                  ([0], [1, 2], [0])):
        observed = multiply_digits(left, right)

        # An f-string (prefix f) evaluates each {expression} and inserts
        # its text into the string.
        # Documentation: https://docs.python.org/3/tutorial/inputoutput.html#formatted-string-literals
        print(f"{left} * {right} = {observed}")

        # `assert` stops the program with an AssertionError if the result
        # differs from the expected value. These are quick smoke checks;
        # pytest provides the more thorough automated verification.
        assert observed == expected
    print("Textbook multiplication examples passed.")
