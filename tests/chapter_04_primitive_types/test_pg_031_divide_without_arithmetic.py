"""Independent tests for EPI 4.6.

pytest parameterization: https://docs.pytest.org/en/stable/how-to/parametrize.html
"""

# pytest enables one test function to run over several examples.
# Documentation: https://docs.pytest.org/en/stable/
import pytest

# Standard library: copies mutable inputs so tests do not share state.
# Documentation: https://docs.python.org/3/library/copy.html
import copy

from epi_python.chapter_04_primitive_types.pg_031_divide_without_arithmetic import divide

@pytest.mark.parametrize(("args", "expected"), [
    ((0, 3), 0),
    ((7, 2), 3),
    ((100, 10), 10),
    ((5, 9), 0),
    ((31, 3), 10),
])
def test_examples(args, expected):
    """Verify representative and boundary conditions independently."""
    assert divide(*copy.deepcopy(args)) == expected

