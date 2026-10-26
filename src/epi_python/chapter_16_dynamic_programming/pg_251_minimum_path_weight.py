"""EPI Python 16.8, textbook printed page 251: Find the minimum weight path in a triangle.

QUESTION: Find the smallest sum from the apex to a base entry of a triangle, stepping to adjacent entries.

TEXTBOOK ALGORITHM: The book scans triangle rows, retaining only minimum path weights for the immediately preceding row.

The complete question, hints, solution development, and variants are in the
adjacent page-numbered reference Markdown, extracted from the supplied PDF.
This executable implementation restores syntax damaged by the PDF text layer;
minor type annotations, examples, and assertions are educational additions.

Run: python -m epi_python.chapter_16_dynamic_programming.pg_251_minimum_path_weight
Test: python -m pytest tests/chapter_16_dynamic_programming/test_pg_251_minimum_path_weight.py -v
"""

def minimum_path_weight(triangle: list[list[int]]) -> int:
    if not triangle:
        return 0
    min_weight_to_curr_row = [0]
    for row in triangle:
        min_weight_to_curr_row = [
            row[j] + min(min_weight_to_curr_row[max(j-1,0)],
                         min_weight_to_curr_row[min(j,len(min_weight_to_curr_row)-1)])
            for j in range(len(row))
        ]
    return min(min_weight_to_curr_row)


if __name__ == '__main__':
    triangle = [[2],[4,4],[8,5,6],[4,2,6,2],[1,5,2,3,4]]
    print('Minimum triangle path:',minimum_path_weight(triangle))
    assert minimum_path_weight([[2],[3,4],[6,5,7],[4,1,8,3]])==11
