"""EPI Python — Exercise 16.12: Find the Longest Nondecreasing Subsequence

Chapter 16: Dynamic Programming
Textbook: pages 257–258 (printed page numbers; problem and solution start on 257).

PROBLEM (from the textbook)
---------------------------
"The problem of finding the longest nondecreasing subsequence in a sequence
of integers has implications to many disciplines, including string matching
and analyzing card games. As a concrete instance, the length of a longest
nondecreasing subsequence for the array in Figure 16.15 is 4. There are
multiple longest nondecreasing subsequences, e.g., <0,4,10,14> and
<0,2,6,9>. Note that elements of non-decreasing subsequence are not
required to immediately follow each other in the original sequence."

Figure 16.15 (an array whose longest nondecreasing subsequences have
length 4):
    index:  0  1  2   3  4   5  6   7  8  9
    A:      0  8  4  12  2  10  6  14  1  9

"Write a program that takes as input an array of numbers and returns the
length of a longest nondecreasing subsequence in the array."

HINT (from the textbook)
------------------------
"Express the longest nondecreasing subsequence ending at an entry in terms
of the longest nondecreasing subsequence appearing in the subarray
consisting of preceding elements."

SOLUTION DEVELOPMENT (following the textbook)
---------------------------------------------
Brute force: enumerate all 2^n subsequences of a length-n array and test
each one. Heuristic pruning helps a little but makes the program very
cumbersome, and the time is still huge.

Use the entries already processed: if we know the lengths of the longest
nondecreasing subsequences ending at indices 0..5, then the longest one
ending at index 6 is found by looking for the longest one ending at an
entry of A[0, 5] whose value is <= A[6]. In Figure 16.15 there are two,
ending at indices 2 and 4, each giving a subsequence of length 3 ending at
A[6].

Define L[i] as the length of the longest nondecreasing subsequence of A
that ends at (and includes) index i; e.g. L[6] = 3 for Figure 16.15. That
subsequence is either just A[i] (length 1, when A[i] is smaller than all
earlier entries), or has some penultimate index j, in which case the part
up to j must be a longest subsequence ending at j. So

    L[i] = 1 if A[i] is less than all previous entries,
    L[i] = 1 + max{L[j] | j < i and A[j] <= A[i]} otherwise.

L can be computed recursively or iteratively. To recover the subsequence
itself, also store for each i the index of the last element of the
subsequence that was extended to obtain L[i].

Computing L for Figure 16.15:
 1. L[0] = 1 (no entries before index 0)
 2. L[1] = 1 + max(L[0]) = 2 (A[0] <= A[1])
 3. L[2] = 1 + max(L[0]) = 2 (A[0] <= A[2] and A[1] > A[2])
 4. L[3] = 1 + max(L[0], L[1], L[2]) = 3 (A[0], A[1], A[2] <= A[3])
 5. L[4] = 1 + max(L[0]) = 2 (A[0] <= A[4]; A[1], A[2], A[3] > A[4])
 6. L[5] = 1 + max(L[0], L[1], L[2], L[4]) = 3 (A[0], A[1], A[2], A[4] <=
    A[5] and A[3] > A[5])
 7. L[6] = 1 + max(L[0], L[2], L[4]) = 3 (A[0], A[2], A[4] <= A[6];
    A[1], A[3], A[5] > A[6])
 8. L[7] = 1 + max(L[0], ..., L[6]) = 4 (A[0] .. A[6] <= A[7])
 9. L[8] = 1 + max(L[0]) = 2 (A[0] <= A[8]; A[1] .. A[7] > A[8])
10. L[9] = 1 + max(L[0], L[1], L[2], L[4], L[6], L[8]) = 4 (A[0], A[1],
    A[2], A[4], A[6], A[8] <= A[9]; A[3], A[5], A[7] > A[9])
So the maximum length is 4; examples of length 4 are <0,8,12,14>,
<0,2,6,9>, <0,4,6,9>.

The book then gives an iterative implementation,
longest_nondecreasing_subsequence_length(A) -> `longest_nondecreasing_subsequence`
below. The file also contains `longest_nondecreasing_subsequence_fast`, an
O(n log n) method that is NOT printed in the book (it addresses the book's
last variant, for which no solution is given).

ADDITIONAL EXAMPLES (added for learning; not printed in this exercise)
---------------------------------------------------------------------
    []               -> 0
    [1]              -> 1
    [3, 1, 2, 2, 5]  -> 4   (1, 2, 2, 5: equal values are allowed)
    [5, 4, 3]        -> 1
    [2, 2, 2]        -> 3
"""

# Python standard library: binary search on sorted lists.
# Module documentation: https://docs.python.org/3/library/bisect.html
# bisect_right API: https://docs.python.org/3/library/bisect.html#bisect.bisect_right
from bisect import bisect_right


def longest_nondecreasing_subsequence(values: list[int]) -> int:
    """Textbook's O(n^2) iterative DP (book: longest_nondecreasing_subsequence_length).

    best_ending_here[i] is L[i]: the length of the longest nondecreasing
    subsequence ENDING at index i. Equality is allowed. An empty list
    returns 0 (a guard not in the book).
    """

    # Type hints such as `list[int]` document intended types only.
    if not values:
        return 0

    # Every entry by itself is a subsequence of length 1.
    best_ending_here = [1] * len(values)

    # enumerate(values) yields (index, value) pairs.
    for i, value in enumerate(values):

        # Every earlier entry values[j] <= value can be followed by value,
        # giving a subsequence of length best_ending_here[j] + 1. The
        # built-in max(a, b) keeps the larger.
        for j in range(i):
            if values[j] <= value:
                best_ending_here[i] = max(
                    best_ending_here[i], best_ending_here[j] + 1
                )

    # The longest subsequence may end anywhere; max(list) is its largest
    # item (it would raise ValueError on an empty list, hence the guard).
    return max(best_ending_here)


