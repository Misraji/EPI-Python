"""Independent tests for EPI 5.13.

pytest parameterization: https://docs.pytest.org/en/stable/how-to/parametrize.html
"""

# pytest enables one test function to run over several examples.
# Documentation: https://docs.pytest.org/en/stable/
import pytest

# Standard library: copies mutable inputs so tests do not share state.
# Documentation: https://docs.python.org/3/library/copy.html
import copy

from epi_python.chapter_05_arrays.pg_055_online_random_sampling import online_random_sample

@pytest.mark.parametrize(("args", "expected"), [
    ((iter([9, 8]), 0), []),
    ((iter([4, 5]), 2), [4, 5]),
])
def test_examples(args, expected):
    """Verify representative and boundary conditions independently."""
    assert online_random_sample(*copy.deepcopy(args)) == expected

def test_generator_stream():
    import random
    for seed in range(30):
        output = online_random_sample((x for x in range(100)), 9, random.Random(seed))
        assert len(output) == 9
        assert len(set(output)) == 9
        assert all(0 <= x < 100 for x in output)
