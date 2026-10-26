# pytest documentation: https://docs.pytest.org/en/stable/
import pytest

from epi_python.chapter_15_recursion.pg_230_solve_sudoku import solve_sudoku


def test_four_by_four():
    grid=[[1,0,0,4],[0,4,1,0],[0,1,4,0],[4,0,0,1]]
    assert solve_sudoku(grid)
    for row in grid:
        assert sorted(row)==[1,2,3,4]
    for c in range(4):
        assert sorted(row[c] for row in grid)==[1,2,3,4]


def test_impossible():
    grid=[[1,1,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    # The original algorithm assumes the partial board is valid, so use an
    # impossible but initially valid board rather than duplicate givens.
    grid=[[1,2,3,0],[0,0,0,4],[0,0,0,0],[0,0,0,0]]
    assert solve_sudoku(grid) is False


def test_bad_shape():
    with pytest.raises(ValueError):
        solve_sudoku([[1,2],[3,4]])
