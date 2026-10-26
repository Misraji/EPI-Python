"""Independent tests for EPI 9.11.

pytest parameterization: https://docs.pytest.org/en/stable/how-to/parametrize.html
"""

# pytest enables one test function to run over several examples.
# Documentation: https://docs.pytest.org/en/stable/
import pytest

# Standard library: copies mutable inputs so tests do not share state.
# Documentation: https://docs.python.org/3/library/copy.html
import copy

from epi_python.chapter_09_binary_trees.pg_124_morris_inorder import morris_values

@pytest.mark.parametrize(("args", "expected"), [
    ((None,), []),
    (((2,(1,None,None),(3,None,None)),), [1,2,3]),
    (((4,(2,(1,None,None),(3,None,None)),(5,None,None)),), [1,2,3,4,5]),
])
def test_examples(args, expected):
    """Verify representative and boundary conditions independently."""
    assert morris_values(*copy.deepcopy(args)) == expected

from epi_python.chapter_09_binary_trees.pg_124_morris_inorder import build_tree, nested_tree, inorder_constant_space


def test_temporary_threads_are_removed():
    source=(4,(2,(1,None,None),(3,None,None)),(5,None,None))
    root=build_tree(source)
    assert inorder_constant_space(root) == [1,2,3,4,5]
    assert nested_tree(root) == source
