"""EPI Python — Exercise 4.1: Computing the Parity of a Word

Chapter 4: Primitive Types
Textbook: pages 24–27 (printed page numbers; the problem starts on 24, the
solution runs through 26 and the variant is printed at the top of 27).

PROBLEM (from the textbook)
---------------------------
The parity of a binary word is 1 if the number of 1s in the word is odd;
otherwise, it is 0. For example, the parity of 1011 is 1, and the parity of
10001000 is 0. Parity checks are used to detect single bit errors in data
storage and communication. It is fairly straightforward to write code that
computes the parity of a single 64-bit word.

How would you compute the parity of a very large number of 64-bit words?

HINT (from the textbook)
------------------------
Use a lookup table, but don't use 2**64 entries!

SOLUTION DEVELOPMENT (following the textbook)
---------------------------------------------
The book develops four programs, from slowest to fastest.

1. Brute force (implemented below as `parity_brute_force`).
   Examine the word one bit at a time, keeping track of how many 1s have
   been seen. Because only "odd or even" matters, the count can be kept
   modulo 2, i.e. as a single bit that is toggled by each 1. The running
   time is O(n), where n is the word size (64 here).

2. Erase the lowest set bit (implemented as `parity_erase_lowest_set_bit`).
   A trick worth memorising: x & (x - 1) is x with its lowest set bit
   removed. Book example: x = (00101100)_2 gives x - 1 = (00101011)_2, so
   x & (x - 1) = (00101000)_2. Each loop iteration therefore removes exactly
   one 1-bit and flips the result. If k is the number of 1-bits in the word
   (for 10001010, k = 3), the loop runs k times, so the time is O(k). This
   helps the best and average cases. (A footnote adds a second trick:
   x & ~(x - 1) isolates the lowest 1-bit of x, where ~ is bitwise
   complement.)

3. Lookup table (implemented as `parity_lookup_table`).
   When very many parities are needed, two keys to speed are processing
   several bits at once and caching results in an array. Caching the
   parity of every 64-bit value would need 2**64 bits (about two exabytes),
   which is impossible. But parity is associative: the bits can be grouped
   in any way. So split the 64-bit word into four non-overlapping 16-bit
   pieces, look up the parity of each piece, and combine the four results.
   16 is chosen because 2**16 = 65536 entries is small enough to store, and
   because 16 divides 64 evenly (10-bit pieces would make the code messier).

   Book's illustration with a 2-bit table: the cache is (0, 1, 1, 0), the
   parities of 00, 01, 10, 11. To find the parity of (11001010), look up
   the pieces 11, 00, 10, 10, getting 0, 0, 1, 1; the parity of those is 0.
   To fetch the first two bits of (11101010), shift right by 6, giving
   (00000011), a valid index. For the next two bits (10), shift right by 4;
   but the shift leaves the leading 11 in place, giving (00001110), which
   would be an out-of-range index. AND-ing with the mask (00000011) keeps
   only the last two bits, (00000010). The other 2-bit lookups need the
   same masking.

4. Word-level XOR folding (implemented as `parity_xor_folding`).
   XOR of two bits is 0 when they are equal and 1 otherwise; XOR is both
   associative and commutative, and the XOR of a group of bits is its
   parity. So the parity of the 64 bits b63..b0 equals the parity of
   (b63..b32) XOR (b31..b0), computed with one shift and one XOR. Repeat on
   32, 16, 8, 4, 2 and 1-bit widths. The high bits left behind are
   meaningless, so the answer must be extracted from the lowest bit.

   Book's 8-bit illustration: parity of (11010111) = parity of 1101 XOR 0111
   = parity of (1010) = parity of 10 XOR 10 = parity of (00); finally 0 XOR 0
   = 0. Bit by bit: the first XOR produces (11011010), of which only the
   low 4 bits matter; the second produces (11101100), of which only the low
   2 bits matter; the third produces (10011010), whose last bit is the
   result, extracted by AND-ing with (00000001).

All four book programs are present below as separate functions, along with
a helper that builds the lookup table, an input check, and a `parity`
alias that calls the brute-force version.

ADDITIONAL EXAMPLES (added for learning; not printed in this exercise)
---------------------------------------------------------------------
    word = 0                 -> 0 (no 1-bits at all)
    word = 2**64 - 1         -> 0 (sixty-four 1-bits, an even number)

Every function here accepts only unsigned 64-bit integers (0 <= word < 2**64)
and raises ValueError otherwise.
"""

# This file has no import statements: it uses only built-in operators,
# built-in types and built-in functions.

# Module-level constants. A leading underscore is a Python naming convention
# meaning "internal to this module; not part of its public interface".
# Python does not enforce it.
_WORD_BITS = 64
_CACHE_BITS = 16

# `1 << n` shifts the integer 1 left by n bit positions, i.e. computes 2**n.
# Subtracting 1 then gives n one-bits: (1 << 16) - 1 == 0xFFFF. This is the
# "machine-independent" way of building a mask that the chapter recommends,
# and it is the book's BIT_MASK = 0xFFFF.
_CACHE_MASK = (1 << _CACHE_BITS) - 1


