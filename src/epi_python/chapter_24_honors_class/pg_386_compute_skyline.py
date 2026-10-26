"""EPI Python 24.26, textbook printed page 386: Draw the skyline.

QUESTION: Build a skyline representation from rectangular buildings.

TEXTBOOK ALGORITHM: The PDF gives a discretized integer-coordinate skyline routine, plus describes the faster divide-and-conquer algorithm.

The complete question, hints, solution development, and variants are in the
adjacent page-numbered reference Markdown, extracted from the supplied PDF.
This executable implementation restores syntax damaged by the PDF text layer;
minor type annotations, examples, and assertions are educational additions.

Run: python -m epi_python.chapter_24_honors_class.pg_386_compute_skyline
Test: python -m pytest tests/chapter_24_honors_class/test_pg_386_compute_skyline.py -v
"""

# collections.namedtuple documentation: https://docs.python.org/3/library/collections.html#collections.namedtuple
from collections import namedtuple


Rectangle=namedtuple('Rectangle',('left','right','height'))


def compute_skyline(buildings: list[Rectangle]) -> list[Rectangle]:
    """Digitized integer-coordinate version printed in the book."""
    if not buildings:return []
    min_left=min(b.left for b in buildings)
    max_right=max(b.right for b in buildings)
    heights=[0]*(max_right-min_left+1)
    for building in buildings:
        for i in range(building.left,building.right+1):
            heights[i-min_left]=max(heights[i-min_left],building.height)
    result=[];left=0
    for i in range(1,len(heights)):
        if heights[i]!=heights[i-1]:
            result.append(Rectangle(left+min_left,i-1+min_left,heights[i-1]))
            left=i
    return result+[Rectangle(left+min_left,max_right,heights[-1])]


if __name__=='__main__':
    r=compute_skyline([Rectangle(1,3,2),Rectangle(2,4,4)])
    print('Skyline:',r)
    assert r==[Rectangle(1,1,2),Rectangle(2,4,4)]
