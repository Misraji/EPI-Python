"""EPI Python — Exercise 24.16: Search in Two Sorted Arrays

Chapter 24: Honors Class
Textbook: pages 372–373 (printed page numbers; problem, solution and the
start of the program on 372, the rest of the program and analysis on 373).

PROBLEM (from the textbook)
---------------------------
You are given two sorted arrays and a positive integer k. Design an
algorithm for computing the kth smallest element in an array consisting of
the elements of the initial two arrays arranged in sorted order. Array
elements may be duplicated within and across the input arrays.

HINT (from the textbook)
------------------------
The first k elements of the first array together with the first k elements
of the second array are initial candidates. Iteratively eliminates a
constant fraction of the candidates.

SOLUTION DEVELOPMENT (following the textbook)
---------------------------------------------
Simplest: merge the arrays into a third sorted array and read off the
answer. The merge is O(m + n), m and n the input lengths.

Somewhat better: build only the first k elements of the merge, O(k). That
beats the full merge for small k, but when k is comparable to m and n it is
still O(m + n).

What is really wanted is a binary search exploiting the sortedness of A and
B. Suppose the first k elements of the union consist of the first x
elements of A and the first k - x elements of B; binary search determines
x.

Keep an interval [b, t] containing x, iterating while b < t and halving it
each time. At the midpoint x = b + floor((t - b) / 2):
  * If A[x] < B[(k - x) - 1], then A[x] must be among the first k - 1
    elements of the union, so set b = x + 1 and continue.
  * Similarly, if A[x - 1] > B[k - x], then A[x - 1] cannot be among the
    first k elements, so set t = x - 1.
  * Otherwise B[(k - x) - 1] <= A[x] and A[x - 1] <= B[k - x]; the answer is
    the larger of A[x - 1] and B[(k - x) - 1], since the first x elements of
    A and the first k - x elements of B, in sorted order, end with one of
    those two.
If the loop ends without returning, then b = t, so x = b = t; return the
larger of A[x - 1] and B[(k - x) - 1] (if they are equal, either one).

The initial b and t must be chosen carefully: naively b = 0, t = k can
produce indices outside the arrays. Starting with b = max(0, k - n) and
t = min(m, k) resolves this.

The book prints one program, `find_kth_in_two_sorted_arrays(A, B, k)`. This
file implements the same partition binary search with a differently
structured loop (see TEXTBOOK CODE COMPARISON).

ADDITIONAL EXAMPLES (added for learning; not printed in this exercise)
---------------------------------------------------------------------
    a=[1, 3, 6], b=[2, 4, 5], k=4 -> 4   (merged: 1, 2, 3, 4, 5, 6)
"""


def find_kth_in_two_sorted_arrays(a: list[int],b: list[int],k: int) -> int:
    """Kth smallest (k is 1-based) of two sorted lists, by partition binary search.

    Based on the textbook's algorithm; the loop structure differs from the
    printed program. Type hints are documentation only.
    """

    # Added validation (not in the book): k must be a valid 1-based rank.
    if k<1 or k>len(a)+len(b):
        raise ValueError('k must be between 1 and total length')

    # Lower bound of elements we will choose in a: at least k - len(b),
    # because b can supply at most len(b) of the k elements.
    low=max(0,k-len(b))

    # Upper bound of elements we will choose in a.
    high=min(len(a),k)
    while low<=high:

        # x = number of elements taken from a; `//` is floor division.
        x=(low+high)//2

        # Conditional expressions `X if cond else Y` supply sentinels at the
        # array edges. float('-inf') / float('inf') are negative / positive
        # infinity, which compare below / above every number, so "no element
        # on this side" never blocks a comparison.
        # ax_left = a[x-1] (last taken from a), ax = a[x] (first not taken).
        ax_left=float('-inf') if x==0 else a[x-1]
        ax=float('inf') if x==len(a) else a[x]

        # by = number taken from b; by_left = b[by-1], by_right = b[by].
        by=k-x
        by_left=float('-inf') if by==0 else b[by-1]
        by_right=float('inf') if by==len(b) else b[by]

        # A[x] < B[(k-x)-1]: too few taken from a.
        if ax<by_left:
            low=x+1

        # A[x-1] > B[k-x]: too many taken from a.
        elif ax_left>by_right:
            high=x-1

        # B[k-x-1] <= A[x] and A[x-1] <= B[k-x]: a valid split; the kth
        # element is the larger of the two last-taken elements.
        else:
            return max(ax_left,by_left)

    # Unreachable for sorted inputs and valid k; reached only if the inputs
    # are not sorted.
    raise RuntimeError('Sorted input required')


# TEXTBOOK POST-SOLUTION DISCUSSION (page 373)
# --------------------------------------------
# Each iteration halves the length of [b, t], so the time complexity is
# O(log k).
#
# VARIANTS
# The book gives no variants for this exercise.


# TEXTBOOK CODE COMPARISON
# ------------------------
# book: `def find_kth_in_two_sorted_arrays(A, B, k)`; bounds `b = max(0, k -
#   len(B))`, `t = min(len(A), k)`; loop `while b < t:` with
#   `x = b + (t - b) // 2` and variables `A_x_1`, `A_x`, `B_k_x_1`, `B_k_x`
#   (sentinels via `x <= 0`, `x >= len(A)`, `k - x <= 0`, `k - x >= len(B)`);
#   same three branches; after the loop it computes `A_b_1`, `B_k_b_1` and
#   returns their max. No input validation.
# file: parameters renamed `a, b` with type hints; bounds named `low` /
#   `high`; loop `while low <= high:` with `x = (low + high) // 2`; variables
#   renamed `ax_left`, `ax`, `by`, `by_left`, `by_right` (sentinel tests use
#   `==` instead of `<=`/`>=`); the post-loop return is replaced by
#   `raise RuntimeError('Sorted input required')`; an added ValueError check
#   for k outside 1..len(a)+len(b). Same results for valid input.


# Python executes this block only when this source file is run directly.
# When pytest imports the file, this block is skipped automatically.
# Documentation: https://docs.python.org/3/library/__main__.html
if __name__=='__main__':

    # The merged order is 1, 2, 3, 4, 5, 6, so the 4th smallest is 4.
    # `assert` raises AssertionError on mismatch; the tests/ folder holds
    # the thorough pytest suite.
    print('4th across two arrays:',find_kth_in_two_sorted_arrays([1,3,6],[2,4,5],4))
    assert find_kth_in_two_sorted_arrays([1,3,6],[2,4,5],4)==4
