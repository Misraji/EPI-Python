"""EPI Python — Exercise 24.12: Compute the Maximum of a Sliding Window

Chapter 24: Honors Class
Textbook: pages 365–366 (printed page numbers; problem, Figure 24.5 and the
start of the solution on 365; the rest of the solution, the program and the
analysis on 366).

PROBLEM (from the textbook)
---------------------------
Network traffic control sometimes requires studying traffic volume over
time. This problem explores the development of an efficient algorithm for
computing the traffic volumes.

You are given traffic at various timestamps and a window length. Compute
for each input timestamp, the maximum traffic over the window length time
interval which ends at that timestamp. See Figure 24.5 for an example.

Figure 24.5 (described): (a) traffic at various timestamps — 1.3 at 0,
2.5 at 2, 3.7 at 3, 1.4 at 5, 2.6 at 6, 2.2 at 8, 1.7 at 9, 1.7 at 14;
(b) the maximum traffic over a window of size 3 at each of those
timestamps — 1.3, 2.5, 3.7, 3.7, 3.7, 2.6, 2.6, 1.7.

HINT (from the textbook)
------------------------
You need to be able to identify the maximum element in a queue quickly.

SOLUTION DEVELOPMENT (following the textbook)
---------------------------------------------
Input: a window length w and an array A of (integer timestamp, traffic
volume) pairs; if A is not sorted by timestamp, sort it first. The traffic
of Figure 24.5(a) is the array <(0, 1.3), (2, 2.5), (3, 3.7), (5, 1.4),
(6, 2.6), (8, 2.2), (9, 1.7), (14, 1.1)>.
[NEEDS PDF REVIEW: page 365 prints the last pair as (14, 1.1), but Figure
24.5(a) and the output on page 366 show 1.7 at timestamp 14.]

Brute force: for each timestamp, find the maximum among the elements whose
timestamps fall in the window ending there. Every window may contain up to
w + 1 elements, so this is O(nw), where n is the length of A.

Improvement: when the window advances, only its boundary changes — some
older elements fall out and one new element comes in. A queue models the
window naturally, and since the maximum of each window is needed, use the
queue-with-maximum structure of Solution 8.9 (Page 109):
  * start with an empty queue-with-maximum Q;
  * enqueue the elements in order of increasing i;
    [NEEDS PDF REVIEW: page 366 writes the enqueued pair as "(t_i, t_i)";
    the second component is presumably the volume but is printed that way.]
  * for each i, dequeue from Q while the difference between t_i and the
    timestamp at Q's head exceeds w (i.e. until it is at most w);
  * the maximum of Q after each step is the result for i.
For Figure 24.5(a) with window size 3 the output is <(0, 1.3), (2, 2.5),
(3, 3.7), (5, 3.7), (6, 3.7), (8, 2.6), (9, 2.6), (14, 1.7)>, drawn in
Figure 24.5(b).

The book's program is `calculate_traffic_volumes(A, w)` with a
`TrafficElement` class and a `QueueWithMax` from Chapter 8.

IMPORTANT: this file does NOT implement that program. It contains
`max_of_sliding_window(values, k)`, which computes the maximum of every
window of k CONSECUTIVE ARRAY ELEMENTS (no timestamps) using a monotonic
deque of indices. See TEXTBOOK CODE COMPARISON below.

ADDITIONAL EXAMPLES (added for learning; not printed in this exercise)
---------------------------------------------------------------------
    values=[], k=1                         -> []
    values=[1, 3, -1, -3, 5, 3, 6, 7], k=3 -> [3, 3, 5, 5, 6, 7]
    values=[2, 1], k=1                     -> [2, 1]
    values=[2, 1], k=2                     -> [2]
"""

# Python standard library: specialized container types.
# Module documentation: https://docs.python.org/3/library/collections.html
# deque API: https://docs.python.org/3/library/collections.html#collections.deque
from collections import deque


