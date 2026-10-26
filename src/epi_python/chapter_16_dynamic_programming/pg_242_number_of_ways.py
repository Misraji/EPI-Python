"""EPI Python 16.3, textbook printed page 242: Count the number of ways to traverse a 2D array.

QUESTION: Count right/down lattice paths from the top-left to the bottom-right of an n-by-m rectangle.

TEXTBOOK ALGORITHM: Use top-down dynamic programming over predecessor positions, as printed in the book.

The complete question, hints, solution development, and variants are in the
adjacent page-numbered reference Markdown, extracted from the supplied PDF.
This executable implementation restores syntax damaged by the PDF text layer;
minor type annotations, examples, and assertions are educational additions.

Run: python -m epi_python.chapter_16_dynamic_programming.pg_242_number_of_ways
Test: python -m pytest tests/chapter_16_dynamic_programming/test_pg_242_number_of_ways.py -v
"""

def number_of_ways(n: int, m: int) -> int:
    if n <= 0 or m <= 0:
        return 0
    ways = [[0] * m for _ in range(n)]

    def compute_number_of_ways_to_xy(x: int, y: int) -> int:
        if x == 0 and y == 0:
            return 1
        if ways[x][y] == 0:
            ways_top = compute_number_of_ways_to_xy(x - 1, y) if x > 0 else 0
            ways_left = compute_number_of_ways_to_xy(x, y - 1) if y > 0 else 0
            ways[x][y] = ways_top + ways_left
        return ways[x][y]

    return compute_number_of_ways_to_xy(n - 1, m - 1)


if __name__ == '__main__':
    print('3x4 grid paths:', number_of_ways(3,4))
    assert number_of_ways(3,4) == 10
