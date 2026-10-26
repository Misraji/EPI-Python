"""EPI Python — Exercise 16.8: Find the Minimum Weight Path in a Triangle

Chapter 16: Dynamic Programming
Textbook: pages 251–252 (printed page numbers; problem and solution start on 251).

PROBLEM (from the textbook)
---------------------------
"A sequence of integer arrays in which the nth array consists of n entries
naturally corresponds to a triangle of numbers. See Figure 16.10 for an
example."

Figure 16.10 (a number triangle):
              2
            4   4
          8   5   6
        4   2   6   2
      1   5   2   3   4

"Define a path in the triangle to be a sequence of entries in the triangle
in which adjacent entries in the sequence correspond to entries that are
adjacent in the triangle. The path must start at the top, descend the
triangle continuously, and end with an entry on the bottom row. The weight
of a path is the sum of the entries."

"Write a program that takes as input a triangle of numbers and returns the
weight of a minimum weight path. For example, the minimum weight path for
the number triangle in Figure 16.10 is shown in bold face, and its weight
is 15."
(The bold entries are 2, 4, 5, 2, 2: 2 + 4 + 5 + 2 + 2 = 15.)

HINT (from the textbook)
------------------------
"What property does the prefix of a minimum weight path have?"

SOLUTION DEVELOPMENT (following the textbook)
---------------------------------------------
Brute force: enumerate every path. Paths are easy to enumerate, but a
triangle with n rows has 2^(n-1) of them.

Better: look at the entries of row i. For any entry, take a minimum weight
path ending there; the part of that path ending in the previous row must
itself be a minimum weight path (to its own endpoint). That gives a DP:
compute, row by row, the minimum weight of a path ending at each entry.
Once row i is done, row i - 1's results are no longer needed for row
i + 1, so storage can be reused (only one row of results is kept).

In list form, entry j of a row is adjacent to entries j - 1 and j of the
row above (where they exist).

The book's program minimum_path_weight(triangle) does exactly this with a
list comprehension; this file implements the same program.

ADDITIONAL EXAMPLES (added for learning; not printed in this exercise)
---------------------------------------------------------------------
    [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]] -> 11   (2 + 3 + 5 + 1)
"""


def minimum_path_weight(triangle: list[list[int]]) -> int:
    """Return the weight of a minimum weight top-to-bottom path (textbook).

    An empty triangle returns 0 (a guard not in the book).
    """

    # Type hints such as `list[list[int]]` document intended types only;
    # Python does not enforce them.
    if not triangle:
        return 0

    # Minimum path weights ending at each entry of the current row. [0]
    # acts as a virtual row above the apex, so the apex gets 0 + its value.
    min_weight_to_curr_row = [0]
    for row in triangle:

        # The list comprehension builds the NEW row of minima from the old
        # one; the old list is read completely before the name is rebound,
        # so no value is overwritten too early.
        #
        # For entry j the two possible parents are j - 1 and j in the
        # previous row (which has one entry fewer). `max(j-1, 0)` clamps the
        # left parent at 0 for the first entry; `min(j, len(prev) - 1)`
        # clamps the right parent at the last index for the final entry. At
        # the edges both indices then name the same single parent.
        # The built-ins max(a, b) / min(a, b) return the larger / smaller
        # argument.
        min_weight_to_curr_row = [
            row[j] + min(min_weight_to_curr_row[max(j-1,0)],
                         min_weight_to_curr_row[min(j,len(min_weight_to_curr_row)-1)])
            for j in range(len(row))
        ]

    # min(list) returns the smallest item: the best path ending anywhere on
    # the bottom row.
    return min(min_weight_to_curr_row)


# TEXTBOOK POST-SOLUTION DISCUSSION (page 252)
# --------------------------------------------
# Each element takes O(1) time, and there are 1 + 2 + ... + n = n(n + 1)/2
# elements, so the time is O(n^2). The space is O(n) (one row of minima).
#
# VARIANTS
# --------
# The book states no variants for this exercise.


# TEXTBOOK CODE COMPARISON
# ------------------------
# * File adds the guard `if not triangle: return 0` (the book's version
#   would return min([0]) = 0 as well, so the behaviour is the same) and
#   type hints.
# * Otherwise the code matches the book's listing.


# Python executes this block only when this source file is run directly.
# When pytest imports the file, this block is skipped automatically.
# Documentation: https://docs.python.org/3/library/__main__.html
if __name__ == '__main__':

    # The first triangle is the book's Figure 16.10 (its minimum path weight
    # is 15, as the book states); it is printed only. The assertion uses an
    # added example: 2 + 3 + 5 + 1 = 11.
    # `assert` stops the program with an AssertionError if the condition is
    # false; this is a quick smoke check, the pytest suite is thorough.
    triangle = [[2],[4,4],[8,5,6],[4,2,6,2],[1,5,2,3,4]]
    print('Minimum triangle path:',minimum_path_weight(triangle))
    assert minimum_path_weight([[2],[3,4],[6,5,7],[4,1,8,3]])==11
