"""Independent tests for EPI 11.9.

pytest parameterization: https://docs.pytest.org/en/stable/how-to/parametrize.html
"""

# pytest enables one test function to run over several examples.
# Documentation: https://docs.pytest.org/en/stable/
import pytest

# Standard library: copies mutable inputs so tests do not share state.
# Documentation: https://docs.python.org/3/library/copy.html
import copy

from epi_python.chapter_11_searching.pg_155_find_missing_ip import find_missing_ip

@pytest.mark.parametrize(("args", "expected"), [
    (([i for i in range(16) if i != 7], 4, 2), 7),
    (([i for i in range(32) if i != 10], 5, 2), 10),
    (([], 4, 2), 0),
])
def test_examples(args, expected):
    """Verify representative and boundary conditions independently."""
    assert find_missing_ip(*copy.deepcopy(args)) == expected

def test_two_pass_factory_can_reopen():
    def data():
        return (i for i in range(64) if i != 19)
    assert find_missing_ip(data, 6, 3) == 19
