"""EPI Python — Exercise 11.3: Search a Cyclically Sorted Array

Chapter 11: Searching
Textbook: pages 147–148 (printed page numbers; problem, solution and
program on 147, remark on duplicates and variants on 148).

PROBLEM (from the textbook)
---------------------------
"An array is said to be cyclically sorted if it is possible to cyclically
shift its entries so that it becomes sorted. For example, the array in
Figure 11.2 is cyclically sorted—a cyclic left shift by 4 leads to a
sorted array."

    378  478  550  631  103  203  220  234  279  368
    A[0] A[1] A[2] A[3] A[4] A[5] A[6] A[7] A[8] A[9]
    (Figure 11.2: A cyclically sorted array.)

"Design an O(log n) algorithm for finding the position of the smallest
element in a cyclically sorted array. Assume all elements are distinct. For
example, for the array in Figure 11.2, your algorithm should return 4."

HINT (from the textbook)
------------------------
"Use the divide and conquer principle."

SOLUTION DEVELOPMENT (following the textbook)
---------------------------------------------
Brute force: scan the whole array keeping a running minimum. This takes
O(n) time for an array of length n and ignores the array's structure.

Exploiting the structure of A, pick any index m and compare A[m] with the
last entry A[n - 1]:
  * If A[m] > A[n - 1], the "wrap-around" point lies after m, so the
    minimum must be at some index in [m + 1, n - 1].
  * If A[m] < A[n - 1], the stretch from m to the end is increasing, so no
    index in [m + 1, n - 1] can hold the minimum; it may, however, be m
    itself.
  * A[m] == A[n - 1] cannot happen (for m != n - 1) because all elements
    are distinct.

These two rules shrink the range on every step, giving a binary search.
In the program the comparison is made against the right end of the current
range, A[right], rather than always against A[n - 1].

The implementation below, search_smallest, follows this idea.

ADDITIONAL EXAMPLES (added for learning; not printed in this exercise)
---------------------------------------------------------------------
    []              -> -1 (empty-array guard added in this file)
    [4, 5, 1, 2, 3] -> 2
    [1, 2, 3]       -> 0 (not rotated at all)
    [2, 1]          -> 1
"""


def search_smallest(cyclic_sorted: list[int]) -> int:
    """Return index of the smallest entry in a rotated distinct sorted array.

    This is the textbook's search_smallest (the only implementation given),
    plus an extra guard that returns -1 for an empty list.

    Type hints: `list[int]` and `-> int` document the expected argument and
    return types; Python does not check them at run time.
    """

    # An empty list is falsy in Python, so `not cyclic_sorted` is True
    # exactly when there are no entries. Without this guard the function
    # would return index 0, which does not exist in an empty list.
    if not cyclic_sorted:
        return -1

    # Tuple unpacking sets both ends of the candidate range at once.
    left,right = 0,len(cyclic_sorted)-1

    # `<` (not `<=`): the loop stops when the range has shrunk to a single
    # index, left == right, which must be the minimum.
    while left < right:

        # `//` is floor division, so middle is an int with
        # left <= middle < right.
        middle=(left+right)//2

        # Book's comment: the minimum must be in A[mid + 1:right + 1].
        if cyclic_sorted[middle] > cyclic_sorted[right]:
            left = middle+1

        # Book's comment: here A[mid] < A[right]; the minimum cannot be in
        # A[mid + 1:right + 1], so it must be in A[left:mid + 1]. Note
        # right = middle (not middle - 1) keeps middle as a candidate.
        else:
            right = middle

    # Book's comment: the loop ends when left == right.
    return left


# TEXTBOOK POST-SOLUTION DISCUSSION (pages 147–148)
# -------------------------------------------------
# Time complexity: the same as binary search, O(log n). Extra space O(1).
#
# The book adds that, when elements may repeat, this problem cannot in
# general be solved in less than linear time. Example: if A consists of
# n - 1 copies of 1 and a single 0, the worst case requires inspecting every
# element to find the 0.
#
# VARIANTS
# --------
# Variant 1 (stated in the book; no solution given): A sequence is strictly
#   ascending if each element is greater than its predecessor. Suppose it is
#   known that an array A consists of a strictly ascending sequence followed
#   by a strictly descending sequence. Design an algorithm for finding the
#   maximum element in A.
#
# Variant 2 (stated in the book; no solution given): Design an O(log n)
#   algorithm for finding the position of an element k in a cyclically
#   sorted array of distinct elements.


# TEXTBOOK CODE COMPARISON
# ------------------------
# Book: `def search_smallest(A):` starting directly with
#   `left, right = 0, len(A) - 1`; same loop and branches, with the comments
#   quoted above.
# File: parameter renamed `cyclic_sorted: list[int]`, return hint `-> int`
#   added; `mid` renamed `middle`; an extra `if not cyclic_sorted: return -1`
#   guard for the empty list is added (not in the book -- the book's version
#   would return 0 for an empty list). The loop body otherwise matches.


# Python executes this block only when this source file is run directly.
# When pytest imports the file, this block is skipped automatically.
# Documentation: https://docs.python.org/3/library/__main__.html
if __name__ == "__main__":
    # Demonstrations check representative input/output behavior: the empty
    # list guard, a rotated list, an unrotated list and a two-element list.
    #
    # `assert` stops the program with an AssertionError if a result is
    # different from the expected value. These are quick smoke checks;
    # pytest provides the more thorough automated verification.
    observed = search_smallest([])
    print("search_smallest:", observed)
    assert observed == -1
    observed = search_smallest([4, 5, 1, 2, 3])
    print("search_smallest:", observed)
    assert observed == 2
    observed = search_smallest([1, 2, 3])
    print("search_smallest:", observed)
    assert observed == 0
    observed = search_smallest([2, 1])
    print("search_smallest:", observed)
    assert observed == 1
