"""Independent tests for EPI 5.19.

pytest parameterization: https://docs.pytest.org/en/stable/how-to/parametrize.html
"""

# pytest enables one test function to run over several examples.
# Documentation: https://docs.pytest.org/en/stable/
import pytest

# Standard library: copies mutable inputs so tests do not share state.
# Documentation: https://docs.python.org/3/library/copy.html
import copy

from epi_python.chapter_05_arrays.pg_064_rotate_matrix import rotate_matrix

@pytest.mark.parametrize(("args", "expected"), [
    (([[1,2], [3,4]],), [[3,1],[4,2]]),
    (([[7]],), [[7]]),
    (([], ), []),
])
def test_examples(args, expected):
    """Verify representative and boundary conditions independently."""
    assert rotate_matrix(*copy.deepcopy(args)) == expected

def test_four_rotations_restore_matrix():
    matrix = [[r * 3 + c for c in range(3)] for r in range(3)]
    original = copy.deepcopy(matrix)
    for _ in range(4):
        rotate_matrix(matrix)
    assert matrix == original
