"""EPI Python — Exercise 16.5: Search for a Sequence in a 2D Array

Chapter 16: Dynamic Programming
Textbook: pages 245–246 (printed page numbers; problem and solution start on 245).

PROBLEM (from the textbook)
---------------------------
"Suppose you are given a 2D array of integers (the "grid"), and a 1D array
of integers (the "pattern"). We say the pattern occurs in the grid if it is
possible to start from some entry in the grid and traverse adjacent entries
in the order specified by the pattern till all entries in the pattern have
been visited. The entries adjacent to an entry are the ones directly above,
below, to the left, and to the right, assuming they exist. For example, the
entries adjacent to (3,4) are (3,3), (3,5), (2,4) and (4,4). It is
acceptable to visit an entry in the grid more than once.

As an example, if the grid is

    [1 2 3]
    [3 4 5]
    [5 6 7]

and the pattern is <1,3,4,6>, then the pattern occurs in the grid—consider
the entries <(0,0), (1,0), (1,1), (2,1)>. However, <1,2,3,4> does not occur
in the grid."

"Write a program that takes as arguments a 2D array and a 1D array, and
checks whether the 1D array occurs in the 2D array."

HINT (from the textbook)
------------------------
"Start with length 1 prefixes of the 1D array, then move on to length
2, 3, ... prefixes."

SOLUTION DEVELOPMENT (following the textbook)
---------------------------------------------
Brute force: enumerate all 1D subarrays (paths) of the 2D array. There are
very many, and the search is not guided by the pattern being sought.

Guided search: let the 2D array be A and the pattern S. Suppose some suffix
of S remains to be matched, together with a starting point. If the suffix
is empty, we are done. Otherwise the suffix occurs from that point exactly
when its first entry equals the entry at the starting point AND the rest of
the suffix occurs starting at some point adjacent to it.

Example, searching for <1,3,4,6> from (0,0): 1 matches A[0][0], so search
for <3,4,6> from (0,1) — which fails at once since A[0][1] != 3 — and from
(1,0). Since A[1][0] = 3, search for <4,6> from the neighbours of (1,0):
from (0,0), which fails immediately, and then from (1,1), which eventually
succeeds. (The book's text says "(0,1)'s neighbors" at this step.)
[NEEDS PDF REVIEW: page 245, the step "search for <4,6> from (0,1)'s
neighbors" — the matched entry is (1,0); confirm the printed wording.]

The same (position, suffix) question can be asked many times, so the
book's program caches intermediate results to avoid repeated recursive
calls with identical arguments. Its program
is_pattern_contained_in_grid(grid, S) has a nested
is_pattern_suffix_contained_starting_at_xy(x, y, offset) and a set
previous_attempts of failed (x, y, offset) states. This file implements the
same algorithm.

ADDITIONAL EXAMPLES (added for learning; not printed in this exercise)
---------------------------------------------------------------------
    grid [[1,2,3],[4,5,6],[7,8,9]], pattern [1,2,5,8] -> True
        (path (0,0) -> (0,1) -> (1,1) -> (2,1))
"""


