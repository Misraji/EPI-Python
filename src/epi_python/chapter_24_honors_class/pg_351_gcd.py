"""EPI Python — Exercise 24.1: Compute the Greatest Common Divisor

Chapter 24: Honors Class
Textbook: pages 351–352 (printed page numbers; problem and solution start on
351, the program and its analysis are on 352).

PROBLEM (from the textbook)
---------------------------
The greatest common divisor (GCD) of nonnegative integers x and y is the
largest integer d such that d divides x evenly, and d divides y evenly,
i.e., x mod d = 0 and y mod d = 0. (When both x and y are 0, take their GCD
to be 0.)

Design an efficient algorithm for computing the GCD of two nonnegative
integers without using multiplication, division or the modulus operators.

HINT (from the textbook)
------------------------
Use case analysis: both even; both odd; one even and one odd.

SOLUTION DEVELOPMENT (following the textbook)
---------------------------------------------
Straightforward recursion: if x equals y, the GCD is x. Otherwise, assuming
(without loss of generality) x > y, GCD(x, y) equals GCD(x - y, y). This
uses no multiplication, division or modulus, but can be extremely slow: for
x = 2^n and y = 2 it makes 2^(n-1) recursive calls.

Repeated subtraction is really division, so when x > y one could use
GCD(x, y) = GCD(y, x mod y) (Euclid's algorithm). That is much faster, but
it relies on integer division/modulus, which the problem forbids.

The textbook's fast solution is also recursive but avoids general
multiplication and division by analysing which of the two numbers are even.

Worked example from the book, GCD(24, 300):
  * Both are even, so the result is 2 x GCD(12, 150). Halving is a right
    shift by 1, so no general division is needed.
  * 12 and 150 are both even: GCD(12, 150) = 2 x GCD(6, 75).
  * 75 is odd, so 2 cannot divide it; GCD(6, 75) = GCD(3, 75).
  * Both odd: GCD(3, 75) = GCD(3, 75 - 3) = GCD(3, 72).
  * Applying the same rules: GCD(3, 72) = GCD(3, 36) = GCD(3, 18) =
    GCD(3, 9) = GCD(3, 6) = GCD(3, 3) = 3.
  * Hence GCD(24, 300) = 2 x 2 x 3 = 12.

General rules:
  * Base cases: equal arguments give that value (GCD(12, 12) = 12); if one
    argument is zero the other is the GCD (GCD(0, 6) = 6).
  * Both even: compute the GCD of the halves and double it.
  * Exactly one even: halve the even one and recurse on the new pair.
  * Both odd: subtract the smaller from the larger and recurse.
  * Doubling is a single left shift; halving is a single right shift.

The book prints one program, `gcd(x, y)`, implementing these rules. NOTE:
the function in this file is NOT that program; it implements Euclid's
remainder algorithm (see TEXTBOOK CODE COMPARISON below).

ADDITIONAL EXAMPLES (added for learning; not printed in this exercise)
---------------------------------------------------------------------
    gcd(0, 0)    -> 0   (the book's convention)
    gcd(20, 8)   -> 4
    gcd(17, 13)  -> 1   (coprime)
    gcd(-12, 18) -> 6   (this file's code accepts negatives via abs())
    gcd(100, 10) -> 10
"""


def gcd(x: int, y: int) -> int:
    """Greatest common divisor using the Euclidean remainder recurrence.

    This is NOT the textbook's printed implementation (which is the
    shift-based binary GCD described in the module docstring). It is the
    Euclid's-algorithm alternative the book mentions and rules out because
    it uses the modulus operator.

    Type hints: `x: int, y: int` and `-> int` are annotations that document
    the expected argument and return types. Python does not enforce them at
    run time; they are read by people, editors and type checkers.
    """

    # abs(n) is a built-in returning the absolute value of a number.
    # The book's problem only considers nonnegative inputs; this file's code
    # additionally accepts negative integers by discarding their signs
    # (the GCD of -12 and 18 is defined here as 6).
    #
    # `a, b = expr1, expr2` is tuple packing/unpacking: both right-hand
    # expressions are evaluated first, then assigned together.
    x, y = abs(x), abs(y)

    # `while y:` uses truthiness: an int is false exactly when it is 0.
    # So the loop runs until the remainder becomes zero.
    while y:

        # Simultaneous assignment again: the old x and y are used on the
        # right-hand side, so no temporary variable is needed.
        # `x % y` is the remainder (modulus) operator. For nonnegative
        # operands it gives the remainder of integer division. The book
        # observes GCD(x, y) = GCD(y, x mod y), which this line applies.
        # Each step shrinks the pair quickly, but note the problem statement
        # explicitly disallows the modulus operator.
        x, y = y, x % y

    # When y reaches 0, GCD(x, 0) = x. If both inputs were 0 the loop never
    # runs and 0 is returned, matching the book's convention.
    return x


# TEXTBOOK POST-SOLUTION DISCUSSION (page 352)
# --------------------------------------------
# The final rule (both odd: subtract the smaller from the larger) produces a
# pair with one even and one odd number, so the next call halves a number.
# Therefore, in every two calls the combined bit length of the two numbers
# drops by at least one. The time complexity is proportional to the total
# number of bits in x and y, i.e., O(log x + log y).
#
# (Remark for this file, not from the book: Euclid's remainder algorithm used
# below also takes O(log(min(x, y))) iterations, but each uses a modulus.)
#
# VARIANTS
# The book gives no variants for this exercise.


# TEXTBOOK CODE COMPARISON
# ------------------------
# book: `def gcd(x, y)` — recursive binary GCD with no multiplication,
#   division or modulus: if x > y swap via `gcd(y, x)`; if x == 0 return y;
#   both even -> `gcd(x >> 1, y >> 1) << 1`; x even, y odd -> `gcd(x >> 1, y)`;
#   x odd, y even -> `gcd(x, y >> 1)`; both odd -> `gcd(x, y - x)`. Parity is
#   tested with `& 1`.
# file: `def gcd(x: int, y: int) -> int` — same name and parameter names,
#   type hints added, but a DIFFERENT ALGORITHM: an iterative Euclidean loop
#   `x, y = y, x % y`, which uses the modulus operator the problem forbids.
#   The file also applies abs() to accept negative inputs (the book assumes
#   nonnegative). The book's binary-GCD implementation is missing from the
#   file. Results agree for nonnegative inputs.


# Python executes this block only when this source file is run directly.
# When pytest imports the file, this block is skipped automatically.
# Documentation: https://docs.python.org/3/library/__main__.html
if __name__ == "__main__":
    # Run a few self-contained examples before exploring the pytest suite.
    # They show the both-zero convention, an ordinary pair, a coprime pair,
    # a negative input (accepted by this file's abs() call) and a pair where
    # one number divides the other.
    #
    # print() with several arguments separates them with a space.
    # `assert` stops the program with an AssertionError if the condition is
    # false; these are quick smoke checks, while the separate tests/ folder
    # holds the thorough pytest suite.
    observed = gcd(0, 0)
    print("gcd:", observed)
    assert observed == 0
    observed = gcd(20, 8)
    print("gcd:", observed)
    assert observed == 4
    observed = gcd(17, 13)
    print("gcd:", observed)
    assert observed == 1
    observed = gcd(-12, 18)
    print("gcd:", observed)
    assert observed == 6
    observed = gcd(100, 10)
    print("gcd:", observed)
    assert observed == 10
