"""EPI Python — Exercise 4.3: Reverse Bits

Chapter 4: Primitive Types
Textbook: page 28 (printed page number; problem, solution, program and
complexity all appear on 28).

PROBLEM (from the textbook)
---------------------------
Write a program that takes a 64-bit unsigned integer and returns the 64-bit
unsigned integer consisting of the bits of the input in reverse order. For
example, if the input is (1110000000000001), the output should be
(1000000000000111).

HINT (from the textbook)
------------------------
Use a lookup table.

SOLUTION DEVELOPMENT (following the textbook)
---------------------------------------------
If the reversal is needed only once, a simple brute force works: go through
the 32 least significant bits and swap each one with its mirror-image most
significant bit, e.g. using the bit-swapping method of Solution 4.2.

If reversals are needed many times, look at the structure of the input with
a cache in mind. View the 64-bit input as four 16-bit integers y3, y2, y1,
y0, with y3 holding the most significant bits. The 16 least significant
bits of the reversed result come from y3, and they appear in the reverse of
their order in y3. For example, if y3 is (1110000000000001), the 16 LSBs of
the result are (1000000000000111).

As with parity (Problem 4.1), build an array-based lookup table A such that
for every 16-bit integer y, A[y] is the bit-reversal of y. The reverse of x
is then: reverse(y0) in the most significant positions, followed by
reverse(y1), then reverse(y2), then reverse(y3) in the least significant
positions.

Book's illustration with 8-bit integers and 2-bit keys: the table is
rev = ((00), (10), (01), (11)). For the input (10010011), the reverse is
rev(11), rev(00), rev(01), rev(10) placed side by side, i.e. (11001001).

Implementations in this file:
- `reverse_bits` is the textbook's lookup-table program (four 16-bit
  lookups), used when width is 64.
- `reverse_bits_brute_force` is an added slow method (see the comparison
  section); it is NOT the book's swap-based brute force.
- `_build_reverse_16_bit_table` builds the table the book calls
  PRECOMPUTED_REVERSE, which the book does not show being built.

ADDITIONAL EXAMPLES (added for learning; not printed in this exercise)
---------------------------------------------------------------------
    x = 0, width 8                     -> 0
    x = 1, width 8                     -> 0x80 (bit 0 moves to bit 7)
    x = 0b1110_0000_0000_0001, width 16 -> 0b1000_0000_0000_0111
                                          (the book's 16-bit pattern)
    x = 0xF0F0_0F0F_1234_5678, width 64 -> checked against brute force
"""

# This file has no import statements: it uses only built-in operators and
# built-in functions.

# A 16-bit mask: `1 << 16` is 2**16, and subtracting 1 gives sixteen 1-bits
# (0xFFFF, the book's BIT_MASK). The leading underscore is a convention for
# "internal to this module"; Python does not enforce it.
_MASK_16 = (1 << 16) - 1


# Type hints (`x: int`, `-> int`) document intended types; Python does not
# enforce them. `width: int = 64` has a default value, so callers may omit it.
def reverse_bits_brute_force(x: int, width: int = 64) -> int:
    """Reverse a word one low bit at a time; O(width) time, O(1) space.

    Added in this repository (not a textbook listing).
    """

    # Reject widths and values that are not an unsigned `width`-bit integer.
    # `0 <= x < limit` is a chained comparison: both tests must hold.
    if width <= 0 or not 0 <= x < (1 << width):

        # ValueError is the built-in exception for an unacceptable value.
        # https://docs.python.org/3/library/exceptions.html#ValueError
        raise ValueError("Expected an unsigned integer fitting the bit width")
    result = 0

    # `_` is the conventional name for a loop variable that is never used.
    for _ in range(width):

        # `result << 1` shifts the output left, making room at bit 0.
        # `x & 1` is the input's current lowest bit; `|` (OR) drops it into
        # that free position. The first bit read from x ends up highest.
        # `x >>= 1` then discards the bit just copied.
        result = (result << 1) | (x & 1)
        x >>= 1
    return result


# `tuple[int, ...]` is a type hint meaning "a tuple of ints of any length".
def _build_reverse_16_bit_table() -> tuple[int, ...]:
    """Cache each possible 16-bit reversal once, at module import.

    Helper added in this repository: the book uses PRECOMPUTED_REVERSE but
    does not print code that builds it.
    """

    # `[0] * n` makes a list of n zeros, one slot per 16-bit value.
    values = [0] * (1 << 16)
    for number in range(1 << 16):
        result = 0
        value = number

        # Same shift-and-OR reversal as above, for exactly 16 bits.
        for _ in range(16):
            result = (result << 1) | (value & 1)
            value >>= 1
        values[number] = result

    # tuple(...) copies the list into an immutable tuple so the shared table
    # cannot be modified by accident.
    return tuple(values)


