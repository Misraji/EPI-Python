"""Independent tests for EPI 12.11.

pytest parameterization: https://docs.pytest.org/en/stable/how-to/parametrize.html
"""

# pytest enables one test function to run over several examples.
# Documentation: https://docs.pytest.org/en/stable/
import pytest

# Standard library: copies mutable inputs so tests do not share state.
# Documentation: https://docs.python.org/3/library/copy.html
import copy

from epi_python.chapter_12_hash_tables.pg_176_collatz_conjecture import collatz_holds_to

@pytest.mark.parametrize(("args", "expected"), [
    ((1,), True),
    ((10,), True),
    ((100,), True),
    ((1000,), True),
])
def test_examples(args, expected):
    """Verify representative and boundary conditions independently."""
    assert collatz_holds_to(*copy.deepcopy(args)) == expected

