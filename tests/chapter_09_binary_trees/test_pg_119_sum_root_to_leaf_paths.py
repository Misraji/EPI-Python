"""Independent tests for EPI 9.5.

pytest parameterization: https://docs.pytest.org/en/stable/how-to/parametrize.html
"""

# pytest enables one test function to run over several examples.
# Documentation: https://docs.pytest.org/en/stable/
import pytest

# Standard library: copies mutable inputs so tests do not share state.
# Documentation: https://docs.python.org/3/library/copy.html
import copy

from epi_python.chapter_09_binary_trees.pg_119_sum_root_to_leaf_paths import sum_root_to_leaf_paths

@pytest.mark.parametrize(("args", "expected"), [
    (((1,(0,None,None),(1,None,None)),), 5),
    (((0,None,None),), 0),
    ((None,), 0),
    (((1,(1,(0,None,None),None),None),), 6),
])
def test_examples(args, expected):
    """Verify representative and boundary conditions independently."""
    assert sum_root_to_leaf_paths(*copy.deepcopy(args)) == expected

