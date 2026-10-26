"""Independent tests for EPI 12.7.

pytest parameterization: https://docs.pytest.org/en/stable/how-to/parametrize.html
"""

# pytest enables one test function to run over several examples.
# Documentation: https://docs.pytest.org/en/stable/
import pytest

# Standard library: copies mutable inputs so tests do not share state.
# Documentation: https://docs.python.org/3/library/copy.html
import copy

from epi_python.chapter_12_hash_tables.pg_171_smallest_subarray_sequential_cover import find_smallest_sequentially_covering_subset

@pytest.mark.parametrize(("args", "expected"), [
    ((["a","b","x","c","a","b","c"], ["a","b","c"]), (4,6)),
    ((["a","b","c"], ["b","a"]), None),
    (([], ["a"]), None),
    ((["a"], []), (0,-1)),
])
def test_examples(args, expected):
    """Verify representative and boundary conditions independently."""
    assert find_smallest_sequentially_covering_subset(*copy.deepcopy(args)) == expected

