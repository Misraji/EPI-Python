"""EPI Python — Exercise 24.28: Compute the Maximum Subarray Sum in a Circular Array

Chapter 24: Honors Class
Textbook: pages 389–391 (printed page numbers; problem starts on 389,
solution on 390).

PROBLEM (from the textbook)
---------------------------
Context: the maximum subarray sum of an ordinary array can be found in
linear time (page 235). If the array A is circular, so that its first and
last elements count as adjacent, that algorithm can give a suboptimal
answer. For the array of Figure 16.2 (page 235), the maximum circular
subarray starts at index 7 and ends at index 3, but the algorithm on page
236 returns the subarray from index 0 to index 3.

"Given a circular array A, compute its maximum subarray sum in O(n) time,
where n is the length of A. Can you devise an algorithm that takes O(n) time
and O(1) space?"

HINT (from the textbook)
------------------------
"The maximum subarray may or may not wrap around."

SOLUTION DEVELOPMENT (following the textbook)
---------------------------------------------
Recall the standard linear-time algorithm: compute S[i], the maximum
subarray sum for a subarray ending at i, as max(S[i - 1] + A[i], A[i]).
It takes O(n) time and O(1) space.

First approach: split into two problems.
1. The non-circular case, solved by the standard algorithm.
2. The wrapping case. Naively one could take the best subarray starting at
   index 0 plus the best subarray ending at index n - 1, but they may
   overlap, and subtracting the overlap does not always work (consider
   <10, -4, 5, -4, 10>). Instead, for every i compute S_i, the best sum of
   a subarray starting at 0 and ending at or before i, and E_i, the best
   sum of a subarray starting after i and ending at the last element. The
   best wrapping sum is the maximum over i of S_i + E_i.
The book's first program implements this; it uses O(n) time and O(n) space.

Second approach: a wrapping maximum subarray is what remains after removing
a minimum subarray, so its sum is sum(A) minus the minimum subarray sum.
(The remainder may leave out the first and/or last element; that is fine.)
This uses O(1) space and O(n) time; the book's second program implements it
with one helper parameterized by max or min.

This file contains a single function, max_subarray_sum_in_circular_array,
an O(n)-time, O(1)-space implementation of the second (complement) idea,
written differently from the book: it requires a nonempty subarray and
special-cases all-negative input. The book's first program (S_i + E_i) is
not in this file. See the code comparison block.

ADDITIONAL EXAMPLES (added for learning; not printed in this exercise)
---------------------------------------------------------------------
    []               -> 0   (file's convention for empty input)
    [1, 2, -4, 3]    -> 6   (3 + 1 + 2, wrapping around)
    [-2, -1, -5]     -> -1  (best nonempty subarray when all are negative)
    [5, -3, 5]       -> 10  (5 + 5, wrapping around)
"""


# Type hints: `values: list[int]` and `-> int` document expected types;
# Python does not enforce annotations at run time.
def max_subarray_sum_in_circular_array(values: list[int]) -> int:
    """Maximum sum of a nonempty subarray, including circular wraparound.

    Implements the textbook's second (O(1)-space) idea: the answer is the
    larger of the best non-wrapping subarray and total minus the minimum
    subarray. Unlike the book's code, subarrays must be nonempty, so an
    all-negative array returns its largest element.
    """

    # Added convention (not in the book): empty input returns 0.
    if not values:
        return 0
    total=0

    # Chained assignment gives both names the same starting value.
    # max_end / min_end: best (largest / smallest) sum of a subarray ending
    # at the current index. max_so_far / min_so_far: best seen anywhere.
    max_end=max_so_far=values[0]
    min_end=min_so_far=values[0]

    # enumerate(values) yields (index, value) pairs. The index is used only
    # to skip the update on the first element, which already initialized
    # the four trackers above.
    for index,value in enumerate(values):
        total+=value

        # `if index:` is false only for index 0 (0 is falsy).
        if index:

            # Standard recurrence: either extend the best subarray ending at
            # the previous index, or start fresh at this value.
            max_end=max(value,max_end+value)
            max_so_far=max(max_so_far,max_end)

            # Same recurrence with min() finds the minimum subarray sum.
            min_end=min(value,min_end+value)
            min_so_far=min(min_so_far,min_end)

    # All elements negative: the minimum subarray is the whole array, and
    # total - min_so_far would be 0 (an empty subarray). Return the largest
    # single element instead.
    if max_so_far<0:
        return max_so_far

    # Otherwise compare the non-circular best with the wrapping best.
    return max(max_so_far,total-min_so_far)


# TEXTBOOK POST-SOLUTION DISCUSSION (pages 390–391)
# -------------------------------------------------
# For the first program (S_i + E_i), both time and space complexity are
# O(n). The book then describes the complement approach (total minus the
# minimum subarray) as using O(1) space and O(n) time, and gives its code.
# No further analysis follows the second program.
#
# VARIANTS
# --------
# The book states no variants for this exercise.


# TEXTBOOK CODE COMPARISON
# ------------------------
# * The book prints two programs, both named
#   `max_subarray_sum_in_circular(A)`:
#   1. nested `find_max_subarray()` (non-circular, starting from 0) and
#      `find_circular_max_subarray()` with inner
#      `compute_running_maximum(A)`, building `maximum_begin` and
#      `maximum_end = compute_running_maximum(A[::-1])[::-1][1:] + [0]`,
#      returning `max(begin + end for begin, end in zip(...))`;
#   2. nested `find_optimum_subarray_using_comp(comp)` called with `max`
#      and `min`, returning `max(find_...(max), sum(A) - find_...(min))`.
#   Program 1 is missing from the file.
# * The file's single function is named
#   `max_subarray_sum_in_circular_array(values: list[int]) -> int` and is a
#   rewritten form of program 2: one loop computing total, max and min
#   together, initialized from values[0] rather than 0.
# * Behavioural differences from the book (both book programs start their
#   running values at 0, i.e. they allow an empty subarray): for an
#   all-negative array the book returns 0, the file returns the largest
#   element; the file returns 0 for empty input via an explicit guard.


# Python executes this block only when this source file is run directly.
# When pytest imports the file, this block is skipped automatically.
# Documentation: https://docs.python.org/3/library/__main__.html
if __name__ == "__main__":

    # Executable demonstration cases; pytest has the full set. Each call is
    # followed by a print of the result and an `assert`, which stops the
    # program with an AssertionError if the result differs from the
    # expected value. All four inputs are added examples (see the module
    # docstring): empty input, a wrapping answer, all-negative input, and
    # another wrapping answer.
    result=max_subarray_sum_in_circular_array([])
    print('max_subarray_sum_in_circular_array', result)
    assert result == 0
    result=max_subarray_sum_in_circular_array([1, 2, -4, 3])
    print('max_subarray_sum_in_circular_array', result)
    assert result == 6
    result=max_subarray_sum_in_circular_array([-2, -1, -5])
    print('max_subarray_sum_in_circular_array', result)
    assert result == -1
    result=max_subarray_sum_in_circular_array([5, -3, 5])
    print('max_subarray_sum_in_circular_array', result)
    assert result == 10
