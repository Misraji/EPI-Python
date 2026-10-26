"""Independent tests for EPI 9.6.

pytest parameterization: https://docs.pytest.org/en/stable/how-to/parametrize.html
"""

# pytest enables one test function to run over several examples.
# Documentation: https://docs.pytest.org/en/stable/
import pytest

# Standard library: copies mutable inputs so tests do not share state.
# Documentation: https://docs.python.org/3/library/copy.html
import copy

from epi_python.chapter_09_binary_trees.pg_120_has_path_sum import has_path_sum_values

@pytest.mark.parametrize(("args", "expected"), [
    (((5,(2,None,None),(3,None,None)),7), True),
    (((5,(2,None,None),(3,None,None)),9), False),
    ((None,0), False),
    (((1,None,None),1), True),
])
def test_examples(args, expected):
    """Verify representative and boundary conditions independently."""
    assert has_path_sum_values(*copy.deepcopy(args)) == expected

