"""EPI Python — Exercise 4.11: Rectangle Intersection

Chapter 4: Primitive Types
Textbook: pages 35–36 (printed page numbers; problem and start of the
solution on 35; the rest of the solution, the program, complexity and
variants on 36).

PROBLEM (from the textbook)
---------------------------
This problem is concerned with rectangles whose sides are parallel to the
X-axis and Y-axis. See Figure 4.2 for examples.

Write a program which tests if two rectangles have a nonempty intersection.
If the intersection is nonempty, return the rectangle formed by their
intersection.

(Figure 4.2, "Examples of XY-aligned rectangles", is a drawing of ten
axis-aligned rectangles labelled A through J that touch or overlap in
various ways; the solution below refers to several pairs from it.)

HINT (from the textbook)
------------------------
Think of the X and Y dimensions independently.

SOLUTION DEVELOPMENT (following the textbook)
---------------------------------------------
The problem does not say whether the boundary belongs to a rectangle; the
book chooses to include it. So, for example, A and B in Figure 4.2 (which
only share a corner) do intersect.

Rectangles can meet in many qualitatively different ways (pairs from
Figure 4.2): partial overlap (D and F), one inside the other (F and G), a
shared side (D and E), a shared corner (A and B), a cross (B and C), a tee
(F and H), and so on. Handling every case separately is quite tricky.

A better approach is to look for conditions that guarantee the rectangles
do NOT intersect. Book example: the rectangle with lower-left point (1, 2),
width 3 and height 4 cannot meet the rectangle with lower-left point (5, 3),
width 2 and height 4, because the first covers X-values 1 to 1 + 3 = 4
(inclusive) and the second covers X-values 5 to 5 + 2 = 7 (inclusive); the
X ranges do not overlap. Likewise, if the Y ranges do not overlap, the
rectangles cannot intersect.

Put the other way: if the X ranges overlap AND the Y ranges overlap, every
point with an X in the common X range and a Y in the common Y range lies in
both rectangles, so the intersection is nonempty. The intersection is then
the rectangle spanned by those common ranges.

The book's program is `intersect_rectangle`, implemented below. When there
is no intersection it returns the sentinel Rectangle(0, 0, -1, -1).

ADDITIONAL EXAMPLES (added for learning; not printed in this exercise)
---------------------------------------------------------------------
    Rectangle(0,0,3,3) and Rectangle(2,1,5,5) -> Rectangle(2,1,1,2)
        (partial overlap)
    Rectangle(0,0,1,1) and Rectangle(1,0,1,1) -> Rectangle(1,0,0,1)
        (shared side: boundaries count, giving a zero-width result)
    Rectangle(0,0,1,1) and Rectangle(4,4,1,1) -> Rectangle(0,0,-1,-1)
        (separate: the "no intersection" sentinel)
"""

# Python standard library: specialized container types.
# Module documentation: https://docs.python.org/3/library/collections.html
# namedtuple: https://docs.python.org/3/library/collections.html#collections.namedtuple
import collections


# collections.namedtuple(typename, field_names) creates a new class: a tuple
# whose items can also be read by name. Rectangle(1, 2, 3, 4) has r.x == 1,
# r.y == 2, r.width == 3, r.height == 4, and still behaves like the tuple
# (1, 2, 3, 4) (so == compares field by field and printing shows the field
# names). Like all tuples it is immutable. Here (x, y) is the lower-left
# corner. This is the same definition the book uses.
Rectangle = collections.namedtuple('Rectangle', ('x','y','width','height'))


