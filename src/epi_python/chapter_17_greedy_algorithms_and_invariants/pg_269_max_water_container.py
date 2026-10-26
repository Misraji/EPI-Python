"""EPI Python — Exercise 17.7: Compute the Maximum Water Trapped by a Pair of
Vertical Lines

Chapter 17: Greedy Algorithms and Invariants
Textbook: pages 269–270 (printed page numbers; problem, Figure 17.4 and
hint on 269; solution, program and complexity on 270).

PROBLEM (from the textbook)
---------------------------
An array of integers naturally defines a set of lines parallel to the
Y-axis, starting from x = 0 as illustrated in Figure 17.4(a). The goal of
this problem is to find the pair of lines that together with the X-axis
"trap" the most water. See Figure 17.4(b) for an example.

Figure 17.4 (book): (a) a graphical depiction of the array
<1, 2, 1, 3, 4, 4, 5, 6, 2, 1, 3, 1, 3, 2, 1, 2, 4, 1>; (b) the shaded area
between lines 4 and 16 is the maximum water that can be trapped by that
array.

Write a program which takes as input an integer array and returns the pair
of entries that trap the maximum amount of water.

HINT (from the textbook)
------------------------
Start with 0 and n - 1 and work your way in.

SOLUTION DEVELOPMENT (following the textbook)
---------------------------------------------
Let A be the array and n its length.

1. Brute force, O(n^2): for every pair of indices i < j the trapped water
   is (j - i) * min(A[i], A[j]), computable in O(1); take the maximum over
   all pairs.

2. Divide and conquer: find the best water using lines only in the left
   half, only in the right half, and across the centre. The crossing case
   combines n/2 left entries with n/2 right entries, so
   T(n) = 2T(n/2) + O(n^2/4), which solves to O(n^2) — no better than brute
   force and harder to code.

3. Two-pointer elimination: begin with the widest pair, 0 and n - 1, and
   record its water ((n - 1) - 0) * min(A[0], A[n - 1]). Suppose
   A[0] > A[n - 1]. Then for every k > 0 the water between k and n - 1 is
   less than that between 0 and n - 1 (narrower, and still limited by
   A[n - 1]), so line n - 1 can be dropped: only the subarray 0..n - 2
   remains interesting. Conversely, if A[0] <= A[n - 1], line 0 never needs
   to be considered again. Repeating this keeps shrinking the subarray to
   be explored while tracking the best water seen — in effect, searching
   for the best trade-off between width and height.

Book worked example (the Figure 17.4 array, indices 0..17):
  (0, 17): capacity 1 x 17 = 17; left height <= right height, so advance
           to (1, 17).
  (1, 17): capacity 1 x 16 = 16; since 2 > 1, advance to (1, 16).
  (1, 16): capacity 2 x 15 = 30; since 2 < 4, advance to (2, 16).
  (2, 16): capacity 1 x 14 = 14; since 1 < 4, advance to (3, 16).
  (3, 16): capacity 3 x 13 = 39; since 3 < 4, advance to (4, 16).
  (4, 16): capacity 4 x 12 = 48. Later iterations (not shown in the book)
           do not exceed 48, which is the result.

Note: although the problem says "return the pair of entries", the book's
program get_max_trapped_water(heights) returns the maximum amount of water.
This file's max_water_container implements the same two-pointer program.

ADDITIONAL EXAMPLES (added for learning; not printed in this exercise)
---------------------------------------------------------------------
    []                           -> 0  (no pair of lines)
    [1]                          -> 0  (only one line)
    [1, 1]                       -> 1  (width 1 x height 1)
    [1, 8, 6, 2, 5, 4, 8, 3, 7]  -> 49 (lines at 1 and 8: 7 x min(8, 7))
"""


# Type hints: `heights: list[int]` and `-> int` document the expected types;
# Python does not enforce them at run time.
def max_water_container(heights: list[int]) -> int:
    """Maximum area between two vertical height lines.

    The textbook's two-pointer program (book name: get_max_trapped_water).
    """

    # Tuple unpacking: start with the widest pair, the first and last line.
    left,right=0,len(heights)-1
    best=0

    # Invariant: the best pair not yet examined lies inside [left, right].
    # When the pointers meet, no pair remains. For an empty list right is
    # -1, so the loop does not run and the answer is 0.
    while left<right:

        # Built-ins max(a, b) and min(a, b) return the larger / smaller
        # argument. Water = width * height of the SHORTER line, because water
        # would spill over the shorter one.
        best=max(best,(right-left)*min(heights[left],heights[right]))

        # Drop the shorter line: pairing it with any line further inward is
        # narrower and still limited by its height, so it cannot do better.
        if heights[left]<heights[right]:
            left+=1
        else:
            right-=1
    return best


# TEXTBOOK POST-SOLUTION DISCUSSION (page 270)
# --------------------------------------------
# Each iteration eliminates one line (the book says "one line or two lines
# at a time") and costs O(1), so the time complexity is O(n).
# (Extra space is O(1): just two indices and the running maximum.)
#
# VARIANTS
# --------
# The book states no variants for this exercise.


# TEXTBOOK CODE COMPARISON
# ------------------------
# - Name: book `def get_max_trapped_water(heights):`; file
#   `def max_water_container(heights: list[int]) -> int:` (renamed, type
#   hints added).
# - Variables: book `i, j, max_water` initialised in one tuple assignment
#   and a separate `width = j - i`; file uses `left, right` and `best`, and
#   computes the width inline.
# - Tie handling differs: the book tests `if heights[i] > heights[j]:
#   j -= 1 else: i += 1` (on equal heights it advances the LEFT pointer);
#   the file tests `heights[left] < heights[right]` (on equal heights it
#   moves the RIGHT pointer). Both are correct and return the same maximum.
# - Neither returns the pair of indices that the problem statement asks
#   for; both return the maximum water.


# Python executes this block only when this source file is run directly.
# When pytest imports the file, this block is skipped automatically.
# Documentation: https://docs.python.org/3/library/__main__.html
if __name__ == "__main__":

    # Demonstrations check representative input/output behavior: empty
    # input, a single line, the smallest real container, and a classic
    # larger example (all added; the book's Figure 17.4 array is not used).
    #
    # `assert` raises AssertionError if its condition is False; these are
    # quick smoke checks, pytest does the thorough testing.
    observed = max_water_container([])
    print("max_water_container:", observed)
    assert observed == 0
    observed = max_water_container([1])
    print("max_water_container:", observed)
    assert observed == 0
    observed = max_water_container([1, 1])
    print("max_water_container:", observed)
    assert observed == 1
    observed = max_water_container([1, 8, 6, 2, 5, 4, 8, 3, 7])
    print("max_water_container:", observed)
    assert observed == 49
