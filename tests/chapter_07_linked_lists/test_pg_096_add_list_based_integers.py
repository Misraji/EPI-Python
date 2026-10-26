"""Independent tests for EPI 7.13.

pytest parameterization: https://docs.pytest.org/en/stable/how-to/parametrize.html
"""

# pytest enables one test function to run over several examples.
# Documentation: https://docs.pytest.org/en/stable/
import pytest

# Standard library: copies mutable inputs so tests do not share state.
# Documentation: https://docs.python.org/3/library/copy.html
import copy

from epi_python.chapter_07_linked_lists.pg_096_add_list_based_integers import add_list_based_integers

@pytest.mark.parametrize(("args", "expected"), [
    (([3,1,4], [7,0,9]), [0,2,3,1]),
    (([9,9], [1]), [0,0,1]),
    (([0], [0]), [0]),
    (([], [1,2]), [1,2]),
])
def test_examples(args, expected):
    """Verify representative and boundary conditions independently."""
    assert add_list_based_integers(*copy.deepcopy(args)) == expected

def test_random_decimal_reference():
    for a in range(0, 1000, 37):
        for b in range(0, 1000, 71):
            def digits(n):
                return [int(x) for x in str(n)][::-1]
            assert add_list_based_integers(digits(a), digits(b)) == digits(a + b)
