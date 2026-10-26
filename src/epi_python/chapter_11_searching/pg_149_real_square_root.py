"""EPI Python — Exercise 11.5: Compute the Real Square Root

Chapter 11: Searching
Textbook: pages 149–150 (printed page numbers; problem, solution and the
start of the program on 149, end of program, complexity and variant on 150).

PROBLEM (from the textbook)
---------------------------
"Square root computations can be implemented using sophisticated numerical
techniques involving iterative methods and logarithms. However, if you were
asked to implement a square root function, you would not be expected to
know these techniques.

Implement a function which takes as input a floating point value and
returns its square root."

HINT (from the textbook)
------------------------
"Iteratively compute a sequence of intervals, each contained in the
previous interval, that contain the result."

SOLUTION DEVELOPMENT (following the textbook)
---------------------------------------------
Let x be the input. One option is two-phase: first find an integer n with
n^2 <= x and (n + 1)^2 > x (for example with the integer square root method
of Solution 11.4), then search inside [n, n + 1] until the desired
tolerance is reached.

The integer phase is unnecessary: binary search can be done directly on
real numbers. If some number is too big to be the square root of x, every
larger number can be discarded; if it is too small, every smaller number
can be discarded.

Choosing the starting interval:
  * The obvious bounds, 0 and the largest representable float, do not work
    well with finite precision arithmetic: squaring the very first midpoint
    already overflows.
  * [0, x] is also wrong in general, because the square root can be larger
    than x, e.g. sqrt(1/4) = 1/2.
  * If x >= 1.0, the bounds can be tightened to [1.0, x], since
    1.0 <= x implies x <= x^2.
  * If x < 1.0, use [x, 1.0], since then the square root is larger than x
    but smaller than 1.0.

The book stresses that this is a fundamental difference from the integer
square root problem (11.4), where the starting interval [0, x] always
contains the answer.

The implementation below, square_root, follows this idea (with a different
stopping test and extra special cases; see the comparison section).

ADDITIONAL EXAMPLES (added for learning; not printed in this exercise)
---------------------------------------------------------------------
    x=2.0   -> approximately 1.41421356...
    x=0.25  -> approximately 0.5 (input below 1.0: answer is larger than x)
    x=100.0 -> approximately 10.0
"""


def square_root(x: float, tolerance: float = 1e-12) -> float:
    """Approximate real sqrt(x) by binary search over a range that brackets it.

    This is the textbook's real-valued square_root (the only implementation
    given), adapted with a `tolerance` parameter and a relative stopping test
    instead of the book's `math.isclose` loop condition.

    Type hints: `x: float`, `tolerance: float` and `-> float` document the
    expected types; Python does not enforce them. `tolerance: float = 1e-12`
    is a parameter with a default value, so callers may omit it. `1e-12` is
    scientific notation for 0.000000000001.
    """

    # `raise ValueError(...)` stops the function with an exception; a
    # negative number has no real square root. (Guard added in this file.)
    # ValueError: https://docs.python.org/3/library/exceptions.html#ValueError
    if x < 0:
        raise ValueError("Square root of negative real is undefined")

    # 0 and 1 are their own square roots; returning them directly also
    # avoids searching an interval of zero width. (Added in this file.)
    if x == 0 or x == 1:
        return x

    # Conditional expression `A if condition else B` picks one of two
    # tuples, which tuple unpacking then assigns to left and right. This is
    # the book's choice of bracket: [x, 1.0] when x < 1, else [1.0, x].
    left, right = (x, 1.0) if x < 1 else (1.0, x)

    # Keep bisecting while the bracket is wider than the tolerance. The
    # width is compared with `tolerance * max(1.0, right)`: max() returns
    # the larger argument, so for large x the allowed width grows with the
    # size of the numbers (a relative tolerance), while for small x it is
    # an absolute tolerance. Floats have limited precision, so an absolute
    # 1e-12 gap could be impossible to reach for very large x.
    # max: https://docs.python.org/3/library/functions.html#max
    while right - left > tolerance * max(1.0, right):

        # `/` is true division and always produces a float.
        middle = (left + right) / 2

        # middle is too big to be the square root: shrink from the right.
        if middle * middle > x:
            right = middle

        # middle is not too big: shrink from the left.
        else:
            left = middle

    # Return the centre of the final, very narrow bracket.
    return (left + right) / 2


# TEXTBOOK POST-SOLUTION DISCUSSION (page 150)
# --------------------------------------------
# Time complexity: O(log(x / s)), where s is the tolerance -- the bracket
# starts with width about x and is halved until it is about s wide.
#
# VARIANTS
# --------
# Variant (stated in the book; no solution given): Given two positive
#   floating point numbers x and y, how would you compute x / y to within a
#   specified tolerance epsilon if the division operator cannot be used?
#   You cannot use any library functions, such as log and exp; addition and
#   multiplication are acceptable.


# TEXTBOOK CODE COMPARISON
# ------------------------
# Book: `def square_root(x):` with comments "Decides the search range
#   according to x's value relative to 1.0." and "Keeps searching as long as
#   left != right."; it loops `while not math.isclose(left, right):`, uses
#   `mid = 0.5 * (left + right)` and a `mid_squared` variable, and
#   `return left`. The book therefore relies on `import math`.
# File: no `math` import; signature adds type hints and a
#   `tolerance: float = 1e-12` parameter; adds a ValueError guard for
#   negative x and an early return for x == 0 or x == 1 (neither in the
#   book); the loop condition is the custom relative test
#   `right - left > tolerance * max(1.0, right)` instead of
#   `math.isclose`; `mid` renamed `middle` and computed as
#   `(left + right) / 2`; no `mid_squared` variable; returns the midpoint
#   `(left + right) / 2` rather than `left`. The bracket choice
#   `(x, 1.0) if x < 1 else (1.0, x)` matches the book (`x < 1` vs
#   `x < 1.0`).


# Python executes this block only when this source file is run directly.
# When pytest imports the file, this block is skipped automatically.
# Documentation: https://docs.python.org/3/library/__main__.html
if __name__ == "__main__":

    # Try inputs above and below 1.0. `2.` is a float literal (same as 2.0).
    # Floating-point results are approximate, so instead of testing for
    # equality the check squares the answer and requires it to be within
    # 1e-7 of x. abs() gives the absolute value of the error, and `**` is
    # exponentiation.
    #
    # `assert` stops the program with an AssertionError if the condition is
    # false. These are quick smoke checks; pytest provides the more
    # thorough automated verification.
    for x in (2., 0.25, 100.):
        approximation = square_root(x)
        print("sqrt:", x, approximation)
        assert abs(approximation ** 2 - x) < 1e-7
