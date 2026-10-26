"""EPI 15.2: Generate all nonattacking placements of n-Queens (printed page 221).

Problem: Generate all nonattacking placements of n-Queens. The problem, examples, discussion, and variants
appear in the PDF and its corresponding page-numbered reference Markdown.

Approach: Backtracking with row, column, and diagonal conflict checks from the book.

Python study exercise based on the textbook algorithm. Some type hints,
data structures, and demonstrations have been adapted for direct execution.
"""

# TEXTBOOK PROBLEM (exercise 15.2, printed page 221):
# Enumerate all nonattacking placements of n queens on an n-by-n chessboard.
# HINT: Place one queen per row and reject column or diagonal conflicts.

def n_queens(n: int) -> list[list[int]]:
    """Return all nonattacking column assignments, one per row."""
    result=[]
    placement=[0]*n

    def solve(row: int) -> None:
        if row==n:
            result.append(list(placement))
            return
        for col in range(n):
            if all(abs(prior_col-col) not in (0,row-prior_row)
                   for prior_row,prior_col in enumerate(placement[:row])):
                placement[row]=col
                solve(row+1)

    solve(0)
    return result


if __name__ == '__main__':
    placements=n_queens(4)
    print('4-queens placements:',placements)
    assert sorted(placements)==[[1,3,0,2],[2,0,3,1]]
