"""Independent tests for EPI 9.8.

pytest parameterization: https://docs.pytest.org/en/stable/how-to/parametrize.html
"""

# pytest enables one test function to run over several examples.
# Documentation: https://docs.pytest.org/en/stable/
import pytest

# Standard library: copies mutable inputs so tests do not share state.
# Documentation: https://docs.python.org/3/library/copy.html
import copy

from epi_python.chapter_09_binary_trees.pg_121_preorder_without_recursion import preorder_values

@pytest.mark.parametrize(("args", "expected"), [
    ((None,), []),
    (((2,(1,None,None),(3,None,None)),), [2,1,3]),
    (((1,(2,(4,None,None),None),(3,None,None)),), [1,2,4,3]),
])
def test_examples(args, expected):
    """Verify representative and boundary conditions independently."""
    assert preorder_values(*copy.deepcopy(args)) == expected

