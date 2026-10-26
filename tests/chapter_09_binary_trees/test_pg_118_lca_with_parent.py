"""Independent tests for EPI 9.4.

pytest parameterization: https://docs.pytest.org/en/stable/how-to/parametrize.html
"""

# pytest enables one test function to run over several examples.
# Documentation: https://docs.pytest.org/en/stable/
import pytest

# Standard library: copies mutable inputs so tests do not share state.
# Documentation: https://docs.python.org/3/library/copy.html
import copy

from epi_python.chapter_09_binary_trees.pg_118_lca_with_parent import lca_parent_value

@pytest.mark.parametrize(("args", "expected"), [
    (((4,(2,(1,None,None),(3,None,None)),(6,None,None)),1,3), 2),
    (((4,(2,None,None),(6,None,None)),2,6), 4),
    (((5,None,None),5,5), 5),
])
def test_examples(args, expected):
    """Verify representative and boundary conditions independently."""
    assert lca_parent_value(*copy.deepcopy(args)) == expected

