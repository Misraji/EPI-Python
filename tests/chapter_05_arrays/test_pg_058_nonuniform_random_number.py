"""Independent tests for EPI 5.16.

pytest parameterization: https://docs.pytest.org/en/stable/how-to/parametrize.html
"""

# pytest enables one test function to run over several examples.
# Documentation: https://docs.pytest.org/en/stable/
import pytest

# Standard library: copies mutable inputs so tests do not share state.
# Documentation: https://docs.python.org/3/library/copy.html
import copy

from epi_python.chapter_05_arrays.pg_058_nonuniform_random_number import nonuniform_random_number

@pytest.mark.parametrize(("args", "expected"), [
    (([7], [1.0]), 7),
    (([2, 3], [1.0, 0.0]), 2),
])
def test_examples(args, expected):
    """Verify representative and boundary conditions independently."""
    assert nonuniform_random_number(*copy.deepcopy(args)) == expected

def test_zero_weight_is_never_selected():
    import random
    rng = random.Random(99)
    assert all(nonuniform_random_number([1, 2, 3], [0, 1, 0], rng) == 2 for _ in range(100))
