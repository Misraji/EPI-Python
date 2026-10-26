"""Independent tests for EPI 10.4.

pytest parameterization: https://docs.pytest.org/en/stable/how-to/parametrize.html
"""

# pytest enables one test function to run over several examples.
# Documentation: https://docs.pytest.org/en/stable/
import pytest

# Standard library: copies mutable inputs so tests do not share state.
# Documentation: https://docs.python.org/3/library/copy.html
import copy

from epi_python.chapter_10_heaps.pg_137_k_closest_stars import find_closest_k_stars

@pytest.mark.parametrize(("args", "expected"), [
    (([(0.,0.,5.), (1.,1.,0.), (0.,0.,1.)], 2), [(0.,0.,1.),(1.,1.,0.)]),
    (([], 4), []),
    (([(1.,0.,0.)], 0), []),
])
def test_examples(args, expected):
    """Verify representative and boundary conditions independently."""
    assert find_closest_k_stars(*copy.deepcopy(args)) == expected

