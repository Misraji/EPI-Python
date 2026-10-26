"""EPI Python — Exercise 24.14: Compute Fair Bonuses

Chapter 24: Honors Class
Textbook: pages 368–370 (printed page numbers; problem starts on 368,
statement, hint and solution development on 369, both programs end on 370).

PROBLEM (from the textbook)
---------------------------
You manage a team of developers. You have to give concert tickets as a
bonus to the developers. For each developer, you know how many lines of
code he wrote the previous week, and you want to reward more productive
developers. (Footnote: In practice, lines-of-code is a very poor
productivity metric.)

The developers sit in a row. Each developer, save for the first and last,
has two neighbors. You must give each developer one or more tickets in such
a way that if a developer has written more lines of code than a neighbor,
then he receives more tickets than his neighbor. (If two neighboring
developers have written an equal number of lines of code, they do not have
to receive the same number of tickets.)

For example, if Andy, Bob, Charlie, and David sit in a row from left to
right, and they wrote 300, 400, 200, and 500 lines of code, respectively,
the previous week, then Andy and Charlie should receive one ticket each,
and Bob and David should receive two tickets, for a total of six tickets.
If instead they wrote 300, 400, 400, and 400 lines of code, respectively,
then Andy, Charlie, and David should receive a single ticket, and Bob
should receive two tickets for a total of five tickets.

Your task is to develop an algorithm that computes the minimum number of
tickets you need to buy to satisfy the constraint.

Write a program for computing the minimum number of tickets to distribute
to the developers, while ensuring that if a developer has written more
lines of code than a neighbor, then he receives more tickets than his
neighbor.

HINT (from the textbook)
------------------------
Consider iteratively improving an assignment that may not satisfy the
constraint.

SOLUTION DEVELOPMENT (following the textbook)
---------------------------------------------
Brute force: give everyone one ticket, then iterate. If every developer is
satisfied, stop. Otherwise, for a developer who wrote more code than a
neighbor but does not have more tickets, give him one more ticket than that
neighbor. The starting assignment is minimal and every added ticket is
necessary. Time is O(kn^2), where k is the most tickets given to any one
developer and n is the number of developers.

Key insight: the least productive developer never needs more than one
ticket. Extend this by processing developers in increasing order of
productivity. When a developer is processed, any already-processed
neighbor is no more productive than he is. If he is more productive than a
neighbor, he must get at least one more ticket than that neighbor; if he is
only as productive as his neighbors, he can get the same number of tickets,
per the problem statement.

Worked walk-through as printed: the algorithm first gives 1 ticket to
David. Andy is next in productivity order and gets 1 ticket, since his only
neighbor is more productive. Next Bob, more productive than Andy, gets
1 + 1 = 2 tickets. Then Charlie, a neighbor of Charlie and David and more
productive than both, gets max(2, 1) + 1 = 3 tickets, for a total of 7.
[NEEDS PDF REVIEW: page 369 — this walk-through does not match either
example printed in the problem (it says Charlie is "a neighbor of Charlie
and David", and the total 7 differs from 6 and 5); transcribed as printed.]

Why it is correct: once a developer is processed, all later developers are
at least as productive, so his bonus never needs to change; and every
ticket assigned is forced by the constraints.

A min-heap is a suitable structure for taking developers in increasing
order of productivity; this is the book's first program,
`calculate_bonus` (here `calculate_bonus_heap`).

After its analysis the book improves this to O(n) — see the discussion
below; that two-pass program is the book's second `calculate_bonus`, and
this file's `calculate_bonus`.

ADDITIONAL EXAMPLES (added for learning; not printed in this exercise)
---------------------------------------------------------------------
    productivity=[1, 2, 2, 1] -> 6 tickets (1, 2, 2, 1)
"""

# Python standard library: heap queue (priority queue) algorithms.
# Module documentation: https://docs.python.org/3/library/heapq.html
# heapify API: https://docs.python.org/3/library/heapq.html#heapq.heapify
# heappop API: https://docs.python.org/3/library/heapq.html#heapq.heappop
import heapq


