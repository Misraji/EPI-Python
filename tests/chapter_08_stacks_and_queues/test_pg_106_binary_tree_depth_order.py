"""Independent tests for EPI 8.6.

pytest parameterization: https://docs.pytest.org/en/stable/how-to/parametrize.html
"""

# pytest enables one test function to run over several examples.
# Documentation: https://docs.pytest.org/en/stable/
import pytest

# Standard library: copies mutable inputs so tests do not share state.
# Documentation: https://docs.python.org/3/library/copy.html
import copy

from epi_python.chapter_08_stacks_and_queues.pg_106_binary_tree_depth_order import depth_order_values

@pytest.mark.parametrize(("args", "expected"), [
    ((None,), []),
    (((1, None, None),), [[1]]),
    (((1,(2,None,None),(3,None,None)),), [[1],[2,3]]),
])
def test_examples(args, expected):
    """Verify representative and boundary conditions independently."""
    assert depth_order_values(*copy.deepcopy(args)) == expected

