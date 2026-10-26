"""EPI Python 24.5, textbook printed page 356: Compute the longest contiguous increasing subarray.

QUESTION: Find indices delimiting the longest strictly increasing contiguous subarray.

TEXTBOOK ALGORITHM: The book uses backward skipping plus forward extension to avoid redundant comparisons.

The complete question, hints, solution development, and variants are in the
adjacent page-numbered reference Markdown, extracted from the supplied PDF.
This executable implementation restores syntax damaged by the PDF text layer;
minor type annotations, examples, and assertions are educational additions.

Run: python -m epi_python.chapter_24_honors_class.pg_356_find_longest_increasing_subarray
Test: python -m pytest tests/chapter_24_honors_class/test_pg_356_find_longest_increasing_subarray.py -v
"""

# collections.namedtuple documentation: https://docs.python.org/3/library/collections.html#collections.namedtuple
from collections import namedtuple


Subarray=namedtuple('Subarray',('start','end'))


def find_longest_increasing_subarray(a: list[int]) -> Subarray:
    if not a:
        return Subarray(0,-1)
    result=Subarray(0,0)
    i,max_length=0,1
    while i<len(a)-max_length:
        for j in range(i+max_length,i,-1):
            if a[j-1]>=a[j]:
                i=j
                break
        else:
            i+=max_length
            while i<len(a) and a[i-1]<a[i]:
                i,max_length=i+1,max_length+1
            result=Subarray(i-max_length,i-1)
    return result


if __name__=='__main__':
    result=find_longest_increasing_subarray([1,2,3,1,4,6,7])
    print('Longest increasing run:',result)
    assert result==Subarray(3,6)