def is_pattern_contained_in_grid(grid: list[list[int]], s: list[int]) -> bool:
    """Return True if pattern `s` can be traced through adjacent grid cells.

    This is the textbook's memoized search (book parameter name `S`). Cells
    may be revisited. An empty pattern is reported as contained.
    """

    # Each entry in previous_attempts is a point in the grid and a suffix of
    # the pattern (identified by its offset). Presence means that suffix is
    # NOT contained in the grid starting from that point (the book's
    # comment). Only failures need recording: a success ends the whole
    # search immediately.
    #
    # `set()` creates an empty set (`{}` would be an empty dict). Tuples are
    # hashable, so (x, y, offset) can be stored in a set and looked up in
    # O(1) average time. The type hint `set[tuple[int,int,int]]` documents
    # this; Python does not enforce hints.
    previous_attempts: set[tuple[int,int,int]] = set()

    # Nested recursive helper: does the suffix s[offset:] occur starting at
    # grid entry (x, y)? It mutates the enclosing set with .add(); no
    # `nonlocal` is needed because the name is never rebound.
    def is_pattern_suffix_contained_starting_at_xy(x: int, y: int, offset: int) -> bool:

        # Nothing left to complete.
        if len(s) == offset:
            return True

        # All of the following must hold, checked left to right with
        # short-circuit `and` (later tests run only if earlier ones pass):
        # * `0 <= x < len(grid)` is a chained comparison meaning
        #   `0 <= x and x < len(grid)`; with the y test it checks that (x, y)
        #   lies inside the grid (so the indexing after it is safe);
        # * the entry equals the next pattern value s[offset];
        # * this state is not already known to fail (the memoization);
        # * some neighbour continues the match. `any(...)` over a generator
        #   expression stops at the first True. The tuple of (a, b) offsets
        #   lists the four neighbours: up, down, left, right.
        if (0 <= x < len(grid) and 0 <= y < len(grid[x])
            and grid[x][y] == s[offset]
            and (x,y,offset) not in previous_attempts
            and any(is_pattern_suffix_contained_starting_at_xy(x+a,y+b,offset+1)
                    for a,b in ((-1,0),(1,0),(0,-1),(0,1)))):
            return True

        # Remember the failure so the same question is never re-explored.
        previous_attempts.add((x,y,offset))
        return False

    # Try every grid entry as the starting point for the whole pattern.
    # The generator has two `for` clauses, like nested loops over rows i and
    # columns j. `A or B` returns A if it is truthy, else B: `or not s` makes
    # the result True for an empty pattern even when the grid is empty (the
    # helper alone would already say True for an empty pattern on a
    # nonempty grid).
    return any(is_pattern_suffix_contained_starting_at_xy(i,j,0)
               for i in range(len(grid)) for j in range(len(grid[i]))) or not s


# TEXTBOOK POST-SOLUTION DISCUSSION (page 246)
# --------------------------------------------
# The complexity is O(nm|S|), where n and m are the dimensions of A: each
# call does a constant amount of work apart from its recursive calls, and
# the number of calls is bounded (the book phrases the bound in terms of the
# entries of the 2D array; with the offset there are at most nm|S|
# distinct (x, y, offset) states).
#
# VARIANTS (each stated in the book; no solution given)
# ----------------------------------------------------
# 1. Solve the same problem when you cannot visit an entry in A more than
#    once.
# 2. Enumerate all solutions when you cannot visit an entry in A more than
#    once.


# TEXTBOOK CODE COMPARISON
# ------------------------
# * Book parameter `S`; file `s`. Type hints added (including on the
#   `previous_attempts` set).
# * Book creates `previous_attempts = set()` after defining the helper;
#   file creates it before.
# * Book returns `any(... for i in range(len(grid)) for j in
#   range(len(grid[i])))`; file appends `or not s`, so an empty pattern on
#   an empty grid returns True (the book would return False).
# * Helper body (conditions, neighbour offsets, recording failures)
#   matches the book. The book's comments ("Nothing left to complete.",
#   "Check if (x, y) lies outside the grid.", and the previous_attempts
#   explanation) are reflected above.


# Python executes this block only when this source file is run directly.
# When pytest imports the file, this block is skipped automatically.
# Documentation: https://docs.python.org/3/library/__main__.html
if __name__ == '__main__':

    # Added example: 1 -> 2 -> 5 -> 8 follows (0,0), (0,1), (1,1), (2,1).
    # `assert` stops the program with an AssertionError if the condition is
    # false; this is a quick smoke check, the pytest suite is thorough.
    grid=[[1,2,3],[4,5,6],[7,8,9]]
    print('Pattern found:',is_pattern_contained_in_grid(grid,[1,2,5,8]))
    assert is_pattern_contained_in_grid(grid,[1,2,5,8])
