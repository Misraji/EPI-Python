"""EPI Python 18.2, textbook printed page 278: Paint a Boolean matrix.

QUESTION: Flip every cell in the four-neighbor connected region containing the given cell.

TEXTBOOK ALGORITHM: The PDF prints both a collections.deque BFS and a recursive DFS. Keep both versions.

The complete question, hints, solution development, and variants are in the
adjacent page-numbered reference Markdown, extracted from the supplied PDF.
This executable implementation restores syntax damaged by the PDF text layer;
minor type annotations, examples, and assertions are educational additions.

Run: python -m epi_python.chapter_18_graphs.pg_278_flip_color
Test: python -m pytest tests/chapter_18_graphs/test_pg_278_flip_color.py -v
"""

# collections.deque documentation: https://docs.python.org/3/library/collections.html#collections.deque
from collections import deque


def flip_color(x: int,y: int,a: list[list[int]]) -> None:
    """Iterative breadth-first implementation in the textbook."""
    color=a[x][y]
    queue=deque([(x,y)])
    a[x][y]=1-a[x][y]
    while queue:

        # popleft() removes the oldest element efficiently (FIFO traversal).
        i,j=queue.popleft()
        for dx,dy in ((0,1),(0,-1),(1,0),(-1,0)):
            nx,ny=i+dx,j+dy
            if 0<=nx<len(a) and 0<=ny<len(a[nx]) and a[nx][ny]==color:
                a[nx][ny]=1-a[nx][ny]
                queue.append((nx,ny))


def flip_color_recursive(x: int,y: int,a: list[list[int]]) -> None:
    """Recursive DFS version also printed in EPI."""
    color=a[x][y]
    a[x][y]=1-a[x][y]
    for dx,dy in ((0,1),(0,-1),(1,0),(-1,0)):
        nx,ny=x+dx,y+dy
        if 0<=nx<len(a) and 0<=ny<len(a[nx]) and a[nx][ny]==color:
            flip_color_recursive(nx,ny,a)


if __name__ == '__main__':
    board=[[1,1,0],[1,0,0]]
    flip_color(0,0,board)
    print('Flipped region:',board)
    assert board==[[0,0,0],[0,0,0]]