def longest_nondecreasing_subsequence_fast(values: list[int]) -> int:
    """O(n log n) length computation; NOT a printed textbook implementation.

    Added for comparison; it addresses the book's variant "Compute the
    longest nondecreasing subsequence in O(n log n) time" (no solution is
    given in the book). minimum_tails[k] is the smallest possible last value
    of a nondecreasing subsequence of length k + 1 seen so far; the list
    stays sorted.
    """
    minimum_tails: list[int] = []
    for number in values:

        # bisect_right(sorted_list, x) uses binary search (O(log n)) to
        # return the insertion point for x AFTER any existing equal values,
        # i.e. the index of the first element strictly greater than x. An
        # equal item may extend a nondecreasing subsequence, so equal tails
        # must be skipped over (bisect_left would give the strictly
        # increasing version).
        # Documentation: https://docs.python.org/3/library/bisect.html#bisect.bisect_right
        index = bisect_right(minimum_tails, number)

        # Past the end: `number` extends the longest subsequence so far.
        # Otherwise it becomes a smaller (better) tail for length index + 1.
        if index == len(minimum_tails):
            minimum_tails.append(number)
        else:
            minimum_tails[index] = number

    # The number of tails is the length of the longest subsequence. (The
    # list itself is generally NOT such a subsequence.)
    return len(minimum_tails)


# TEXTBOOK POST-SOLUTION DISCUSSION (page 258)
# --------------------------------------------
# Time O(n^2): each L[i] takes O(n) time. Space O(n), to store L.
#
# VARIANTS (each stated in the book; no solution given)
# ----------------------------------------------------
# 1. Write a program that takes an array of numbers and returns a longest
#    nondecreasing subsequence in the array (the subsequence, not just its
#    length).
# 2. A sequence <a_0, a_1, ..., a_{n-1}> is alternating if a_i < a_{i+1}
#    for even i and a_i > a_{i+1} for odd i. Given an array A of length n,
#    find a longest subsequence <i_0, ..., i_{k-1}> such that
#    <A[i_0], A[i_1], ..., A[i_{k-1}]> is alternating.
# 3. A sequence is weakly alternating if no three consecutive terms are
#    increasing or decreasing. Given A of length n, find a longest
#    subsequence <i_0, ..., i_{k-1}> such that <A[i_0], ..., A[i_{k-1}]> is
#    weakly alternating.
# 4. A sequence is convex if a_i < (a_{i-1} + a_{i+1}) / 2 for
#    1 <= i <= n - 2. Given A of length n, find a longest subsequence
#    <i_0, ..., i_{k-1}> such that <A[i_0], ..., A[i_{k-1}]> is convex.
# 5. A sequence is bitonic if there is a k such that a_i < a_{i+1} for
#    0 <= i < k and a_i > a_{i+1} for k <= i < n - 1. Given A of length n,
#    find a longest subsequence <i_0, ..., i_{k-1}> such that
#    <A[i_0], ..., A[i_{k-1}]> is bitonic.
# 6. A sequence of points in the plane is ascending if each point is above
#    and to the right of the previous point. How would you find a maximum
#    ascending subset of a set of points in the plane?
# 7. Compute the longest nondecreasing subsequence in O(n log n) time.


# TEXTBOOK CODE COMPARISON
# ------------------------
# * Book: `def longest_nondecreasing_subsequence_length(A)`; file
#   `def longest_nondecreasing_subsequence(values: list[int]) -> int`
#   (renamed function and parameter, type hints added).
# * Book list `max_length`; file `best_ending_here`. Book loops
#   `for i in range(1, len(A))` and computes each entry in one expression:
#   `max_length[i] = max(1 + max([max_length[j] for j in range(i) if A[i] >=
#   A[j]], default=0), max_length[i])`. File uses `enumerate` over all i and
#   an explicit inner loop updating with `max(...)` (same values).
# * File adds `if not values: return 0` (the book's final `max(max_length)`
#   would raise ValueError on an empty list).
# * `longest_nondecreasing_subsequence_fast` (bisect_right, O(n log n)) and
#   the `bisect` import are NOT in the book; they are an added helper.


# Python executes this block only when this source file is run directly.
# When pytest imports the file, this block is skipped automatically.
# Documentation: https://docs.python.org/3/library/__main__.html
if __name__ == "__main__":

    # Added examples for the textbook DP: empty input, one element, a mix
    # with equal values, a strictly decreasing list, and all-equal values;
    # then the added fast version on the mixed example.
    # `assert` stops the program with an AssertionError if the condition is
    # false; these are quick smoke checks, the pytest suite is thorough.
    result=longest_nondecreasing_subsequence([])
    print('longest_nondecreasing_subsequence', result)
    assert result == 0
    result=longest_nondecreasing_subsequence([1])
    print('longest_nondecreasing_subsequence', result)
    assert result == 1
    result=longest_nondecreasing_subsequence([3, 1, 2, 2, 5])
    print('longest_nondecreasing_subsequence', result)
    assert result == 4
    result=longest_nondecreasing_subsequence([5, 4, 3])
    print('longest_nondecreasing_subsequence', result)
    assert result == 1
    result=longest_nondecreasing_subsequence([2, 2, 2])
    print('longest_nondecreasing_subsequence', result)
    assert result == 3
    assert longest_nondecreasing_subsequence_fast([3, 1, 2, 2, 5]) == 4
    print("PDF quadratic DP and optional binary-search optimization: passed")
