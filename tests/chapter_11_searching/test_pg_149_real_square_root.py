"""Independent tests for EPI 11.5.

pytest parameterization: https://docs.pytest.org/en/stable/how-to/parametrize.html
"""

# pytest enables one test function to run over several examples.
# Documentation: https://docs.pytest.org/en/stable/
import pytest

# Standard library: copies mutable inputs so tests do not share state.
# Documentation: https://docs.python.org/3/library/copy.html
import copy

from epi_python.chapter_11_searching.pg_149_real_square_root import square_root

@pytest.mark.parametrize(("args", "expected"), [
    ((0.0,), 0.0),
    ((1.0,), 1.0),
])
def test_examples(args, expected):
    """Verify representative and boundary conditions independently."""
    assert square_root(*copy.deepcopy(args)) == expected

def test_real_sqrt_matches_standard_library():
    import math
    for x in (0., 1e-6, 0.25, 2., 10., 123456.):
        assert math.isclose(square_root(x), math.sqrt(x), rel_tol=1e-8, abs_tol=1e-8)
