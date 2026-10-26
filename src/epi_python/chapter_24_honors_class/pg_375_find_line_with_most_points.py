"""EPI Python 24.19, textbook printed page 375: Find the line through the most points.

QUESTION: Compute the maximum number of points lying on a common straight line.

TEXTBOOK ALGORITHM: For each anchor group slopes by reduced integer differences and account for overlapping points.

The complete question, hints, solution development, and variants are in the
adjacent page-numbered reference Markdown, extracted from the supplied PDF.
This executable implementation restores syntax damaged by the PDF text layer;
minor type annotations, examples, and assertions are educational additions.

Run: python -m epi_python.chapter_24_honors_class.pg_375_find_line_with_most_points
Test: python -m pytest tests/chapter_24_honors_class/test_pg_375_find_line_with_most_points.py -v
"""

# collections.defaultdict docs: https://docs.python.org/3/library/collections.html#collections.defaultdict
from collections import defaultdict

# math.gcd docs: https://docs.python.org/3/library/math.html#math.gcd
from math import gcd

# collections.namedtuple docs: https://docs.python.org/3/library/collections.html#collections.namedtuple
from collections import namedtuple


Point=namedtuple('Point',('x','y'))


def find_line_with_most_points(points: list[Point]) -> int:
    result=0
    for i,p1 in enumerate(points):
        slope_table=defaultdict(int)
        overlap_points=1
        for p2 in points[i+1:]:
            if p1==p2:
                overlap_points+=1
            else:
                x_diff,y_diff=p1.x-p2.x,p1.y-p2.y
                divisor=gcd(x_diff,y_diff)
                x_diff//=divisor
                y_diff//=divisor
                if x_diff<0 or (x_diff==0 and y_diff<0):
                    x_diff,y_diff=-x_diff,-y_diff
                slope_table[(x_diff,y_diff)]+=1
        result=max(result,overlap_points+max(slope_table.values(),default=0))
    return result


if __name__=='__main__':
    points=[Point(0,0),Point(1,1),Point(2,2),Point(0,1)]
    print('Most collinear points:',find_line_with_most_points(points))
    assert find_line_with_most_points(points)==3
