"""EPI Python — Exercise 24.19: Find the Line Through the Most Points

Chapter 24: Honors Class
Textbook: pages 375–376 (printed page numbers; problem and solution start on 375).

PROBLEM (from the textbook)
---------------------------
"You are given a set of points in the plane. Each point has integer
coordinates. Design an algorithm for computing a line that contains the
maximum number of points in the set."

HINT (from the textbook)
------------------------
"A line can be uniquely represented by two numbers."

SOLUTION DEVELOPMENT (following the textbook)
---------------------------------------------
Although there are infinitely many lines in the plane, only lines passing
through at least two of the given points matter.

Brute force: enumerate every line determined by a pair of points (there are
n(n - 1)/2 pairs for n points), keep the lines in a hash table, and then for
each line iterate over all points and test whether each point lies on it.
Iterating over all points for every line costs O(n * n(n - 1)/2) = O(n^3).

Better: as each pair of points is processed, immediately add both points to
the point-set of the line they define. Each pair needs one lookup, possibly
an insert of a new line into the hash table, and two inserts into that
line's point-set; all are O(1) hash-table operations, so this phase takes
O(n^2) time. Space is also O(n^2), which follows from the time bound. It
might appear the space could be larger (O(n^2) lines, each holding up to
O(n) points), but the number of lines and the number of points per line are
inversely related. A final pass over the at most n(n - 1)/2 lines finds the
one with the largest point-set, so the overall time is O(n^2).

Designing a hash function for lines is the subtle part. The line through
(x1, y1) and (x2, y2) is

    y = ((y2 - y1) / (x2 - x1)) * x + (x2*y1 - x1*y2) / (x2 - x1).

* Hashing the slope and Y-intercept as a pair of floating-point numbers is
  fragile: with finite-precision arithmetic, three collinear points may be
  mapped to different buckets.
* A robust approach treats the slope and intercept as rationals, i.e. pairs
  of integers (numerator, denominator), put into a canonical form before
  hashing: for example, the denominator is made nonnegative and relatively
  prime to the numerator.
* Lines parallel to the Y-axis (vertical lines) are a special case: use the
  X-intercept in place of the Y-intercept and use 1/0 as the slope.

The printed program then simplifies the bookkeeping: it fixes each point p1
in turn as an anchor and, in a fresh table, counts the later points p2 by
the reduced direction (x difference, y difference) from p1. Points identical
to p1 are counted separately as overlap points. All points with the same
reduced direction from the same anchor lie on one line through the anchor,
so no intercept is needed. The answer is the maximum, over anchors, of the
overlap count plus the largest slope count. The single function in this
file, find_line_with_most_points, follows that program (see the code
comparison near the end of the file for its differences from the book).
Note that the program returns the number of points on the best line rather
than the line itself.

ADDITIONAL EXAMPLES (added for learning; not printed in this exercise)
---------------------------------------------------------------------
    points (0,0), (1,1), (2,2), (0,1)  -> 3  ((0,0), (1,1), (2,2) on y = x)
"""

# Python standard library: specialized container types.
# Module documentation: https://docs.python.org/3/library/collections.html
# defaultdict API: https://docs.python.org/3/library/collections.html#collections.defaultdict
from collections import defaultdict

# Python standard library: mathematical functions.
# Module documentation: https://docs.python.org/3/library/math.html
# gcd API: https://docs.python.org/3/library/math.html#math.gcd
from math import gcd

# Python standard library: specialized container types.
# Module documentation: https://docs.python.org/3/library/collections.html
# namedtuple API: https://docs.python.org/3/library/collections.html#collections.namedtuple
from collections import namedtuple


# collections.namedtuple('Point', ('x', 'y')) creates a new class: a tuple
# subclass whose two items can also be read by name, as p.x and p.y. A
# Point is immutable and hashable like an ordinary tuple, and two Points
# with the same coordinates compare equal with `==`, which the algorithm
# uses to detect duplicate (overlapping) points. This matches the book.
Point=namedtuple('Point',('x','y'))


