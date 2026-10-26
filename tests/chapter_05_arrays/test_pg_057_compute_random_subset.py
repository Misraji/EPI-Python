"""Independent tests for EPI 5.15.

pytest parameterization: https://docs.pytest.org/en/stable/how-to/parametrize.html
"""

# pytest enables one test function to run over several examples.
# Documentation: https://docs.pytest.org/en/stable/
import pytest

# Standard library: copies mutable inputs so tests do not share state.
# Documentation: https://docs.python.org/3/library/copy.html
import copy

from epi_python.chapter_05_arrays.pg_057_compute_random_subset import random_subset

@pytest.mark.parametrize(("args", "expected"), [
    ((0, 0), []),
    ((1, 1), [0]),
])
def test_examples(args, expected):
    """Verify representative and boundary conditions independently."""
    assert random_subset(*copy.deepcopy(args)) == expected

def test_sparse_permutation_invariants():
    import random
    for n in range(1, 35):
        for k in (0, 1, n // 2, n):
            result = random_subset(n, k, random.Random(n + k))
            assert len(result) == k
            assert len(set(result)) == k
            assert set(result) <= set(range(n))
