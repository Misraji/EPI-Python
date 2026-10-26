"""EPI Python 24.16, textbook printed page 372: Search in two sorted arrays.

QUESTION: Return kth smallest element (one-based) across two sorted arrays without fully merging them.

TEXTBOOK ALGORITHM: Binary search the number of values taken from the first input and compare boundary values.

The complete question, hints, solution development, and variants are in the
adjacent page-numbered reference Markdown, extracted from the supplied PDF.
This executable implementation restores syntax damaged by the PDF text layer;
minor type annotations, examples, and assertions are educational additions.

Run: python -m epi_python.chapter_24_honors_class.pg_372_find_kth_in_two_sorted_arrays
Test: python -m pytest tests/chapter_24_honors_class/test_pg_372_find_kth_in_two_sorted_arrays.py -v
"""

def find_kth_in_two_sorted_arrays(a: list[int],b: list[int],k: int) -> int:
    if k<1 or k>len(a)+len(b):
        raise ValueError('k must be between 1 and total length')
    low=max(0,k-len(b))
    high=min(len(a),k)
    while low<=high:
        x=(low+high)//2
        ax_left=float('-inf') if x==0 else a[x-1]
        ax=float('inf') if x==len(a) else a[x]
        by=k-x
        by_left=float('-inf') if by==0 else b[by-1]
        by_right=float('inf') if by==len(b) else b[by]
        if ax<by_left:
            low=x+1
        elif ax_left>by_right:
            high=x-1
        else:
            return max(ax_left,by_left)
    raise RuntimeError('Sorted input required')


if __name__=='__main__':
    print('4th across two arrays:',find_kth_in_two_sorted_arrays([1,3,6],[2,4,5],4))
    assert find_kth_in_two_sorted_arrays([1,3,6],[2,4,5],4)==4
