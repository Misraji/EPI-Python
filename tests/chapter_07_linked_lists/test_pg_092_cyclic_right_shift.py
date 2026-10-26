"""Independent tests for EPI 7.9.

pytest parameterization: https://docs.pytest.org/en/stable/how-to/parametrize.html
"""

# pytest enables one test function to run over several examples.
# Documentation: https://docs.pytest.org/en/stable/
import pytest

# Standard library: copies mutable inputs so tests do not share state.
# Documentation: https://docs.python.org/3/library/copy.html
import copy

from epi_python.chapter_07_linked_lists.pg_092_cyclic_right_shift import cyclic_shift_values

@pytest.mark.parametrize(("args", "expected"), [
    (([1, 2, 3, 4], 1), [4,1,2,3]),
    (([1, 2, 3], 3), [1,2,3]),
    (([1, 2, 3], 5), [2,3,1]),
    (([], 3), []),
])
def test_examples(args, expected):
    """Verify representative and boundary conditions independently."""
    assert cyclic_shift_values(*copy.deepcopy(args)) == expected

