"""EPI Python — Exercise 24.34: Find the Longest Subarray Whose Sum <= k

Chapter 24: Honors Class
Textbook: pages 400–402 (printed page numbers; problem starts on 400,
solution on 401).

PROBLEM (from the textbook)
---------------------------
The book considers the longest subarray subject to a constraint on its sum.
For the array of Figure 24.11 (page 400),

    A[0..9] = <431, -15, 639, 342, -14, 565, -924, 635, 167, -70>,

the longest subarray whose sum is no more than 184 is A[3, 6].

"Design an algorithm that takes as input an array A of n numbers and a key k,
and returns the length of a longest subarray of A for which the subarray sum
is less than or equal to k."

HINT (from the textbook)
------------------------
"When can you be sure that an index i cannot be the starting point of a
subarray with the desired property, without looking past i?"

SOLUTION DEVELOPMENT (following the textbook)
---------------------------------------------
Brute force: compute the sum of A[i, j] for every 0 <= i <= j <= n - 1. With
the prefix-sum array P, P[i] = A[0] + ... + A[i] (one O(n) pass), the sum of
A[i, j] is P[j] - P[i - 1], taking P[-1] = 0. That is O(n^2) time and O(n)
extra space (for P).

Key observation for O(n): if u < v and P[u] >= P[v], then u can never be the
best ending point. For any w <= u, A[w, v] is longer than A[w, u], and if
A[w, u] meets the constraint, so does A[w, v]. This motivates the array Q of
suffix minima of P: Q[n - 1] = P[n - 1] and Q[i] = min(P[i], Q[i + 1]) for
i < n - 1.

For indices a <= b, let M(a, b) be the minimum possible sum of a subarray
that starts at a and extends to b or beyond. Then M(0, b) = Q[b] and
M(a, b) = Q[b] - P[a - 1] for a > 0.
* If M(a, b) > k, no subarray starting at a and containing b satisfies the
  constraint, so a can be incremented.
* If M(a, b) <= k, some subarray of length at least b - a + 1 satisfies it,
  so compare b - a + 1 with the best length so far, update if larger, and
  increment b.
Start with a = b = 0 and apply these increments until b = n; this finds the
maximum length. The book proves this after the program (see the
post-solution notes below).

The book prints one program; find_longest_subarray_less_equal_k below
follows it.

ADDITIONAL EXAMPLES (added for learning; not printed in this exercise)
---------------------------------------------------------------------
    A = [1, 2, -3, 4], k = 3        -> 3  (e.g. [1, 2, -3], sum 0)
    A = [4, -3, 2, 1, -4, 5], k = 3 -> printed by the __main__ block
"""

# Python standard library: iterator building blocks.
# Module documentation: https://docs.python.org/3/library/itertools.html
# accumulate API: https://docs.python.org/3/library/itertools.html#itertools.accumulate
import itertools


# Type hints: `a: list[int]`, `k: int`, `-> int` (a length). Annotations
# document expected types; Python does not enforce them.
def find_longest_subarray_less_equal_k(a: list[int], k: int) -> int:
    """Return the length of a longest subarray of `a` with sum <= k.

    This is the textbook's single implementation (prefix sums P, suffix
    minima Q, and two indices that only move forward).
    """

    # Added guard (not in the book): prefix_sum[-1] below would raise
    # IndexError for an empty list.
    if not a:
        return 0

    # Builds the prefix sum array P (book's comment). itertools.accumulate(a)
    # returns an iterator yielding running totals a[0], a[0]+a[1], ...;
    # it is lazy, so list(...) collects all values into a list that can be
    # indexed randomly.
    prefix_sum = list(itertools.accumulate(a))

    # Early return if the sum of the whole array is <= k (book's comment):
    # the entire array is then the longest subarray.
    if prefix_sum[-1] <= k:
        return len(a)

    # Builds Q = min_prefix_sum: Q[i] = min(P[i], Q[i + 1]).
    # prefix_sum[:] is a full slice, i.e. a shallow copy, so the original P
    # is kept. range(len(a)-2, -1, -1) counts down from n - 2 to 0 (the stop
    # value -1 is excluded, the step -1 goes backward).
    min_prefix_sum = prefix_sum[:]
    for i in range(len(a)-2,-1,-1):
        min_prefix_sum[i] = min(min_prefix_sum[i],min_prefix_sum[i+1])

    # Chained assignment: start (the book's a), end (b) and max_length all
    # begin at 0.
    start = end = max_length = 0
    while start<len(a) and end<len(a):

        # M(start, end) = Q[end] - P[start - 1], with P[-1] taken as 0. The
        # conditional expression `x if cond else y` handles start == 0
        # (0 is falsy). Without it, prefix_sum[-1] would be Python's last
        # element, not 0.
        minimum_sum = min_prefix_sum[end] - (prefix_sum[start-1] if start else 0)
        if minimum_sum <= k:

            # Some subarray from start extending to end or beyond fits:
            # record end - start + 1 and try a longer one.
            max_length = max(max_length,end-start+1)
            end += 1
        else:

            # minimum_sum > k: no subarray starting at `start` that reaches
            # `end` can work, so advance the start.
            start += 1
    return max_length


