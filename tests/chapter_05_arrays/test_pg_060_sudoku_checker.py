"""Independent tests for EPI 5.17.

pytest parameterization: https://docs.pytest.org/en/stable/how-to/parametrize.html
"""

# pytest enables one test function to run over several examples.
# Documentation: https://docs.pytest.org/en/stable/
import pytest

# Standard library: copies mutable inputs so tests do not share state.
# Documentation: https://docs.python.org/3/library/copy.html
import copy

from epi_python.chapter_05_arrays.pg_060_sudoku_checker import is_valid_sudoku

@pytest.mark.parametrize(("args", "expected"), [
    (([[0, 0, 0, 0] for _ in range(4)],), True),
    (([[1, 1, 0, 0]] + [[0]*4 for _ in range(3)],), False),
    (([[1, 0, 0, 0], [0, 2, 0, 0], [0, 0, 3, 0], [0, 0, 0, 4]],), True),
    (([[2, 0, 0, 0], [0, 2, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]],), False),
])
def test_examples(args, expected):
    """Verify representative and boundary conditions independently."""
    assert is_valid_sudoku(*copy.deepcopy(args)) == expected

from epi_python.chapter_05_arrays.pg_060_sudoku_checker import is_valid_sudoku_pythonic


def test_both_solutions_agree_on_constructed_cases():
    for n in (1, 4, 9):
        grid = [[0] * n for _ in range(n)]
        assert is_valid_sudoku(grid) == is_valid_sudoku_pythonic(grid) == True
        grid[0][0] = 1
        assert is_valid_sudoku(grid) == is_valid_sudoku_pythonic(grid) == True
