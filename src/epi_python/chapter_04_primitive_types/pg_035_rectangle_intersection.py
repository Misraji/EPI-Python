"""EPI exercise 4.11, printed page 35: Rectangle intersection.

EDUCATIONAL RECONSTRUCTION — not a verbatim verified code transcription.
Problem: Rectangle intersection.
Method/complexity: Constant-time intersection of axis-aligned rectangles, O(1) auxiliary space.
For the book's original explanation and variants, see:
    pg_035_exercise_04_11_rectangle_intersection.md

Run: python -m epi_python.chapter_04_primitive_types.pg_035_rectangle_intersection
Test: python -m pytest tests/chapter_04_primitive_types/test_pg_035_rectangle_intersection.py -v
"""

# NamedTuple supports tuple-like immutable records with named attributes.
# Documentation: https://docs.python.org/3/library/typing.html#typing.NamedTuple
from typing import NamedTuple


class Rectangle(NamedTuple):
    x: int
    y: int
    width: int
    height: int


def intersect_rectangle(a: Rectangle, b: Rectangle) -> Rectangle | None:
    """Return positive-area overlap, or None for no overlap."""
    x1, y1 = max(a.x, b.x), max(a.y, b.y)
    x2 = min(a.x + a.width, b.x + b.width)
    y2 = min(a.y + a.height, b.y + b.height)
    if x1 >= x2 or y1 >= y2:
        return None
    return Rectangle(x1, y1, x2 - x1, y2 - y1)


if __name__ == "__main__":
    a, b = Rectangle(0, 0, 3, 3), Rectangle(2, 1, 5, 5)
    print("intersection:", intersect_rectangle(a, b))
    assert intersect_rectangle(a, b) == Rectangle(2, 1, 1, 2)
