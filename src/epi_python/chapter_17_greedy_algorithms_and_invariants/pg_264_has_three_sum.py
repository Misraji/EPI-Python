"""EPI Python — Exercise 17.4: The 3-Sum Problem

Chapter 17: Greedy Algorithms and Invariants
Textbook: pages 264–266 (printed page numbers; the "Invariants boot camp"
helper has_two_sum is on 264, the problem starts on 264, the solution and
program are on 265, and the last variants end on 266).

PROBLEM (from the textbook)
---------------------------
Design an algorithm that takes as input an array and a number, and
determines if there are three entries in the array (not necessarily
distinct) which add up to the specified number. For example, if the array
is <11, 2, 5, 7, 3> then there are three entries in the array which add up
to 21 (3, 7, 11 and 5, 5, 11). (Note that we can use 5 twice, since the
problem statement said we can use the same entry more than once.) However,
no three entries add up to 22.

HINT (from the textbook)
------------------------
How would you check if a given array entry can be added to two more entries
to get the specified number?

SOLUTION DEVELOPMENT (following the textbook)
---------------------------------------------
Background from the "Invariants boot camp" (page 264), which this solution
builds on. Two-sum in a SORTED array: decide whether two entries add up to
a target. Example: in <-2, 1, 2, 4, 7, 11> some entries add to 6, to 0 and
to 13, but none add to 10.
  - Brute force: two nested loops, O(n^2).
  - Hash table: insert every element, then for each element e look up
    K - e (K the target). O(n) time but O(n) extra storage.
  - Invariant approach (best): maintain a subarray that is guaranteed to
    contain a solution if one exists. Start with the whole array and shrink
    it from one end each step, using sortedness: if leftmost + rightmost is
    less than the target, the leftmost element can never be part of a
    solution, so drop it; symmetrically, if the sum is too big, drop the
    rightmost element. The book's function has_two_sum(A, t) does this with
    two indices i and j (looping while i <= j, so an entry may pair with
    itself). Time O(n), space O(1) because the subarray is just two
    variables.

Now the 3-sum problem itself. Let A be the input array and t the target.

1. Brute force: try all triples with three nested loops. Time O(n^3),
   space O(1).
2. Hash table: store all entries in a hash table, then for every pair
   A[i] + A[j] look up t - (A[i] + A[j]). Time O(n^2), but space O(n).
3. Sort first to avoid extra space: for each A[i], look for indices j, k
   with A[j] + A[k] = t - A[i]. Iterating over A[j] and binary searching
   for A[k] makes each such search O(n log n).
4. Improve each search to O(n) with the two-pointer idea: start with
   A[0] + A[n - 1]. If it equals t - A[i], done. If it is smaller, move to
   A[1] + A[n - 1]: A[0] cannot pair with anything to reach t - A[i], since
   A[n - 1] is the largest value. If it is larger, move to A[0] + A[n - 2].
   Each step eliminates one entry in O(1) time, giving O(n) per search. The
   invariant: if two elements summing to the desired value exist, they lie
   inside the subarray currently under consideration.

Book worked example: sorting <11, 2, 5, 7, 3> gives <2, 3, 5, 7, 11>. For
A[0] = 2, checking whether some A[j], A[k] give A[0] + A[j] + A[k] = 21
means searching for two entries that add up to 21 - 2 = 19.

The book's program has_three_sum(A, t) sorts A in place and returns
any(has_two_sum(A, t - a) for a in A). This file's has_three_sum
implements the same algorithm with the two-sum loop written inline (see
TEXTBOOK CODE COMPARISON below).

ADDITIONAL EXAMPLES (added for learning; not printed in this exercise)
---------------------------------------------------------------------
    values=[],        target=0  -> False (no entries at all)
    values=[1, 2, 3], target=6  -> True  (1 + 2 + 3)
    values=[1, 2, 3], target=9  -> True  (3 + 3 + 3, repetition allowed)
    values=[1, 2, 3], target=0  -> False
    values=[0],       target=0  -> True  (0 + 0 + 0)
"""


