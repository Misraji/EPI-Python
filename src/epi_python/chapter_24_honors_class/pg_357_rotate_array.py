"""EPI Python — Exercise 24.6: Rotate an Array

Chapter 24: Honors Class
Textbook: pages 357–359 (printed page numbers; problem and solution start on
357, the programs are on 358–359, a closing remark is on 359).

PROBLEM (from the textbook)
---------------------------
Let A be an array of n elements. If memory is not a concern, rotating A by
i positions is trivial; we create a new array B of length n, and set
B[j] = A[(i + j) mod n] for each j. If all we have is additional storage for
c elements, we can repeatedly rotate the array by c a total of ceil(i/c)
times; this increases the time complexity to O(n ceil(i/c)).

Design an algorithm for rotating an array A of n elements to the right by
i positions. Do not use library functions implementing rotate.

HINT (from the textbook)
------------------------
Use concrete examples to form a hypothesis relating n, i, and the number of
cycles.

SOLUTION DEVELOPMENT (following the textbook)
---------------------------------------------
Two brute-force algorithms:
  * shift by one position, i times: O(ni) time, O(1) space;
  * use an extra array of length i as a buffer and move elements i at a
    time: O(n) time, O(i) space.

To get both O(n) time and O(1) space, use the fact that a permutation can
be applied with constant extra storage (Problem 5.10 on Page 50), applied
to the permutation that corresponds to the rotation.

A rotation is not itself a cyclic permutation, but as a permutation it
decomposes into cyclic permutations. Examples from the book:
  * n = 6, i = 2: the rotation is the permutation <4, 5, 1, 2, 3, 4>, which
    is achieved by the cycles (0, 2, 4) and (1, 3, 5).
    [NEEDS PDF REVIEW: page 357 prints the permutation as <4,5,1,2,3,4>,
    which repeats 4 and is not a permutation of 0..5; transcribed as
    printed.]
  * n = 15, i = 6: the cycles are <0, 6, 12, 3, 9>, <1, 7, 13, 4, 10> and
    <2, 8, 14, 5, 11>.
These suggest two conjectures:
  (1.) All cycles have the same length and are shifted versions of the
       cycle <0, i mod n, 2i mod n, ..., (l - 1)i mod n>.
  (2.) The number of cycles is GCD(n, i).
They can be justified heuristically (a formal proof needs the prime
factorizations of i and n). Assuming them, apply the rotation one cycle at a
time: the cycles start at indices 0, 1, 2, ..., GCD(n, i) - 1, and each
cycle is applied by shifting its elements along one at a time. This is the
book's first program (`rotate_array` with a nested
`apply_cyclic_permutation`); in this file it is `rotate_array_cycles`.

Simpler alternative (after the first program's analysis), which works well
in practice: with A = <1, 2, 3, 4, a, b> and i = 2, the rotated array
consists of two subarrays, <1, 2, 3, 4> and <a, b>, each in its original
order; rotation just exchanges these two blocks. To do that in O(n) time
with O(1) space, use array reversal:
  * reverse all of A: <1, 2, 3, 4, a, b> becomes A' = <b, a, 4, 3, 2, 1>;
  * reverse the first i elements of A': <a, b, 4, 3, 2, 1>;
  * reverse the remaining elements from index i: <a, b, 1, 2, 3, 4>, which
    is the rotated A.
This is the book's second `rotate_array`, and this file's `rotate_array`.

The book then gives a third, "very natural" slicing version,
`rotate_array_naive`, noting that its use of sublists copies from the
original list and so needs linear space. This file has a function of that
name too, but with different slicing code (see TEXTBOOK CODE COMPARISON).

ADDITIONAL EXAMPLES (added for learning; not printed in this exercise)
---------------------------------------------------------------------
    rotate right by 2: [1, 2, 3, 4, 5] -> [4, 5, 1, 2, 3]
"""

# Python standard library: mathematical functions.
# Module documentation: https://docs.python.org/3/library/math.html
# gcd API: https://docs.python.org/3/library/math.html#math.gcd
import math


def rotate_array_cycles(rotate_amount: int,a: list[int]) -> None:
    """Textbook solution 1: apply the rotation one cyclic permutation at a time.

    Rotates `a` right by `rotate_amount` in place, using O(1) extra space.
    `-> None` documents that the function returns nothing (it mutates its
    argument). Type hints are not enforced by Python.
    """

    # Added guard (not in the book): `len(a)` would be 0 below, and `% 0`
    # raises ZeroDivisionError.
    if not a:
        return

    # `%=` replaces rotate_amount by its remainder mod n; rotating by n is
    # the identity. For a positive divisor, Python's % always returns a
    # nonnegative result (e.g. -1 % 5 == 4), so negative amounts become
    # equivalent right rotations.
    rotate_amount%=len(a)
    if rotate_amount==0:
        return

    # math.gcd(x, y) returns the greatest common divisor of two integers.
    # By conjecture (2.) the number of independent cycles equals
    # GCD(n, rotate_amount); each has n / GCD elements.
    num_cycles=math.gcd(len(a),rotate_amount)

    # `//` is floor (integer) division; the result is exact here since the
    # GCD divides n.
    cycle_length=len(a)//num_cycles

    # Each cycle starts at a different offset 0, 1, ..., num_cycles - 1.
    for offset in range(num_cycles):

        # (This loop body is the book's nested apply_cyclic_permutation.)
        # temp carries the value currently being moved along the cycle.
        temp=a[offset]
        for i in range(1,cycle_length):

            # Destination of the carried value: rotate_amount places further
            # along, wrapping around with % len(a).
            idx=(offset+i*rotate_amount)%len(a)

            # Tuple swap: put the carried value at idx and pick up the value
            # that was there, all in one statement.
            a[idx],temp=temp,a[idx]

        # The last carried value wraps back to the cycle's start.
        a[offset]=temp


