"""EPI 16.12: Find the longest nondecreasing subsequence, printed page 257.

Educational reconstruction, not a verbatim transcription. Algorithm: Patience sorting maintains minimum tails per subsequence length, using bisect_right for equality.
The corresponding chapter's exercise Markdown retains the PDF text-layer
explanations, question and variants (with known OCR mistakes).

Run: python -m epi_python.chapter_16_dynamic_programming.pg_257_longest_nondecreasing_subsequence
Tests: python -m pytest tests/chapter_16_dynamic_programming/test_pg_257_longest_nondecreasing_subsequence.py -v
"""

# bisect_right locates the insertion point AFTER equal elements.
# Documentation: https://docs.python.org/3/library/bisect.html#bisect.bisect_right
from bisect import bisect_right


def longest_nondecreasing_subsequence(values: list[int]) -> int:
    """Length of a longest nondecreasing, not necessarily contiguous subsequence."""
    minimum_tails=[]
    for number in values:
        index=bisect_right(minimum_tails,number)
        if index==len(minimum_tails):
            minimum_tails.append(number)
        else:
            minimum_tails[index]=number
    return len(minimum_tails)

if __name__ == "__main__":
    # Executable demonstration cases; pytest has the full set.
    result=longest_nondecreasing_subsequence([])
    print('longest_nondecreasing_subsequence', result)
    assert result == 0
    result=longest_nondecreasing_subsequence([1])
    print('longest_nondecreasing_subsequence', result)
    assert result == 1
    result=longest_nondecreasing_subsequence([3, 1, 2, 2, 5])
    print('longest_nondecreasing_subsequence', result)
    assert result == 4
    result=longest_nondecreasing_subsequence([5, 4, 3])
    print('longest_nondecreasing_subsequence', result)
    assert result == 1
    result=longest_nondecreasing_subsequence([2, 2, 2])
    print('longest_nondecreasing_subsequence', result)
    assert result == 3
