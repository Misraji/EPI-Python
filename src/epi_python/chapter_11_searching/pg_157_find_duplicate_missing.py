"""EPI Python — Exercise 11.10: Find the Duplicate and Missing Elements

Chapter 11: Searching
Textbook: pages 157–158 (printed page numbers; introduction, problem and
start of the solution on 157, worked example, program and complexity on
158).

PROBLEM (from the textbook)
---------------------------
The exercise opens with a simpler warm-up (summarised in the solution notes
below), then poses:

"You are given an array of n integers, each between 0 and n - 1,
inclusive. Exactly one element appears twice, implying that exactly one
number between 0 and n - 1 is missing from the array. How would you compute
the duplicate and missing numbers?"

HINT (from the textbook)
------------------------
"Consider performing multiple passes through the array."

SOLUTION DEVELOPMENT (following the textbook)
---------------------------------------------
Warm-up from the introduction. If an array holds n - 1 DISTINCT integers
from 0 to n - 1, exactly one number in that range is missing.
  * Sum method: 0 + 1 + ... + (n - 1) = (n - 1)n / 2, so the missing number
    is (n - 1)n / 2 minus the array's sum -- O(n) time, O(1) space.
    Book's example: for <5, 3, 0, 1, 2>, n = 6; 5(6)/2 = 15 and
    5 + 3 + 0 + 1 + 2 = 11, so the missing number is 15 - 11 = 4.
  * Likewise, if an array has n + 1 integers from 0 to n - 1 with exactly
    one value appearing twice, the duplicate is the array's sum minus
    (n - 1)n / 2.
  * XOR method: XOR all integers 0 .. n - 1 together with all array
    entries. Every value present cancels with its copy from the range,
    leaving only the missing value. (The same idea finds the duplicated
    value in the second warm-up.) Book's example: <5, 3, 0, 1, 2> in binary
    is <101, 011, 000, 001, 010>; their XOR is 101. The XOR of 0..5 is 001.
    101 XOR 001 = 100 = 4, the missing number.

The real problem (one duplicate t AND one missing m):

Brute force: put entries in a hash table; the value inserted twice is the
duplicate; then test 0 .. n - 1 against the table to find the missing
value. O(n) time and O(n) space. Sorting first gives O(1) space, after which
both values are easy to find, but time rises to O(n log n).

Better: use collective properties of the numbers. The array's sum is
exactly (n - 1)n / 2 + t - m, one equation in two unknowns. A second
equation could come from the product or the sum of squares, but those
produce very large integers, so the book rejects them in practice.

Using XOR: XOR of 0 .. n - 1 together with all array entries gives
m XOR t. On its own that does not separate m and t, but since m != t, some
bit of m XOR t is 1, i.e., m and t differ in that bit. (Book's
illustration: 01101 XOR 11100 = 10001; the 1s mark exactly the bits where
the two numbers differ.)

Pick a bit position k where they differ. XOR together only the numbers
0 .. n - 1 whose kth bit is 1 and only the array entries whose kth bit is
1; call the result h. By the warm-up's cancellation logic, h is either m
or t. One more pass through the array tells which: if h occurs in the
array it is the duplicate, otherwise the missing value. The other value is
h XOR (m XOR t).

Book's worked example: A = <5, 3, 0, 3, 1, 2>, so t = 3 and m = 4.
  * In binary A is <101, 011, 000, 011, 001, 010>; XOR of the entries is
    110.
  * XOR of 0..5 is 001; 110 XOR 001 = 111 = m XOR t.
  * Use the least significant set bit (value 1). Numbers 0..5 with that bit
    set: 001, 011, 101. Array entries with that bit set: 101, 011, 011,
    001. XOR of these seven values is 011 = 3.
  * Another pass shows 3 is in the array, so 3 is the duplicate. The
    missing entry is 011 XOR (all entries) XOR (0..5) = 100 = 4.

The implementation below, find_duplicate_missing, follows this method.

ADDITIONAL EXAMPLES (added for learning; not printed in this exercise)
---------------------------------------------------------------------
    [0, 1, 1, 3] -> (1, 2)   (duplicate 1, missing 2)
    [0]          -> raises ValueError (guard added in this file)
"""


