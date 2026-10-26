"""EPI exercise 8.9, printed page 109: Implement a queue with max API.

EDUCATIONAL RECONSTRUCTION — not a verbatim verified code transcription.
Problem: Implement a queue with max API.
Method/complexity: Monotone deque tracks possible maxima; amortized O(1) enqueue/dequeue/max, O(n) storage.
For the book's original explanation and variants, see:
    pg_109_exercise_08_09_implement_a_queue_with_max_api.md

Run: python -m epi_python.chapter_08_stacks_and_queues.pg_109_queue_with_max
Test: python -m pytest tests/chapter_08_stacks_and_queues/test_pg_109_queue_with_max.py -v
"""

# deque supports constant-time access and removal from both ends.
# Documentation: https://docs.python.org/3/library/collections.html#collections.deque
from collections import deque


class QueueWithMax:
    """FIFO queue with amortized constant-time maximum queries."""
    def __init__(self):
        self._queue = deque()
        self._max_candidates = deque()

    def enqueue(self, value: int) -> None:
        self._queue.append(value)
        while self._max_candidates and self._max_candidates[-1] < value:
            self._max_candidates.pop()
        self._max_candidates.append(value)

    def dequeue(self) -> int:
        if not self._queue:
            raise IndexError("dequeue from empty queue")
        value = self._queue.popleft()
        if value == self._max_candidates[0]:
            self._max_candidates.popleft()
        return value

    def max(self) -> int:
        if not self._max_candidates:
            raise IndexError("max from empty queue")
        return self._max_candidates[0]


def queue_max_history(values: list[int]) -> list[int]:
    q = QueueWithMax()
    result = []
    for value in values:
        q.enqueue(value)
        result.append(q.max())
    return result


if __name__ == "__main__":
    queue = QueueWithMax()
    for x in [3, 1, 5]:
        queue.enqueue(x)
    print("queue max:", queue.max())
    assert queue.max() == 5
    assert queue.dequeue() == 3 and queue.max() == 5
