"""EPI Python — Exercise 16.4: Compute the Binomial Coefficients

Chapter 16: Dynamic Programming
Textbook: pages 244–245 (printed page numbers; problem and solution start on 244).

PROBLEM (from the textbook)
---------------------------
"The symbol C(n, k) is the short form for the expression
n(n-1)...(n-k+1) / (k(k-1)...(3)(2)(1)). It is the number of ways to choose
a k-element subset from an n-element set. It is not obvious that the
expression defining C(n, k) always yields an integer. Furthermore, direct
computation of C(n, k) from this expression quickly results in the
numerator or denominator overflowing if integer types are used, even if the
final result fits in a 32-bit integer. If floats are used, the expression
may not yield a 32-bit integer."
(The book writes C(n, k) as the usual stacked "n over k" symbol.)

"Design an efficient algorithm for computing C(n, k) which has the property
that it never overflows if the final result fits in the integer word size."

HINT (from the textbook)
------------------------
"Write an equation."

SOLUTION DEVELOPMENT (following the textbook)
---------------------------------------------
Brute force: compute n(n-1)...(n-k+1), then k(k-1)...(3)(2)(1), and divide.
As the problem says, this can overflow even when the answer fits in a word.

Cancelling common factors between numerator and denominator is tempting,
but it requires factoring numbers, which is itself hard.

Better: avoid multiplication and division entirely. C(n, k) counts the
size-k subsets of an n-element set, which can be enumerated recursively
(as in Solution 15.5, page 226): a size-k subset of {0, 1, ..., n-1} either
contains the nth element or not. So find all size-(k-1) subsets of the
first n - 1 elements and add the nth element to each, and find all size-k
subsets of the first n - 1 elements; their union is all size-k subsets.

Since only the NUMBER of subsets matters, this gives the identity

    C(n, k) = C(n - 1, k) + C(n - 1, k - 1),

a direct recursion with base cases C(r, r) = C(r, 0) = 1. If C(n, k) fits in
a 32-bit integer, so do the results of the subcalls (they are smaller), so
intermediate results cannot overflow.

Example: C(5, 2) = C(4, 2) + C(4, 1). Expanding C(4, 2) gives
C(3, 2) + C(3, 1); expanding C(3, 2) gives C(2, 2) + C(2, 1). C(2, 2) is a
base case, returning 1. Continuing, C(4, 2) = 6 and C(4, 1) = 4, so
C(5, 2) = 6 + 4 = 10.

A naive recursion makes repeated subcalls with identical arguments and is
exponential; caching intermediate results avoids that. The book's program
compute_binomial_coefficient(n, k) does this top-down with a nested
compute_x_choose_y(x, y) and a 2D cache x_choose_y.

This file instead computes the same identity BOTTOM-UP, one row of Pascal's
triangle at a time; the book's memoized recursion is not in this file (see
TEXTBOOK CODE COMPARISON).

ADDITIONAL EXAMPLES (added for learning; not printed in this exercise)
---------------------------------------------------------------------
    C(0, 0) -> 1
    C(5, 2) -> 10   (the book's worked example)
    C(4, 4) -> 1
    C(4, 5) -> 0    (k > n: no such subsets)
"""


def compute_binomial_coefficients(n: int, k: int) -> int:
    """Compute C(n, k) using Pascal's addition rule, row by row.

    NOT the book's printed program (a memoized recursion); this is a
    bottom-up evaluation of the same identity
    C(i, j) = C(i - 1, j - 1) + C(i - 1, j). Only additions are used, so
    no intermediate value exceeds the final row's entries. Returns 0 when
    k < 0 or k > n.
    """

    # Type hints such as `n: int` are not enforced by Python. Python ints
    # are unbounded, so overflow cannot happen here anyway; the algorithm
    # still shows the overflow-free technique the book asks for.
    if k < 0 or k > n:
        return 0

    # Row 0 of Pascal's triangle: C(0, 0) = 1.
    row=[1]
    for i in range(1,n+1):

        # Row i has i + 1 entries; both ends are 1 (C(i, 0) = C(i, i) = 1).
        # `[1]*(i+1)` builds a list of i + 1 ones.
        current=[1]*(i+1)

        # Interior entries: C(i, j) = C(i-1, j-1) + C(i-1, j).
        for j in range(1,i):
            current[j]=row[j-1]+row[j]
        row=current
    return row[k]


# TEXTBOOK POST-SOLUTION DISCUSSION (page 245)
# --------------------------------------------
# There are O(nk) subproblems, and once C(n - 1, k) and C(n - 1, k - 1) are
# known, C(n, k) takes O(1) time; so the time is O(nk). The space is also
# O(nk); the book notes that it can easily be reduced to O(k).
#
# VARIANTS
# --------
# The book states no variants for this exercise.


# TEXTBOOK CODE COMPARISON
# ------------------------
# * Book: `def compute_binomial_coefficient(n, k)` (singular "coefficient")
#   with nested memoized `compute_x_choose_y(x, y)`: base case
#   `if y in (0, x): return 1`; if `x_choose_y[x][y] == 0`, compute
#   `without_y = compute_x_choose_y(x - 1, y)` and
#   `with_y = compute_x_choose_y(x - 1, y - 1)` and cache their sum; cache
#   `x_choose_y = [[0] * (k + 1) for _ in range(n + 1)]`; returns
#   `compute_x_choose_y(n, k)`.
# * File: `compute_binomial_coefficients(n: int, k: int) -> int` (plural),
#   an iterative bottom-up Pascal's-triangle computation with lists `row`
#   and `current`; no recursion and no 2D cache. It uses O(n) space (one
#   row of up to n + 1 entries) and O(n^2) time, rather than the book's
#   O(nk).
# * File adds the `k < 0 or k > n` guard returning 0.
# * The book's memoized recursive implementation is MISSING from the file.


# Python executes this block only when this source file is run directly.
# When pytest imports the file, this block is skipped automatically.
# Documentation: https://docs.python.org/3/library/__main__.html
if __name__ == "__main__":

    # Added examples (C(5, 2) = 10 is also the book's worked example):
    # the smallest case, an ordinary case, k = n, and k > n.
    # `assert` stops the program with an AssertionError if the condition is
    # false; these are quick smoke checks, the pytest suite is thorough.
    observed = compute_binomial_coefficients(0, 0)
    print("compute_binomial_coefficients:", observed)
    assert observed == 1
    observed = compute_binomial_coefficients(5, 2)
    print("compute_binomial_coefficients:", observed)
    assert observed == 10
    observed = compute_binomial_coefficients(4, 4)
    print("compute_binomial_coefficients:", observed)
    assert observed == 1
    observed = compute_binomial_coefficients(4, 5)
    print("compute_binomial_coefficients:", observed)
    assert observed == 0
