"""Independent tests for EPI 4.5.

pytest parameterization: https://docs.pytest.org/en/stable/how-to/parametrize.html
"""

# pytest enables one test function to run over several examples.
# Documentation: https://docs.pytest.org/en/stable/
import pytest

# Standard library: copies mutable inputs so tests do not share state.
# Documentation: https://docs.python.org/3/library/copy.html
import copy

from epi_python.chapter_04_primitive_types.pg_029_multiply_without_arithmetic import multiply

@pytest.mark.parametrize(("args", "expected"), [
    ((0, 9), 0),
    ((7, 6), 42),
    ((13, 9), 117),
    ((1, 12345), 12345),
    ((15, 15), 225),
])
def test_examples(args, expected):
    """Verify representative and boundary conditions independently."""
    assert multiply(*copy.deepcopy(args)) == expected