# TEXTBOOK POST-SOLUTION DISCUSSION (page 402)
# --------------------------------------------
# Correctness argument (paraphrased). Let A[a*, b*] be a longest subarray
# meeting the constraint. b is incremented until M(a, b) > k; in particular,
# when a moves to a + 1, A[a, b - 1] meets the constraint but A[a, b] does
# not, so A[a, b - 1] is the longest valid subarray starting at a.
#
# The loop ends when b = n. Then a >= a*: otherwise A[a, n - 1] would meet
# the constraint (b reached n) and be longer than A[a*, b*], since
# (n - 1) - a + 1 > b* - a* + 1, contradicting optimality. So a equals a* at
# some iteration. At that moment b <= b*, because A[a* - 1, b - 1] meets
# the constraint: if b > b*, that subarray would be longer than
# b* - a* + 1 (the book writes (b - 1) - (a* - 1) + 1 = b - a* + 1 >
# b* - a* + 1), contradicting the maximality of A[a*, b*]. With b <= b* and
# a = a*, the algorithm increments b until it reaches b* (A[a*, b*] meets the
# constraint), and so records b* - a* + 1 as the optimum.
#
# Complexity (from the solution development): O(n) time, since a and b only
# increase, and O(n) extra space for P and Q.
#
# VARIANTS
# --------
# * Design an algorithm for finding the longest subarray of a given array
#   such that the average of the subarray elements is <= k.
#   (stated in the book; no solution given)


# TEXTBOOK CODE COMPARISON
# ------------------------
# * Signature: book `def find_longest_subarray_less_equal_k(A, k)`; file
#   renames `A` to `a` and adds type hints.
# * Added: `if not a: return 0` guard.
# * Suffix minima: the book builds `min_prefix_sum` with
#   `list(reversed(functools.reduce(lambda s, v: s + [min(v, s[-1])],
#   reversed(prefix_sum[:-1]), [prefix_sum[-1]])))`; the file copies
#   `prefix_sum[:]` and fills it with an explicit backward `for` loop. No
#   `functools` import in the file. Same values.
# * Loop: book uses indices `a`, `b`, `min_curr_sum`, and
#   `min_prefix_sum[b] - prefix_sum[a - 1] if a > 0 else min_prefix_sum[b]`;
#   file uses `start`, `end`, `minimum_sum` and
#   `min_prefix_sum[end] - (prefix_sum[start-1] if start else 0)`.
#   The book updates the best length with `curr_length` and an `if`; the
#   file uses `max(...)`. Same logic.


# Python executes this block only when this source file is run directly.
# When pytest imports the file, this block is skipped automatically.
# Documentation: https://docs.python.org/3/library/__main__.html
if __name__ == '__main__':

    # Added example: print the answer for one array with k = 3.
    array = [4,-3,2,1,-4,5]
    print('Longest subarray with sum <= 3:', find_longest_subarray_less_equal_k(array,3))

    # `assert` stops with an AssertionError if the condition is false. This
    # checks a second added example ([1, 2, -3] has sum 0 <= 3, length 3).
    # pytest provides the more thorough verification.
    assert find_longest_subarray_less_equal_k([1,2,-3,4],3)==3
