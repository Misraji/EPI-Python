"""EPI 10.5: Compute the median of online data, printed page 139.

Educational reconstruction, not a verbatim transcription. Algorithm: Two heaps preserve lower and upper halves, allowing O(log n) per update and O(1) median.
The corresponding chapter's exercise Markdown retains the PDF text-layer
explanations, question and variants (with known OCR mistakes).

Run: python -m epi_python.chapter_10_heaps.pg_139_online_median
Tests: python -m pytest tests/chapter_10_heaps/test_pg_139_online_median.py -v
"""

# heapq.heappush/heappop manage min-heaps, used for both halves.
# Documentation: https://docs.python.org/3/library/heapq.html
import heapq


def online_median(values: list[int]) -> list[float]:
    """Return median after each newly observed input value."""
    smaller=[]  # negatives: Python min-heap emulates max-heap
    larger=[]
    result=[]
    for number in values:
        heapq.heappush(smaller,-number)
        heapq.heappush(larger,-heapq.heappop(smaller))
        if len(larger)>len(smaller):
            heapq.heappush(smaller,-heapq.heappop(larger))
        if len(smaller)==len(larger):
            result.append((-smaller[0]+larger[0])/2)
        else:
            result.append(float(-smaller[0]))
    return result

if __name__ == "__main__":
    # Executable demonstration cases; pytest has the full set.
    result=online_median([])
    print('online_median', result)
    assert result == []
    result=online_median([1])
    print('online_median', result)
    assert result == [1.0]
    result=online_median([1, 2])
    print('online_median', result)
    assert result == [1.0, 1.5]
    result=online_median([1, 0, 3, 5, 2])
    print('online_median', result)
    assert result == [1.0, 0.5, 1.0, 2.0, 2.0]
