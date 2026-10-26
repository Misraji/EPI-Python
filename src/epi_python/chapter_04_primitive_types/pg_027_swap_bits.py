"""EPI Python — Exercise 4.2: Swap Bits

Chapter 4: Primitive Types
Textbook: pages 27–28 (printed page numbers; the problem and program are on
27, the complexity sentence is at the top of 28).

PROBLEM (from the textbook)
---------------------------
A 64-bit integer can be viewed as an array of 64 bits, with the bit at
index 0 corresponding to the least significant bit (LSB), and the bit at
index 63 corresponding to the most significant bit (MSB). Implement code
that takes as input a 64-bit integer and swaps the bits at indices i and j.
Figure 4.1 illustrates bit swapping for an 8-bit integer.

Figure 4.1 (book's example): the 8-bit integer 73 is the bit array
    MSB 0 1 0 0 1 0 0 1 LSB
(LSB at index 0). Swapping the bits at indices 1 and 6 gives
    MSB 0 0 0 0 1 0 1 1 LSB
which is the integer 11.

HINT (from the textbook)
------------------------
When is the swap necessary?

SOLUTION DEVELOPMENT (following the textbook)
---------------------------------------------
The book opens by recalling bit-manipulation shortcuts from the chapter
introduction: x & (x - 1) clears the lowest set bit of x, and x & ~(x - 1)
extracts the lowest set bit. Its examples:
    16 & (16 - 1) = 0,    11 & (11 - 1) = 10,   20 & (20 - 1) = 16,
    16 & ~(16 - 1) = 16,  11 & ~(11 - 1) = 1,   20 & ~(20 - 1) = 4.

Brute force: use bitmasks to pull out bit i and bit j into local variables,
then write the saved j-th bit into position i and the saved i-th bit into
position j with further masking. This works for swapping anything stored in
an array, not just bits.

Better, because a bit has only two possible values:
1. First test whether the two bits differ.
2. If they are equal, swapping them leaves the integer unchanged, so do
   nothing.
3. If they differ, swapping them is the same as flipping each of them. In
   Figure 4.1 the bits at indices 1 and 6 differ, so flipping both performs
   the swap.

The program uses the standard idioms for testing a bit (shift then AND 1)
and flipping bits (XOR with a mask). The book says the result is slightly
more succinct and efficient than brute force. It is implemented below as
`swap_bits`.

ADDITIONAL EXAMPLES (added for learning; not printed in this exercise)
---------------------------------------------------------------------
    x = 8 = 0b1000, i = 0, j = 3  -> 1 = 0b0001 (bits differ: both flipped)
    x = 9 = 0b1001, i = 0, j = 3  -> 9           (bits equal: no change)
    x = 0,          i = 1, j = 2  -> 0
    x = 1,          i = 0, j = 0  -> 1           (a bit swapped with itself)
"""

# This file has no import statements: it uses only built-in operators.


# Type hints (`x: int`, `-> int`) document the intended types; Python does
# not check or enforce them at runtime.
def swap_bits(x: int, i: int, j: int) -> int:
    """Return x with the bits at positions i and j exchanged.

    This is the textbook's single implementation (the "flip if different"
    method). Python ints are immutable, so a new int is returned.
    """

    # Extract the i-th and j-th bits, and see if they differ (book comment).
    # `x >> i` shifts right by i places, moving bit i to position 0;
    # `& 1` then keeps only that lowest bit, giving 0 or 1.
    if ((x >> i) & 1) != ((x >> j) & 1):

        # i-th and j-th bits differ; swap them by flipping their values
        # (book comment).
        # `1 << i` is an int with only bit i set (a one-bit mask). `|`
        # (bitwise OR) combines the two masks into one with bits i and j set.
        # XOR with 1 flips a bit (1 ^ 1 = 0, 0 ^ 1 = 1) and XOR with 0
        # leaves it alone, so `x ^= mask` flips exactly bits i and j.
        x ^= (1 << i) | (1 << j)
    return x


# TEXTBOOK POST-SOLUTION DISCUSSION (page 28)
# -------------------------------------------
# The time complexity is O(1), independent of the word size.
#
# VARIANTS
# --------
# The book gives no variants for this exercise.


# TEXTBOOK CODE COMPARISON
# ------------------------
# - Book: `def swap_bits(x, i, j)`; file: same name and parameter names, with
#   `: int` / `-> int` type hints added.
# - Book builds a local variable `bit_mask = (1 << i) | (1 << j)` and then
#   does `x ^= bit_mask`; file folds this into one statement
#   `x ^= (1 << i) | (1 << j)` with no `bit_mask` variable.
# - Book's test is `(x >> i) & 1 != (x >> j) & 1`; file adds parentheses
#   around each side. (In Python `&` binds more tightly than `!=`, unlike in
#   C, so both forms mean the same thing; the parentheses only add clarity.)
# - The book's code comments are not present in the file's code; they have
#   been restored above as comments.


# Python executes this block only when this source file is run directly.
# When pytest imports the file, this block is skipped automatically.
# Documentation: https://docs.python.org/3/library/__main__.html
if __name__ == "__main__":

    # Each tuple is (number, i, j, expected_result); these four are the
    # added examples listed in the module docstring. Tuple unpacking in the
    # `for` statement assigns the four items to four names at once.
    for number, i, j, expected in ((8,0,3,1),(9,0,3,9),(0,1,2,0),(1,0,0,1)):
        observed = swap_bits(number,i,j)

        # f-string: each expression in {} is evaluated and its value inserted.
        # https://docs.python.org/3/reference/lexical_analysis.html#f-strings
        print(f"swap_bits({number}, {i}, {j}) = {observed}")

        # `assert` stops the program with an AssertionError if the condition
        # is false. These are quick smoke checks; pytest does the thorough
        # testing in the separate tests/ folder.
        assert observed == expected
