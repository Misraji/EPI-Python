"""EPI Python — Exercise 24.32: Trapping Water

Chapter 24: Honors Class
Textbook: pages 398–399 (printed page numbers; problem and solution start
on 398).

PROBLEM (from the textbook)
---------------------------
"The goal of this problem is to compute the capacity of a type of
one-dimensional container. The computation is illustrated in Figure 24.10.

A one-dimensional container is specified by an array of n nonnegative
integers, specifying the height of each unit-width rectangle. Design an
algorithm for computing the capacity of the container."

Figure 24.10 (page 398) shows a stepped solid region with the trapped water
drawn as horizontal lines; for that container the capacity is
1 + 2 + 1 + 3 = 7.

HINT (from the textbook)
------------------------
"Draw pictures, and focus on the extremes."

SOLUTION DEVELOPMENT (following the textbook)
---------------------------------------------
Picture pouring water in. At maximum capacity the water surface forms a
region where the level is nondecreasing followed by a region where it is
nonincreasing, and the switch happens around the maximum entry of A.

Let A[m] be a maximum entry. Compute the capacities of A[0, m - 1] and
A[m, n - 1] separately, each by one iteration: for each entry of A[0, m - 1],
add the difference between the running maximum and the entry's value to the
total. Handle A[m, n - 1] the same way, scanning from the right end toward
m.

The book prints one program; calculate_trapping_water below follows it.

ADDITIONAL EXAMPLES (added for learning; not printed in this exercise)
---------------------------------------------------------------------
    [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]  -> 6
"""


# Type hints: `heights: list[int]` and `-> int` document expected types;
# Python does not enforce annotations at run time.
def calculate_trapping_water(heights: list[int]) -> int:
    """Return the total water the container `heights` can hold.

    This is the textbook's single implementation (split at a maximum, then
    a running-maximum scan from each end toward it).
    """

    # Added guard (not in the book): max() raises ValueError on an empty
    # list, so an empty container returns 0 directly.
    if not heights:
        return 0

    # Finds the index with maximum height (book's comment). max(heights)
    # returns the largest value; list.index(value) returns the index of its
    # first occurrence (O(n)).
    # Docs: https://docs.python.org/3/library/stdtypes.html#common-sequence-operations
    max_h = heights.index(max(heights))

    # Assume the element just past the end of `values` is the maximum
    # height (the book's comment says "heights[-1] is maximum height"), so
    # every dip below the running maximum is held in by that wall.
    def trapping_water_till_end(values):
        volume = 0

        # float('-inf') is negative infinity: it compares smaller than every
        # number, so the first height always becomes the running maximum.
        highest_level_seen = float('-inf')
        for height in values:
            if height >= highest_level_seen:
                highest_level_seen = height
            else:

                # Water above this bar rises to the highest wall seen so
                # far on this side.
                volume += highest_level_seen - height
        return volume

    # Left part: heights[:max_h] is a slice of everything before the peak.
    # Right part: heights[max_h + 1:] is everything after it; reversed(...)
    # returns an iterator going backwards over that list, so the scan moves
    # from the right end toward the peak.
    # Docs: https://docs.python.org/3/library/functions.html#reversed
    return (trapping_water_till_end(heights[:max_h])
            + trapping_water_till_end(reversed(heights[max_h + 1:])))


# TEXTBOOK POST-SOLUTION DISCUSSION (page 399)
# --------------------------------------------
# Finding a maximum takes O(n) time and each of the two scans takes O(n), so
# the total time is O(n). The book gives the space complexity as O(1), since
# only a few variables are recorded. (In this Python code the slices
# heights[:max_h] and heights[max_h + 1:] do create copies, O(n) extra
# space; iterating with indices would avoid that.)
#
# VARIANTS
# --------
# * Solve the water filling problem with an algorithm that accesses A's
#   elements in order and can read an element only once. Use minimum
#   additional space. (stated in the book; no solution given)


# TEXTBOOK CODE COMPARISON
# ------------------------
# * Signature: book `def calculate_trapping_water(heights)`; file adds type
#   hints `list[int]` / `-> int`.
# * Added: `if not heights: return 0` guard.
# * Inner function: book `trapping_water_till_end(heights)` with
#   `partial_sum, highest_level_seen = 0, float('-inf')` and loop variable
#   `h`; file names the parameter `values`, the accumulator `volume`, the
#   loop variable `height`, and initializes on two lines. Same logic.
# * The `max_h` computation and the final return expression match the
#   book.


# Python executes this block only when this source file is run directly.
# When pytest imports the file, this block is skipped automatically.
# Documentation: https://docs.python.org/3/library/__main__.html
if __name__ == '__main__':

    # Added example: a common test container that holds 6 units.
    example = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    print('Trapped volume:', calculate_trapping_water(example))

    # `assert` stops with an AssertionError if the condition is false; a
    # quick smoke check. pytest provides the more thorough verification.
    assert calculate_trapping_water(example) == 6
