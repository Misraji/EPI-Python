"""EPI Python — Exercise 8.9: Implement a Queue with Max API

Chapter 8: Stacks and Queues
Textbook: pages 109–111 (printed page numbers; problem and solution start on
page 109, Figure 8.4 and the first program on page 110, the second program
and its complexity on page 111).

PROBLEM (from the textbook)
---------------------------
"Implement a queue with enqueue, dequeue, and max operations. The max
operation returns the maximum element currently stored in the queue."

HINT (from the textbook)
------------------------
"When can an element never be returned by max, regardless of future
updates?"

SOLUTION DEVELOPMENT (following the textbook)
---------------------------------------------
Brute force: keep a variable holding the current maximum and update it on
every enqueue and dequeue. Enqueue is trivial (compare the new value with
the current maximum), but dequeue is slow: when the maximum leaves, every
remaining element must be examined, O(n) time for a queue of size n.

Key observation: suppose element s entered the queue before a later element
b with b > s. Because s leaves the queue before b, s can never again be the
maximum, whatever enqueues and dequeues follow. Such elements can be
ignored.

Approach: alongside the queue, keep a deque holding exactly those queue
entries that have no later entry greater than themselves. The deque keeps
them in queue order (the candidate nearest the queue's head comes first).
Each deque entry is greater than or equal to the entries after it, so the
head of the deque is the queue's maximum.

Updating the deque:
  * Dequeue: if the element just removed from the queue equals the deque's
    head, remove the deque's head too; otherwise leave the deque alone.
  * Enqueue: repeatedly remove the deque's tail while it is smaller than the
    new entry (stop when the tail is >= the new entry), then append the new
    entry at the deque's tail.

Figure 8.4 (textbook example). The queue Q starts as 3, 1, 3, 2, 0; the
operations are enqueue 1, dequeue, dequeue, enqueue 2, enqueue 4, dequeue,
enqueue 4. Heads are on the left. As printed:
    start      Q = 3,1,3,2,0          D = 3,3,2,0
    enqueue 1  Q = 3,1,3,2,0,1        D = 3,3,2,1
    dequeue    Q = 1,3,2,0,1          D = 3,2,1
    dequeue    Q = 3,2,0,1            D = 3,2,1
    enqueue 2  Q = 3,2,0,1,2          D = 3,2,2
    enqueue 4  Q = 3,2,0,1,2,4        D = 4
    dequeue    Q = 2,0,1,2,4          D = 4
    enqueue 4  Q = 3,2,0,1,2,4,4      D = 4,4
The head of D always holds the maximum of Q. (Note: the last panel's Q is
printed as 3,2,0,1,2,4,4; following from the previous panel it would be
2,0,1,2,4,4. This looks like a misprint in the figure; D is unaffected.)

The book presents two programs: the deque-based `QueueWithMax` (page 110),
implemented here as `QueueWithMax`, and a reduction to two stacks-with-max
(page 111, also named `QueueWithMax` in the book), implemented here as
`QueueWithMaxTwoStacks`.

ADDITIONAL EXAMPLES (added for learning; not printed in this exercise)
---------------------------------------------------------------------
    queue_max_history([3, 1, 5, 2]) -> [3, 3, 5, 5]
    enqueue 3, 1, 5; max -> 5; dequeue -> 3; max -> 5
"""

# Python standard library: specialized container types.
# Module documentation: https://docs.python.org/3/library/collections.html
# deque API: https://docs.python.org/3/library/collections.html#collections.deque
#
# `from module import name` binds just that name, so it is used as `deque`
# rather than `collections.deque`.
from collections import deque

# Local project import: the Chapter 8.1 `Stack` (stack with O(1) max),
# needed by the second textbook design. This is the repository's own module
# pg_098_stack_with_max.py in the same chapter package, imported absolutely
# through the installed `epi_python` package; it is not a standard-library
# module.
# Import system documentation: https://docs.python.org/3/reference/import.html
# Modules and packages tutorial: https://docs.python.org/3/tutorial/modules.html
from epi_python.chapter_08_stacks_and_queues.pg_098_stack_with_max import Stack

class QueueWithMax:
    """FIFO queue with amortized constant-time maximum queries.

    This is the textbook's first, deque-based implementation (page 110).
    """
    def __init__(self):

        # collections.deque() with no argument creates an empty
        # double-ended queue. append() adds at the right end, popleft()
        # removes from the left end, and pop() removes from the right end,
        # each in O(1) time; d[0] and d[-1] read the two ends.
        # _queue holds every element in FIFO order.
        # Documentation: https://docs.python.org/3/library/collections.html#collections.deque
        self._queue = deque()

        # A second deque of maximum candidates (D in Figure 8.4): non-increasing
        # from left to right, so its leftmost item is the current maximum.
        # A deque is needed because candidates are removed from BOTH ends.
        self._max_candidates = deque()

    def enqueue(self, value: int) -> None:
        self._queue.append(value)

        # Evict dominated candidates from the right end: any candidate
        # strictly smaller than the new value entered earlier and so can never
        # be the maximum again. `and` short-circuits, so [-1] is only read
        # when the deque is nonempty. Equal values are kept (strict `<`), which
        # matters because duplicates are dequeued one at a time.
        # deque.pop(): https://docs.python.org/3/library/collections.html#collections.deque.pop
        while self._max_candidates and self._max_candidates[-1] < value:
            self._max_candidates.pop()
        self._max_candidates.append(value)

    def dequeue(self) -> int:
        if not self._queue:
            raise IndexError("dequeue from empty queue")

        # deque.popleft() removes and returns the oldest element.
        # Documentation: https://docs.python.org/3/library/collections.html#collections.deque.popleft
        value = self._queue.popleft()

        # If the departing value is the current maximum candidate, it leaves
        # the candidate deque too; otherwise it was already evicted.
        if value == self._max_candidates[0]:
            self._max_candidates.popleft()
        return value

    def max(self) -> int:
        if not self._max_candidates:
            raise IndexError("max from empty queue")
        return self._max_candidates[0]