# Type hints: `values: list[int]`, `target: int` and `-> bool` document the
# expected types. Python stores but does NOT enforce annotations.
def has_three_sum(values: list[int], target: int) -> bool:
    """Check whether three values (repetitions allowed) sum to target.

    Implements the textbook's sort-then-two-pointer solution (book:
    has_three_sum calling has_two_sum), with the two-sum search inlined.
    Unlike the book, the caller's list is not modified.
    """

    # sorted(iterable) creates a NEW sorted list without modifying the input.
    # (The book instead calls A.sort(), which reorders the caller's list.)
    # The two-pointer search below is only correct on sorted data.
    # Documentation: https://docs.python.org/3/library/functions.html#sorted
    ordered = sorted(values)

    # Fix each entry in turn as the first of the three numbers; the inner
    # loop then solves two-sum for target - candidate.
    for candidate in ordered:

        # Tuple unpacking sets both pointers at once: the subarray
        # ordered[left..right] is the region that must contain the other
        # two entries if they exist (the book's invariant).
        left, right = 0, len(ordered) - 1

        # `<=` rather than `<` lets left == right, i.e. the same entry may
        # be used twice, as the problem allows ("not necessarily distinct").
        while left <= right:
            total = candidate + ordered[left] + ordered[right]
            if total == target:
                return True

            # Too small: ordered[left] cannot reach the target even with the
            # largest remaining value, so discard it. Too large:
            # ordered[right] is too big even with the smallest remaining
            # value, so discard it.
            if total < target:
                left += 1
            else:
                right -= 1
    return False


# TEXTBOOK POST-SOLUTION DISCUSSION (page 265)
# --------------------------------------------
# Extra space is O(1) (beyond the in-place sort in the book's version). Time
# is the sort, O(n log n), plus n runs of the O(n) sorted two-sum search,
# which is O(n^2) overall.
#
# (Note for this file: because it uses sorted(), it allocates an O(n)
# sorted copy, which the book's in-place version does not.)
#
# VARIANTS
# --------
# Variant 1 (stated in the book; no solution given): Solve the same problem
# when the three elements must be distinct. For example, if A =
# <5, 2, 3, 4, 3> and t = 9, then A[2] + A[2] + A[2] is not acceptable,
# A[2] + A[2] + A[4] is not acceptable, but A[1] + A[2] + A[3] and
# A[1] + A[3] + A[4] are acceptable.
#
# Variant 2 (stated in the book; no solution given): Solve the same problem
# when k, the number of elements to sum, is an additional input.
#
# Variant 3 (stated in the book; no solution given): Write a program that
# takes as input an array of integers A and an integer T, and returns a
# 3-tuple (A[p], A[q], A[r]) where p, q, r are all distinct, minimizing
# |T - (A[p] + A[q] + A[r])|, and A[p] <= A[r] <= A[s]. (The last condition
# is reproduced as printed on page 266; it mentions an index s that is not
# otherwise defined.)
#
# Variant 4 (stated in the book; no solution given): Write a program that
# takes as input an array of integers A and an integer T, and returns the
# number of 3-tuples (p, q, r) such that A[p] + A[q] + A[r] <= T and
# A[p] <= A[q] <= A[r].


# TEXTBOOK CODE COMPARISON
# ------------------------
# - Book: two functions, `def has_two_sum(A, t)` (boot camp, page 264) and
#   `def has_three_sum(A, t)` (page 265) whose body is `A.sort()` and
#   `return any(has_two_sum(A, t - a) for a in A)` with the comment "Finds
#   if the sum of two numbers in A equals to t - a."
# - File: only `def has_three_sum(values: list[int], target: int) -> bool`
#   (parameters renamed from A, t; type hints added). The book's
#   has_two_sum helper is NOT a separate function here; its two-pointer
#   loop is inlined, comparing candidate + ordered[left] + ordered[right]
#   with target instead of A[i] + A[j] with t - a.
# - The file uses `sorted(values)` (new list; input untouched) instead of
#   the book's in-place `A.sort()`.
# - The book's any(...) generator is replaced by an explicit for loop with
#   an early `return True`. Same results.


# Python executes this block only when this source file is run directly.
# When pytest imports the file, this block is skipped automatically.
# Documentation: https://docs.python.org/3/library/__main__.html
if __name__ == "__main__":

    # Run a few self-contained examples before exploring the pytest suite:
    # an empty list, an exact triple, a repeated entry (3 + 3 + 3), an
    # unreachable target, and a single zero used three times.
    #
    # `assert` raises AssertionError if its condition is False; these are
    # quick smoke checks, pytest does the thorough testing.
    observed = has_three_sum([], 0)
    print("has_three_sum:", observed)
    assert observed == False
    observed = has_three_sum([1, 2, 3], 6)
    print("has_three_sum:", observed)
    assert observed == True
    observed = has_three_sum([1, 2, 3], 9)
    print("has_three_sum:", observed)
    assert observed == True
    observed = has_three_sum([1, 2, 3], 0)
    print("has_three_sum:", observed)
    assert observed == False
    observed = has_three_sum([0], 0)
    print("has_three_sum:", observed)
    assert observed == True
