"""EPI Python — Exercise 24.26: Draw the Skyline

Chapter 24: Honors Class
Textbook: pages 386–388 (printed page numbers; problem and solution start
on 386).

PROBLEM (from the textbook)
---------------------------
"A number of buildings are visible from a point. A building appears as a
rectangle, with the bottom of each building lying on a fixed horizontal
line. A building is specified using its left and right coordinates, and its
height. One building may partly obstruct another, as shown in Figure
24.8(a) on the facing page. The skyline is the list of coordinates and
corresponding heights of what is visible."

The book's example: Figure 24.8(a) (page 387) shows eight overlapping
buildings labelled A to H on x-coordinates 0 to 18 with heights up to 6
(F is the tallest), and Figure 24.8(b) shows their skyline. (The patterned
rectangles inside the skyline in Figure 24.8(b) belong to Problem 17.8 on
page 270 and are not relevant here.)

"Design an efficient algorithm for computing the skyline."

HINT (from the textbook)
------------------------
"Think of an efficient way of merging skylines."

SOLUTION DEVELOPMENT (following the textbook)
---------------------------------------------
Incremental approach: the skyline of one building is trivial. To add a new
building with left and right coordinates L and R and height H to a known
skyline, scan the existing skyline from the left to find where L belongs,
then continue until R is passed, raising every height that is below H up to
H. This is simple but O(n^2) for n buildings, since adding the n-th building
can need O(n) comparisons.

Key observation: two skylines (each listed in left-to-right order) can be
merged in linear time, the same time it takes to merge a single building in,
while accomplishing far more.

Textbook solution (described, not printed): divide and conquer. Compute the
skyline of each half of the buildings and merge the two results. The merge
resembles adding a single building: walk both skylines left to right,
matching X coordinates and updating heights, in O(n) time. The book says its
website links to a program for this algorithm. The recurrence
T(n) = 2T(n/2) + O(n) (the O(n) is the merge) solves to O(n log n).

Merge example from Figure 24.8: merge the skyline of buildings A, B, C, D
with that of E, F, G, H. From 0 to 7 only A-D are present, so their skyline
sets the height. At 7 the A-D skyline is taller than the E-H one, so its
height 4 is used from there. At 8 the E-H skyline is taller, so its height 3
is used. After 9 only E-H buildings remain, so their skyline sets the
height.

Alternative printed by the book, described as hugely simpler and, except on
degenerate inputs, much faster in practice: "digitize" the problem. Let l be
the left-most coordinate of any building and r the right-most; the skyline
spans l to r. Keep an array whose i-th entry is the current skyline height at
coordinate i, initially all 0s. For each building, iterate over its
coordinates and wherever the skyline is lower than the building, raise it to
the building's height.

The program in this file, compute_skyline, is this digitized algorithm (the
only program the book prints for this exercise). The divide-and-conquer
algorithm is not implemented in the book or in this file.

ADDITIONAL EXAMPLES (added for learning; not printed in this exercise)
---------------------------------------------------------------------
    buildings (1,3,h=2), (2,4,h=4)  ->  [(1,1,h=2), (2,4,h=4)]
    (coordinates are integer and inclusive at both ends)
"""

# Python standard library: specialized container types.
# Module documentation: https://docs.python.org/3/library/collections.html
# namedtuple API: https://docs.python.org/3/library/collections.html#collections.namedtuple
from collections import namedtuple


# collections.namedtuple('Rectangle', ('left', 'right', 'height')) creates a
# tuple subclass whose items can also be read by name: b.left, b.right,
# b.height. Instances are immutable, print readably (e.g.
# Rectangle(left=1, right=1, height=2)), and compare equal when all fields
# are equal, which the __main__ assertion uses. A Rectangle describes both
# input buildings and output skyline segments. This matches the book.
Rectangle=namedtuple('Rectangle',('left','right','height'))


