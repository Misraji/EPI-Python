"""Independent tests for EPI 11.10.

pytest parameterization: https://docs.pytest.org/en/stable/how-to/parametrize.html
"""

# pytest enables one test function to run over several examples.
# Documentation: https://docs.pytest.org/en/stable/
import pytest

# Standard library: copies mutable inputs so tests do not share state.
# Documentation: https://docs.python.org/3/library/copy.html
import copy

from epi_python.chapter_11_searching.pg_157_find_duplicate_missing import find_duplicate_missing

@pytest.mark.parametrize(("args", "expected"), [
    (([0, 1, 1, 3],), (1,2)),
    (([3,1,2,3],), (3,0)),
    (([0,0],), (0,1)),
])
def test_examples(args, expected):
    """Verify representative and boundary conditions independently."""
    assert find_duplicate_missing(*copy.deepcopy(args)) == expected

def test_against_simple_set_reference():
    for n in range(2, 25):
        for duplicate, missing in ((0,n-1),(n-1,0),(n//2,(n//2+1)%n)):
            if duplicate == missing:
                continue
            values = [duplicate if x == missing else x for x in range(n)]
            assert find_duplicate_missing(values) == (duplicate, missing)
