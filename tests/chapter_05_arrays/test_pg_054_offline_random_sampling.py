"""Independent tests for EPI 5.12.

pytest parameterization: https://docs.pytest.org/en/stable/how-to/parametrize.html
"""

# pytest enables one test function to run over several examples.
# Documentation: https://docs.pytest.org/en/stable/
import pytest

# Standard library: copies mutable inputs so tests do not share state.
# Documentation: https://docs.python.org/3/library/copy.html
import copy

from epi_python.chapter_05_arrays.pg_054_offline_random_sampling import random_sampling

@pytest.mark.parametrize(("args", "expected"), [
    ((0, [1, 2]), []),
    ((2, [5, 5]), [5, 5]),
])
def test_examples(args, expected):
    """Verify representative and boundary conditions independently."""
    assert random_sampling(*copy.deepcopy(args)) == expected

def test_sampling_always_selects_valid_members():
    import random
    for seed in range(40):
        values = list(range(20))
        chosen = random_sampling(8, values, random.Random(seed))
        assert len(chosen) == 8
        assert len(set(chosen)) == 8
        assert set(chosen) <= set(range(20))