def queue_max_history(values: list[int]) -> list[int]:
    """Enqueue each value into a QueueWithMax and record max() after each.

    Repository helper added for testing/learning; not in the textbook.
    """
    q = QueueWithMax()
    result = []
    for value in values:
        q.enqueue(value)
        result.append(q.max())
    return result




class QueueWithMaxTwoStacks:
    """PDF's second queue-with-max implementation, reduced to two max-stacks.

    This is the textbook's second implementation (page 111; the book also
    names it `QueueWithMax`). An element is pushed into `_incoming` when
    enqueued. If `_outgoing` is empty on dequeue, move all incoming elements
    to it, reversing order. The queue's max is the max of either nonempty
    stack; each element is moved at most once, so total work is O(number of
    operations).
    """

    def __init__(self):

        # Two stacks-with-max from Exercise 8.1: one receives enqueues, the
        # other serves dequeues (the two-stack queue of Exercise 8.8).
        self._incoming = Stack()
        self._outgoing = Stack()

    def enqueue(self, value: int) -> None:
        self._incoming.push(value)

    def dequeue(self) -> int:

        # Refill the outgoing stack only when it is empty; popping from one
        # stack and pushing onto the other reverses the order so the oldest
        # element is on top.
        if self._outgoing.empty():
            while not self._incoming.empty():
                self._outgoing.push(self._incoming.pop())
        if self._outgoing.empty():
            raise IndexError('empty queue')
        return self._outgoing.pop()

    def max(self) -> int:

        # The queue's elements are split between the two stacks, so its
        # maximum is the larger of the two stack maxima. Each stack's max()
        # is O(1) but raises IndexError when empty, hence the empty checks.
        # The built-in max(a, b) returns the larger of its two arguments.
        # max(): https://docs.python.org/3/library/functions.html#max
        if not self._incoming.empty():
            if self._outgoing.empty():
                return self._incoming.max()
            return max(self._incoming.max(), self._outgoing.max())
        if not self._outgoing.empty():
            return self._outgoing.max()
        raise IndexError('empty queue')


# TEXTBOOK POST-SOLUTION DISCUSSION (pages 110–111)
# -------------------------------------------------
# Deque-based design: dequeue is O(1). One enqueue can evict many candidates
# from the deque, but each element enters and leaves the deque at most once,
# so any sequence of n enqueues and dequeues takes O(n) time in total
# (O(1) amortized each). max is O(1): it just reads the deque's head.
#
# Alternative often presented (reduction): Exercise 8.1 gives an efficient
# stack with max, and Exercise 8.8 builds a queue from two stacks; combining
# them, a queue built from two stacks-with-max also supports max. The book
# finds this less natural than the deque approach. Since the stack-with-max
# has O(1) amortized push, pop and max, and the two-stack queue has O(1)
# amortized enqueue and dequeue, this design has O(1) amortized enqueue,
# dequeue and max.
#
# VARIANTS
# The textbook gives no variants for this exercise.


# TEXTBOOK CODE COMPARISON
# ------------------------
# Book program 1, `class QueueWithMax` (page 110): fields `_entries` and
# `_candidates_for_max` created with `collections.deque()`; `enqueue(self,
# x)` with the comment "Eliminate dominated elements in
# _candidates_for_max."; `dequeue` checks `if self._entries:` and raises
# IndexError('empty queue') at the end; `max` checks the candidates and
# raises IndexError('empty queue').
# File `QueueWithMax`: fields renamed `_queue` and `_max_candidates`;
# imports `deque` directly (`from collections import deque`); parameter
# `value: int` with return hints; dequeue and max use early-raise guard
# clauses with different messages ("dequeue from empty queue", "max from
# empty queue"); the book's comment is not present. Same algorithm.
#
# Book program 2, also `class QueueWithMax` (page 111): stacks `_enqueue`
# and `_dequeue` (of type `Stack` from Solution 8.1); dequeue returns inside
# `if not self._dequeue.empty():` and raises otherwise; max uses a
# conditional expression `self._enqueue.max() if self._dequeue.empty() else
# max(...)`.
# File `QueueWithMaxTwoStacks`: renamed class; stacks renamed `_incoming` and
# `_outgoing`; dequeue raises when empty, then pops; max written as a nested
# if instead of a conditional expression; `value: int` and return hints
# added. It imports the repository's `Stack` (first 8.1 design). Same logic.
#
# Helper not in the book: `queue_max_history`.


# Python executes this block only when this source file is run directly.
# When pytest imports the file, this block is skipped automatically.
# Documentation: https://docs.python.org/3/library/__main__.html
if __name__ == "__main__":

    # Deque-based design: after enqueuing 3, 1, 5 the maximum is 5; removing
    # the oldest element (3) does not change it.
    # `assert` stops the program with an AssertionError if the condition is
    # false; these are quick smoke checks, pytest does the thorough testing.
    queue = QueueWithMax()
    for x in [3, 1, 5]:
        queue.enqueue(x)
    print("queue max:", queue.max())
    assert queue.max() == 5
    assert queue.dequeue() == 3 and queue.max() == 5

    # The same scenario on the two-stacks-with-max design gives the same
    # answers.
    alternate = QueueWithMaxTwoStacks()
    for x in (3, 1, 5):
        alternate.enqueue(x)
    assert alternate.max() == 5
    assert alternate.dequeue() == 3 and alternate.max() == 5
    print('second PDF queue-with-max design:', alternate.max())
