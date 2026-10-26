"""EPI Python 24.17, textbook printed page 373: Find the kth largest element - large n, small k.

QUESTION: Find kth largest number in a stream of unknown length using O(k) storage.

TEXTBOOK ALGORITHM: Repeatedly partition batches of size 2k-1 using book Chapter 11 selection algorithm, retaining only k candidates.

The complete question, hints, solution development, and variants are in the
adjacent page-numbered reference Markdown, extracted from the supplied PDF.
This executable implementation restores syntax damaged by the PDF text layer;
minor type annotations, examples, and assertions are educational additions.

Run: python -m epi_python.chapter_24_honors_class.pg_373_find_kth_largest_unknown_length
Test: python -m pytest tests/chapter_24_honors_class/test_pg_373_find_kth_largest_unknown_length.py -v
"""

# Chapter 11 selection algorithm used directly by this textbook exercise.
from epi_python.chapter_11_searching.pg_153_kth_largest_element import find_kth_largest


def find_kth_largest_unknown_length(stream,k: int) -> int:
    if k<=0:raise ValueError('k must be positive')
    candidates=[]
    for x in stream:
        candidates.append(x)
        if len(candidates)>=2*k-1:
            # The book's selection algorithm partitions in place, keeping k largest first.
            # Our Chapter 11 helper returns a value without reordering the supplied list,
            # so use the pivot threshold to retain exactly k values, including duplicates.
            cutoff=find_kth_largest(k,candidates)
            larger=[v for v in candidates if v>cutoff]
            candidates=larger+[cutoff]*(k-len(larger))
    if len(candidates)<k:
        raise ValueError('Fewer than k elements in stream')
    return find_kth_largest(k,candidates)


if __name__=='__main__':
    print('Third largest:',find_kth_largest_unknown_length(iter([3,1,5,2,4]),3))
    assert find_kth_largest_unknown_length(iter([3,1,5,2,4]),3)==3
