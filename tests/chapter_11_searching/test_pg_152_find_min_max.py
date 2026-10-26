"""Independent tests for EPI 11.7.

pytest parameterization: https://docs.pytest.org/en/stable/how-to/parametrize.html
"""

# pytest enables one test function to run over several examples.
# Documentation: https://docs.pytest.org/en/stable/
import pytest

# Standard library: copies mutable inputs so tests do not share state.
# Documentation: https://docs.python.org/3/library/copy.html
import copy

from epi_python.chapter_11_searching.pg_152_find_min_max import find_min_max

@pytest.mark.parametrize(("args", "expected"), [
    (([4,1,3,2],), (1,4)),
    (([7],), (7,7)),
    (([-3,-1,-7],), (-7,-1)),
])
def test_examples(args, expected):
    """Verify representative and boundary conditions independently."""
    assert find_min_max(*copy.deepcopy(args)) == expected

