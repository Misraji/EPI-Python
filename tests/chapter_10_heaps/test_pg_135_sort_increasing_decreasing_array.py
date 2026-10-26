"""Independent tests for EPI 10.2.

pytest parameterization: https://docs.pytest.org/en/stable/how-to/parametrize.html
"""

# pytest enables one test function to run over several examples.
# Documentation: https://docs.pytest.org/en/stable/
import pytest

# Standard library: copies mutable inputs so tests do not share state.
# Documentation: https://docs.python.org/3/library/copy.html
import copy

from epi_python.chapter_10_heaps.pg_135_sort_increasing_decreasing_array import sort_k_increasing_decreasing_array

@pytest.mark.parametrize(("args", "expected"), [
    (([1,3,5,4,2,6,9],), [1,2,3,4,5,6,9]),
    (([], ), []),
    (([4,3,2,1],), [1,2,3,4]),
    (([2,2,2],), [2,2,2]),
])
def test_examples(args, expected):
    """Verify representative and boundary conditions independently."""
    assert sort_k_increasing_decreasing_array(*copy.deepcopy(args)) == expected

def test_matches_sort_for_random_walks():
    import random
    rng = random.Random(7)
    for n in range(1, 70):
        walk = [0]
        for _ in range(n - 1):
            walk.append(walk[-1] + rng.randrange(-3, 4))
        assert sort_k_increasing_decreasing_array(walk) == sorted(walk)
