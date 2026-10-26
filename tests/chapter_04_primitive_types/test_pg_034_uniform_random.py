"""Independent tests for EPI 4.10.

pytest parameterization: https://docs.pytest.org/en/stable/how-to/parametrize.html
"""

# pytest enables one test function to run over several examples.
# Documentation: https://docs.pytest.org/en/stable/
import pytest

# Standard library: copies mutable inputs so tests do not share state.
# Documentation: https://docs.python.org/3/library/copy.html
import copy

from epi_python.chapter_04_primitive_types.pg_034_uniform_random import uniform_random

@pytest.mark.parametrize(("args", "expected"), [
    ((4, 4), 4),
    ((0, 0), 0),
])
def test_examples(args, expected):
    """Verify representative and boundary conditions independently."""
    assert uniform_random(*copy.deepcopy(args)) == expected

def test_generated_values_remain_in_bounds():
    # Determinism makes random tests reproducible.
    import random
    r = random.Random(184)
    generated = [uniform_random(-4, 7, lambda: r.getrandbits(1)) for _ in range(200)]
    assert set(generated) == set(range(-4, 8))
