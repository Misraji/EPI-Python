"""EPI Python 24.31, textbook printed page 395: Implement Huffman coding.

QUESTION: Compute minimum weighted-average binary code length using Huffman coding.

TEXTBOOK ALGORITHM: The PDF constructs a min-heap of frequency nodes, merges the two lightest, then visits codes.

The complete question, hints, solution development, and variants are in the
adjacent page-numbered reference Markdown, extracted from the supplied PDF.
This executable implementation restores syntax damaged by the PDF text layer;
minor type annotations, examples, and assertions are educational additions.

Run: python -m epi_python.chapter_24_honors_class.pg_395_huffman_encoding
Test: python -m pytest tests/chapter_24_honors_class/test_pg_395_huffman_encoding.py -v
"""

# heapq documentation: https://docs.python.org/3/library/heapq.html
import heapq

# collections.namedtuple documentation: https://docs.python.org/3/library/collections.html#collections.namedtuple
from collections import namedtuple

# itertools.count documentation: https://docs.python.org/3/library/itertools.html#itertools.count
from itertools import count


CharWithFrequency=namedtuple('CharWithFrequency',('c','freq'))


def huffman_encoding(symbols: list[CharWithFrequency]) -> float:
    """Return average codeword length for frequency percentages (as in the book)."""
    if not symbols:return 0.0
    serial=count()
    heap=[(s.freq,next(serial),s) for s in symbols]
    heapq.heapify(heap)
    while len(heap)>1:
        lf,_,left=heapq.heappop(heap)
        rf,_,right=heapq.heappop(heap)
        heapq.heappush(heap,(lf+rf,next(serial),(left,right)))
    code_lengths={}
    def assign(node,depth):
        if isinstance(node,CharWithFrequency):
            code_lengths[node.c]=max(1,depth)
        else:
            assign(node[0],depth+1)
            assign(node[1],depth+1)
    assign(heap[0][2],0)
    return sum(code_lengths[s.c]*s.freq/100 for s in symbols)


if __name__=='__main__':
    result=huffman_encoding([CharWithFrequency('a',50),CharWithFrequency('b',25),CharWithFrequency('c',25)])
    print('Average Huffman code length:',result)
    assert result==1.5
