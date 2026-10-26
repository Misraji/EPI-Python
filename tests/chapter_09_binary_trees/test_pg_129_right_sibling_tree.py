"""Independent tests for EPI 9.16.

pytest parameterization: https://docs.pytest.org/en/stable/how-to/parametrize.html
"""

# pytest enables one test function to run over several examples.
# Documentation: https://docs.pytest.org/en/stable/
import pytest

# Standard library: copies mutable inputs so tests do not share state.
# Documentation: https://docs.python.org/3/library/copy.html
import copy

from epi_python.chapter_09_binary_trees.pg_129_right_sibling_tree import sibling_pairs

@pytest.mark.parametrize(("args", "expected"), [
    ((None,), []),
    (((1,None,None),), [(1,None)]),
    (((1,(2,None,None),(3,None,None)),), [(1,None),(2,3),(3,None)]),
])
def test_examples(args, expected):
    """Verify representative and boundary conditions independently."""
    assert sibling_pairs(*copy.deepcopy(args)) == expected