# Type hints: `points: list[Point]` says the argument is expected to be a
# list of Point objects and `-> int` says an int is returned. Annotations
# are documentation for readers and tools; Python does not enforce them at
# run time. (The book's function has no annotations.)
def find_line_with_most_points(points: list[Point]) -> int:
    """Return the largest number of input points lying on one line.

    This is the textbook's single implementation (anchor point plus a
    table of reduced slopes), with the small changes recorded in the
    TEXTBOOK CODE COMPARISON block below.
    """
    result=0

    # enumerate(points) yields (index, item) pairs: (0, points[0]),
    # (1, points[1]), ... The index i is needed so that the inner loop can
    # consider only points after p1, so each pair is examined exactly once.
    for i,p1 in enumerate(points):

        # collections.defaultdict(int) is a dictionary that, when a missing
        # key is read or updated, first inserts that key with the value
        # int() == 0. That lets `slope_table[key] += 1` count occurrences
        # without checking whether the key exists. A fresh table is built
        # for each anchor p1, since slopes are relative to p1.
        slope_table=defaultdict(int)

        # p1 itself is on every line through p1, so start at 1.
        overlap_points=1

        # points[i+1:] is a slice: a new list with the items after index i.
        # (Slicing copies; that costs O(n) per anchor, within the O(n^2) total.)
        for p2 in points[i+1:]:
            if p1==p2:
                overlap_points+=1
            else:

                # Tuple packing/unpacking assigns both differences in one
                # statement: the right-hand side builds a 2-tuple and its
                # items are assigned to x_diff and y_diff in order.
                x_diff,y_diff=p1.x-p2.x,p1.y-p2.y

                # math.gcd(a, b) returns the greatest common divisor of
                # two integers. The result is always nonnegative, and
                # gcd(0, b) == abs(b). Because p1 != p2, at least one
                # difference is nonzero, so divisor > 0 and the divisions
                # below are safe. Dividing both differences by their gcd
                # reduces the direction to lowest terms, e.g. (2, 4) and
                # (3, 6) both become (1, 2), so equal slopes share a key.
                divisor=gcd(x_diff,y_diff)

                # `//` is floor division. Since divisor divides both values
                # exactly, the results are exact integers (no floats, so no
                # rounding problems as warned about in the book).
                x_diff//=divisor
                y_diff//=divisor

                # Canonical sign: (1, 2) and (-1, -2) describe the same
                # direction. Flip signs so x_diff is positive, or, for a
                # vertical direction (x_diff == 0), so y_diff is positive.
                # A vertical line therefore always gets the key (0, 1),
                # the book's "slope 1/0".
                if x_diff<0 or (x_diff==0 and y_diff<0):
                    x_diff,y_diff=-x_diff,-y_diff

                # The key is a tuple; tuples of ints are hashable and can
                # be dictionary keys.
                slope_table[(x_diff,y_diff)]+=1

        # slope_table.values() is a view of all counts. max(iterable,
        # default=0) returns the largest item, or 0 if the iterable is
        # empty (which happens when p1 is the last point or all later
        # points coincide with p1); without default=, max() would raise
        # ValueError on an empty iterable. The outer max keeps the best
        # count over all anchors.
        result=max(result,overlap_points+max(slope_table.values(),default=0))
    return result


# TEXTBOOK POST-SOLUTION DISCUSSION (pages 375–376)
# -------------------------------------------------
# The book prints no further analysis after the program; the exercise ends
# with the listing. The complexity discussion (O(n^2) time and O(n^2) space
# for the hash-table-of-lines approach) comes before the program and is
# summarized in the module docstring. For the printed anchor-based program,
# the two nested loops examine each of the n(n - 1)/2 pairs once, and each
# per-anchor table holds at most n - 1 entries.
#
# VARIANTS
# --------
# The book states no variants for this exercise.


# TEXTBOOK CODE COMPARISON
# ------------------------
# * Point: the book writes `collections.namedtuple("Point", ("x", "y"))`;
#   the file imports `namedtuple` directly. Same behaviour.
# * Imports: the book uses `collections.defaultdict` and `fractions.gcd`;
#   the file uses `from collections import defaultdict` and
#   `from math import gcd` (fractions.gcd no longer exists in current
#   Python 3; it was removed in Python 3.9).
# * Signature: book `def find_line_with_most_points(points)`; file adds
#   type hints `points: list[Point]` and `-> int`.
# * Vertical lines: the book has an explicit branch
#   `elif p1.x == p2.x:` that counts key (0, 1) with the comment
#   "# A vertical line with slope 1/0." The file has no such branch;
#   vertical pairs go through the general gcd path and the sign
#   normalization turns them into (0, 1).
# * Reduction: the book divides with `/` (true division, which produces
#   floats in Python 3) and stores the variable as `gcd`; the file uses
#   `divisor` and floor division `//=`, keeping integer keys.
# * Sign normalization: the book has no sign-normalizing step, so in the
#   book (1, 2) and (-1, -2) could be distinct keys depending on how gcd
#   signs its result; the file adds
#   `if x_diff<0 or (x_diff==0 and y_diff<0): ...` to make keys canonical.
# * The final `result = max(...)` and return statement match the book.


# Python executes this block only when this source file is run directly.
# When pytest imports the file, this block is skipped automatically.
# Documentation: https://docs.python.org/3/library/__main__.html
if __name__=='__main__':

    # Added example: three points on the line y = x plus one point off it.
    points=[Point(0,0),Point(1,1),Point(2,2),Point(0,1)]

    # print() with several arguments separates them with a space.
    print('Most collinear points:',find_line_with_most_points(points))

    # `assert` stops the program with an AssertionError if the condition
    # is false. This is a quick smoke check; the pytest suite in tests/
    # provides the more thorough verification.
    assert find_line_with_most_points(points)==3
