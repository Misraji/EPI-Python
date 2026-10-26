"""EPI Python — Exercise 24.5: Compute the Longest Contiguous Increasing Subarray

Chapter 24: Honors Class
Textbook: pages 356–357 (printed page numbers; problem and solution on 356,
the program and its analysis on 357).

PROBLEM (from the textbook)
---------------------------
An array is increasing if each element is less than its succeeding element
except for the last element.

Implement an algorithm that takes as input an array A of n elements, and
returns the beginning and ending indices of a longest increasing subarray
of A. For example, if A = <2, 11, 3, 5, 13, 7, 19, 17, 23>, the longest
increasing subarray is <3, 5, 13>, and you should return (2, 4).

HINT (from the textbook)
------------------------
If A[i] >= A[i + 1], instead of checking A[i + 1] < A[i + 2], go further
out in the array.

SOLUTION DEVELOPMENT (following the textbook)
---------------------------------------------
Brute force: test every subarray. Two nested loops choose the start and end
indices, an inner loop checks that the subarray is increasing, and some
bookkeeping tracks the longest one. This is O(n^3), e.g. for the array
<0, 1, 2, 3, ..., n - 1>. Caching whether A[i, j] is increasing when
examining A[i, j + 1] easily improves it to O(n^2).

Looking at the example more carefully: the longest increasing subarray
ending at 3 is A[2, 2], because 3 < 11. Since 13 > 5, the longest one ending
at 13 is the longest one ending at 5 (namely A[2, 3]) extended by 13, i.e.
A[2, 4]. In general, the longest increasing subarray ending at index j + 1
is
  (1.) just the single entry A[j + 1], if A[j + 1] <= A[j]; or
  (2.) the longest increasing subarray ending at j extended by A[j + 1], if
       A[j + 1] > A[j].
Using this directly gives an O(n) algorithm. Extra space is O(1): only the
length of the longest subarray ending at j is needed when processing
j + 1, plus two variables for the length and end index of the best
subarray so far.

Heuristic improvement (the program printed in the book): suppose A[i - 1]
is not less than A[i] (so a new subarray must start at i) and the longest
increasing subarray seen so far has length L. Jump ahead to index i + L and
work backwards toward i: if for some j with i < j <= i + L we have A[j - 1]
not less than A[j], all indices before j can be skipped, since no
increasing subarray starting there can beat the current best. Example from
the book: after processing 13, work back from index 4 + 3 = 7 (13's index
plus the current best length 3). Since A[7] = 17 is smaller than
A[6] = 19, earlier entries need not be examined — no increasing subarray
ending at A[7] can be longer than the current best.

The book prints one program, `find_longest_increasing_subarray`, using this
backward-check/forward-extend scheme; this file implements it.

ADDITIONAL EXAMPLES (added for learning; not printed in this exercise)
---------------------------------------------------------------------
    [1, 2, 3, 1, 4, 6, 7] -> Subarray(start=3, end=6)  (the run 1, 4, 6, 7)
    []                    -> Subarray(start=0, end=-1) (file-only guard)
"""

# Python standard library: specialized container types.
# Module documentation: https://docs.python.org/3/library/collections.html
# namedtuple API: https://docs.python.org/3/library/collections.html#collections.namedtuple
from collections import namedtuple


# namedtuple(typename, field_names) creates a new tuple subclass whose items
# can also be read by name. Subarray(2, 4) is still a tuple equal to (2, 4),
# but its fields are available as .start and .end, which documents the
# meaning of the two returned indices. Instances are immutable.
Subarray=namedtuple('Subarray',('start','end'))


def find_longest_increasing_subarray(a: list[int]) -> Subarray:
    """Textbook implementation: backward skip check, then forward extension.

    Returns Subarray(start, end), inclusive indices of a longest strictly
    increasing contiguous run. Type hints (`a: list[int]`, `-> Subarray`)
    are documentation only; Python does not enforce them.
    """

    # Added guard (not in the book): an empty list has no run; this returns
    # the "empty" range (0, -1). `not a` is True for an empty list.
    if not a:
        return Subarray(0,-1)

    # Best so far: the single entry at index 0 (length 1).
    result=Subarray(0,0)

    # Tuple assignment: i is the start of the current candidate run,
    # max_length the length of the best run found so far.
    i,max_length=0,1

    # Only continue while a run starting at i could be longer than the best.
    while i<len(a)-max_length:

        # Backward check and skip if A[j] >= A[j + 1].
        #
        # range(start, stop, -1) counts DOWN from start to stop + 1 (stop is
        # excluded). Here j goes i+max_length, ..., i+1, so we test the pairs
        # just beyond the best length first, moving back toward i.
        for j in range(i+max_length,i,-1):
            if a[j-1]>=a[j]:

                # A descent at j: no run starting before j (at or after i)
                # can beat max_length, so restart the search at j.
                i=j
                break

        # for/else: the `else` block of a `for` loop runs only if the loop
        # finished WITHOUT executing `break`.
        # https://docs.python.org/3/tutorial/controlflow.html#break-and-continue-statements-and-else-clauses-on-loops
        # Forward check if it is not skippable (the loop ended normally):
        # a[i..i+max_length] is already increasing, i.e. longer than the
        # best, so extend it as far as it goes.
        else:
            i+=max_length

            # `and` short-circuits, so a[i] is not read once i == len(a).
            while i<len(a) and a[i-1]<a[i]:
                i,max_length=i+1,max_length+1

            # The run ends at i - 1 and has max_length elements.
            result=Subarray(i-max_length,i-1)
    return result


# TEXTBOOK POST-SOLUTION DISCUSSION (page 357)
# --------------------------------------------
# Skipping is only a heuristic: it does not improve the worst case. For an
# array of alternating 0s and 1s every element is still examined, so the
# bound is O(n). The best case improves to O(max(n / L, L)), where L is the
# length of the longest increasing subarray.
#
# VARIANTS
# The book gives no variants for this exercise.


# TEXTBOOK CODE COMPARISON
# ------------------------
# book: `Subarray = collections.namedtuple('Subarray', ('start', 'end'))`
#   (module imported as `collections`); `def
#   find_longest_increasing_subarray(A)` starting directly with `result =
#   Subarray(0, 0)`; same for/else backward-check and forward-extend loop.
# file: imports the name directly (`from collections import namedtuple`);
#   parameter renamed `a: list[int]` with return hint `-> Subarray`; an added
#   `if not a: return Subarray(0, -1)` guard for empty input; the rest of the
#   loop matches the book's listing.


# Python executes this block only when this source file is run directly.
# When pytest imports the file, this block is skipped automatically.
# Documentation: https://docs.python.org/3/library/__main__.html
if __name__=='__main__':

    # The final run 1, 4, 6, 7 (indices 3..6) beats the initial run 1, 2, 3.
    # Printing a namedtuple shows its field names: Subarray(start=3, end=6).
    # `assert` raises AssertionError if the result differs; a namedtuple
    # compares equal to another with the same values.
    result=find_longest_increasing_subarray([1,2,3,1,4,6,7])
    print('Longest increasing run:',result)
    assert result==Subarray(3,6)
