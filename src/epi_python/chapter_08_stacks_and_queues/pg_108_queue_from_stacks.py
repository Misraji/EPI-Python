"""EPI 8.8: Implement a queue using stacks — printed page 108.

Educational reconstruction; not a verified verbatim textbook transcription.
Question: Implement a queue using stacks
Algorithm: Push onto incoming stack; on dequeue, transfer only when outgoing stack is empty. Amortized O(1).
Read the corresponding `pg_108_exercise_...md` file for the extracted
book's problem, worked explanations and variants. OCR is unverified.

Run: python -m epi_python.chapter_08_stacks_and_queues.pg_108_queue_from_stacks
Test: python -m pytest tests/chapter_08_stacks_and_queues/test_pg_108_queue_from_stacks.py -v
"""

class Queue:
    """FIFO queue implemented with two LIFO Python lists."""
    def __init__(self) -> None:
        self._incoming = []
        self._outgoing = []

    def enqueue(self, item: int) -> None:
        self._incoming.append(item)

    def dequeue(self) -> int:
        if not self._outgoing:
            while self._incoming:
                self._outgoing.append(self._incoming.pop())
        if not self._outgoing:
            raise IndexError('dequeue from empty queue')
        return self._outgoing.pop()


def queue_from_stacks(values: list[int]) -> list[int]:
    """Demonstrate the FIFO sequence produced by the Queue class."""
    queue = Queue()
    for value in values:
        queue.enqueue(value)
    return [queue.dequeue() for _ in values]


if __name__ == "__main__":
    # Demonstrations check representative input/output behavior.
    observed = queue_from_stacks([])
    print("queue_from_stacks:", observed)
    assert observed == []
    observed = queue_from_stacks([1])
    print("queue_from_stacks:", observed)
    assert observed == [1]
    observed = queue_from_stacks([1, 2, 3])
    print("queue_from_stacks:", observed)
    assert observed == [1, 2, 3]
