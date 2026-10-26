"""EPI 24.12: Compute the maximum of a sliding window — printed page 365.

Educational reconstruction; not a verified verbatim textbook transcription.
Question: Compute the maximum of a sliding window
Algorithm: A monotonic deque holds indices of potential maxima; amortized O(n) total work.
Read the corresponding `pg_365_exercise_...md` file for the extracted
book's problem, worked explanations and variants. OCR is unverified.

Run: python -m epi_python.chapter_24_honors_class.pg_365_max_of_sliding_window
Test: python -m pytest tests/chapter_24_honors_class/test_pg_365_max_of_sliding_window.py -v
"""

# deque is a double-ended queue; its popleft() avoids O(n) list shifts.
# Documentation: https://docs.python.org/3/library/collections.html#collections.deque
from collections import deque


def max_of_sliding_window(values: list[int], k: int) -> list[int]:
    """Maximum in every consecutive window of k elements."""
    if k<=0:
        raise ValueError('window size must be positive')
    if k>len(values):
        return []
    candidates=deque()
    result=[]
    for index,value in enumerate(values):
        while candidates and candidates[0] <= index-k:
            candidates.popleft()
        while candidates and values[candidates[-1]] <= value:
            candidates.pop()
        candidates.append(index)
        if index>=k-1:
            result.append(values[candidates[0]])
    return result


if __name__ == "__main__":
    # Demonstrations check representative input/output behavior.
    observed = max_of_sliding_window([], 1)
    print("max_of_sliding_window:", observed)
    assert observed == []
    observed = max_of_sliding_window([1, 3, -1, -3, 5, 3, 6, 7], 3)
    print("max_of_sliding_window:", observed)
    assert observed == [3, 3, 5, 5, 6, 7]
    observed = max_of_sliding_window([2, 1], 1)
    print("max_of_sliding_window:", observed)
    assert observed == [2, 1]
    observed = max_of_sliding_window([2, 1], 2)
    print("max_of_sliding_window:", observed)
    assert observed == [2]
