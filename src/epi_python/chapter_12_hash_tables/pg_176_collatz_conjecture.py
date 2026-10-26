"""EPI Python — Exercise 12.11: Test the Collatz Conjecture

Chapter 12: Hash Tables
Textbook: pages 176–177 (printed page numbers; problem and acceleration
ideas on 176, remaining ideas, program and complexity on 177).

PROBLEM (from the textbook)
---------------------------
"The Collatz conjecture is the following: Take any natural number. If it
is odd, triple it and add one; if it is even, halve it. Repeat the process
indefinitely. No matter what number you begin with, you will eventually
arrive at 1.

As an example, if we start with 11 we get the sequence 11, 34, 17, 52, 26,
13, 40, 20, 10, 5, 16, 8, 4, 2, 1. Despite intense efforts, the Collatz
conjecture has not been proved or disproved.

Suppose you were given the task of checking the Collatz conjecture for the
first billion integers. A direct approach would be to compute the
convergence sequence for each number in this set.

Test the Collatz conjecture for the first n positive integers."

HINT (from the textbook)
------------------------
"How would you efficiently check the conjecture for n assuming it holds for
all m < n?"

SOLUTION DEVELOPMENT (following the textbook)
---------------------------------------------
The book notes that interview questions like this are often open-ended,
with no definite best solution; the goal is a good heuristic, coded well.

The hypothesis can fail in two ways: a sequence returns to a number it has
already visited (so it loops forever), or a sequence grows without bound.
Unbounded growth cannot be tested with a fixed integer word length, so
overflows are simply flagged.

Basic approach: for every number, apply the rules repeatedly until 1 is
reached. Ideas the book lists for speeding this up:
  * Reuse computation: store every number already shown to converge to 1;
    reaching such a number means the current sequence converges too.
  * Skip even numbers: an even number is immediately halved, and the
    result has already been checked.
  * If every number up to k has been tested, a chain can stop as soon as it
    reaches a number <= k, and numbers below k need not be stored in the
    hash table.
  * If multiplication and division are expensive, use bit shifting and
    addition.
  * Split the search set and explore the parts in parallel on many
    computers, as in Solution 19.9 on page 299.
Because values in a sequence can exceed 32 bits, use 64-bit integers and
keep checking for overflow, or use arbitrary precision integers. (Python
ints are arbitrary precision, so they never overflow.)

The implementation below, collatz_holds_to, uses the "reuse computation"
and loop-detection ideas, but differs from the book's program in which
numbers it stores and when it stops a chain (see the comparison section).
Like the book's program, it is an empirical check of 1..n, not a proof.

ADDITIONAL EXAMPLES (added for learning; not printed in this exercise)
---------------------------------------------------------------------
    n=1000 -> True (every start from 1 to 1000 reaches 1)
    n=0    -> raises ValueError (guard added in this file)
"""


def collatz_holds_to(n: int) -> bool:
    """Verify all starts from 1..n; remember proven positive intermediate values.

    This corresponds to the textbook's test_collatz_conjecture (the only
    implementation given), restructured: it caches every value on each
    converging path (not only odd values) and stops a chain only when it
    reaches a cached value.

    Type hints: `n: int` and `-> bool` document the expected types; Python
    does not enforce them.
    """

    # Only positive limits make sense. (Guard added in this file.)
    # ValueError: https://docs.python.org/3/library/exceptions.html#ValueError
    if n < 1:
        raise ValueError("n must be positive")

    # `{1}` is a set literal containing 1: the hash set of numbers known to
    # reach 1. (Note that `{}` alone would be an empty dict, not a set.)
    verified = {1}

    # range(2, n + 1) gives 2, 3, ..., n; 1 is trivially fine.
    for start in range(2, n + 1):
        current = start

        # set() is an empty set: the values seen on this start's chain.
        # set: https://docs.python.org/3/library/stdtypes.html#set
        path = set()

        # Follow the chain until it joins a value already known to converge.
        while current not in verified:

            # A repeated value within one chain means an infinite loop, which
            # would disprove the conjecture.
            if current in path:
                return False
            path.add(current)

            # `current & 1` is bitwise AND with 1: it is 1 (truthy) for odd
            # numbers and 0 (falsy) for even ones -- the "bit operations
            # instead of division" idea from the book.
            if current & 1:
                current = 3 * current + 1

            # `//=` is in-place floor division: halve an even number,
            # keeping an int.
            else:
                current //= 2

        # Every value on the path leads to a verified value, so all of them
        # converge. set.update(iterable) adds all items of the iterable.
        # set.update: https://docs.python.org/3/library/stdtypes.html#frozenset.update
        verified.update(path)
    return True


# TEXTBOOK POST-SOLUTION DISCUSSION (page 177)
# --------------------------------------------
# Little can be said about the time complexity beyond the obvious: it is at
# least proportional to n. (Chain lengths and the size of intermediate
# values depend on the data.)
#
# VARIANTS
# --------
# The book gives no variants for this exercise.


# TEXTBOOK CODE COMPARISON
# ------------------------
# Book: `def test_collatz_conjecture(n):` with
#   `verified_numbers = set()` ("Stores odd numbers already tested to
#   converge to 1."); loops `for i in range(3, n + 1)` ("Starts from 3,
#   hypothesis holds trivially for 1."); for each i keeps a `sequence` set
#   and `test_i`, looping `while test_i >= i` (stops once the chain drops
#   below i, since smaller numbers are already verified); returns False on a
#   repeated value; for odd test_i (`test_i % 2`) it `break`s if test_i is
#   in verified_numbers, otherwise adds it and sets `test_i = 3 * test_i +
#   1`; for even test_i does `test_i //= 2`. Returns True.
# File: renamed `collatz_holds_to` with type hints; adds a ValueError for
#   n < 1; loops from 2 instead of 3; `verified` starts as {1} and stores
#   EVERY value of each completed path (via `verified.update(path)`), not
#   just odd ones; the loop condition is `current not in verified` instead
#   of `test_i >= i` (no early stop on dropping below the start, and no
#   `break`); parity is tested with `current & 1` instead of `% 2`.


# Python executes this block only when this source file is run directly.
# When pytest imports the file, this block is skipped automatically.
# Documentation: https://docs.python.org/3/library/__main__.html
if __name__ == "__main__":

    # Check every start from 1 to 1000. `assert` stops the program with an
    # AssertionError if the condition is false; this is a quick smoke check,
    # while pytest provides the more thorough automated verification.
    print("Collatz validated to 1000:", collatz_holds_to(1000))
    assert collatz_holds_to(1000)