def find_duplicate_missing(values: list[int]) -> tuple[int, int]:
    """Return (duplicate, missing) among indices 0..n-1 using XOR partition.

    This is the textbook's find_duplicate_missing (the only implementation
    given), with explicit loops instead of functools.reduce and a plain
    tuple instead of the book's DuplicateAndMissing namedtuple.

    Type hints: `list[int]` is the argument type; `tuple[int, int]` means a
    2-tuple of ints (duplicate, missing) is returned. Python does not
    enforce annotations.
    """
    n = len(values)

    # With fewer than two positions there cannot be both a duplicate and a
    # missing value. (Guard added in this file.)
    # ValueError: https://docs.python.org/3/library/exceptions.html#ValueError
    if n < 2:
        raise ValueError("Need at least two positions")

    # Book's comment: compute the XOR of all numbers from 0 to |A| - 1 and
    # all entries in A. The indices 0..n-1 are exactly the numbers that
    # should be present. `^` is bitwise XOR and `^=` is its augmented
    # assignment. enumerate() yields (index, value) pairs.
    # enumerate: https://docs.python.org/3/library/functions.html#enumerate
    # Afterwards `difference` equals missing XOR duplicate.
    difference = 0
    for i, value in enumerate(values):
        difference ^= i ^ value

    # Book's comment: we need a bit that's set to 1 in the XOR; such a bit
    # exists if there is a single missing and a single duplicated number.
    #
    # `x & -x` isolates the lowest set bit of x (e.g. 0b0110 -> 0b0010).
    # Python ints behave like two's-complement numbers with infinitely many
    # sign bits, so -x is ~x + 1 and the trick works for any positive int.
    # It gives the same result as the book's `x & ~(x - 1)`.
    bit = difference & -difference

    # bit == 0 means difference was 0, so no duplicate/missing pair exists.
    if bit == 0:
        raise ValueError("Expected exactly one duplicate and missing entry")
    candidate = 0
    for i, value in enumerate(values):

        # Book's comment: focus on entries and numbers in which the
        # differ-bit is 1. `i & bit` is nonzero (truthy) exactly when that
        # bit is set in i.
        if i & bit:
            candidate ^= i
        if value & bit:
            candidate ^= value

    # Book's comment: the result is either the missing value or the
    # duplicated entry. list.count(x) counts occurrences of x in the list
    # (another O(n) pass). Exactly two copies means it is the duplicate,
    # and the missing value is recovered by XOR with `difference`.
    # list.count: https://docs.python.org/3/tutorial/datastructures.html#more-on-lists
    if values.count(candidate) == 2:
        return candidate, candidate ^ difference

    # Otherwise the candidate is the missing value.
    return candidate ^ difference, candidate


# TEXTBOOK POST-SOLUTION DISCUSSION (page 158)
# --------------------------------------------
# Time complexity O(n) (a constant number of passes over the array); space
# complexity O(1).
#
# VARIANTS
# --------
# The book gives no variants for this exercise.


# TEXTBOOK CODE COMPARISON
# ------------------------
# Book: defines
#   `DuplicateAndMissing = collections.namedtuple('DuplicateAndMissing',
#   ('duplicate', 'missing'))` and `def find_duplicate_missing(A):`.
#   It computes `miss_XOR_dup = functools.reduce(lambda v, i: v ^ i[0] ^
#   i[1], enumerate(A), 0)` (so it imports collections and functools), then
#   `differ_bit, miss_or_dup = miss_XOR_dup & (~(miss_XOR_dup - 1)), 0`,
#   loops over `enumerate(A)` XOR-ing `i` and `a` when `& differ_bit` is
#   set, and tests membership with `if miss_or_dup in A:` before returning
#   a DuplicateAndMissing namedtuple.
# File: no namedtuple and no collections/functools imports; parameter
#   renamed `values: list[int]` with return hint `tuple[int, int]`; adds
#   ValueError guards for n < 2 and for a zero XOR (not in the book);
#   the reduce/lambda is replaced by an explicit loop into `difference`;
#   the lowest set bit is computed as `difference & -difference` instead
#   of `& ~(x - 1)` (equivalent); the variable names change
#   (`miss_XOR_dup` -> `difference`, `differ_bit` -> `bit`, `miss_or_dup`
#   -> `candidate`); membership is tested with `values.count(candidate) ==
#   2` instead of `in A`; returns a plain tuple (duplicate, missing).


# Python executes this block only when this source file is run directly.
# When pytest imports the file, this block is skipped automatically.
# Documentation: https://docs.python.org/3/library/__main__.html
if __name__ == "__main__":

    # In [0, 1, 1, 3] the value 1 appears twice and 2 is missing, so the
    # result tuple is (1, 2).
    # `assert` stops the program with an AssertionError if the condition is
    # false; this is a quick smoke check, while pytest provides the more
    # thorough automated verification.
    print("duplicate, missing:", find_duplicate_missing([0, 1, 1, 3]))
    assert find_duplicate_missing([0,1,1,3]) == (1,2)
