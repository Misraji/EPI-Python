"""EPI Python — Exercise 8.7: Implement a Circular Queue

Chapter 8: Stacks and Queues
Textbook: pages 107–108 (printed page numbers; problem, solution and start of
the program on page 107, rest of the program and complexity on page 108).

PROBLEM (from the textbook)
---------------------------
"A queue can be implemented using an array and two additional fields, the
beginning and the end indices. This structure is sometimes referred to as a
circular queue. Both enqueue and dequeue have O(1) time complexity. If the
array is fixed, there is a maximum number of entries that can be stored. If
the array is dynamically resized, the total time for m combined enqueue and
dequeue operations is O(m).

Implement a queue API using an array for storing elements. Your API should
include a constructor function, which takes as argument the initial capacity
of the queue, enqueue and dequeue functions, and a function which returns the
number of elements stored. Implement dynamic resizing to support storing an
arbitrarily large number of elements."

HINT (from the textbook)
------------------------
"Track the head and tail. How can you differentiate a full queue from an
empty one?"

SOLUTION DEVELOPMENT (following the textbook)
---------------------------------------------
Brute force: store the queue in an array with the head fixed at index 0 and
a variable holding the tail's index. Enqueue is O(1), but dequeue is O(n)
for n stored elements, because all remaining elements must shift one place
left to fill the hole at index 0.

Better: also keep a variable for the head's index; then dequeue just
advances the head, which is O(1). Indices wrap around the end of the array
(hence "circular").

Resizing: when enqueueing into a full array the array must grow, but simply
making it longer is not enough, because the queue's elements may not be
contiguous. Example from the book: the array <e, b, c, d> with e the tail
and b the head; growing it to <e, b, c, d, _, _, _, _> leaves no place to
enqueue without overwriting elements or moving them. So, on resize, the
elements are first rearranged so they appear consecutively starting at
index 0 (head at 0, tail just after the last element), and then extra empty
slots are added.

Full versus empty: when head == tail the queue could be either, so the book
keeps an explicit count of stored elements.

The book's program is a class `Queue` (constant SCALE_FACTOR = 2; methods
enqueue, dequeue, size). This file's `CircularQueue` implements the same
idea; differences are listed in the code comparison at the end.

ADDITIONAL EXAMPLES (added for learning; not printed in this exercise)
---------------------------------------------------------------------
    q = CircularQueue(2); enqueue 1, 2, 3 (forces a resize to capacity 4);
    dequeue three times -> 1, 2, 3; q.size() -> 0
    circular_queue_roundtrip([5, 6, 7]) -> [5, 6, 7]
"""


class CircularQueue:
    """An automatically growing circular array with FIFO semantics.

    Implements the textbook's circular `Queue` (pages 107–108), without a
    stored tail index (the tail is computed from head and size).
    """

    # `capacity: int = 1` is a parameter with a type hint and a default value:
    # CircularQueue() starts with one slot. Hints are not enforced by Python.
    def __init__(self, capacity: int = 1):
        if capacity <= 0:
            raise ValueError("Initial capacity must be positive")

        # [None] * capacity creates a list of `capacity` None placeholders:
        # the fixed-size "array" of slots. Multiplying a list repeats it.
        self._entries = [None] * capacity

        # _head is the index of the front element; _size counts stored
        # elements, which distinguishes an empty queue (0) from a full one
        # (len(self._entries)), even though head alone cannot.
        self._head = 0
        self._size = 0

    def enqueue(self, value) -> None:

        # Full: every slot is occupied. Rebuild the array so the elements
        # appear consecutively from index 0, followed by as many empty slots
        # again (doubling the capacity, like the book's SCALE_FACTOR = 2).
        if self._size == len(self._entries):

            # The list comprehension reads the elements in queue order:
            # logical position j is physical index (head + j) % capacity.
            # `%` (modulo) wraps an index that runs past the end back to the
            # start; for non-negative operands it gives the remainder.
            # `+` concatenates the copied elements with `size` new None slots.
            self._entries = [self._entries[(self._head + j) % len(self._entries)]
                             for j in range(self._size)] + [None] * self._size
            self._head = 0

        # The tail slot (first free slot) is `size` positions after the head,
        # wrapped around with modulo.
        tail = (self._head + self._size) % len(self._entries)
        self._entries[tail] = value
        self._size += 1

    def dequeue(self):
        if self._size == 0:

            # Like list.pop() on an empty list, report an IndexError.
            raise IndexError("dequeue from empty queue")
        value = self._entries[self._head]

        # Clearing the slot drops the queue's reference to the object, so it
        # can be garbage-collected if nothing else uses it.
        self._entries[self._head] = None

        # Advance the head one slot, wrapping from the last index to 0.
        self._head = (self._head + 1) % len(self._entries)
        self._size -= 1
        return value

    def size(self) -> int:
        return self._size