def max_of_sliding_window(values: list[int], k: int) -> list[int]:
    """Maximum in every consecutive window of k elements (file's own version).

    NOT the textbook's `calculate_traffic_volumes`: it uses a fixed count of
    elements rather than a timestamp interval, and a monotonic deque instead
    of the book's QueueWithMax class. The deque idea is the same one behind
    a queue with maximum: keep only elements that could still become a
    window maximum.

    Type hints (`list[int]`, `int`, `-> list[int]`) are documentation only.
    """

    # `raise` stops with an exception for an impossible window size.
    if k<=0:
        raise ValueError('window size must be positive')

    # No complete window exists.
    if k>len(values):
        return []

    # collections.deque() creates an empty double-ended queue. Unlike a list,
    # it removes items from the LEFT end in O(1) time (list.pop(0) shifts
    # every other element, O(n)). Here it stores INDICES of candidate maxima,
    # with their values in decreasing order from left to right.
    candidates=deque()
    result=[]

    # enumerate(values) yields (index, value) pairs.
    # https://docs.python.org/3/library/functions.html#enumerate
    for index,value in enumerate(values):

        # candidates[0] is the leftmost (oldest) index. If it is at or before
        # index - k it has left the window ending at `index`.
        # deque.popleft() removes and returns the leftmost item in O(1).
        # `candidates and ...`: an empty deque is falsy, so the index is not
        # read when the deque is empty.
        while candidates and candidates[0] <= index-k:
            candidates.popleft()

        # candidates[-1] is the rightmost (newest) index. Any earlier value
        # <= the new value can never be a maximum again (the new value is
        # larger or equal and stays in the window longer), so discard it.
        # deque.pop() removes and returns the rightmost item.
        while candidates and values[candidates[-1]] <= value:
            candidates.pop()

        # deque.append(x) adds x at the right end.
        candidates.append(index)

        # Once the first full window is reached, the leftmost candidate is
        # the maximum of the current window.
        if index>=k-1:
            result.append(values[candidates[0]])
    return result


# TEXTBOOK POST-SOLUTION DISCUSSION (page 366)
# --------------------------------------------
# Each element is enqueued once and dequeued at most once. Because the
# queue-with-maximum structure takes O(1) amortized time per operation, the
# total time is O(n). The additional space is O(w).
#
# (For this file's deque version the same argument applies: each index is
# appended once and removed at most once, giving O(n) time and O(k) space.)
#
# VARIANTS
# The book gives no variants for this exercise.


# TEXTBOOK CODE COMPARISON
# ------------------------
# book: `class TrafficElement` with `__init__(self, time, volume)`, `__lt__`
#   (compares volume) and `__eq__` (compares time and volume), needed by
#   QueueWithMax; `def calculate_traffic_volumes(A, w)` enqueues each
#   traffic_info into a `QueueWithMax()` (from Chapter 8), dequeues while
#   `traffic_info.time - sliding_window.head().time > w`, and appends
#   `TrafficElement(traffic_info.time, sliding_window.max().volume)`.
# file: completely different program. `max_of_sliding_window(values: list[int],
#   k: int) -> list[int]` works on plain values with a window of k
#   consecutive elements (no timestamps), uses `collections.deque` as a
#   monotonic queue of indices, raises ValueError for k <= 0, returns [] when
#   k > len(values), and outputs only maxima of complete windows (n - k + 1
#   values, versus one per timestamp in the book). The book's TrafficElement,
#   calculate_traffic_volumes and the QueueWithMax dependency are all
#   missing from the file.


# Python executes this block only when this source file is run directly.
# When pytest imports the file, this block is skipped automatically.
# Documentation: https://docs.python.org/3/library/__main__.html
if __name__ == "__main__":
    # Demonstrations check representative input/output behavior: an empty
    # input, a classic mixed-sign example with k = 3, a window of size 1
    # (each element is its own maximum) and a window covering the whole list.
    #
    # `assert` stops the program with an AssertionError if a result is
    # different from the expected value; the tests/ folder holds the
    # thorough pytest suite.
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
