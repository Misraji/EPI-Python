"""EPI exercise 8.7, printed page 107: Implement a circular queue.

EDUCATIONAL RECONSTRUCTION — not a verbatim verified code transcription.
Problem: Implement a circular queue.
Method/complexity: Circular buffer, resize by doubling; amortized O(1) operations, O(n) storage.
For the book's original explanation and variants, see:
    pg_107_exercise_08_07_implement_a_circular_queue.md

Run: python -m epi_python.chapter_08_stacks_and_queues.pg_107_circular_queue
Test: python -m pytest tests/chapter_08_stacks_and_queues/test_pg_107_circular_queue.py -v
"""

class CircularQueue:
    """An automatically growing circular array with FIFO semantics."""
    def __init__(self, capacity: int = 1):
        if capacity <= 0:
            raise ValueError("Initial capacity must be positive")
        self._entries = [None] * capacity
        self._head = 0
        self._size = 0

    def enqueue(self, value) -> None:
        if self._size == len(self._entries):
            self._entries = [self._entries[(self._head + j) % len(self._entries)]
                             for j in range(self._size)] + [None] * self._size
            self._head = 0
        tail = (self._head + self._size) % len(self._entries)
        self._entries[tail] = value
        self._size += 1

    def dequeue(self):
        if self._size == 0:
            raise IndexError("dequeue from empty queue")
        value = self._entries[self._head]
        self._entries[self._head] = None
        self._head = (self._head + 1) % len(self._entries)
        self._size -= 1
        return value

    def size(self) -> int:
        return self._size


def circular_queue_roundtrip(values: list[int]) -> list[int]:
    queue = CircularQueue(2)
    for value in values:
        queue.enqueue(value)
    return [queue.dequeue() for _ in values]


if __name__ == "__main__":
    queue = CircularQueue(2)
    for x in [1,2,3]:
        queue.enqueue(x)
    print("circular queue:", [queue.dequeue() for _ in range(3)])
    assert queue.size() == 0