def circular_queue_roundtrip(values: list[int]) -> list[int]:
    """Enqueue all values into a CircularQueue(2), then dequeue them all.

    Repository helper added for testing/learning; not in the textbook.
    """
    queue = CircularQueue(2)
    for value in values:
        queue.enqueue(value)

    # A list comprehension that calls dequeue() once per original value;
    # `_` marks the loop variable as unused.
    return [queue.dequeue() for _ in values]


# TEXTBOOK POST-SOLUTION DISCUSSION (page 108)
# --------------------------------------------
# dequeue runs in O(1) time. enqueue runs in O(1) amortized time: an
# occasional resize copies all n elements, but because the capacity grows by
# a constant factor, the copying cost averaged over the enqueues is O(1).
#
# VARIANTS
# The textbook gives no variants for this exercise.


# TEXTBOOK CODE COMPARISON
# ------------------------
# Book: `class Queue` with class constant `SCALE_FACTOR = 2`;
# `__init__(self, capacity)` (no default, no validation) sets `_entries`,
# and `_head = _tail = _num_queue_elements = 0`. `enqueue(self, x)`: when
# full ("Needs to resize."), it makes the elements consecutive with the
# slice concatenation `self._entries[self._head:] +
# self._entries[:self._head]`, resets `_head, _tail = 0,
# _num_queue_elements`, then extends with `+= [None] * (len * SCALE_FACTOR
# - len)`; it writes at `_tail` and advances `_tail` modulo the length.
# `dequeue`: raises IndexError('empty queue') when empty, decrements the
# count, reads `ret = self._entries[self._head]` and advances the head; it
# does not clear the slot. `size` returns `_num_queue_elements`.
# File: class renamed `CircularQueue`; `capacity: int = 1` default and a
# ValueError for capacity <= 0 added; no `SCALE_FACTOR` constant (doubling
# is hard-coded by appending `size` None slots); no `_tail` field (tail is
# computed as (head + size) % len); count renamed `_size`; the reordering on
# resize uses a modulo-indexed list comprehension instead of slicing;
# `enqueue(self, value) -> None`; dequeue clears the vacated slot and uses a
# different error message; `size() -> int` hint added.
# Helper not in the book: `circular_queue_roundtrip`.


# Python executes this block only when this source file is run directly.
# When pytest imports the file, this block is skipped automatically.
# Documentation: https://docs.python.org/3/library/__main__.html
if __name__ == "__main__":

    # Start with capacity 2 and enqueue three values: the third enqueue finds
    # the array full and triggers a resize. The dequeues must still return
    # 1, 2, 3 in first-in, first-out order.
    queue = CircularQueue(2)
    for x in [1,2,3]:
        queue.enqueue(x)
    print("circular queue:", [queue.dequeue() for _ in range(3)])

    # `assert` stops the program with an AssertionError if the condition is
    # false; here it confirms the queue is empty after three dequeues.
    assert queue.size() == 0
