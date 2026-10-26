"""EPI Python — Exercise 5.8: Computing an Alternation

Chapter 5: Arrays
Textbook: pages 48–49 (printed page numbers; problem and solution start on
page 48, the program and remarks finish at the top of page 49).

PROBLEM (from the textbook)
---------------------------
"Write a program that takes an array A of n numbers, and rearranges A's
elements to get a new array B having the property that
B[0] <= B[1] >= B[2] <= B[3] >= B[4] <= B[5] >= ...."

HINT (from the textbook)
------------------------
"Can you solve the problem by making local changes to A?"

SOLUTION DEVELOPMENT (following the textbook)
---------------------------------------------
1. Sort A and interleave the lower and upper halves of the sorted array.
   Or: sort A and then swap the pairs (A[1], A[2]), (A[3], A[4]), ....
   Either way the cost is that of sorting, O(n log n).
2. Sorting is more than needed: it is enough to partition the elements
   around the median and then interleave. Median finding takes O(n) time
   (the book points to Solution 11.8 on page 153), which is then the time
   for the whole approach.
3. The required order is purely local, so even the median is unnecessary.
   Scan the array and swap A[i] with A[i + 1] when i is even and
   A[i] > A[i + 1], or when i is odd and A[i] < A[i + 1]. That yields the
   desired arrangement. (Fixing a pair never breaks the previous pair:
   e.g. at an even i, if A[i] > A[i + 1] we swap in a smaller value at i,
   and A[i - 1] >= A[i] already held for the larger value, so it still
   holds.)

The book prints one program, `rearrange(A)`, which expresses step 3 by
sorting each two-element slice ascending (even i) or descending (odd i).
It is implemented here as `rearrange_alternation_in_place`. The file also
has `rearrange_alternation`, a helper added in this repository that
applies the same swap rule (step 3 as described in words) to a copy.

ADDITIONAL EXAMPLES (added for learning; not printed in this exercise)
---------------------------------------------------------------------
    []           -> []
    [3, 2]       -> [2, 3]
    [1, 2, 3, 4] -> [1, 3, 2, 4]
    [4, 3, 2, 1] -> [3, 4, 1, 2]
"""



# `values: list[int]` and `-> list[int]` are type hints that document the
# intended types; Python does not enforce them at run time. `list[int]`
# requires Python 3.9 or newer.
# Documentation: https://docs.python.org/3/library/typing.html
def rearrange_alternation(values: list[int]) -> list[int]:
    """Return alternating <= and >= neighbors starting with <=.

    Helper added in this repository (not a printed textbook program). It
    applies the book's described swap rule to a copy, leaving `values`
    unchanged.
    """

    # `list.copy()` returns a new, shallow copy of the list, so the
    # caller's list is not modified.
    # Documentation: https://docs.python.org/3/tutorial/datastructures.html
    result = values.copy()
    for i in range(len(result) - 1):

        # `i % 2 == 0` tests for an even index. In `i % 2` on its own, the
        # value 1 (odd) is truthy and 0 (even) is falsy, so the second
        # clause means "i is odd and the pair is increasing".
        # Even i needs result[i] <= result[i + 1]; odd i needs >=.
        if (i % 2 == 0 and result[i] > result[i + 1]) or (i % 2 and result[i] < result[i + 1]):

            # `a, b = b, a` swaps two entries via tuple packing/unpacking.
            result[i], result[i + 1] = result[i + 1], result[i]
    return result



# `-> None` documents that the function returns nothing useful: it works
# by modifying its argument.
def rearrange_alternation_in_place(values: list[int]) -> None:
    """Textbook's online algorithm; rearrange the ORIGINAL list in place.

    This is the book's `rearrange(A)` program. Sorting two-element slices
    uses O(1) working space per step. At each position, sort ascending for
    even i and descending for odd i. This fixes the local inequality
    without disturbing any prior inequality.
    """
    for i in range(len(values)):

        # `values[i:i + 2]` is a slice holding at most two items (only one
        # at the last index, because slices stop quietly at the end).
        # `sorted(iterable, reverse=...)` creates a NEW sorted list;
        # reverse=True sorts in descending order. `bool(i % 2)` is True for
        # odd i, so odd positions get the larger value first.
        # Here the source is at most two entries, so the temporary is O(1).
        # Slice assignment writes these entries back to the SAME input list.
        # Documentation: https://docs.python.org/3/library/functions.html#sorted
        # Documentation: https://docs.python.org/3/library/stdtypes.html#mutable-sequence-types
        values[i:i + 2] = sorted(values[i:i + 2], reverse=bool(i % 2))


# TEXTBOOK POST-SOLUTION DISCUSSION (page 49)
# ------------------------------------------
# The time complexity is O(n), the same as the median-based approach, but
# this one is much easier to implement. It also works in an online
# fashion: it never needs to keep more than two elements in memory, and
# never re-reads an earlier element. The book remarks that it is a nice
# example of designing an algorithm by iteratively refining a brute-force
# solution.
#
# VARIANTS
# --------
# The book gives no variants for this exercise.


# TEXTBOOK CODE COMPARISON
# ------------------------
# - Book: `def rearrange(A)` with body
#   `for i in range(len(A)): A[i:i + 2] = sorted(A[i:i + 2], reverse=i % 2)`.
#   File: `rearrange_alternation_in_place(values: list[int]) -> None`;
#   same loop, but `reverse=bool(i % 2)` instead of `reverse=i % 2`.
# - `rearrange_alternation` is a helper not printed in the book: it
#   copies the input, loops to len - 1, and swaps by the explicit
#   even/odd comparison rule described in the book's prose, returning the
#   new list.


# Python executes this block only when this source file is run directly.
# When pytest imports the file, this block is skipped automatically.
# Documentation: https://docs.python.org/3/library/__main__.html
if __name__ == "__main__":
    # Demonstrations check representative input/output behavior.
    #
    # All examples are added for learning. print() with several arguments
    # separates them with a space. `assert` stops the program with an
    # AssertionError if a condition is false; pytest provides the more
    # thorough automated verification.
    observed = rearrange_alternation([])
    print("rearrange_alternation:", observed)
    assert observed == []
    observed = rearrange_alternation([3, 2])
    print("rearrange_alternation:", observed)
    assert observed == [2, 3]
    observed = rearrange_alternation([1, 2, 3, 4])
    print("rearrange_alternation:", observed)
    assert observed == [1, 3, 2, 4]
    observed = rearrange_alternation([4, 3, 2, 1])
    print("rearrange_alternation:", observed)
    assert observed == [3, 4, 1, 2]

    # id() returns an integer identifying an object while it exists.
    # Comparing it before and after shows the textbook version rearranged
    # the same list object rather than producing a new one.
    # Documentation: https://docs.python.org/3/library/functions.html#id
    sample = [4, 3, 2, 1]
    before_id = id(sample)
    rearrange_alternation_in_place(sample)
    print("Textbook alternation (in place):", sample)
    assert id(sample) == before_id and sample == [3, 4, 1, 2]