# Type hints (`a: Rectangle`, `-> Rectangle`) document intended types;
# Python does not enforce them at runtime.
def intersect_rectangle(a: Rectangle, b: Rectangle) -> Rectangle:
    """Return the boundary-inclusive overlap, or the book's no-overlap sentinel.

    This is the textbook implementation, with the book's nested
    `is_intersect` test written inline as its negation.
    """

    # The rectangles are disjoint exactly when one lies entirely to the
    # left/right of the other, or entirely above/below it. Strict `>` / `<`
    # are used, so rectangles that merely touch (share an edge or corner)
    # are NOT treated as disjoint: the boundary is part of the rectangle.
    # The parentheses let the condition continue onto the next line.
    if (a.x > b.x+b.width or a.x+a.width < b.x
            or a.y > b.y+b.height or a.y+a.height < b.y):

        # No intersection (book comment). Width and height of -1 cannot
        # describe a real rectangle, so this value works as a "none" marker.
        return Rectangle(0,0,-1,-1)

    # Tuple unpacking assigns two values at once. The overlap's lower-left
    # corner is the larger of the two lower-left coordinates, found with the
    # built-in max(); its upper-right corner uses the smaller of the two
    # right/top edges, found with min().
    # https://docs.python.org/3/library/functions.html#max
    # https://docs.python.org/3/library/functions.html#min
    x1,y1 = max(a.x,b.x), max(a.y,b.y)
    x2 = min(a.x+a.width,b.x+b.width)
    y2 = min(a.y+a.height,b.y+b.height)

    # Convert the corners back to (x, y, width, height) form.
    return Rectangle(x1,y1,x2-x1,y2-y1)


# TEXTBOOK POST-SOLUTION DISCUSSION (page 36)
# -------------------------------------------
# The time complexity is O(1), since the number of operations is constant.
#
# VARIANTS
# --------
# 1. Given four points in the plane, how would you check if they are the
#    vertices of a rectangle? (stated in the book; no solution given)
# 2. How would you check if two rectangles, not necessarily aligned with the
#    X and Y axes, intersect? (stated in the book; no solution given)


# TEXTBOOK CODE COMPARISON
# ------------------------
# - `Rectangle` namedtuple definition matches the book.
# - Book: `def intersect_rectangle(R1, R2)`; file: parameters renamed `a`,
#   `b`, with `Rectangle` type hints.
# - Book defines a nested helper `is_intersect(R1, R2)` returning
#   `R1.x <= R2.x + R2.width and R1.x + R1.width >= R2.x and R1.y <= ...`
#   and tests `if not is_intersect(R1, R2)`. File has no helper: it writes
#   the negated condition directly (`a.x > b.x+b.width or ...`), which is
#   logically equivalent.
# - Book returns `Rectangle(max(...), max(...), min(...) - max(...),
#   min(...) - max(...))` in one expression; file stores the corners in
#   `x1, y1, x2, y2` first. Same result, including the sentinel
#   `Rectangle(0, 0, -1, -1)`.


# Python executes this block only when this source file is run directly.
# When pytest imports the file, this block is skipped automatically.
# Documentation: https://docs.python.org/3/library/__main__.html
if __name__ == "__main__":

    # Each example is (first_rectangle, second_rectangle, expected_result):
    # partial overlap, a shared side (touching counts, giving zero width),
    # and two separate rectangles (the sentinel). All three are added.
    examples = ((Rectangle(0,0,3,3),Rectangle(2,1,5,5),Rectangle(2,1,1,2)),
                (Rectangle(0,0,1,1),Rectangle(1,0,1,1),Rectangle(1,0,0,1)),
                (Rectangle(0,0,1,1),Rectangle(4,4,1,1),Rectangle(0,0,-1,-1)))
    for a,b,expected in examples:
        result = intersect_rectangle(a,b)

        # f-string: each expression in {} is evaluated and inserted. A
        # namedtuple prints with its field names, e.g. Rectangle(x=2, y=1, ...).
        # https://docs.python.org/3/reference/lexical_analysis.html#f-strings
        print(f"intersection of {a} and {b}: {result}")

        # `assert` stops the program with an AssertionError if the condition
        # is false. Namedtuples compare equal when all fields are equal.
        # These are quick smoke checks; pytest does the thorough testing.
        assert result == expected
