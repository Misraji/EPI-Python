"""Independent tests for EPI 7.12.

pytest parameterization: https://docs.pytest.org/en/stable/how-to/parametrize.html
"""

# pytest enables one test function to run over several examples.
# Documentation: https://docs.pytest.org/en/stable/
import pytest

# Standard library: copies mutable inputs so tests do not share state.
# Documentation: https://docs.python.org/3/library/copy.html
import copy

from epi_python.chapter_07_linked_lists.pg_095_list_pivot import list_pivot_values

@pytest.mark.parametrize(("args", "expected"), [
    (([3,2,2,5,1,2], 2), [1,2,2,2,3,5]),
    (([4,5], 3), [4,5]),
    (([2,1,0], 3), [2,1,0]),
    (([], 2), []),
])
def test_examples(args, expected):
    """Verify representative and boundary conditions independently."""
    assert list_pivot_values(*copy.deepcopy(args)) == expected

def test_pivot_is_stable():
    for values, pivot in [([3,1,4,1,5,9,2,6], 4), ([1,1,1], 1), ([], 3)]:
        expected = [x for x in values if x < pivot] + [x for x in values if x == pivot] + [x for x in values if x > pivot]
        assert list_pivot_values(values, pivot) == expected
