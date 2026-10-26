"""EPI Python — Exercise 4.7: Compute x^y

Chapter 4: Primitive Types
Textbook: page 32 (printed page number; problem, solution, program and
complexity all appear on 32).

PROBLEM (from the textbook)
---------------------------
Write a program that takes a double x and an integer y and returns x^y. You
can ignore overflow and underflow.

HINT (from the textbook)
------------------------
Exploit mathematical properties of exponentiation.

SOLUTION DEVELOPMENT (following the textbook)
---------------------------------------------
Assume first that y is nonnegative.

Brute force: compute x**2 = x * x, then x**3 = x**2 * x, and so on. That is
y - 1 multiplications, which is O(2**n) where n is the number of bits needed
to write y.

To be faster, make each multiplication do more work. Book example: for
1.1**21, rather than multiplying by 1.1 twenty times, compute
1.1**2 = 1.21 once and then multiply 1.1 by 1.21 ten times: 11
multiplications in total. Going on to compute 1.1**3, 1.1**4, etc. does
better still.

When y is a power of 2, the fewest multiplications come from repeated
squaring: x, x**2, (x**2)**2 = x**4, (x**4)**2 = x**8, .... For a general
y, look at y in binary and use the rule x**(y0 + y1) = x**y0 * x**y1.

Book's small cases (exponents in binary):
    x**(1010)_2 = x**((101)_2 + (101)_2) = x**(101)_2 * x**(101)_2
    x**(101)_2  = x**((100)_2 + (1)_2)   = x**(100)_2 * x
                = x**(10)_2 * x**(10)_2 * x
In general: if the least significant bit of y is 0, the result is
(x**(y/2))**2; otherwise it is x * (x**(y/2))**2 (with y/2 rounded down).
That gives a recursive algorithm for nonnegative y.

For negative y, the only change is to replace x by 1/x and y by -y.

The book's implementation replaces the recursion with a while loop, to avoid
the cost of function calls. It is implemented below as `power`.

ADDITIONAL EXAMPLES (added for learning; not printed in this exercise)
---------------------------------------------------------------------
    power(2.0, 10)  -> 1024.0  (10 = (1010)_2, so 2**2 * 2**8)
    power(2.0, -2)  -> 0.25    (negative exponent: (1/2)**2)
    power(-2.0, 3)  -> -8.0    (negative base, odd exponent)
"""

# This file has no import statements: it uses only built-in operators.


# Type hints: `x: float` and `-> float` say x and the result are floating
# point numbers; `y: int` says the exponent is an integer. Python does not
# enforce hints (an int passed as x still works).
def power(x: float, y: int) -> float:
    """Exponentiation by squaring, loop form (textbook implementation).

    Handles negative integer exponents by inverting x.
    """
    if y < 0:

        # Added in this repository: 1.0 / 0 would fail anyway, but this
        # raises ZeroDivisionError (the built-in exception for division by
        # zero) with a clearer message.
        # https://docs.python.org/3/library/exceptions.html#ZeroDivisionError
        if x == 0:
            raise ZeroDivisionError("Zero cannot have a negative exponent")

        # x**(-y) == (1/x)**y. Simultaneous assignment computes both new
        # values from the old x and y before assigning. `1.0/x` always gives
        # a float in Python 3 (`/` is true division).
        x, y = 1.0/x, -y
    result = 1.0

    # Process the bits of y from least significant upward; a nonzero int is
    # truthy, so the loop ends when all bits have been shifted out.
    while y:

        # `y & 1` is the current lowest bit of y. When it is set, the current
        # x (which equals original_x ** (2**k) for bit k) is part of the
        # product, so multiply it into the result.
        if y & 1:
            result *= x

        # Square x for the next bit position, and shift y right (`>>= 1`,
        # i.e. y // 2) to expose the next bit.
        x *= x
        y >>= 1
    return result


# TEXTBOOK POST-SOLUTION DISCUSSION (page 32)
# -------------------------------------------
# The number of multiplications is at most twice the index of y's most
# significant bit, so the time complexity is O(n), where n is the number of
# bits in y.
#
# VARIANTS
# --------
# The book gives no variants for this exercise.


# TEXTBOOK CODE COMPARISON
# ------------------------
# - Book: `def power(x, y)`; file: `power(x: float, y: int) -> float`.
# - Book keeps y unchanged and loops on a copy: `result, power = 1.0, y`,
#   then `if y < 0: power, x = -power, 1.0 / x`, and
#   `x, power = x * x, power >> 1` in one statement. File reuses `y` itself
#   (no `power` variable), sets `result = 1.0` separately, and splits the
#   update into `x *= x` and `y >>= 1`.
# - File adds a check that raises ZeroDivisionError for x == 0 with y < 0;
#   the book has none.


# Python executes this block only when this source file is run directly.
# When pytest imports the file, this block is skipped automatically.
# Documentation: https://docs.python.org/3/library/__main__.html
if __name__ == "__main__":

    # Each tuple is (x, y); all three are added examples.
    for x,y in ((2.0,10),(2.0,-2),(-2.0,3)):
        observed = power(x,y)

        # f-string: each expression in {} is evaluated and inserted.
        # https://docs.python.org/3/reference/lexical_analysis.html#f-strings
        print(f"{x} ** {y} = {observed}")

        # `assert` stops the program with an AssertionError if the condition
        # is false. Python's `**` is used only to check the answer. Comparing
        # floats with == is safe here because these are exact powers of two;
        # in general math.isclose() is preferred for floats.
        # These are quick smoke checks; pytest does the thorough testing.
        assert observed == x**y
