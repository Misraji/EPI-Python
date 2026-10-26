"""Independent tests for EPI 9.3.

pytest parameterization: https://docs.pytest.org/en/stable/how-to/parametrize.html
"""

# pytest enables one test function to run over several examples.
# Documentation: https://docs.pytest.org/en/stable/
import pytest

# Standard library: copies mutable inputs so tests do not share state.
# Documentation: https://docs.python.org/3/library/copy.html
import copy

from epi_python.chapter_09_binary_trees.pg_117_lowest_common_ancestor import lca_value

@pytest.mark.parametrize(("args", "expected"), [
    (((4,(2,(1,None,None),(3,None,None)),(6,None,None)),1,3), 2),
    (((4,(2,None,None),(6,None,None)),2,6), 4),
    (((4,(2,None,None),(6,None,None)),2,100), None),
])
def test_examples(args, expected):
    """Verify representative and boundary conditions independently."""
    assert lca_value(*copy.deepcopy(args)) == expected

