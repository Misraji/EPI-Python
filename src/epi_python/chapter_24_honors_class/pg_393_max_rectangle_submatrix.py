"""EPI Python 24.30, textbook printed page 393: Find the maximum 2D subarray.

QUESTION: Find maximum all-ones rectangle and maximum all-ones square areas in a Boolean matrix.

TEXTBOOK ALGORITHM: Book stores vertical/horizontal runs for rectangle and bottom-right square recurrence for square.

The complete question, hints, solution development, and variants are in the
adjacent page-numbered reference Markdown, extracted from the supplied PDF.
This executable implementation restores syntax damaged by the PDF text layer;
minor type annotations, examples, and assertions are educational additions.

Run: python -m epi_python.chapter_24_honors_class.pg_393_max_rectangle_submatrix
Test: python -m pytest tests/chapter_24_honors_class/test_pg_393_max_rectangle_submatrix.py -v
"""

def max_rectangle_submatrix(a: list[list[int]]) -> int:
    if not a:return 0
    rows,cols=len(a),len(a[0])
    vertical=[[0]*cols for _ in a]
    horizontal=[[0]*cols for _ in a]
    for i in reversed(range(rows)):
        for j in reversed(range(cols)):
            if a[i][j]:
                vertical[i][j]=1+(vertical[i+1][j] if i+1<rows else 0)
                horizontal[i][j]=1+(horizontal[i][j+1] if j+1<cols else 0)
    maximum=0
    for i in range(rows):
        for j in range(cols):
            min_width=cols
            for height in range(1,vertical[i][j]+1):
                min_width=min(min_width,horizontal[i+height-1][j])
                maximum=max(maximum,height*min_width)
    return maximum


def max_square_submatrix(a: list[list[int]]) -> int:
    if not a:return 0
    rows,cols=len(a),len(a[0])
    table=[[0]*cols for _ in a]
    largest=0
    for i in reversed(range(rows)):
        for j in reversed(range(cols)):
            if a[i][j]:
                table[i][j]=1+min(table[i+1][j] if i+1<rows else 0,
                                  table[i][j+1] if j+1<cols else 0,
                                  table[i+1][j+1] if i+1<rows and j+1<cols else 0)
                largest=max(largest,table[i][j]**2)
    return largest


if __name__=='__main__':
    g=[[1,1,0],[1,1,1],[1,1,1]]
    print('Largest rectangle/square:',max_rectangle_submatrix(g),max_square_submatrix(g))
    assert max_rectangle_submatrix(g)==6 and max_square_submatrix(g)==4
