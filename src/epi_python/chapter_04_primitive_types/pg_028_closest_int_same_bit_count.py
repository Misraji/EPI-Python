"""EPI Python — Exercise 4.4: Find a Closest Integer with the Same Weight

Chapter 4: Primitive Types
Textbook: pages 28–29 (printed page numbers; the problem starts at the bottom
of 28, the hint, solution, program and variant are on 29).

PROBLEM (from the textbook)
---------------------------
Define the weight of a nonnegative integer x to be the number of bits that
are set to 1 in its binary representation. For example, since 92 in base-2
equals (1011100)_2, the weight of 92 is 4.

Write a program which takes as input a nonnegative integer x and returns a
number y which is not equal to x, but has the same weight as x and their
difference, |y - x|, is as small as possible. You can assume x is not 0, or
all 1s. For example, if x = 6, you should return 5. You can assume the
integer fits in 64 bits.

HINT (from the textbook)
------------------------
Start with the least significant bit.

SOLUTION DEVELOPMENT (following the textbook)
---------------------------------------------
Brute force: try x - 1, x + 1, x - 2, x + 2, ... and stop at the first value
with the same weight as x. This can be very slow. Book example: x = 2**3 = 8
has weight 1, and only powers of 2 have weight 1, so the search tries
7, 9, 6, 10, 5, 11, 4 and stops at 4. It examines 2**(3-1) - 1 numbers
below 8 (7, 6, 5, then 4 which succeeds) and 2**(3-1) - 1 numbers above 8
(9, 10, 11). The same happens in general: for x = 2**30 the nearest power of
two is 2**29, so the weights of all integers between 2**29 and 2**30, and
between 2**30 and 2**30 + 2**29 - 1, are computed: over a billion integers.

A tempting heuristic: swap the LSB with the rightmost bit that differs from
it. This works for some inputs, e.g. (10)_2 gives (01)_2, the closest
possible. But it fails in general: for (111)_2 = 7 it gives (1110)_2 = 14,
while (1011)_2 = 11 has the same weight and is closer to 7.

The correct approach comes from a little math. If we flip the bit at index
k1 and the bit at index k2, with k1 > k2, the result differs from the
original by 2**k1 - 2**k2 in absolute value. To make that small, k1 should
be as small as possible and k2 as close to k1 as possible. To keep the
weight unchanged the two bits must differ (otherwise both flips go the same
way and change the count of 1s). So the smallest usable k1 is the rightmost
bit that differs from the LSB, and k2 is the bit right next to it. In short:
swap the two rightmost consecutive bits that differ.

The book gives one program, implemented below as
`closest_int_same_bit_count`.

ADDITIONAL EXAMPLES (added for learning; not printed in this exercise)
---------------------------------------------------------------------
(using an 8-bit width, as in the `__main__` block)
    x = 6  = 0b0110 -> 5  = 0b0101  (the book's example)
    x = 7  = 0b0111 -> 11 = 0b1011  (the case where the heuristic fails)
    x = 8  = 0b1000 -> 4  = 0b0100
    x = 10 = 0b1010 -> 9  = 0b1001
"""

# This file has no import statements: it uses only built-in operators,
# range() and the built-in ValueError exception.


# Type hints (`x: int`, `-> int`) document intended types; Python does not
# enforce them. `width: int = 64` is a parameter with a default value: a
# caller may omit it (64 bits, the book's NUM_UNSIGNED_BITS) or pass another
# width, as the `__main__` block does with 8.
def closest_int_same_bit_count(x: int, width: int = 64) -> int:
    """Swap the lowest pair of adjacent unequal bits (textbook implementation).

    Raises ValueError when no such pair exists within `width` bits, i.e. all
    the examined bits are 0 or all are 1.
    """

    # range(width - 1) yields 0, 1, ..., width - 2, so `index + 1` never
    # goes past the top bit of the word.
    for index in range(width - 1):

        # `x >> index` moves bit `index` to position 0 and `& 1` isolates it
        # (0 or 1); the same is done for the neighbouring bit `index + 1`.
        # Scanning from index 0 upward finds the RIGHTMOST pair that differs.
        if ((x >> index) & 1) != ((x >> (index + 1)) & 1):

            # `1 << n` is a mask with only bit n set; `|` combines the two
            # masks. XOR with the mask flips both bits. Because the bits
            # differ, flipping both is a swap: the number of 1s (the weight)
            # stays the same. (Book comment: "Swaps bit-i and bit-(i + 1).")
            mask = (1 << index) | (1 << (index + 1))
            return x ^ mask

    # Book comment: "Raise error if all bits of x are 0 or 1."
    # `raise` stops the function with an exception; ValueError is the
    # built-in exception for a value the function cannot handle.
    # https://docs.python.org/3/library/exceptions.html#ValueError
    raise ValueError("No distinct number of this width has the same popcount")


# TEXTBOOK POST-SOLUTION DISCUSSION (page 29)
# -------------------------------------------
# The time complexity is O(n), where n is the integer width.
#
# VARIANTS
# --------
# Solve the same problem in O(1) time and space.
# (stated in the book; no solution given)


# TEXTBOOK CODE COMPARISON
# ------------------------
# - Book: `def closest_int_same_bit_count(x)` with a local constant
#   `NUM_UNSIGNED_BITS = 64`; file: adds a parameter `width: int = 64` in
#   place of that constant, plus type hints.
# - Loop variable renamed from `i` to `index`; the book's test
#   `(x >> i) & 1 != (x >> (i + 1)) & 1` gains parentheses around each side
#   (same meaning in Python, where `&` binds tighter than `!=`).
# - Book flips in place with `x ^= (1 << i) | (1 << (i + 1))` then
#   `return x`; file builds a local `mask` and returns `x ^ mask`.
# - Book's error message is 'All bits are 0 or 1'; file's message is
#   "No distinct number of this width has the same popcount".


# Python executes this block only when this source file is run directly.
# When pytest imports the file, this block is skipped automatically.
# Documentation: https://docs.python.org/3/library/__main__.html
if __name__ == "__main__":

    # Each tuple is (number, expected_result). 6 -> 5 is the book's example;
    # 7 -> 11 is the input the book uses to show the heuristic failing; the
    # rest are added. All are run with an 8-bit width (second argument).
    for number, expected in ((6,5),(7,11),(8,4),(10,9)):
        observed = closest_int_same_bit_count(number,8)

        # f-string: each expression in {} is evaluated and inserted.
        # https://docs.python.org/3/reference/lexical_analysis.html#f-strings
        print(f"closest same-weight integer to {number}: {observed}")

        # `assert` stops the program with an AssertionError if the condition
        # is false. These are quick smoke checks; pytest does the thorough
        # testing in the separate tests/ folder.
        assert observed == expected
