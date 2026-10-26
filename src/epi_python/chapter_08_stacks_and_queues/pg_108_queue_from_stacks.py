"""EPI Python — Exercise 8.8: Implement a Queue Using Stacks

Chapter 8: Stacks and Queues
Textbook: pages 108–109 (printed page numbers; problem and solution on page
108, the program and complexity at the top of page 109).

PROBLEM (from the textbook)
---------------------------
"Queue insertion and deletion follows first-in, first-out semantics; stack
insertion and deletion is last-in, first-out.

How would you implement a queue given a library implementing stacks?"

HINT (from the textbook)
------------------------
"It is impossible to solve this problem with a single stack."

SOLUTION DEVELOPMENT (following the textbook)
---------------------------------------------
Straightforward approach: enqueue pushes onto one stack. The element to
dequeue is then at the BOTTOM of that stack. To reach it, pop every element
off and push it onto a second stack, pop the top of the second stack (it was
the bottom of the first), and then move all the remaining elements back onto
the first stack.

Drawback: every dequeue pushes and pops every element twice, so dequeue is
O(n) for n stored elements (enqueue is O(1)).

Improvement: once elements have been moved to the second stack they are in
dequeue order, so every following dequeue is a simple pop from the second
stack, until it runs empty. This still holds when enqueues happen in
between, as long as enqueues always go onto the first stack. When the second
stack is empty and a dequeue is requested, transfer everything from the
first stack to the second again. In short: the first stack serves enqueue
and the second serves dequeue.

The book's program is a class `Queue` with stacks `_enq` and `_deq`; this
file's `Queue` implements the same algorithm with stacks named `_incoming`
and `_outgoing`.

ADDITIONAL EXAMPLES (added for learning; not printed in this exercise)
---------------------------------------------------------------------
    queue_from_stacks([])        -> []
    queue_from_stacks([1])       -> [1]
    queue_from_stacks([1, 2, 3]) -> [1, 2, 3]   (first in, first out)
"""


class Queue:
    """FIFO queue implemented with two LIFO Python lists.

    Implements the textbook's two-stack `Queue` (pages 108–109).
    """

    # `-> None` is a return-type hint (constructors return None).
    def __init__(self) -> None:

        # Two Python lists used as stacks (append = push, pop = pop).
        # _incoming receives enqueued items; _outgoing holds items in the
        # order they will be dequeued (the oldest item on top).
        self._incoming = []
        self._outgoing = []

    def enqueue(self, item: int) -> None:
        self._incoming.append(item)

    def dequeue(self) -> int:

        # Only when the outgoing stack is empty (an empty list is falsy) are
        # the incoming items transferred. Popping from one stack and pushing
        # onto the other reverses their order, so the OLDEST item ends up on
        # top of _outgoing.
        if not self._outgoing:
            while self._incoming:
                self._outgoing.append(self._incoming.pop())

        # Still empty after the transfer: the whole queue is empty. Raise
        # IndexError, as list.pop() does on an empty list.
        if not self._outgoing:
            raise IndexError('dequeue from empty queue')
        return self._outgoing.pop()


def queue_from_stacks(values: list[int]) -> list[int]:
    """Demonstrate the FIFO sequence produced by the Queue class.

    Repository helper added for testing/learning; not in the textbook.
    """
    queue = Queue()
    for value in values:
        queue.enqueue(value)

    # A list comprehension calling dequeue() once per enqueued value; `_`
    # marks the loop variable as unused.
    return [queue.dequeue() for _ in values]


# TEXTBOOK POST-SOLUTION DISCUSSION (page 109)
# --------------------------------------------
# A sequence of m operations takes O(m) time in total, because each element
# is pushed at most twice and popped at most twice (once on each stack).
# So each operation is O(1) amortized.
#
# VARIANTS
# The textbook gives no variants for this exercise.


# TEXTBOOK CODE COMPARISON
# ------------------------
# Book: `class Queue` with `__init__(self)` doing the tuple assignment
# `self._enq, self._deq = [], []`; `enqueue(self, x)`; `dequeue(self)` with
# the comment "Transfers the elements in _enq to _deq." and "_deq is still
# empty!", raising IndexError('empty queue').
# File: same class name and algorithm; attributes renamed `_incoming` and
# `_outgoing` and assigned on separate lines; `enqueue(self, item: int) ->
# None`, `dequeue(self) -> int`, `__init__ -> None` hints added; the error
# message is 'dequeue from empty queue'.
# Helper not in the book: `queue_from_stacks`.


# Python executes this block only when this source file is run directly.
# When pytest imports the file, this block is skipped automatically.
# Documentation: https://docs.python.org/3/library/__main__.html
if __name__ == "__main__":

    # Demonstrations check representative input/output behavior: an empty
    # sequence, a single element, and several elements coming out in the
    # same order they went in.
    #
    # `assert` stops the program with an AssertionError if the condition is
    # false; these are quick smoke checks, pytest does the thorough testing.
    observed = queue_from_stacks([])
    print("queue_from_stacks:", observed)
    assert observed == []
    observed = queue_from_stacks([1])
    print("queue_from_stacks:", observed)
    assert observed == [1]
    observed = queue_from_stacks([1, 2, 3])
    print("queue_from_stacks:", observed)
    assert observed == [1, 2, 3]
