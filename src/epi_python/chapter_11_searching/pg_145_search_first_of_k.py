"""EPI Python — Exercise 11.1: Search a Sorted Array for First Occurrence of k

Chapter 11: Searching
Textbook: pages 145–146 (printed page numbers; problem and solution start
on 145, complexity remark and variants on 146).

PROBLEM (from the textbook)
---------------------------
"Binary search commonly asks for the index of any element of a sorted
array that is equal to a specified element. The following problem has a
slight twist on this."

    -14  -10   2  108  108  243  285  285  285  401
    A[0] A[1] A[2] A[3] A[4] A[5] A[6] A[7] A[8] A[9]
    (Figure 11.1: A sorted array with repeated elements.)

"Write a method that takes a sorted array and a key and returns the index
of the first occurrence of that key in the array. Return -1 if the key does
not appear in the array. For example, when applied to the array in
Figure 11.1 your algorithm should return 3 if the given key is 108; if it
is 285, your algorithm should return 6."

HINT (from the textbook)
------------------------
"What happens when every entry equals k? Don't stop when you first see k."

SOLUTION DEVELOPMENT (following the textbook)
---------------------------------------------
Naive approach: run an ordinary binary search to find *some* index holding
the key k (returning -1 if k is absent), then walk backwards from that index
until the first copy of k is reached. The binary search part costs
O(log n) for an array of n entries, but the backward walk can cost O(n) in
the worst case -- picture an array in which every entry equals k.

Key insight: binary search works by keeping a set of candidate answers and
shrinking it. Here, if the entry at index i equals k, we cannot yet tell
whether i is the *first* such index, but we do know that no index after i
can be the first one. So every index i + 1 and above is discarded from the
candidate set, and i is remembered as the best answer found so far.

Worked example from the book (Figure 11.1, k = 108):
  1. Candidates start as all indices, [0, 9].
  2. Midpoint 4 holds 108 = k: record 4 as an occurrence, candidates
     become [0, 3].
  3. Midpoint 1 holds -10 < k: candidates become [2, 3].
  4. Midpoint 2 holds 2 < k: candidates become [3, 3].
  5. Midpoint 3 holds 108 = k: the first-seen occurrence is updated to 3.
  6. The interval is now [3, 2], which is empty, so the search stops and
     the answer is 3.

The implementation below, search_first_of_k, follows this idea.

ADDITIONAL EXAMPLES (added for learning; not printed in this exercise)
---------------------------------------------------------------------
    sorted_array=[],              key=5 -> -1 (empty array)
    sorted_array=[1, 2, 2, 2, 3], key=2 -> 1
    sorted_array=[1, 2, 3],       key=1 -> 0 (key at the very start)
    sorted_array=[1, 2, 3],       key=9 -> -1 (key absent)
    sorted_array=[3, 3, 3],       key=3 -> 0 (every entry equals k)
"""


def search_first_of_k(sorted_array: list[int], key: int) -> int:
    """Return index of first key occurrence, or -1.

    This is the textbook's search_first_of_k (the only implementation given
    for this exercise), with the `>` and `==` branches merged into one `>=`
    branch.

    Type hints: `sorted_array: list[int]` says the argument is expected to
    be a list of ints, and `-> int` says an int is returned. Python records
    these annotations but does not enforce them at run time.
    """

    # Tuple unpacking assigns both names in one statement. The candidate set
    # is always the slice sorted_array[left:right + 1]; for an empty list,
    # right starts at -1 so the loop below never runs.
    left, right = 0, len(sorted_array) - 1

    # -1 is the "not found" answer, returned unchanged if key never appears.
    result = -1
    while left <= right:

        # `//` is floor division: it divides and rounds down to an int, so
        # middle is always a valid index between left and right. (Python
        # ints are unbounded, so left + right cannot overflow here.)
        middle = (left + right) // 2

        # When the midpoint is >= key, the first occurrence (if any) cannot
        # be to the right of middle, so the right half is discarded. If it
        # is an exact match, it is remembered as the best answer so far --
        # we do NOT stop, because an earlier copy may exist (the hint).
        if sorted_array[middle] >= key:
            if sorted_array[middle] == key:
                result = middle
            right = middle - 1

        # Otherwise sorted_array[middle] < key, so middle and everything to
        # its left are too small and can be discarded.
        else:
            left = middle + 1
    return result


# TEXTBOOK POST-SOLUTION DISCUSSION (pages 145–146)
# -------------------------------------------------
# Complexity: still O(log n) time, because every iteration halves the size
# of the candidate set. Only a few index variables are used, so the extra
# space is O(1).
#
# VARIANTS
# --------
# Variant 1 (stated in the book; no solution given): Design an efficient
#   algorithm that takes a sorted array and a key, and finds the index of
#   the first occurrence of an element greater than that key. For the array
#   in Figure 11.1, the answer should be 9 when the key is 285, and 1 when
#   the key is -13.
#
# Variant 2 (stated in the book; no solution given): Let A be an unsorted
#   array of n integers with A[0] >= A[1] and A[n - 2] <= A[n - 1]. Call
#   index i a "local minimum" if A[i] is less than or equal to its
#   neighbors. How would you efficiently find a local minimum, if one
#   exists?
#
# Variant 3 (stated in the book; no solution given): Write a program that
#   takes a sorted array A of integers and an integer k, and returns the
#   interval enclosing k, i.e., the pair of integers L and U such that L is
#   the first occurrence of k in A and U is the last occurrence of k in A.
#   If k does not appear in A, return [-1, -1]. For example, if
#   A = <1, 2, 2, 4, 4, 4, 7, 11, 11, 13> and k = 11, return [7, 8].
#
# Variant 4 (stated in the book; no solution given): Write a program which
#   tests if p is a prefix of a string in an array of sorted strings.


# TEXTBOOK CODE COMPARISON
# ------------------------
# Book: `def search_first_of_k(A, k):` with
#   `left, right, result = 0, len(A) - 1, -1` and a three-way
#   if / elif / else (`A[mid] > k`, `A[mid] == k`, else `A[mid] < k`),
#   including the comments "A[left:right + 1] is the candidate set." and
#   "Nothing to the right of mid can be solution."
# File: parameters renamed `sorted_array: list[int]` and `key: int`, return
#   type hint `-> int` added; the local `mid` is renamed `middle`; `result`
#   is initialised in a separate statement; the `>` and `==` branches are
#   merged into a single `>= key` branch with a nested `== key` test. The
#   behaviour is the same as the book's listing.


# Python executes this block only when this source file is run directly.
# When pytest imports the file, this block is skipped automatically.
# Documentation: https://docs.python.org/3/library/__main__.html
if __name__ == "__main__":
    # Run a few self-contained examples before exploring the pytest suite.
    # They cover an empty array, a run of duplicates, a key at index 0, an
    # absent key, and an array where every entry equals the key.
    #
    # `assert` stops the program with an AssertionError if a result is
    # different from the expected value. These are quick smoke checks;
    # pytest provides the more thorough automated verification.
    observed = search_first_of_k([], 5)
    print("search_first_of_k:", observed)
    assert observed == -1
    observed = search_first_of_k([1, 2, 2, 2, 3], 2)
    print("search_first_of_k:", observed)
    assert observed == 1
    observed = search_first_of_k([1, 2, 3], 1)
    print("search_first_of_k:", observed)
    assert observed == 0
    observed = search_first_of_k([1, 2, 3], 9)
    print("search_first_of_k:", observed)
    assert observed == -1
    observed = search_first_of_k([3, 3, 3], 3)
    print("search_first_of_k:", observed)
    assert observed == 0
