"""Independent tests for EPI 6.11.

pytest parameterization: https://docs.pytest.org/en/stable/how-to/parametrize.html
"""

# pytest enables one test function to run over several examples.
# Documentation: https://docs.pytest.org/en/stable/
import pytest

# Standard library: copies mutable inputs so tests do not share state.
# Documentation: https://docs.python.org/3/library/copy.html
import copy

from epi_python.chapter_06_strings.pg_078_snake_string import snake_string

@pytest.mark.parametrize(("args", "expected"), [
    (("Hello World!",), "e lHloWrdlo!"),
    (("",), ""),
    (("ABCD",), "BACD"),
])
def test_examples(args, expected):
    """Verify representative and boundary conditions independently."""
    assert snake_string(*copy.deepcopy(args)) == expected