def rotate_array(rotate_amount: int,a: list[int]) -> None:
    """Textbook solution 2: the simpler triple-reverse algorithm (in place)."""

    # Added guard (not in the book) against `% 0` on an empty list.
    if not a:
        return
    i=rotate_amount%len(a)

    # A nested function: `reverse` is defined inside rotate_array, so it can
    # read the enclosing variable `a` (a closure). It mutates the list's
    # contents, which needs no `nonlocal` declaration because the name `a`
    # itself is never reassigned. begin and end are inclusive indices.
    def reverse(begin: int,end: int) -> None:
        while begin<end:
            a[begin],a[end]=a[end],a[begin]
            begin,end=begin+1,end-1

    # Reverse everything, then the first i elements, then the rest.
    # When i == 0, reverse(0, -1) does nothing (0 < -1 is false) and the
    # third call undoes the first, leaving `a` unchanged.
    reverse(0,len(a)-1)
    reverse(0,i-1)
    reverse(i,len(a)-1)


def rotate_array_naive(i: int,a: list[int]) -> None:
    """Concise slicing version with O(n) extra storage.

    Corresponds to the book's `rotate_array_naive`, but uses a different
    slicing expression (see TEXTBOOK CODE COMPARISON).
    """

    # A nonempty list is truthy, so the body is skipped for [].
    if a:
        i%=len(a)

        # Slicing: a[-i:] is the last i elements, a[:-i] all but the last i;
        # `+` concatenates them into a NEW list (this copying is why the
        # method needs linear extra space).
        # `X if cond else Y` is a conditional expression; it binds more
        # loosely than `+`, so this is (a[-i:] + a[:-i]) if i else a[:].
        # The `i == 0` case is needed because a[-0:] is a[0:], the whole list.
        # Assigning to the full slice `a[:] = ...` replaces the contents of
        # the existing list object in place, so the caller sees the change
        # (plain `a = ...` would only rebind the local name).
        a[:]=a[-i:]+a[:-i] if i else a[:]


# TEXTBOOK POST-SOLUTION DISCUSSION (pages 358–359)
# -------------------------------------------------
# Cyclic-permutation solution: O(n) time, since constant work is done per
# entry; O(1) space.
#
# The triple-reverse solution also runs in O(n) time with O(1) space; the
# slicing ("naive") version copies sublists and so uses linear space.
#
# Final remark: a completely different approach rotates in blocks of k,
# reusing freed space as temporary storage. It can be made to work, but the
# final rotation has to be done very carefully and the code is complex.
#
# VARIANTS
# The book gives no variants for this exercise.


# TEXTBOOK CODE COMPARISON
# ------------------------
# Solution 1 — book: `def rotate_array(rotate_amount, A)` with a nested
#   `apply_cyclic_permutation(rotate_amount, offset)` called for each cycle
#   `c`; GCD computed with `fractions.gcd(len(A), rotate_amount)`
#   (fractions.gcd was removed in Python 3.9).
#   file: renamed `rotate_array_cycles(rotate_amount: int, a: list[int]) ->
#   None`; the nested function is inlined as the loop body with loop
#   variable `offset`; uses `math.gcd`; added `if not a: return` guard.
# Solution 2 — book: `def rotate_array(i, A)`, `i %= len(A)`, nested
#   `reverse(begin, end)`, three reverse calls.
#   file: `rotate_array(rotate_amount: int, a: list[int]) -> None`; first
#   parameter renamed and `i = rotate_amount % len(a)` assigned separately;
#   type hints on the nested reverse; added empty-list guard. Same algorithm.
# Solution 3 — book: `def rotate_array_naive(i, A)`: `i %= len(A)`, then
#   `A[:] = A[::-1]`, `A[:i] = A[:i][::-1]`, `A[i:] = A[i:][::-1]` (the
#   triple reverse done with slices).
#   file: `rotate_array_naive(i: int, a: list[int]) -> None` uses a
#   different expression, `a[:] = a[-i:] + a[:-i] if i else a[:]`
#   (concatenating the two blocks), wrapped in `if a:`. Same result.


# Python executes this block only when this source file is run directly.
# When pytest imports the file, this block is skipped automatically.
# Documentation: https://docs.python.org/3/library/__main__.html
if __name__=='__main__':

    # Run all three versions on a fresh list each time (they mutate their
    # argument), rotating [1, 2, 3, 4, 5] right by 2.
    # `fn.__name__` is the function's name, printed to label each result.
    # `assert` raises AssertionError if a result differs; the tests/ folder
    # holds the thorough pytest suite.
    for fn in (rotate_array_cycles,rotate_array,rotate_array_naive):
        a=[1,2,3,4,5]
        fn(2,a)
        print(fn.__name__,a)
        assert a==[4,5,1,2,3]