def calculate_bonus(productivity: list[int]) -> int:
    """Textbook solution 2: two linear passes, O(n) time.

    Type hints (`list[int]`, `-> int`) are documentation; Python does not
    enforce them.
    """

    # Initially assigns one ticket to everyone. `[1] * n` builds a list of
    # n ones (safe because ints are immutable).
    tickets=[1]*len(productivity)

    # From left to right: beat the left neighbor when more productive.
    for i in range(1,len(productivity)):
        if productivity[i]>productivity[i-1]:
            tickets[i]=tickets[i-1]+1

    # From right to left: reversed(range(n - 1)) yields n-2, ..., 1, 0.
    # https://docs.python.org/3/library/functions.html#reversed
    # max(...) keeps whatever the left-to-right pass already required while
    # also beating the right neighbor; counts only ever increase.
    for i in reversed(range(len(productivity)-1)):
        if productivity[i]>productivity[i+1]:
            tickets[i]=max(tickets[i],tickets[i+1]+1)

    # sum(iterable) adds all items: the total number of tickets.
    return sum(tickets)


def calculate_bonus_heap(productivity: list[int]) -> int:
    """Textbook solution 1: process developers from least productive with a min-heap.

    O(n log n) time.
    """

    # Initially assigns one ticket to everyone.
    tickets=[1]*len(productivity)

    # Stores (productivity, index) pairs in a min-heap ordered by
    # productivity. Tuples compare element by element, so ties in
    # productivity are broken by the smaller index.
    # The list comprehension with enumerate builds one pair per developer.
    heap=[(p,i) for i,p in enumerate(productivity)]

    # heapq.heapify(list) rearranges the list in place, in O(n) time, so
    # that heap[0] is always the smallest item (a binary min-heap stored in a
    # plain list). heapq has no separate heap class; the functions operate
    # on ordinary lists.
    heapq.heapify(heap)

    # Fills tickets from lowest rating to highest rating.
    while heap:

        # heapq.heappop(heap) removes and returns the smallest item in
        # O(log n), keeping the heap property. We unpack the pair and ignore
        # the productivity value: `_` is a conventional name for a value we
        # do not use.
        _,i=heapq.heappop(heap)

        # Handles the left neighbor (`and` short-circuits, so i-1 is only
        # used when i > 0).
        if i>0 and productivity[i]>productivity[i-1]:
            tickets[i]=max(tickets[i],tickets[i-1]+1)

        # Handles the right neighbor.
        if i+1<len(productivity) and productivity[i]>productivity[i+1]:
            tickets[i]=max(tickets[i],tickets[i+1]+1)
    return sum(tickets)


# TEXTBOOK POST-SOLUTION DISCUSSION (page 370)
# --------------------------------------------
# Heap solution: each extraction from a min-heap is O(log n), so the total
# time is O(n log n).
#
# This approach is still in the spirit of brute force: a total ordering of
# the developers is overkill, because the constraint is very local. Two
# passes over the array give O(n) time:
#   * give everyone one ticket;
#   * left-to-right pass: a developer more productive than his left neighbor
#     gets one more ticket than that neighbor;
#   * the same in a right-to-left pass.
# Every ticket added is required, so no smaller total is possible. Every
# developer more productive than his right neighbor ends with more tickets
# than that neighbor; and one more productive than his left neighbor already
# had more tickets after the first pass, and the second pass can only
# increase his count.
#
# VARIANTS
# The book gives no variants for this exercise.


# TEXTBOOK CODE COMPARISON
# ------------------------
# Heap solution — book: `def calculate_bonus(productivity)`, building
#   `EmployeeData = collections.namedtuple('EmployeeData', ('productivity',
#   'index'))` and `min_heap = [EmployeeData(p, i) ...]`; popped with
#   `next_dev = heapq.heappop(min_heap)[1]`; the left-neighbor case assigns
#   `tickets[next_dev] = tickets[next_dev - 1] + 1` (no max); the right case
#   uses max.
#   file: renamed `calculate_bonus_heap(productivity: list[int]) -> int`;
#   plain `(p, i)` tuples instead of the namedtuple (no collections import);
#   heap named `heap`, index unpacked as `_, i`; the left-neighbor case also
#   uses `max(tickets[i], tickets[i-1] + 1)`. Same results.
# Two-pass solution — book: `def calculate_bonus(productivity)` with the
#   same two loops. file: same name, type hints added; matches the book's
#   listing otherwise.


# Python executes this block only when this source file is run directly.
# When pytest imports the file, this block is skipped automatically.
# Documentation: https://docs.python.org/3/library/__main__.html
if __name__=='__main__':

    # Both implementations on [1, 2, 2, 1]: the middle developers each beat
    # one neighbor and tie with each other, giving tickets 1, 2, 2, 1 = 6.
    # `fn.__name__` is the function's name, used to label the output.
    # `assert` raises AssertionError on mismatch; the tests/ folder holds
    # the thorough pytest suite.
    for fn in (calculate_bonus,calculate_bonus_heap):
        print(fn.__name__,fn([1,2,2,1]))
        assert fn([1,2,2,1])==6
