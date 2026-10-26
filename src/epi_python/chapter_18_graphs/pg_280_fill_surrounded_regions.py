"""EPI Python 18.3, textbook printed page 280: Compute enclosed regions.

QUESTION: Convert white cells without a white path to the board boundary into black cells.

TEXTBOOK ALGORITHM: Multi-source BFS from all boundary white cells marks them temporary, then recolors all other whites.

The complete question, hints, solution development, and variants are in the
adjacent page-numbered reference Markdown, extracted from the supplied PDF.
This executable implementation restores syntax damaged by the PDF text layer;
minor type annotations, examples, and assertions are educational additions.

Run: python -m epi_python.chapter_18_graphs.pg_280_fill_surrounded_regions
Test: python -m pytest tests/chapter_18_graphs/test_pg_280_fill_surrounded_regions.py -v
"""

# collections.deque documentation: https://docs.python.org/3/library/collections.html#collections.deque
from collections import deque


def fill_surrounded_regions(board: list[list[str]]) -> None:
    if not board or not board[0]:
        return
    n,m=len(board),len(board[0])

    # deque efficiently supports FIFO traversal in breadth-first search.
    q=deque([(i,j) for i in range(n) for j in (0,m-1)]
            + [(i,j) for j in range(m) for i in (0,n-1)])
    while q:
        x,y=q.popleft()
        if 0<=x<n and 0<=y<m and board[x][y]=='W':
            board[x][y]='T'  # Temporary mark for boundary-connected whites.
            q.extend([(x-1,y),(x+1,y),(x,y-1),(x,y+1)])
    board[:]=[['B' if c != 'T' else 'W' for c in row] for row in board]


if __name__ == '__main__':
    board=[list('BBBB'),list('BWWB'),list('BBWB'),list('BWBB')]
    fill_surrounded_regions(board)
    print('Enclosed whites filled:',board)
    assert board==[list('BBBB'),list('BBBB'),list('BBBB'),list('BWBB')]