def _check_word(word: int) -> None:
    """Restrict inputs to the unsigned 64-bit domain discussed in the book.

    Helper added in this repository; the book has no such function.
    """

    # Python ints are unbounded (they never overflow) and may be negative.
    # The book's algorithms assume a 64-bit unsigned word (for example the
    # XOR-folding version only folds 64 bits), so other values are rejected.
    # A chained comparison `a <= b < c` means `a <= b and b < c`.
    if not 0 <= word < (1 << _WORD_BITS):

        # `raise` stops the function and signals an error to the caller.
        # ValueError is the built-in exception for "right type, bad value".
        # https://docs.python.org/3/library/exceptions.html#ValueError
        raise ValueError("Expected an unsigned 64-bit integer")


# Type hints such as `word: int` and `-> int` document the intended types of
# parameters and return values. Python does NOT check or enforce them at
# runtime; they help readers and tools such as type checkers.
def parity_brute_force(word: int) -> int:
    """Textbook implementation 1: inspect one bit at a time (O(n))."""
    _check_word(word)
    result = 0

    # A nonzero int is truthy, so the loop stops when all bits are gone.
    while word:

        # `& 1` extracts the low bit (1 if it is set, else 0). XOR-ing it in
        # (`^=`) toggles the running parity exactly when that bit is 1; this
        # is the "count modulo 2" from the book.
        # `>>= 1` shifts right by one place, discarding the bit just tested.
        result ^= word & 1
        word >>= 1
    return result


def parity_erase_lowest_set_bit(word: int) -> int:
    """Textbook implementation 2: drop the lowest set bit each round (O(k))."""
    _check_word(word)
    result = 0
    while word:

        # `word & (word - 1)` clears the LOWEST 1-bit of a nonzero integer:
        # subtracting 1 turns that bit into 0 and the zeros below it into 1s,
        # and the AND keeps only the bits the two values share. Exactly one
        # 1-bit disappears per round, so the parity flips every round
        # (`result ^= 1`). The book's comment: "Drops the lowest set bit of x."
        result ^= 1
        word &= word - 1
    return result


# `tuple[int, ...]` is a type hint meaning "a tuple of any length whose items
# are all ints". (Writing built-in types with square brackets in hints works
# from Python 3.9.) Again, Python does not enforce it.
def _build_16bit_parity_cache() -> tuple[int, ...]:
    """Precompute parity for all 65,536 unsigned 16-bit numbers.

    Helper added in this repository: the book uses a table called
    PRECOMPUTED_PARITY but does not print the code that builds it.
    """

    # `[0] * size` creates a list with `size` copies of 0.
    values = [0] * (1 << _CACHE_BITS)
    for word in range(1, len(values)):

        # The parity of `word` is the parity of `word >> 1` (all bits except
        # the lowest), XOR the lowest bit. `word >> 1` is smaller than
        # `word`, so its entry has already been filled in.
        values[word] = values[word >> 1] ^ (word & 1)

    # tuple(...) copies the list into an immutable tuple, so no caller can
    # accidentally alter the shared cache.
    return tuple(values)


# The table is built once, when Python first imports this module, and is then
# reused by every call. This is the book's PRECOMPUTED_PARITY.
_PRECOMPUTED_PARITY = _build_16bit_parity_cache()


def parity_lookup_table(word: int) -> int:
    """Textbook implementation 3: XOR four cached 16-bit parities (O(n/L))."""
    _check_word(word)

    # Each `>>` moves one 16-bit piece down to the low end of the integer.
    # `& _CACHE_MASK` then discards any higher bits that the shift left
    # behind (the book's "masking" step), producing an index 0..65535.
    # The top piece (`word >> 48`) needs no mask because a 64-bit word has
    # nothing above bit 63. XOR-ing the four piece parities gives the parity
    # of the whole word, because parity is associative.
    # The outer parentheses let the expression continue over several lines.
    return (
        _PRECOMPUTED_PARITY[word >> 48]
        ^ _PRECOMPUTED_PARITY[(word >> 32) & _CACHE_MASK]
        ^ _PRECOMPUTED_PARITY[(word >> 16) & _CACHE_MASK]
        ^ _PRECOMPUTED_PARITY[word & _CACHE_MASK]
    )


def parity_xor_folding(word: int) -> int:
    """Textbook implementation 4: XOR-fold 64 bits down to one (O(log n))."""
    _check_word(word)

    # `word ^= word >> 32` XORs the upper 32 bits onto the lower 32 bits, so
    # the low 32 bits now have the same parity as the whole word. Each later
    # line halves the width again (16, 8, 4, 2, 1). The bits above the
    # current width become meaningless "garbage" that is never used.
    # These are the shift widths printed in the textbook.
    word ^= word >> 32
    word ^= word >> 16
    word ^= word >> 8
    word ^= word >> 4
    word ^= word >> 2
    word ^= word >> 1

    # Only the lowest bit is the answer; `& 1` extracts it (book: `x & 0x1`).
    return word & 1


