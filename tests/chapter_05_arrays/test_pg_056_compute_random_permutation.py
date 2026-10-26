"""Independent tests for EPI 5.14.

pytest parameterization: https://docs.pytest.org/en/stable/how-to/parametrize.html
"""

# pytest enables one test function to run over several examples.
# Documentation: https://docs.pytest.org/en/stable/
import pytest

# Standard library: copies mutable inputs so tests do not share state.
# Documentation: https://docs.python.org/3/library/copy.html
import copy

from epi_python.chapter_05_arrays.pg_056_compute_random_permutation import compute_random_permutation

@pytest.mark.parametrize(("args", "expected"), [
    ((0,), []),
    ((1,), [0]),
])
def test_examples(args, expected):
    """Verify representative and boundary conditions independently."""
    assert compute_random_permutation(*copy.deepcopy(args)) == expected

def test_permutation_property():
    import random
    for size in range(20):
        for seed in range(5):
            result = compute_random_permutation(size, random.Random(seed))
            assert sorted(result) == list(range(size))
