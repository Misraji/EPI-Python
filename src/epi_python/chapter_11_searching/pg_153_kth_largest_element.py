"""EPI Python — Exercise 11.8: Find the kth Largest Element

Chapter 11: Searching
Textbook: pages 153–155 (printed page numbers; problem starts on 153,
program and average-case analysis on 154, worst case and variants on 155).

PROBLEM (from the textbook)
---------------------------
"Many algorithms require as a subroutine the computation of the kth
largest element of an array. The first largest element is simply the
largest element. The nth largest element is the smallest element, where n
is the length of the array.

For example, if the input array A = <3, 2, 1, 5, 4>, then A[3] is the first
largest element in A, A[0] is the third largest element in A, and A[2] is
the fifth largest element in A.

Design an algorithm for computing the kth largest element in an array."

HINT (from the textbook)
------------------------
"Use divide and conquer in conjunction with randomization."

SOLUTION DEVELOPMENT (following the textbook)
---------------------------------------------
Brute force: sort A in descending order and return the entry at index
k - 1. That is O(n log n) for n = len(A).

Sorting does more work than needed. For k = 1 (the largest element) a
single O(n) pass is enough.

For general k, a candidate set of k elements can be kept in a min-heap, as
in Solution 10.4 (page 138): O(n log k) time and O(k) space. That beats
sorting, but it is not in-place, and it still does extra work -- it
effectively produces the k largest elements in sorted order when only the
kth one is wanted.

In-place idea: choose an element at random (the "pivot") and partition the
remaining entries into those greater than the pivot and those less than it.
(The problem says the elements are distinct, so nothing else equals the
pivot.) Then:
  * exactly k - 1 elements greater than the pivot: the pivot is the kth
    largest;
  * more than k - 1 greater: the answer is greater than the pivot, so the
    pivot and everything smaller can be discarded;
  * fewer than k - 1 greater: the pivot and everything greater can be
    discarded.

On average each round halves the number of entries still under
consideration, which is why the approach is fast. A naive implementation
needs O(n) extra memory for the two groups, but that is avoided by doing the
partitioning inside the array itself.

The book's program numbers ranks from one. Its comment example: for
A = [3, 1, -1, 2], find_kth_largest(1, A) returns 3, find_kth_largest(2, A)
returns 2, find_kth_largest(3, A) returns 1, and find_kth_largest(4, A)
returns -1.

This file contains TWO functions:
  * find_kth_largest_pdf -- the book's randomized-pivot algorithm, with a
    partition helper that takes the comparison function (operator.gt).
  * find_kth_largest -- an earlier repository quickselect that is NOT the
    book's code: it uses a middle-position pivot and a two-pointer
    (Hoare-style) partition on a copy of the list.

ADDITIONAL EXAMPLES (added for learning; not printed in this exercise)
---------------------------------------------------------------------
    find_kth_largest(3, [3, 1, 5, 2, 4])     -> 3
    find_kth_largest_pdf(3, [3, 1, 5, 2, 4]) -> 3 (and the list is
                                                  rearranged in place)
    k outside 1..len(values)                 -> raises ValueError
"""

# Python standard library: functions corresponding to Python's operators.
# Module documentation: https://docs.python.org/3/library/operator.html
# operator.gt: https://docs.python.org/3/library/operator.html#operator.gt
import operator

# Python standard library: pseudo-random number generators.
# Module documentation: https://docs.python.org/3/library/random.html
# random.randint: https://docs.python.org/3/library/random.html#random.randint
# random.Random: https://docs.python.org/3/library/random.html#random.Random
import random


