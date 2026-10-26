"""EPI Python — Exercise 4.6: Compute x/y

Chapter 4: Primitive Types
Textbook: page 31 (printed page number; problem, solution, program and
complexity all appear on 31).

PROBLEM (from the textbook)
---------------------------
Given two positive integers, compute their quotient, using only the
addition, subtraction, and shifting operators.

HINT (from the textbook)
------------------------
Relate x/y to (x - y)/y.

SOLUTION DEVELOPMENT (following the textbook)
---------------------------------------------
Brute force: keep subtracting y from x until what is left is less than y.
The number of subtractions is the quotient x/y, and what is left is the
remainder. This is very slow: for y = 1 and x = 2**31 - 1 it needs
2**31 - 1 iterations.

Better: do more work per iteration. Find the largest k with 2**k * y <= x,
subtract 2**k * y from x, and add 2**k to the quotient. Book example:
x = (1011)_2 = 11 and y = (10)_2 = 2. Then k = 2, because 2 * 2**2 <= 11
but 2 * 2**3 > 11. Subtract (1000)_2 from (1011)_2 to get (11)_2, add
2**2 = (100)_2 to the quotient, and continue with x = (11)_2.

Why 2**k * y: it is cheap to compute by shifting, and x is at least halved
each iteration. If the quotient needs n bits, there are O(n) iterations. If
the largest k is found each time by trying k = 0, 1, 2, ..., each iteration
costs O(n), for O(n**2) overall.

Improvement: the largest k only ever decreases. So after finding the first
k with 2**k * y <= x, later iterations test 2**(k-1) * y, 2**(k-2) * y,
2**(k-3) * y, ... against x, instead of starting again from 2**0 * y.

Continuing the example: after the quotient becomes (100)_2, x is (11)_2.
The largest k with 2**k * y <= (11)_2 is 0, so add 2**0 = (1)_2, making the
quotient (101)_2, and x becomes (11)_2 - (10)_2 = (1)_2. Since (1)_2 < y,
stop: the quotient is (101)_2 = 5 and the remainder is (1)_2.

The book's program `divide(x, y)` implements the improved, decreasing-k
version. This file's `divide` instead implements the earlier approach that
searches upward for the largest k in each iteration (see TEXTBOOK CODE
COMPARISON).

ADDITIONAL EXAMPLES (added for learning; not printed in this exercise)
---------------------------------------------------------------------
    divide(17, 3) -> 5
    divide(6, 3)  -> 2
    divide(0, 1)  -> 0  (x = 0 is accepted here, though the book says
                         "positive integers")
(divide(11, 2) -> 5 in the `__main__` block is the book's example.)
"""

# This file has no import statements: it uses only built-in operators.


# Type hints (`x: int`, `-> int`) document intended types; Python does not
# enforce them at runtime.
def divide(x: int, y: int) -> int:
    """Unsigned binary long division using shifts and subtraction.

    Repository version: re-finds the largest shifted divisor from y upward
    on every outer iteration (the book's O(n**2) idea), rather than the
    book's printed decreasing-power program.
    """

    # Input check added in this repository: the book assumes positive inputs.
    if x < 0 or y <= 0:

        # ValueError is the built-in exception for an unacceptable value.
        # https://docs.python.org/3/library/exceptions.html#ValueError
        raise ValueError("Expected x >= 0 and y > 0")
    quotient = 0

    # Keep going while at least one more copy of y fits in the remainder x.
    while x >= y:

        # Simultaneous assignment: multiple = y (that is 2**0 * y) and
        # factor = 1 (2**0) at the same time.
        multiple, factor = y, 1

        # `multiple << 1` doubles `multiple` (shift left by one bit). Keep
        # doubling while the doubled value still fits in x; at the end
        # `multiple` is 2**k * y for the largest such k, and `factor` is 2**k.
        while (multiple << 1) <= x:
            multiple <<= 1
            factor <<= 1

        # Add 2**k to the quotient and remove 2**k * y from the remainder.
        quotient += factor
        x -= multiple
    return quotient


# TEXTBOOK POST-SOLUTION DISCUSSION (page 31)
# -------------------------------------------
# The book's program is grade-school long division applied to binary
# numbers: each iteration handles one more bit. Assuming each shift and add
# takes O(1) time, its time complexity is O(n).
# (The file's upward search re-scans k each iteration, which is the O(n**2)
# version the book discusses before its improvement.)
#
# VARIANTS
# --------
# The book gives no variants for this exercise.


# TEXTBOOK CODE COMPARISON
# ------------------------
# - Book: `def divide(x, y)`; file: `divide(x: int, y: int) -> int`.
# - Different structure. Book: `result, power = 0, 32`,
#   `y_power = y << power`; while `x >= y`, an inner loop shifts `y_power`
#   right and decrements `power` while `y_power > x`, then
#   `result += 1 << power` and `x -= y_power`. The power only decreases
#   across iterations (O(n)).
#   File: variables `quotient`, `multiple`, `factor`; each outer iteration
#   restarts from `multiple, factor = y, 1` and shifts LEFT while
#   `(multiple << 1) <= x` (the O(n**2) approach). The book's starting
#   power of 32 (which assumes the quotient fits in 32 bits) does not appear.
# - File adds an input check raising ValueError for x < 0 or y <= 0.


# Python executes this block only when this source file is run directly.
# When pytest imports the file, this block is skipped automatically.
# Documentation: https://docs.python.org/3/library/__main__.html
if __name__ == "__main__":

    # Each tuple is (x, y). (11, 2) is the book's example; the rest are added.
    for x,y in ((11,2),(17,3),(6,3),(0,1)):
        observed = divide(x,y)

        # f-string: each expression in {} is evaluated and inserted.
        # https://docs.python.org/3/reference/lexical_analysis.html#f-strings
        print(f"{x} // {y} = {observed}")

        # `assert` stops the program with an AssertionError if the condition
        # is false. `//` is Python's floor division, used only to check the
        # answer. These are quick smoke checks; pytest does thorough testing.
        assert observed == x//y
