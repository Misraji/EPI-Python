"""Independent tests for EPI 11.8.

pytest parameterization: https://docs.pytest.org/en/stable/how-to/parametrize.html
"""

# pytest enables one test function to run over several examples.
# Documentation: https://docs.pytest.org/en/stable/
import pytest

# Standard library: copies mutable inputs so tests do not share state.
# Documentation: https://docs.python.org/3/library/copy.html
import copy

from epi_python.chapter_11_searching.pg_153_kth_largest_element import find_kth_largest

@pytest.mark.parametrize(("args", "expected"), [
    ((1, [3,1,5,2,4]), 5),
    ((5, [3,1,5,2,4]), 1),
    ((3, [3,1,5,2,4]), 3),
    ((2, [5,5,3]), 5),
])
def test_examples(args, expected):
    """Verify representative and boundary conditions independently."""
    assert find_kth_largest(*copy.deepcopy(args)) == expected

def test_quickselect_against_sorted_reference():
    import random
    rng = random.Random(37)
    for n in range(1, 50):
        values = [rng.randrange(-30, 31) for _ in range(n)]
        expected = sorted(values, reverse=True)
        for k in (1, (n + 1) // 2, n):
            assert find_kth_largest(k, values) == expected[k - 1]