def find_kth_largest(k: int, values: list[int]) -> int:
    """Quickselect: find kth largest element (1-based), without full sorting.

    NOT the textbook's listing: this is a repository quickselect with a
    deterministic middle-position pivot and a two-pointer partition. The
    textbook's randomized version is find_kth_largest_pdf below. The
    caller's list is not modified (a copy is partitioned).

    Type hints: `k: int`, `values: list[int]`, `-> int` document expected
    types; Python does not enforce them.
    """

    # Chained comparison: `1 <= k <= len(values)` means
    # `1 <= k and k <= len(values)`. Ranks outside that range have no answer.
    # ValueError: https://docs.python.org/3/library/exceptions.html#ValueError
    if not 1 <= k <= len(values):
        raise ValueError("k out of bounds")

    # `values[:]` is a full slice, i.e. a shallow copy of the list. Rebinding
    # the local name means the swaps below never touch the caller's list.
    values = values[:]

    # The kth largest ends up at index k - 1 when the list is arranged in
    # DESCENDING order (larger values to the left).
    target = k - 1
    left, right = 0, len(values) - 1
    while left <= right:

        # Pivot is the value at the middle position (`//` = floor division).
        pivot_value = values[(left + right) // 2]
        i, j = left, right

        # Two-pointer partition for descending order: i moves right past
        # values larger than the pivot, j moves left past values smaller
        # than the pivot, and out-of-place pairs are swapped.
        while i <= j:
            while values[i] > pivot_value:
                i += 1
            while values[j] < pivot_value:
                j -= 1
            if i <= j:

                # Tuple swap: the right-hand side is evaluated first, then
                # unpacked, so the two entries exchange places without a
                # temporary variable.
                values[i], values[j] = values[j], values[i]
                i += 1
                j -= 1

        # After partitioning, indices <= j hold values >= pivot and indices
        # >= i hold values <= pivot; continue only in the side containing
        # target. If target lies strictly between j and i, it holds the
        # pivot value and is the answer.
        if target <= j:
            right = j
        elif target >= i:
            left = i
        else:
            return values[target]

    # RuntimeError signals a broken internal invariant; it should never be
    # reached for valid input.
    # RuntimeError: https://docs.python.org/3/library/exceptions.html#RuntimeError
    raise RuntimeError("Quickselect partition invariant failed")



def find_kth_largest_pdf(k: int, values: list[int], rng=None) -> int:
    """Full PDF randomized-pivot algorithm; partitions the original array.

    This is the textbook's find_kth_largest (randomized quickselect), with
    the book's nested find_kth / partition_around_pivot structure flattened.
    The printed exercise assumes distinct array entries. This function
    mutates `values` (the caller's list is rearranged in place), exactly as
    the book's version rearranges A.

    `rng=None` is an optional parameter: pass an object with a `randint`
    method (for example `random.Random(11)`) to make the pivot choices
    reproducible; by default the module-level `random` functions are used.
    """

    # Chained comparison: 1 <= k and k <= len(values).
    # ValueError: https://docs.python.org/3/library/exceptions.html#ValueError
    if not 1 <= k <= len(values):
        raise ValueError('Rank out of range')

    # Conditional expression `A if condition else B`. The `random` module
    # itself has a module-level randint function, so it can stand in for a
    # random.Random instance here. `is None` is the idiomatic test for the
    # None default.
    generator = random if rng is None else rng

    # A nested function: it can read (and, through item assignment, modify)
    # the enclosing function's `values` list. `compare` is a two-argument
    # function deciding which side of the pivot an element belongs on.
    #
    # Book's comment, paraphrased: partition values[left:right + 1] around
    # the element at pivot_index and return the pivot's new index. Afterwards
    # values[left:new] holds elements "greater" than the pivot and
    # values[new + 1:right + 1] holds elements "less" than it, where the
    # ordering is defined by `compare`.
    def partition(left: int, right: int, pivot_index: int, compare) -> int:
        pivot_value=values[pivot_index]
        new_pivot=left

        # Move the pivot out of the way, to the right end of the range.
        values[pivot_index], values[right] = values[right], values[pivot_index]
        for i in range(left,right):

            # With compare = operator.gt this is `values[i] > pivot_value`:
            # larger elements are swapped into the growing left block.
            if compare(values[i],pivot_value):
                values[i],values[new_pivot] = values[new_pivot],values[i]
                new_pivot+=1

        # Put the pivot between the "greater" block and the rest.
        values[right],values[new_pivot] = values[new_pivot],values[right]
        return new_pivot

    left,right=0,len(values)-1
    while left <= right:

        # randint(a,b) chooses an integer from the inclusive range [a,b].
        # Unlike range(), BOTH endpoints can be returned, so any index in
        # the current range may become the pivot. A random pivot makes the
        # bad (worst-case) splits very unlikely.
        # Documentation: https://docs.python.org/3/library/random.html#random.randint
        pivot=generator.randint(left,right)

        # operator.gt(a, b) is the function form of `a > b`. Passing it
        # makes the partition put larger elements first, so the kth largest
        # belongs at index k - 1.
        # Documentation: https://docs.python.org/3/library/operator.html#operator.gt
        split=partition(left,right,pivot,operator.gt)

        # Exactly k - 1 elements are greater than the pivot: found it.
        if split==k-1:
            return values[split]

        # Too many greater elements: the answer is left of the pivot.
        if split>k-1:
            right=split-1

        # Too few: the answer is right of the pivot.
        else:
            left=split+1

    # Should be unreachable for a valid k.
    # RuntimeError: https://docs.python.org/3/library/exceptions.html#RuntimeError
    raise RuntimeError('Selection invariant failed')


# TEXTBOOK POST-SOLUTION DISCUSSION (pages 154–155)
# -------------------------------------------------
# Each round is expected to cut the remaining entries roughly in half, so
# the average time satisfies T(n) = O(n) + T(n/2), which solves to
# T(n) = O(n). Space complexity is O(1) (the partitioning is in place).
#
# Worst case: O(n^2), which happens when the randomly chosen pivot is always
# the smallest or largest element of the current subarray. The chance of
# this falls off exponentially with the array length, so in practice it is
# a non-issue; for this reason the randomized selection algorithm is
# sometimes described as having almost certain O(n) time complexity.
#
# VARIANTS
# --------
# Variant 1 (stated in the book; no solution given): Design an algorithm for
#   finding the median of an array.
#
# Variant 2 (stated in the book; no solution given): Design an algorithm for
#   finding the kth largest element of A in the presence of duplicates. The
#   kth largest element is defined to be A[k - 1] after A has been sorted in
#   a stable manner, i.e., if A[i] = A[j] and i < j then A[i] must appear
#   before A[j] after stable sorting.
#
# Variant 3 (stated in the book; no solution given): A number of apartment
#   buildings are coming up on a new street. The postal service wants to
#   place a single mailbox on the street, minimizing the total distance
#   residents walk to collect their mail each day. (Different buildings may
#   have different numbers of residents.) Devise an algorithm that computes
#   where to place the mailbox so as to minimize the total distance that
#   residents travel to get to the mailbox. The input is an array of
#   building objects, each with a field for the number of residents in that
#   building and a field for the building's distance from the start of the
#   street.


# TEXTBOOK CODE COMPARISON
# ------------------------
# Book: `def find_kth_largest(k, A):` containing a nested
#   `def find_kth(comp):`, which in turn contains a nested
#   `def partition_around_pivot(left, right, pivot_idx):`; the body ends
#   with `return find_kth(operator.gt)`. Uses `random.randint(left, right)`
#   and names `pivot_idx`, `new_pivot_idx`, with if / elif / else on
#   `new_pivot_idx == k - 1`, `> k - 1`, `< k - 1`. No input validation.
# File, find_kth_largest_pdf: the book's algorithm with the two nesting
#   levels flattened into one nested helper `partition(left, right,
#   pivot_index, compare)` that takes the comparison as a parameter
#   (instead of capturing `comp`); type hints added; extra `rng=None`
#   parameter so a seeded `random.Random` can be injected; adds a
#   ValueError range check and a final RuntimeError (neither in the book);
#   names changed (`pivot_idx` -> `pivot_index`/`pivot`, `new_pivot_idx` ->
#   `new_pivot`/`split`); `if` / `if` / `else` instead of if / elif / else
#   after a returning branch.
# File, find_kth_largest: an extra function NOT in the book -- a
#   deterministic middle-pivot, two-pointer quickselect working on a copy of
#   the list, with its own ValueError/RuntimeError. The book's name
#   `find_kth_largest` is used for this non-book function, while the book's
#   algorithm lives in `find_kth_largest_pdf`.


# Python executes this block only when this source file is run directly.
# When pytest imports the file, this block is skipped automatically.
# Documentation: https://docs.python.org/3/library/__main__.html
if __name__ == "__main__":

    # The repository quickselect: the 3rd largest of [3, 1, 5, 2, 4] is 3.
    # `assert` stops the program with an AssertionError if the condition is
    # false; these are quick smoke checks, while pytest provides the more
    # thorough automated verification.
    print("third largest:", find_kth_largest(3, [3,1,5,2,4]))
    assert find_kth_largest(3, [3,1,5,2,4]) == 3

    # The PDF version uses a randomized pivot and modifies the list.
    # random.Random(11) creates an independent generator seeded with 11, so
    # the pivot sequence (and therefore the final arrangement of `original`)
    # is the same on every run. Printing `original` afterwards shows that
    # the list was rearranged in place.
    # Documentation: https://docs.python.org/3/library/random.html#random.Random
    original=[3,1,5,2,4]
    assert find_kth_largest_pdf(3,original,random.Random(11)) == 3
    print('PDF randomized quickselect:',original)
