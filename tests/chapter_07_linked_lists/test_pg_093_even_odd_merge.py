"""Independent tests for EPI 7.10.

pytest parameterization: https://docs.pytest.org/en/stable/how-to/parametrize.html
"""

# pytest enables one test function to run over several examples.
# Documentation: https://docs.pytest.org/en/stable/
import pytest

# Standard library: copies mutable inputs so tests do not share state.
# Documentation: https://docs.python.org/3/library/copy.html
import copy

from epi_python.chapter_07_linked_lists.pg_093_even_odd_merge import even_odd_merge_values

@pytest.mark.parametrize(("args", "expected"), [
    (([0, 1, 2, 3, 4],), [0,2,4,1,3]),
    (([1,2,3,4],), [1,3,2,4]),
    (([], ), []),
    (([9],), [9]),
])
def test_examples(args, expected):
    """Verify representative and boundary conditions independently."""
    assert even_odd_merge_values(*copy.deepcopy(args)) == expected

