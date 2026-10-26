"""Independent tests for EPI 6.2.

pytest parameterization: https://docs.pytest.org/en/stable/how-to/parametrize.html
"""

# pytest enables one test function to run over several examples.
# Documentation: https://docs.pytest.org/en/stable/
import pytest

# Standard library: copies mutable inputs so tests do not share state.
# Documentation: https://docs.python.org/3/library/copy.html
import copy

from epi_python.chapter_06_strings.pg_069_convert_base import convert_base

@pytest.mark.parametrize(("args", "expected"), [
    (("615", 7, 13), "1A7"),
    (("0", 2, 16), "0"),
    (("FF", 16, 10), "255"),
    (("-101", 2, 10), "-5"),
    (("10", 10, 2), "1010"),
])
def test_examples(args, expected):
    """Verify representative and boundary conditions independently."""
    assert convert_base(*copy.deepcopy(args)) == expected

