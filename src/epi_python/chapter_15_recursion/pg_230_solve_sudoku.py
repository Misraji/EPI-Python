"""EPI Python 15.9, textbook printed page 230: Implement a Sudoku solver.

QUESTION: Fill an incomplete Sudoku grid, preserving row, column, and subgrid constraints.

TEXTBOOK ALGORITHM: Backtracking fills entries in row-major order and checks only affected constraints; book uses math.sqrt and itertools.product.

The complete question, hints, solution development, and variants are in the
adjacent page-numbered reference Markdown, extracted from the supplied PDF.
This executable implementation restores syntax damaged by the PDF text layer;
minor type annotations, examples, and assertions are educational additions.

Run: python -m epi_python.chapter_15_recursion.pg_230_solve_sudoku
Test: python -m pytest tests/chapter_15_recursion/test_pg_230_solve_sudoku.py -v
"""

# itertools.product documentation: https://docs.python.org/3/library/itertools.html#itertools.product
import itertools

# math.isqrt documentation: https://docs.python.org/3/library/math.html#math.isqrt
import math


def solve_sudoku(partial_assignment: list[list[int]]) -> bool:
    """Modify grid in place; return whether a valid completion exists."""
    empty_entry = 0
    n = len(partial_assignment)
    region_size = math.isqrt(n)
    if not n or region_size * region_size != n or any(len(row) != n for row in partial_assignment):
        raise ValueError('Sudoku must be a nonempty square with square subregions')

    def valid_to_add(i: int, j: int, value: int) -> bool:
        if any(value == partial_assignment[k][j] for k in range(n)):
            return False
        if value in partial_assignment[i]:
            return False
        region_i, region_j = i // region_size, j // region_size

        # product(..., repeat=2) enumerates every (row, column) offset in the box.
        return not any(value == partial_assignment[region_size * region_i + a]
                           [region_size * region_j + b]
                       for a, b in itertools.product(range(region_size), repeat=2))

    def solve_partial_sudoku(i: int, j: int) -> bool:
        if i == n:
            i, j = 0, j + 1
            if j == n:
                return True
        if partial_assignment[i][j] != empty_entry:
            return solve_partial_sudoku(i + 1, j)
        for value in range(1, n + 1):
            if valid_to_add(i, j, value):
                partial_assignment[i][j] = value
                if solve_partial_sudoku(i + 1, j):
                    return True
                partial_assignment[i][j] = empty_entry
        return False

    return solve_partial_sudoku(0, 0)


if __name__ == '__main__':
    sample = [[1, 0, 0, 4], [0, 4, 1, 0], [0, 1, 4, 0], [4, 0, 0, 1]]
    assert solve_sudoku(sample)
    print('Solved 4x4 Sudoku:', sample)
