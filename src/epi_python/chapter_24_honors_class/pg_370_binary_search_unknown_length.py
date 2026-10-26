"""EPI Python 24.15, textbook printed page 370: Search a sorted array of unknown length.

QUESTION: Find a value in a sorted array supporting index lookup but not length introspection.

TEXTBOOK ALGORITHM: Exponential probing finds an upper bound; binary search treats IndexError as infinity.

The complete question, hints, solution development, and variants are in the
adjacent page-numbered reference Markdown, extracted from the supplied PDF.
This executable implementation restores syntax damaged by the PDF text layer;
minor type annotations, examples, and assertions are educational additions.

Run: python -m epi_python.chapter_24_honors_class.pg_370_binary_search_unknown_length
Test: python -m pytest tests/chapter_24_honors_class/test_pg_370_binary_search_unknown_length.py -v
"""

def binary_search_unknown_length(a, k: int) -> int:
    p=0
    while True:
        try:
            idx=(1<<p)-1
            if a[idx]==k:
                return idx
            if a[idx]>k:
                break
        except IndexError:
            break
        p+=1
    left,right=(1<<max(0,p-1)),(1<<p)-2
    if p==0:
        left=0
    while left<=right:
        mid=left+(right-left)//2
        try:
            if a[mid]==k:
                return mid
            if a[mid]>k:
                right=mid-1
            else:
                left=mid+1
        except IndexError:
            right=mid-1
    return -1


if __name__=='__main__':
    print('Index:',binary_search_unknown_length([1,3,5,7,9],7))
    assert binary_search_unknown_length([1,3,5,7,9],7)==3
