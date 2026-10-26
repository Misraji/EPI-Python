"""EPI Python — Exercise 24.15: Search a Sorted Array of Unknown Length

Chapter 24: Honors Class
Textbook: pages 370–372 (printed page numbers; introduction on 370,
statement, hint, solution and most of the program on 371, the program's end
and its analysis on 372).

PROBLEM (from the textbook)
---------------------------
Binary search is usually applied to an array of known length. Sometimes,
the array is "virtual", i.e., it is an abstraction of data that is spread
across multiple machines. In such cases, the length is not known in
advance; accessing elements beyond the end results in an exception.

Design an algorithm that takes a sorted array whose length is not known,
and a key, and returns an index of an array element which is equal to the
key. Assume that an out-of-bounds access throws an exception.

HINT (from the textbook)
------------------------
Can divide and conquer be used to find the end of the array?

SOLUTION DEVELOPMENT (following the textbook)
---------------------------------------------
Brute force: scan one element at a time until the key is found or an
exception is raised (meaning the key is absent). O(n), n the array length.

Use sortedness instead. With a known length, binary search would do. The
length can be found by testing whether indices 0, 1, 3, 7, 15, ... are
valid; at the first invalid index, say 2^i - 1, binary search over
[2^(i-1), 2^i - 2] finds the first invalid index, which is the length.

Better still: compare the element at index 2^i - 1 with the key. If it is
greater than the key, binary search for the key over indices
[2^(i-1), 2^i - 2]. Out-of-bounds indices can be handled just like valid
ones by treating them as holding infinity.

Worked examples (array of Figure 11.1 on Page 145, not reproduced here):
  * Key 243: examine indices 0, 1, 3, 7. Since A[7] = 285 > 243, do a
    conventional binary search for 243 over [4, 6].
  * Key 400: examine indices 0, 1, 3, 7, 15. Index 15 is invalid, so stop
    and binary search over [8, 14]. The first midpoint, 11, is out of
    bounds and treated as infinity, so the interval becomes [8, 10]. Next
    comes [8, 8], then the empty [8, 7]: 400 is not present.

The book prints one program, `binary_search_unknown_length(A, k)`,
implemented here with small differences.

ADDITIONAL EXAMPLES (added for learning; not printed in this exercise)
---------------------------------------------------------------------
    a=[1, 3, 5, 7, 9], k=7 -> 3
"""


def binary_search_unknown_length(a, k: int) -> int:
    """Textbook implementation: exponential probing, then binary search.

    `a` can be any sorted sequence supporting a[i] that raises IndexError
    out of bounds; len(a) is never called. Returns an index of k, or -1.
    `k: int` and `-> int` are type hints, not enforced by Python.
    """

    # Find the possible range where k exists.
    p=0

    # `while True:` loops forever until a `break` or `return`.
    while True:

        # try/except: if any statement in the `try` block raises IndexError
        # (an out-of-bounds a[idx]), control jumps to the `except
        # IndexError:` block instead of crashing. This is how the unknown
        # end of the array is detected.
        # https://docs.python.org/3/tutorial/errors.html#handling-exceptions
        try:

            # `1 << p` is a left shift: 1 multiplied by 2**p. So idx is
            # 2^p - 1, probing 0, 1, 3, 7, 15, ...
            idx=(1<<p)-1
            if a[idx]==k:
                return idx

            # The probe exceeds k, so k (if present) lies before idx.
            if a[idx]>k:
                break
        except IndexError:
            break
        p+=1

    # Binary search between indices 2^(p - 1) and 2^p - 2, inclusive.
    # max(0, p-1) avoids a negative shift count (which raises ValueError).
    left,right=(1<<max(0,p-1)),(1<<p)-2

    # File addition: when p == 0 the search range starts at 0 (in practice
    # right is then -1 and the loop below does not run).
    if p==0:
        left=0
    while left<=right:

        # `//` is floor division. `left + (right - left) // 2` is the
        # midpoint; Python ints never overflow, so this form is just the
        # book's habit carried over from fixed-width languages.
        mid=left+(right-left)//2
        try:
            if a[mid]==k:
                return mid
            if a[mid]>k:
                right=mid-1
            else:
                left=mid+1

        # Search the left part if out-of-bounds: an invalid index behaves
        # like a value of infinity, greater than k.
        except IndexError:
            right=mid-1

    # Nothing matched k.
    return -1


# TEXTBOOK POST-SOLUTION DISCUSSION (page 372)
# --------------------------------------------
# The first loop runs O(log n) times, since the probed index doubles each
# iteration. The second loop is a conventional binary search, O(log n). The
# total time complexity is O(log n).
#
# VARIANTS
# The book gives no variants for this exercise.


# TEXTBOOK CODE COMPARISON
# ------------------------
# book: `def binary_search_unknown_length(A, k)`; probe loop uses
#   `if ... return idx` / `elif A[idx] > k: break`; then
#   `left, right = 1 << max(0, (p - 1)), (1 << p) - 2`; the search loop uses
#   `if / elif / else` inside `try`.
# file: parameter renamed `a` (no hint) and `k: int`, `-> int` added; `elif`
#   written as a second `if` (equivalent here because the first branch
#   returns); an added `if p == 0: left = 0` statement after computing the
#   bounds (no effect on results, since right is -1 then). Otherwise the same
#   statements.


# Python executes this block only when this source file is run directly.
# When pytest imports the file, this block is skipped automatically.
# Documentation: https://docs.python.org/3/library/__main__.html
if __name__=='__main__':

    # A plain list stands in for the "virtual" array: indexing past its end
    # raises IndexError, which the function catches. 7 is at index 3.
    # `assert` raises AssertionError on mismatch; the tests/ folder holds
    # the thorough pytest suite.
    print('Index:',binary_search_unknown_length([1,3,5,7,9],7))
    assert binary_search_unknown_length([1,3,5,7,9],7)==3
