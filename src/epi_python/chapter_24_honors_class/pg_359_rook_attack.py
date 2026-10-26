"""EPI Python 24.7, textbook printed page 359: Identify positions attacked by rooks.

QUESTION: If any matrix entry is zero, set its entire row and column to zero in place.

TEXTBOOK ALGORITHM: Use the first row and first column for O(1)-space row/column markers.

The complete question, hints, solution development, and variants are in the
adjacent page-numbered reference Markdown, extracted from the supplied PDF.
This executable implementation restores syntax damaged by the PDF text layer;
minor type annotations, examples, and assertions are educational additions.

Run: python -m epi_python.chapter_24_honors_class.pg_359_rook_attack
Test: python -m pytest tests/chapter_24_honors_class/test_pg_359_rook_attack.py -v
"""

def rook_attack(a: list[list[int]]) -> None:
    if not a or not a[0]:
        return
    m,n=len(a),len(a[0])
    first_row_zero=any(not a[0][j] for j in range(n))
    first_column_zero=any(not a[i][0] for i in range(m))
    for i in range(1,m):
        for j in range(1,n):
            if not a[i][j]:
                a[i][0]=a[0][j]=0
    for i in range(1,m):
        if not a[i][0]:
            for j in range(1,n):a[i][j]=0
    for j in range(1,n):
        if not a[0][j]:
            for i in range(1,m):a[i][j]=0
    if first_row_zero:
        for j in range(n):a[0][j]=0
    if first_column_zero:
        for i in range(m):a[i][0]=0


if __name__=='__main__':
    board=[[1,1,1],[1,0,1],[1,1,1]]
    rook_attack(board)
    print('Rook attacked cells:',board)
    assert board==[[1,0,1],[0,0,0],[1,0,1]]