def parity(word: int) -> int:
    """Compatibility entry point that calls textbook implementation 1.

    Added in this repository so that the name `parity` keeps working.
    """
    return parity_brute_force(word)


# TEXTBOOK POST-SOLUTION DISCUSSION (pages 25–26)
# -----------------------------------------------
# Brute force: O(n) time, n = word size.
#
# Erasing the lowest set bit: O(k) time, k = number of 1-bits; better in the
# best and average cases.
#
# Lookup table: with L the width of the cached words and n the word size,
# there are n/L lookups, so the time is O(n/L), assuming word-level
# operations such as shifts take O(1) time. This does not count the one-time
# cost of initialising the table.
#
# XOR folding: O(log n) time, improving on the O(n) worst case of the
# earlier methods.
#
# Caching and word-level operations can be combined, e.g. fold with XOR down
# to 16 bits and then do a single table lookup.
#
# Measured runtimes depend on the data. The lowest-set-bit refinement is very
# fast on sparse inputs. On random inputs it is about 20% faster than brute
# force; the table approach is a further four times faster; and the
# associativity (XOR-folding) approach halves the run time again.
#
# VARIANTS (page 27)
# ------------------
# Write expressions using bitwise operators, equality checks and Boolean
# operators that do the following in O(1) time
# (stated in the book; no solution given):
#   - Right propagate the rightmost set bit in x, e.g. turn (01010000)_2
#     into (01011111)_2.
#   - Compute x mod a power of two, e.g. return 13 for 77 mod 64.
#   - Test whether x is a power of 2, i.e. true for x = 1, 2, 4, 8, ...,
#     false for every other value.


# TEXTBOOK CODE COMPARISON
# ------------------------
# - The book prints four functions all named `def parity(x)`. The file gives
#   them distinct names: `parity_brute_force`, `parity_erase_lowest_set_bit`,
#   `parity_lookup_table`, `parity_xor_folding`; the parameter is renamed
#   from `x` to `word`, and `: int` / `-> int` type hints are added.
# - Every file function calls the added helper `_check_word`, which raises
#   ValueError for values outside 0 <= word < 2**64. The book has no input
#   check.
# - Lookup table: the book uses local constants `MASK_SIZE = 16`,
#   `BIT_MASK = 0xFFFF` and shifts written as `3 * MASK_SIZE`,
#   `2 * MASK_SIZE`, `MASK_SIZE`; the file uses module constants
#   `_CACHE_BITS`, `_CACHE_MASK = (1 << 16) - 1` and literal shifts 48, 32,
#   16. The book's table `PRECOMPUTED_PARITY` is never shown being built; the
#   file adds `_build_16bit_parity_cache()` and `_PRECOMPUTED_PARITY`.
# - XOR folding: the book returns `x & 0x1`; the file returns `word & 1`
#   (same value).
# - The file adds a `parity(word)` wrapper that calls the brute-force version
#   and the module constant `_WORD_BITS`.
# - Otherwise the loop bodies match the book's listings.


# Python executes this block only when this source file is run directly
# (for example `python -m epi_python.chapter_04_primitive_types.pg_024_parity`).
# When pytest imports the file, this block is skipped automatically.
# Documentation: https://docs.python.org/3/library/__main__.html
if __name__ == "__main__":

    # Each example is (word, expected_parity). The first two are the book's
    # examples 1011 and 10001000; `0b...` writes an int in binary. The last
    # two (added) are zero and the largest 64-bit value (64 one-bits).
    examples = ((0b1011, 1), (0b10001000, 0), (0, 0), ((1 << 64) - 1, 0))

    # Functions are ordinary objects in Python, so they can be stored in a
    # tuple and called later through a variable.
    approaches = (
        parity_brute_force,
        parity_erase_lowest_set_bit,
        parity_lookup_table,
        parity_xor_folding,
    )
    for word, expected in examples:

        # A list comprehension calls every implementation on the same word.
        results = [algorithm(word) for algorithm in approaches]

        # f-string: expressions in {} are evaluated and inserted. The format
        # spec `:016x` prints the int in lowercase hexadecimal, padded with
        # zeros to 16 digits (one 64-bit word).
        # https://docs.python.org/3/reference/lexical_analysis.html#f-strings
        print(f"word=0x{word:016x}: parity results={results}")

        # all(iterable) is True when every item is true (and for an empty
        # iterable). Here it checks that all four answers equal `expected`.
        # https://docs.python.org/3/library/functions.html#all
        # `assert` stops the program with an AssertionError if the condition
        # is false. These are quick smoke checks; pytest does the thorough
        # testing in the separate tests/ folder.
        assert all(value == expected for value in results)
    print("All four textbook parity implementations passed.")
