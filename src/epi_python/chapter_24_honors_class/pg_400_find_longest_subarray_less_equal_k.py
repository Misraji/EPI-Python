"""EPI Python 24.34, textbook printed page 400: Find the longest subarray whose sum less than k.

QUESTION: Find maximum length of a contiguous subarray with sum at most k; negative numbers are allowed.

TEXTBOOK ALGORITHM: Build prefix sums and suffix minima, then advance two pointers using minimum possible ending sums.

The complete question, hints, solution development, and variants are in the
adjacent page-numbered reference Markdown, extracted from the supplied PDF.
This executable implementation restores syntax damaged by the PDF text layer;
minor type annotations, examples, and assertions are educational additions.

Run: python -m epi_python.chapter_24_honors_class.pg_400_find_longest_subarray_less_equal_k
Test: python -m pytest tests/chapter_24_honors_class/test_pg_400_find_longest_subarray_less_equal_k.py -v
"""

# itertools.accumulate documentation: https://docs.python.org/3/library/itertools.html#itertools.accumulate
import itertools


def find_longest_subarray_less_equal_k(a: list[int], k: int) -> int:
    if not a:
        return 0

    # accumulate computes each prefix sum lazily; list materializes the results.
    prefix_sum = list(itertools.accumulate(a))
    if prefix_sum[-1] <= k:
        return len(a)
    min_prefix_sum = prefix_sum[:]
    for i in range(len(a)-2,-1,-1):
        min_prefix_sum[i] = min(min_prefix_sum[i],min_prefix_sum[i+1])
    start = end = max_length = 0
    while start<len(a) and end<len(a):
        minimum_sum = min_prefix_sum[end] - (prefix_sum[start-1] if start else 0)
        if minimum_sum <= k:
            max_length = max(max_length,end-start+1)
            end += 1
        else:
            start += 1
    return max_length


if __name__ == '__main__':
    array = [4,-3,2,1,-4,5]
    print('Longest subarray with sum <= 3:', find_longest_subarray_less_equal_k(array,3))
    assert find_longest_subarray_less_equal_k([1,2,-3,4],3)==3
