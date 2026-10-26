"""Independent tests for EPI 9.13.

pytest parameterization: https://docs.pytest.org/en/stable/how-to/parametrize.html
"""

# pytest enables one test function to run over several examples.
# Documentation: https://docs.pytest.org/en/stable/
import pytest

# Standard library: copies mutable inputs so tests do not share state.
# Documentation: https://docs.python.org/3/library/copy.html
import copy

from epi_python.chapter_09_binary_trees.pg_127_reconstruct_preorder_markers import reconstruct_marked_tree

@pytest.mark.parametrize(("args", "expected"), [
    (([1,2,None,None,3,None,None],), (1,(2,None,None),(3,None,None))),
    (([None],), None),
    (([1,None,None],), (1,None,None)),
])
def test_examples(args, expected):
    """Verify representative and boundary conditions independently."""
    assert reconstruct_marked_tree(*copy.deepcopy(args)) == expected

