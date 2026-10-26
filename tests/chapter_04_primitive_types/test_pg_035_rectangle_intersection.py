"""Independent tests for EPI 4.11.

pytest parameterization: https://docs.pytest.org/en/stable/how-to/parametrize.html
"""

# pytest enables one test function to run over several examples.
# Documentation: https://docs.pytest.org/en/stable/
import pytest

# Standard library: copies mutable inputs so tests do not share state.
# Documentation: https://docs.python.org/3/library/copy.html
import copy

from epi_python.chapter_04_primitive_types.pg_035_rectangle_intersection import intersect_rectangle, Rectangle

@pytest.mark.parametrize(("args", "expected"), [
    ((Rectangle(0, 0, 2, 2), Rectangle(1, 1, 3, 3)), Rectangle(1, 1, 1, 1)),
])
def test_examples(args, expected):
    """Verify representative and boundary conditions independently."""
    assert intersect_rectangle(*copy.deepcopy(args)) == expected

from epi_python.chapter_04_primitive_types.pg_035_rectangle_intersection import Rectangle


def test_non_overlapping_rectangles():
    assert intersect_rectangle(Rectangle(0, 0, 1, 1), Rectangle(4, 4, 1, 1)) == Rectangle(0, 0, -1, -1)


def test_boundary_touch_is_intersection_in_the_pdf():
    assert intersect_rectangle(Rectangle(0, 0, 1, 1), Rectangle(1, 0, 1, 1)) == Rectangle(1, 0, 0, 1)
