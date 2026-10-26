"""EPI Python — Exercise 11.7: Find the Min and Max Simultaneously

Chapter 11: Searching
Textbook: pages 152–153 (printed page numbers; problem and solution on
152, program, complexity and variant on 153).

PROBLEM (from the textbook)
---------------------------
"Given an array of comparable objects, you can find either the min or the
max of the elements in the array with n - 1 comparisons, where n is the
length of the array.

Comparing elements may be expensive, e.g., a comparison may involve a
number of nested calls or the elements being compared may be long strings.
Therefore, it is natural to ask if both the min and the max can be computed
with less than the 2(n - 1) comparisons required to compute the min and the
max independently.

Design an algorithm to find the min and max elements in an array. For
example, if A = <3, 2, 5, 1, 2, 4>, you should return 1 for the min and 5
for the max."

HINT (from the textbook)
------------------------
"Use the fact that a < b and b < c implies a < c to reduce the number of
compares used by the brute-force approach."

SOLUTION DEVELOPMENT (following the textbook)
---------------------------------------------
Brute force: find the min and the max in two independent passes, using
2(n - 1) comparisons. One comparison can be saved by computing the min
first and then not comparing the min element again when computing the max.

Tournament analogy: think of finding the strongest and the weakest player
in a group, where players are totally ordered. A player who has won a game
can never be the weakest, so there is no point looking at winners when
searching for the weakest. Instead, play n/2 matches between disjoint
pairs: the strongest player is among the n/2 winners, and the weakest is
among the n/2 losers.

Applied to the array: compare successive pairs to split the elements into
n/2 min-candidates and n/2 max-candidates (n/2 comparisons). Then
n/2 - 1 comparisons find the min of the min-candidates, and n/2 - 1 find
the max of the max-candidates: 3n/2 - 2 comparisons in total.

Done naively this needs O(n) storage for the candidate lists. Instead it
can run in a streaming fashion, keeping a running min and max while each
successive pair is processed -- three comparisons per pair (one inside
the pair, one against the min, one against the max).

Book's worked example, A = <3, 2, 5, 1, 2, 4>:
  * Compare 3 and 2: 3 > 2, so min = 2 and max = 3.
  * Compare 5 and 1: 5 > 1. Compare 5 with the current max 3 -> max = 5.
    Compare 1 with the current min 2 -> min = 1.
  * Compare 2 and 4: 4 > 2. Compare 4 with the current max 5 -> no change.
    Compare 2 with the current min 1 -> no change.
  Result: min 1, max 5.

The implementation below, find_min_max, follows this pairwise idea.

ADDITIONAL EXAMPLES (added for learning; not printed in this exercise)
---------------------------------------------------------------------
    [4, 1, 3, 2] -> (1, 4)
    []           -> raises ValueError (guard added in this file)
"""


def find_min_max(values: list[int]) -> tuple[int, int]:
    """Find both extrema with pairwise comparisons (~3n/2 compares).

    This is the textbook's find_min_max (the only implementation given),
    restructured: it returns a plain (min, max) tuple instead of the book's
    MinMax namedtuple, and handles an odd-length list at the start instead
    of at the end.

    Type hints: `list[int]` is the argument type and `tuple[int, int]` says
    a 2-tuple of ints is returned. Python does not enforce annotations.
    """

    # An empty list is falsy; there is no min or max to report, so raise an
    # exception. (Guard added in this file; the book's code would fail with
    # IndexError.)
    # ValueError: https://docs.python.org/3/library/exceptions.html#ValueError
    if not values:
        raise ValueError("Requires nonempty input")

    # `%` is the remainder operator. For an odd length, len % 2 is 1
    # (truthy). Then the first element alone seeds both the running min and
    # the running max, and pairing starts at index 1, so the rest of the
    # list has an even length. `low = high = values[0]` is chained
    # assignment: both names refer to the same value.
    if len(values) % 2:
        low = high = values[0]
        start = 1

    # For an even length, the first pair seeds the min and max.
    # `values[:2]` is a slice holding the first two elements. sorted()
    # returns a NEW ascending list (the input is untouched); for two items
    # it needs just one comparison. Tuple-style unpacking then assigns the
    # smaller to low and the larger to high.
    # sorted: https://docs.python.org/3/library/functions.html#sorted
    else:
        low, high = sorted(values[:2])
        start = 2

    # range(start, len(values), 2) yields start, start + 2, ... -- the
    # third argument is the step -- so i is the first index of each pair.
    # range: https://docs.python.org/3/library/stdtypes.html#range
    for i in range(start, len(values), 2):

        # One comparison inside the pair: sorted() on a 2-tuple returns the
        # pair in ascending order. Only `small` can be a new min and only
        # `large` can be a new max (the tournament idea).
        small, large = sorted((values[i], values[i+1]))

        # Built-in min() and max() return the smaller / larger argument.
        # Each makes one comparison, giving three comparisons per pair.
        # min: https://docs.python.org/3/library/functions.html#min
        # max: https://docs.python.org/3/library/functions.html#max
        low, high = min(low, small), max(high, large)

    # `return low, high` builds and returns the tuple (low, high).
    return low, high


# TEXTBOOK POST-SOLUTION DISCUSSION (page 153)
# --------------------------------------------
# Time complexity O(n); space complexity O(1) (only the running min and max
# are kept).
#
# VARIANTS
# --------
# Variant (stated in the book; no solution given): What is the least number
#   of comparisons required to find the min and the max in the worst-case?


# TEXTBOOK CODE COMPARISON
# ------------------------
# Book: defines a module-level
#   `MinMax = collections.namedtuple('MinMax', ('smallest', 'largest'))`
#   (so it imports collections) and `def find_min_max(A):` with a nested
#   helper `def min_max(a, b)` returning `MinMax(a, b) if a < b else
#   MinMax(b, a)`. It returns `MinMax(A[0], A[0])` when `len(A) <= 1`,
#   seeds `global_min_max = min_max(A[0], A[1])`, loops
#   `for i in range(2, len(A) - 1, 2)` combining each `local_min_max` with
#   `min(...)` / `max(...)`, and, if `len(A) % 2`, folds in the last element
#   A[-1] at the end ("If there is odd number of elements in the array, we
#   still need to compare the last element with the existing answer.").
#   Returns the MinMax namedtuple (fields .smallest / .largest).
# File: no MinMax namedtuple and no collections import; no nested min_max
#   helper -- `sorted(...)` on two elements is used instead; parameter
#   renamed `values: list[int]` with return hint `tuple[int, int]`; adds a
#   ValueError for empty input (book: len <= 1 branch, which would raise
#   IndexError for an empty list); an odd length is handled up front by
#   seeding with values[0] and pairing from index 1, instead of handling
#   the last element after the loop; returns a plain tuple (low, high).


# Python executes this block only when this source file is run directly.
# When pytest imports the file, this block is skipped automatically.
# Documentation: https://docs.python.org/3/library/__main__.html
if __name__ == "__main__":

    # An even-length example: the result tuple is (min, max).
    # `assert` stops the program with an AssertionError if the condition is
    # false; this is a quick smoke check, while pytest provides the more
    # thorough automated verification.
    print("min and max:", find_min_max([4, 1, 3, 2]))
    assert find_min_max([4, 1, 3, 2]) == (1, 4)