# `_PRECOMPUTED_REVERSE` is the book's lookup table PRECOMPUTED_REVERSE. It is
# built once, when the module is imported, and shared by every call.
_PRECOMPUTED_REVERSE = _build_reverse_16_bit_table()


def reverse_bits(x: int, width: int = 64) -> int:
    """Four cached 16-bit lookups (textbook implementation for 64-bit words).

    For any other `width`, this repository version falls back to the added
    `reverse_bits_brute_force`.
    """
    if width != 64:
        return reverse_bits_brute_force(x, width)
    if not 0 <= x < (1 << 64):
        raise ValueError("Expected an unsigned 64-bit integer")

    # Each line extracts one 16-bit piece (`>>` moves it to the low end,
    # `& _MASK_16` discards higher bits), reverses it by table lookup, and
    # shifts the reversed piece to its mirror position with `<<`:
    #   y0 (bits 0-15)  -> top    (shift 48)
    #   y1 (bits 16-31) -> shift 32
    #   y2 (bits 32-47) -> shift 16
    #   y3 (bits 48-63) -> bottom (no shift)
    # `|` (bitwise OR) joins the four non-overlapping pieces into one int.
    # Parentheses let the expression span several lines.
    return (
        (_PRECOMPUTED_REVERSE[x & _MASK_16] << 48)
        | (_PRECOMPUTED_REVERSE[(x >> 16) & _MASK_16] << 32)
        | (_PRECOMPUTED_REVERSE[(x >> 32) & _MASK_16] << 16)
        | _PRECOMPUTED_REVERSE[(x >> 48) & _MASK_16]
    )


# TEXTBOOK POST-SOLUTION DISCUSSION (page 28)
# -------------------------------------------
# The time complexity is the same as for Solution 4.1 (parity by lookup
# table): O(n/L) for n-bit integers and L-bit cache keys (here n = 64,
# L = 16, so four lookups), not counting the table's construction.
#
# VARIANTS
# --------
# The book gives no variants for this exercise.


# TEXTBOOK CODE COMPARISON
# ------------------------
# - Book: `def reverse_bits(x)`; file: `reverse_bits(x: int, width: int = 64)`
#   with type hints and an extra `width` parameter. For width != 64 it calls
#   `reverse_bits_brute_force`; for width 64 it validates 0 <= x < 2**64
#   (raising ValueError), which the book does not do.
# - Book uses local constants `MASK_SIZE = 16`, `BIT_MASK = 0xFFFF` and
#   shifts written `3 * MASK_SIZE`, `2 * MASK_SIZE`, `MASK_SIZE`; file uses a
#   module constant `_MASK_16 = (1 << 16) - 1` and literal shifts 48/32/16.
#   Book's last term `(x >> (3 * MASK_SIZE)) & BIT_MASK` keeps the mask; the
#   file also keeps it (`(x >> 48) & _MASK_16`). Same order of pieces.
# - Book's table name `PRECOMPUTED_REVERSE`; file: `_PRECOMPUTED_REVERSE`
#   plus the added builder `_build_reverse_16_bit_table()`.
# - `reverse_bits_brute_force` is not in the book. The book describes (but
#   does not code) a brute force that swaps each of the low 32 bits with its
#   mirror high bit via Solution 4.2; the file's version instead shifts bits
#   one at a time from x into the result.


# Python executes this block only when this source file is run directly.
# When pytest imports the file, this block is skipped automatically.
# Documentation: https://docs.python.org/3/library/__main__.html
if __name__ == "__main__":

    # Each tuple is (x, width). Underscores inside number literals such as
    # 0b1110_0000_0000_0001 are ignored by Python and only aid reading. The
    # 16-bit example is the book's pattern; the others are added.
    for x, width in ((0, 8), (1, 8), (0b1110_0000_0000_0001, 16),
                     (0xF0F0_0F0F_1234_5678, 64)):

        # The brute-force result serves as the expected answer; for width 64
        # this checks the table version against it.
        expected = reverse_bits_brute_force(x, width)
        observed = reverse_bits(x, width)

        # f-string: expressions in {} are evaluated and inserted. The format
        # spec `:#x` prints an int in hexadecimal with a `0x` prefix.
        # https://docs.python.org/3/reference/lexical_analysis.html#f-strings
        print(f"reverse({x:#x}, width={width}) -> {observed:#x}")

        # `assert` stops the program with an AssertionError if the condition
        # is false. These are quick smoke checks; pytest does the thorough
        # testing in the separate tests/ folder.
        assert observed == expected
    print("Both textbook bit-reversal approaches passed.")
