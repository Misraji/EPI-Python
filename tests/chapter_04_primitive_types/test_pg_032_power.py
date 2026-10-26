"""Independent tests for EPI 4.7.

pytest parameterization: https://docs.pytest.org/en/stable/how-to/parametrize.html
"""

# pytest enables one test function to run over several examples.
# Documentation: https://docs.pytest.org/en/stable/
import pytest

# Standard library: copies mutable inputs so tests do not share state.
# Documentation: https://docs.python.org/3/library/copy.html
import copy

from epi_python.chapter_04_primitive_types.pg_032_power import power

@pytest.mark.parametrize(("args", "expected"), [
    ((2.0, 10), 1024.0),
    ((2.0, -2), 0.25),
    ((-2.0, 3), -8.0),
    ((8.0, 0), 1.0),
    ((0.0, 4), 0.0),
])
def test_examples(args, expected):
    """Verify representative and boundary conditions independently."""
    assert power(*copy.deepcopy(args)) == expected

