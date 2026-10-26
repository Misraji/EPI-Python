"""EPI Python — Exercise 11.4: Compute the Integer Square Root

Chapter 11: Searching
Textbook: pages 148–149 (printed page numbers; problem, solution and the
start of the program on 148, rest of program and complexity on 149).

PROBLEM (from the textbook)
---------------------------
"Write a program which takes a nonnegative integer and returns the largest
integer whose square is less than or equal to the given integer. For
example, if the input is 16, return 4; if the input is 300, return 17,
since 17^2 = 289 < 300 and 18^2 = 324 > 300."

HINT (from the textbook)
------------------------
"Look out for a corner-case."

SOLUTION DEVELOPMENT (following the textbook)
---------------------------------------------
Brute force: square 1, 2, 3, ... in turn, stopping as soon as the square
exceeds the key k. That is O(k) time; for a 32-bit integer it may take over
a billion iterations.

Taking steps of size 1 is wasteful. If x^2 < k, no number smaller than x
can be the answer; if x^2 > k, neither x nor any number larger than x can
be the answer. Being able to throw away large ranges like this points to
binary search.

The algorithm keeps an interval of values whose squares have not yet been
classified as <= k or > k:
  * Start with the interval [0, k].
  * Let m = floor((l + r) / 2) and compare m^2 with k.
  * If m^2 <= k, every integer <= m also has square <= k, so the interval
    becomes [m + 1, r].
  * If m^2 > k, every integer >= m has square > k, so the interval
    becomes [l, m - 1].
  * Stop when the interval is empty. Then every number below l has square
    <= k and l's square is > k, so the answer is l - 1.

Book's worked example, k = 21:
  [0, 21]: m = 10, 10^2 > 21  -> [0, 9]
  [0, 9]:  m = 4,  4^2 < 21   -> [5, 9]
  [5, 9]:  m = 7,  7^2 > 21   -> [5, 6]
  [5, 6]:  m = 5,  5^2 > 21   -> [5, 4]
  The right end is now below the left end (empty interval), so the
  result is 5 - 1 = 4.

Book's second example, k = 25: the intervals are [0, 25], [0, 11],
[6, 11], [6, 7], [6, 5], and the value returned is 6 - 1 = 5.

The implementation below, square_root, follows this idea (it records the
last good midpoint in `result` instead of returning left - 1; see the
comparison section).

ADDITIONAL EXAMPLES (added for learning; not printed in this exercise)
---------------------------------------------------------------------
    k=0  -> 0
    k=1  -> 1
    k=2  -> 1
    k=15 -> 3
    k=-1 -> raises ValueError (guard added in this file)
"""


def square_root(k: int) -> int:
    """Floor of the integer square root of nonnegative k.

    This is the textbook's square_root (integer version, the only
    implementation given), with an added negative-input check and the
    answer tracked in a separate `result` variable.

    Type hints: `k: int` and `-> int` document the expected types; Python
    does not check them at run time.
    """

    # `raise ValueError(...)` stops the function with an exception. The
    # problem is only defined for nonnegative integers, so a negative k is
    # rejected instead of silently returning a wrong answer.
    # ValueError: https://docs.python.org/3/library/exceptions.html#ValueError
    if k < 0:
        raise ValueError('negative input')

    # Book's comment: candidate interval [left, right] where everything
    # before left has square <= k, and everything after right has
    # square > k. Tuple unpacking sets both ends at once.
    left,right = 0,k
    result=0
    while left <= right:

        # `//` is floor division, giving an int midpoint. Python ints are
        # unbounded, so middle*middle never overflows, even for huge k --
        # one reason this integer-only approach is exact.
        middle=(left+right)//2

        # middle is a viable answer: remember it and look for a larger one.
        if middle*middle <= k:
            result=middle
            left=middle+1

        # middle is too big, and so is everything above it.
        else:
            right=middle-1

    # When the loop ends, result equals the book's `left - 1`.
    return result


# TEXTBOOK POST-SOLUTION DISCUSSION (page 149)
# --------------------------------------------
# Time complexity: that of binary search over the interval [0, k], i.e.,
# O(log k). Only a few variables are used, so extra space is O(1).
#
# VARIANTS
# --------
# The book gives no variants for this exercise.


# TEXTBOOK CODE COMPARISON
# ------------------------
# Book: `def square_root(k):` with `left, right = 0, k`, the candidate
#   interval comment, a `mid_squared = mid * mid` variable, branches
#   `left = mid + 1` / `right = mid - 1`, and `return left - 1`.
# File: type hints `k: int` and `-> int` added; a `raise ValueError` guard
#   for negative input is added (not in the book); `mid` renamed `middle`;
#   no `mid_squared` variable (the product is computed inline); a separate
#   `result` variable records the last midpoint whose square was <= k and is
#   returned instead of `left - 1` (same value for nonnegative k).


# Python executes this block only when this source file is run directly.
# When pytest imports the file, this block is skipped automatically.
# Documentation: https://docs.python.org/3/library/__main__.html
if __name__ == "__main__":
    # Demonstrations check representative input/output behavior, including
    # the small corner cases 0 and 1 and a non-perfect square (15 -> 3).
    #
    # `assert` stops the program with an AssertionError if a result is
    # different from the expected value. These are quick smoke checks;
    # pytest provides the more thorough automated verification.
    observed = square_root(0)
    print("square_root:", observed)
    assert observed == 0
    observed = square_root(1)
    print("square_root:", observed)
    assert observed == 1
    observed = square_root(2)
    print("square_root:", observed)
    assert observed == 1
    observed = square_root(15)
    print("square_root:", observed)
    assert observed == 3
