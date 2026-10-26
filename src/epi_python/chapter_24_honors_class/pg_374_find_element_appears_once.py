"""EPI Python — Exercise 24.18: Find an Element That Appears Only Once

Chapter 24: Honors Class
Textbook: pages 374–375 (printed page numbers; problem and solution
development on 374, the program, analysis and variant on 375).

PROBLEM (from the textbook)
---------------------------
Given an integer array of length n, where each element except for one
appears twice, with the remaining element appearing only once, we can use
O(n) space and O(n) time to find the element that appears exactly once,
e.g., using a hash table. However, there is a better solution: compute the
bitwise-XOR of all the elements in the array. Because x XOR x = 0, all
elements that appear an even number of times cancel out, and the element
that appears exactly once remains. Therefore, this problem can be solved
using O(1) space.

Given an integer array, in which each entry but one appears in triplicate,
with the remaining element appearing once, find the element appearing once.
For example, if the array is <2, 4, 2, 5, 2, 5, 5>, you should return 4.

HINT (from the textbook)
------------------------
Count the number of 1s at each index.

SOLUTION DEVELOPMENT (following the textbook)
---------------------------------------------
The brute-force solutions (hash table or sorting) also work here, with the
same time and space complexities.
(The book refers to them as "the brute-force solutions in Solution 24.18".)

Solution 11.10 on Page 157 can be seen as counting, mod 2, for each bit
position, how many entries have a 1 there: the XOR of the elements at
indices [0, i - 1] says exactly which bit positions have been 1 an odd
number of times in those elements.

The analogue here is to count mod 3, for each bit position, how many times
that bit has been 1. Counting mod 3 removes the elements that appear three
times, so the positions whose count is 1 are exactly the 1-bits of the
element that appears once.

Worked example from the book: <2, 4, 2, 5, 2, 5, 5> in binary is
<(010), (100), (010), (101), (010), (101), (101)>. The number of 1s in
position 0 (the LSB) across all 7 entries is 3; in position 1 it is 3; in
position 2 it is 4. Taking each count mod 3 cancels the elements that
appear three times, leaving a 1 in the MSB and 0 in the other two positions:
binary 100, i.e. 4, the element that appeared once.

Implementation: an array C of integers, one entry per bit of the integer
word size; C[i] counts the 1s in bit position i over all inputs. After all
input is processed, C[i] mod 3 is 1 exactly at the bit positions where the
once-appearing element has a 1.

The book prints one program, `find_element_appears_once(A)`, implemented
here with small differences.

ADDITIONAL EXAMPLES (added for learning; not printed in this exercise)
---------------------------------------------------------------------
    [6, 6, 6, -3, 7, 7, 7] -> -3   (negative values via 32-bit two's complement)
"""


def find_element_appears_once(a: list[int]) -> int:
    """Textbook implementation: per-bit counts mod 3 over 32-bit words.

    Assumes values fit in a signed 32-bit integer. Type hints (`list[int]`,
    `-> int`) are documentation; Python does not enforce them.
    """

    # One counter per bit position of a 32-bit word (the array C).
    counts=[0]*32
    for value in a:
        for i in range(32):

            # `value >> i` shifts right by i bits, bringing bit i to the
            # lowest position; `& 1` (bitwise AND with 1) keeps only that
            # bit, giving 0 or 1.
            # Python ints are unbounded and `>>` on a negative number is an
            # arithmetic (floor) shift, so for a negative value this still
            # reads the bits of its two's-complement form, e.g. -3 has 1s in
            # all positions except bit 1 (and so on up to bit 31).
            counts[i]+=(value>>i)&1

    # Rebuild the answer: bit i is set when counts[i] % 3 is nonzero
    # (a nonzero int is truthy).
    # `1 << i` is 2**i. enumerate(counts) yields (position, count) pairs, and
    # sum(...) adds the selected powers of two from the generator
    # expression.
    # https://docs.python.org/3/library/functions.html#enumerate
    # https://docs.python.org/3/library/functions.html#sum
    result=sum(1<<i for i,c in enumerate(counts) if c%3)

    # Any result greater than or equal to 2**31 must correspond to a
    # negative value: the result was assembled as an UNSIGNED 32-bit number,
    # so if bit 31 (the sign bit) is set, subtract 2**32 to get the signed
    # value. `**` is exponentiation. Conditional expression
    # `X if cond else Y`.
    return result if result<2**31 else result-2**32


# TEXTBOOK POST-SOLUTION DISCUSSION (page 375)
# --------------------------------------------
# Time: O(n). Space: O(1) (32 counters, independent of n).
#
# VARIANTS
# 1. Solve the same problem when one entry appears twice and the rest appear
#    three times. (stated in the book; no solution given)


# TEXTBOOK CODE COMPARISON
# ------------------------
# book: `def find_element_appears_once(A)`; inner loop does
#   `counts[i] += x & 1` then `x >>= 1` (shifting the loop variable itself);
#   a nested helper `def handle_negative(n): return n if n < 2**31 else n -
#   2**32`; returns `handle_negative(sum(1 << i for i, c in enumerate(counts)
#   if c % 3))`.
# file: parameter renamed `a: list[int]` with `-> int`; loop variable `value`
#   left unchanged and bit i read as `(value >> i) & 1`; the sum is stored in
#   `result` and the sign correction is done inline with a conditional
#   expression instead of the nested `handle_negative` function. Same
#   results.


# Python executes this block only when this source file is run directly.
# When pytest imports the file, this block is skipped automatically.
# Documentation: https://docs.python.org/3/library/__main__.html
if __name__=='__main__':

    # 6 and 7 each appear three times; -3 appears once. The example shows the
    # 2**32 sign correction recovering a negative answer.
    # `assert` raises AssertionError on mismatch; the tests/ folder holds
    # the thorough pytest suite.
    print('Unique integer:',find_element_appears_once([6,6,6,-3,7,7,7]))
    assert find_element_appears_once([6,6,6,-3,7,7,7])==-3