# Type hints: input and output are lists of Rectangle. Annotations are
# documentation only; Python does not enforce them.
def compute_skyline(buildings: list[Rectangle]) -> list[Rectangle]:
    """Digitized integer-coordinate version printed in the book.

    This is the textbook's "alternative to the textbook solution" (the only
    program printed for this exercise). It returns maximal runs of equal
    height as Rectangles with inclusive integer left/right coordinates.
    """

    # Added guard (not in the book): min()/max() below would raise
    # ValueError on an empty list.
    if not buildings:return []

    # min()/max() over a generator expression: `b.left for b in buildings`
    # produces each building's left coordinate lazily, and min() returns the
    # smallest. These give the skyline's extent l..r.
    # Docs: https://docs.python.org/3/library/functions.html#min
    #       https://docs.python.org/3/library/functions.html#max
    min_left=min(b.left for b in buildings)
    max_right=max(b.right for b in buildings)

    # `[0] * k` builds a list of k zeros: one height per integer coordinate
    # from min_left to max_right inclusive (hence the + 1). Index
    # i - min_left corresponds to coordinate i.
    heights=[0]*(max_right-min_left+1)

    # Raise the skyline under each building to the building's height.
    # range(a, b + 1) covers a..b inclusive.
    for building in buildings:
        for i in range(building.left,building.right+1):
            heights[i-min_left]=max(heights[i-min_left],building.height)

    # Turn the height array into segments: whenever the height changes
    # between positions i - 1 and i, close the run that ended at i - 1.
    # `;` puts two statements on one line.
    result=[];left=0
    for i in range(1,len(heights)):
        if heights[i]!=heights[i-1]:
            result.append(Rectangle(left+min_left,i-1+min_left,heights[i-1]))
            left=i

    # Close the final run; heights[-1] is the last element. `+` concatenates
    # the result list with a one-element list.
    return result+[Rectangle(left+min_left,max_right,heights[-1])]


# TEXTBOOK POST-SOLUTION DISCUSSION (page 388)
# --------------------------------------------
# The digitized algorithm runs in O(nW) time, where W is the width of the
# widest building. In theory W can be huge, which would make it much worse
# than the O(n log n) divide-and-conquer solution. In practice W is a
# constant, so the digitized version is much faster, and it is also far
# simpler to write and to understand.
#
# VARIANTS
# --------
# * Solve the skyline problem when each building is shaped like an
#   isosceles triangle with a 90 degree angle at its apex.
#   (stated in the book; no solution given)


# TEXTBOOK CODE COMPARISON
# ------------------------
# * Import: book uses `collections.namedtuple(...)`; file imports
#   `namedtuple` directly. The Rectangle definition is otherwise the same.
# * Signature: book `def compute_skyline(buildings)`; file adds type hints
#   `list[Rectangle]` for the parameter and return value.
# * Added guard `if not buildings:return []` (not in the book).
# * Extent: book `min(buildings, key=lambda b: b.left).left` and
#   `max(buildings, key=lambda b: b.right).right`; file uses
#   `min(b.left for b in buildings)` / `max(b.right for b in buildings)`.
#   Same values.
# * `result = []` and `left = 0` are on one line separated by `;` in the
#   file. The loops and the return statement match the book.
# * The divide-and-conquer textbook solution is not printed in the book
#   (it refers to its website) and is not present in the file.


# Python executes this block only when this source file is run directly.
# When pytest imports the file, this block is skipped automatically.
# Documentation: https://docs.python.org/3/library/__main__.html
if __name__=='__main__':

    # Added example: a height-2 building on 1..3 partly hidden by a
    # height-4 building on 2..4.
    r=compute_skyline([Rectangle(1,3,2),Rectangle(2,4,4)])
    print('Skyline:',r)

    # `assert` stops with an AssertionError if the condition is false.
    # Named tuples compare like ordinary tuples, item by item. pytest
    # provides the more thorough verification.
    assert r==[Rectangle(1,1,2),Rectangle(2,4,4)]
