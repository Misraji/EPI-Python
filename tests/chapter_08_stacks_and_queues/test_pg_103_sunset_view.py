"""Independent tests for EPI 8.5.

pytest parameterization: https://docs.pytest.org/en/stable/how-to/parametrize.html
"""

# pytest enables one test function to run over several examples.
# Documentation: https://docs.pytest.org/en/stable/
import pytest

# Standard library: copies mutable inputs so tests do not share state.
# Documentation: https://docs.python.org/3/library/copy.html
import copy

from epi_python.chapter_08_stacks_and_queues.pg_103_sunset_view import examine_buildings_with_sunset

@pytest.mark.parametrize(("args", "expected"), [
    (([3,7,8,3,6,1],), [2,4,5]),
    (([1,2,3],), [2]),
    (([3,2,1],), [0,1,2]),
    (([], ), []),
])
def test_examples(args, expected):
    """Verify representative and boundary conditions independently."""
    assert examine_buildings_with_sunset(*copy.deepcopy(args)) == expected

