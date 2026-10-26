"""Independent tests for EPI 5.10.

pytest parameterization: https://docs.pytest.org/en/stable/how-to/parametrize.html
"""

# pytest enables one test function to run over several examples.
# Documentation: https://docs.pytest.org/en/stable/
import pytest

# Standard library: copies mutable inputs so tests do not share state.
# Documentation: https://docs.python.org/3/library/copy.html
import copy

from epi_python.chapter_05_arrays.pg_050_apply_permutation import apply_permutation

@pytest.mark.parametrize(("args", "expected"), [
    (([2, 0, 1], ["a", "b", "c"]), ["b", "c", "a"]),
    (([0, 1], [7, 8]), [7, 8]),
    (([], []), []),
])
def test_examples(args, expected):
    """Verify representative and boundary conditions independently."""
    assert apply_permutation(*copy.deepcopy(args)) == expected

