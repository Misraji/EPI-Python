"""Independent tests for EPI 5.3.

pytest parameterization: https://docs.pytest.org/en/stable/how-to/parametrize.html
"""

# pytest enables one test function to run over several examples.
# Documentation: https://docs.pytest.org/en/stable/
import pytest

# Standard library: copies mutable inputs so tests do not share state.
# Documentation: https://docs.python.org/3/library/copy.html
import copy

from epi_python.chapter_05_arrays.pg_043_multiply_digits import multiply_digits

@pytest.mark.parametrize(("args", "expected"), [
    (([1, 2, 3], [4, 5]), [5, 5, 3, 5]),
    (([-2], [3]), [-6]),
    (([0], [1, 2]), [0]),
    (([9, 9], [9, 9]), [9, 8, 0, 1]),
])
def test_examples(args, expected):
    """Verify representative and boundary conditions independently."""
    assert multiply_digits(*copy.deepcopy(args)) == expected

