"""Independent tests for EPI 5.18.

pytest parameterization: https://docs.pytest.org/en/stable/how-to/parametrize.html
"""

# pytest enables one test function to run over several examples.
# Documentation: https://docs.pytest.org/en/stable/
import pytest

# Standard library: copies mutable inputs so tests do not share state.
# Documentation: https://docs.python.org/3/library/copy.html
import copy

from epi_python.chapter_05_arrays.pg_061_spiral_ordering import matrix_in_spiral_order

@pytest.mark.parametrize(("args", "expected"), [
    (([[1,2], [3,4]],), [1,2,4,3]),
    (([[1,2,3]],), [1,2,3]),
    (([[1], [2], [3]],), [1,2,3]),
    (([], ), []),
    (([[1,2,3], [4,5,6]],), [1,2,3,6,5,4]),
])
def test_examples(args, expected):
    """Verify representative and boundary conditions independently."""
    assert matrix_in_spiral_order(*copy.deepcopy(args)) == expected

