"""EPI Python 16.5, textbook printed page 245: Search for a sequence in a 2D array.

QUESTION: Determine whether a number sequence can be traced through orthogonally adjacent matrix cells.

TEXTBOOK ALGORITHM: Memoize failed (row, column, offset) attempts; the textbook allows revisiting cells.

The complete question, hints, solution development, and variants are in the
adjacent page-numbered reference Markdown, extracted from the supplied PDF.
This executable implementation restores syntax damaged by the PDF text layer;
minor type annotations, examples, and assertions are educational additions.

Run: python -m epi_python.chapter_16_dynamic_programming.pg_245_is_pattern_contained_in_grid
Test: python -m pytest tests/chapter_16_dynamic_programming/test_pg_245_is_pattern_contained_in_grid.py -v
"""

def is_pattern_contained_in_grid(grid: list[list[int]], s: list[int]) -> bool:
    previous_attempts: set[tuple[int,int,int]] = set()

    def is_pattern_suffix_contained_starting_at_xy(x: int, y: int, offset: int) -> bool:
        if len(s) == offset:
            return True
        if (0 <= x < len(grid) and 0 <= y < len(grid[x])
            and grid[x][y] == s[offset]
            and (x,y,offset) not in previous_attempts
            and any(is_pattern_suffix_contained_starting_at_xy(x+a,y+b,offset+1)
                    for a,b in ((-1,0),(1,0),(0,-1),(0,1)))):
            return True
        previous_attempts.add((x,y,offset))
        return False

    return any(is_pattern_suffix_contained_starting_at_xy(i,j,0)
               for i in range(len(grid)) for j in range(len(grid[i]))) or not s


if __name__ == '__main__':
    grid=[[1,2,3],[4,5,6],[7,8,9]]
    print('Pattern found:',is_pattern_contained_in_grid(grid,[1,2,5,8]))
    assert is_pattern_contained_in_grid(grid,[1,2,5,8])
