"""EPI Python — Exercise 4.5: Compute x × y Without Arithmetical Operators

Chapter 4: Primitive Types
Textbook: pages 29–31 (printed page numbers; the problem starts at the
bottom of 29, the solution and program are on 30, and the complexity
analysis is at the top of 31).

PROBLEM (from the textbook)
---------------------------
Sometimes the processors used in ultra low-power devices such as hearing
aids do not have dedicated hardware for performing multiplication. A program
that needs to perform multiplication must do so explicitly using lower-level
primitives.

Write a program that multiplies two nonnegative integers. The only operators
you are allowed to use are
    - assignment,
    - the bitwise operators >>, <<, |, &, ~, ^ and
    - equality checks and Boolean combinations thereof.
You may use loops and functions that you write yourself. These constraints
imply, for example, that you cannot use increment or decrement, or test if
x < y.

HINT (from the textbook)
------------------------
Add using bitwise operations; multiply using shift-and-add.

SOLUTION DEVELOPMENT (following the textbook)
---------------------------------------------
Brute force: start the result at 0 and add x to it y times. For 5 x 3 that
means 0 + 5, 5 + 5, 10 + 5. This can take O(2**n) time, where n is the
number of bits in the input, and it still does not say how to add without an
add instruction.

Grade-school multiplication uses shift-and-add rather than repeated
addition, and the same works in binary: start the result at 0 and walk
through the bits of x; whenever bit k of x is 1, add 2**k * y to the result.
2**k * y is just y shifted left by k places.

Addition must also be built by hand: apply grade-school addition to binary,
computing the sum one bit at a time and "rippling" the carry along.

Book's worked multiplication, 13 = (1101)_2 times 9 = (1001)_2:
- Bit 0 of 13 is 1, so the result becomes (1001)_2.
- Bit 1 is 0, so nothing is added.
- Bit 2 is 1: shift (1001)_2 left by 2 to get (100100)_2 and add it,
  giving (101101)_2.
- Bit 3 is 1: shift (1001)_2 left by 3 to get (1001000)_2 and add it,
  giving (1110101)_2 = 117.

Book's worked addition, (101101)_2 + (1001000)_2, bit by bit from the LSB:
- bit 0: exactly one operand bit is 1, so the sum bit is 1;
- bit 1: both operand bits are 0, so the sum bit is 0;
- bit 2: exactly one operand bit is 1, so the sum bit is 1;
- bit 3: both operand bits are 1, so the sum bit is 0 and a 1 is carried;
- bit 4: carry-in is 1 and both operand bits are 0, so the sum bit is 1;
- the remaining bits are handled the same way.

The book's program `multiply(x, y)` contains a nested ripple-carry `add`.
In this file `multiply` is the shift-and-add loop, and the addition is done
by `add_bits`, which uses a different (carry-propagation) bitwise method
from the book's ripple-carry `add`; see TEXTBOOK CODE COMPARISON.

ADDITIONAL EXAMPLES (added for learning; not printed in this exercise)
---------------------------------------------------------------------
    multiply(7, 6)  -> 42
    multiply(0, 5)  -> 0   (x has no 1-bits, so nothing is ever added)
(13 x 9 = 117 in the `__main__` block is the book's example.)
"""

# This file has no import statements: it uses only built-in operators.


# Type hints (`a: int`, `-> int`) document intended types; Python does not
# enforce them at runtime.
def add_bits(a: int, b: int) -> int:
    """Add unsigned integers without Python's `+` operator.

    Added in this repository in place of the book's nested `add`; it is a
    different bitwise addition method (see TEXTBOOK CODE COMPARISON).
    """

    # Loop until there is no carry left to add in.
    while b:

        # `a ^ b` (XOR) adds the bits in each position while ignoring carries
        # (1+0 -> 1, 1+1 -> 0). `a & b` marks the positions where both bits
        # are 1, i.e. where a carry is produced, and `<< 1` moves each carry
        # one place left, where it must be added next.
        # `a, b = ..., ...` is simultaneous assignment: both right-hand values
        # are computed from the OLD a and b before either name is updated.
        # Python ints are unbounded, so for nonnegative inputs the carries
        # eventually run out and the loop ends.
        a, b = a ^ b, (a & b) << 1
    return a


def multiply(x: int, y: int) -> int:
    """Shift-and-add multiplication (textbook's `multiply` outer loop).

    Uses `add_bits` instead of the book's nested `add`.
    """

    # Input check added in this repository. Note that `<` is one of the
    # operators the problem statement forbids; it is used here only to
    # validate arguments, not in the multiplication itself.
    if x < 0 or y < 0:

        # ValueError is the built-in exception for an unacceptable value.
        # https://docs.python.org/3/library/exceptions.html#ValueError
        raise ValueError("Expected nonnegative integers")
    result = 0

    # Examines each bit of x (book comment). A nonzero int is truthy, so the
    # loop ends once every 1-bit of x has been shifted out.
    while x:

        # `x & 1` is the current lowest bit of x, i.e. bit k of the original
        # x. When it is 1, add 2**k * y, which is the current value of y
        # (y has been shifted left k times so far).
        if x & 1:
            result = add_bits(result, y)

        # Move to the next bit of x (`>>= 1`) and double y (`<<= 1`), so
        # that y always equals 2**k times the original y.
        x >>= 1
        y <<= 1
    return result


# TEXTBOOK POST-SOLUTION DISCUSSION (page 31)
# -------------------------------------------
# Addition takes O(n) time, where n is the number of bits needed to
# represent the operands. Multiplication performs n additions, so the total
# time complexity is O(n**2).
#
# VARIANTS
# --------
# The book gives no variants for this exercise.


# TEXTBOOK CODE COMPARISON
# ------------------------
# - Book: one function `def multiply(x, y)` with a nested `def add(a, b)`.
#   File: two top-level functions, `add_bits(a: int, b: int) -> int` and
#   `multiply(x: int, y: int) -> int`, with type hints.
# - Different addition algorithm: the book's `add` is a ripple-carry adder
#   that walks a one-bit mask `k` across the operands, computing
#   `carryout = (ak & bk) | (ak & carryin) | (bk & carryin)` and
#   `running_sum |= ak ^ bk ^ carryin`, with variables running_sum,
#   carryin, k, temp_a, temp_b, and returns `running_sum | carryin`. The
#   file's `add_bits` instead repeats `a, b = a ^ b, (a & b) << 1` until no
#   carry remains. Both are bitwise-only, but the book's listing is not
#   present in the file.
# - Book's multiply variable is `running_sum`; file uses `result`. Book
#   updates with `x, y = x >> 1, y << 1`; file uses two statements
#   `x >>= 1` and `y <<= 1` (same effect).
# - File adds a negative-input check raising ValueError (book has none);
#   that check uses `<`, which the problem's rules disallow.


# Python executes this block only when this source file is run directly.
# When pytest imports the file, this block is skipped automatically.
# Documentation: https://docs.python.org/3/library/__main__.html
if __name__ == "__main__":

    # Each tuple is (x, y). (13, 9) is the book's worked example; (7, 6)
    # and (0, 5) are added.
    for x,y in ((7,6),(13,9),(0,5)):
        observed = multiply(x,y)

        # f-string: each expression in {} is evaluated and inserted.
        # https://docs.python.org/3/reference/lexical_analysis.html#f-strings
        print(f"{x} * {y} = {observed}")

        # `assert` stops the program with an AssertionError if the condition
        # is false. Here Python's own `*` is used only to check the answer.
        # These are quick smoke checks; pytest does the thorough testing.
        assert observed == x*y
