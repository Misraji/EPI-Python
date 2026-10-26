"""EPI Python 24.25, textbook printed page 385: Count inversions.

QUESTION: Count pairs (i,j) where i<j and A[i]>A[j].

TEXTBOOK ALGORITHM: Merge-sort halves recursively; count cross inversions when right entry precedes remaining left entries.

The complete question, hints, solution development, and variants are in the
adjacent page-numbered reference Markdown, extracted from the supplied PDF.
This executable implementation restores syntax damaged by the PDF text layer;
minor type annotations, examples, and assertions are educational additions.

Run: python -m epi_python.chapter_24_honors_class.pg_385_count_inversions
Test: python -m pytest tests/chapter_24_honors_class/test_pg_385_count_inversions.py -v
"""

def count_inversions(a: list[int]) -> int:
    def merge_sort_count(start,end):
        if end-start<=1:return 0
        mid=(start+end)//2
        inv=merge_sort_count(start,mid)+merge_sort_count(mid,end)
        i,j=start,mid
        merged=[]
        while i<mid and j<end:
            if a[i]<=a[j]:
                merged.append(a[i]);i+=1
            else:
                merged.append(a[j]);inv+=mid-i;j+=1
        a[start:end]=merged+a[i:mid]+a[j:end]
        return inv
    return merge_sort_count(0,len(a))


if __name__=='__main__':
    data=[3,6,4,2,5,1]
    print('Inversions:',count_inversions(data))
    assert count_inversions([3,6,4,2,5,1])==10
