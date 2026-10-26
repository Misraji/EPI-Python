"""EPI Python — Exercise 17.3: The Interval Covering Problem

Chapter 17: Greedy Algorithms and Invariants
Textbook: pages 262–263 (printed page numbers; problem and solution start
on 262, program, complexity and variants on 263).

PROBLEM (from the textbook)
---------------------------
Consider a foreman responsible for a number of tasks on the factory floor.
Each task starts at a fixed time and ends at a fixed time. The foreman wants
to visit the floor to check on the tasks. Your job is to help him minimize
the number of visits he makes. In each visit, he can check on all the tasks
taking place at the time of the visit. A visit takes place at a fixed time,
and he can only check on tasks taking place at exactly that time. For
example, if there are tasks at times [0, 3], [2, 6], [3, 4], [6, 9], then
visit times 0, 2, 3, 6 cover all tasks. A smaller set of visit times that
also cover all tasks is 3, 6. In the abstract, you are to solve the
following problem.

You are given a set of closed intervals. Design an efficient algorithm for
finding a minimum sized set of numbers that covers all the intervals.

HINT (from the textbook)
------------------------
Think about extremal points.

SOLUTION DEVELOPMENT (following the textbook)
---------------------------------------------
Only interval endpoints need to be considered as visit times; restricting
attention to them loses no optimality.

Brute force: enumerate every subset of the endpoints, check whether it
covers every interval, and remember the smallest covering subset. A set of
k endpoints has 2^k subsets, so this is very expensive.

Two plausible greedy ideas fail:
  - Return the left endpoint of every interval. Fast, but as the problem's
    own example shows, it may use more visits than necessary.
  - Repeatedly pick the endpoint lying in the most intervals. Book
    counterexample: [1, 2], [2, 3], [3, 4], [2, 3], [3, 4], [4, 5]. Point 3
    is in four intervals, more than any other point, but choosing it leaves
    [1, 2] and [4, 5] uncovered, so two more points are needed (3 total).
    Choosing 2 and 4 instead covers three intervals each and all six
    together.

The insight is to focus on an extreme case: the interval that ENDS first
(minimum right endpoint). Some chosen number must lie in it, and the best
choice is its right endpoint: any other interval covered by some point of
this first-ending interval is also covered by its right endpoint (otherwise
our interval would not be the one that ends first). After choosing that
point, drop every interval it covers and repeat on the rest.

Resulting algorithm:

1. Sort the intervals by right endpoint.
2. Select the first interval's right endpoint.
3. Scan forward for the first interval NOT covered by the selected point;
   when found, select its right endpoint and continue scanning.

Book worked example: [1, 2], [2, 3], [3, 4], [2, 3], [3, 4], [4, 5] sorted
on right endpoints is [1, 2], [2, 3], [2, 3], [3, 4], [3, 4], [4, 5]. The
leftmost right endpoint 2 covers [1, 2], [2, 3], [2, 3]. Reaching [3, 4],
we select 4, which covers [3, 4], [3, 4], [4, 5]. No intervals remain, so
{2, 4} is a minimum covering set.

find_minimum_visits below is the textbook's single implementation; it
returns the NUMBER of visits (not the visit times themselves).

ADDITIONAL EXAMPLES (added for learning; not printed in this exercise)
---------------------------------------------------------------------
The __main__ block reuses the intervals from the problem statement,
[0, 3], [2, 6], [3, 4], [6, 9], and checks that 2 visits suffice. (The
greedy actually selects times 3 and 9 — a different, equally small set
than the book's 3, 6.)
"""

# Python standard library: specialized container types.
# Module documentation: https://docs.python.org/3/library/collections.html
# namedtuple API: https://docs.python.org/3/library/collections.html#collections.namedtuple
from collections import namedtuple

# Python standard library: functions corresponding to Python operators.
# Module documentation: https://docs.python.org/3/library/operator.html
# attrgetter API: https://docs.python.org/3/library/operator.html#operator.attrgetter
from operator import attrgetter


# namedtuple('Interval', ('left', 'right')) creates a new class: a tuple
# subclass whose two positions can also be read as .left and .right.
# Interval(2, 6) is still an immutable 2-tuple, but interval.left reads far
# more clearly in the algorithm than interval[0].
Interval = namedtuple('Interval',('left','right'))


# Type hints: `list[Interval]` documents a list of Interval tuples and
# `-> int` the result type. Python does not enforce annotations at run time.
def find_minimum_visits(intervals: list[Interval]) -> int:
    """Count the minimum visits needed (the textbook's implementation).

    Sorts the caller's list in place by right endpoint.
    """

    # The book's comment: sort intervals based on the right endpoints.
    #
    # list.sort(key=f) sorts in place, comparing f(item) instead of the item
    # itself. operator.attrgetter('right') returns a function equivalent to
    # `lambda obj: obj.right`, so the intervals are ordered by right
    # endpoint — exactly the "ends first" order the greedy needs. Python's
    # sort is stable: intervals with equal right endpoints keep their
    # original relative order (which does not matter here).
    intervals.sort(key=attrgetter('right'))

    # Tuple unpacking assigns two variables in one statement.
    # float('-inf') is negative infinity: it compares less than every
    # number, so the first interval's left endpoint is always "greater"
    # and the first interval always triggers a visit.
    last_visit_time, num_visits = float('-inf'), 0
    for interval in intervals:

        # Closed intervals: the last visit covers this interval iff
        # left <= last_visit_time (its right end is >= last_visit_time
        # because of the sort). If left is larger, the book notes that the
        # current right endpoint, last_visit_time, will not cover any more
        # intervals, so a new visit at this interval's right endpoint is made.
        if interval.left > last_visit_time:
            last_visit_time = interval.right
            num_visits += 1
    return num_visits


# TEXTBOOK POST-SOLUTION DISCUSSION (page 263)
# --------------------------------------------
# After the initial sort, each interval is processed in O(1) time, so the
# scan is O(n), where n is the number of intervals. The total time is
# therefore dominated by the sort: O(n log n).
#
# VARIANTS
# --------
# Variant 1 (stated in the book; no solution given): You are responsible
# for the security of a castle with a circular perimeter. A total of n
# robots patrol the perimeter; each robot is responsible for a closed
# connected subset of the perimeter, i.e., an arc (arcs for different
# robots may overlap). You want to monitor the robots by installing cameras
# at the center of the castle that look out to the perimeter, each camera
# looking along a ray. Minimize the number of cameras. (Book Figure 17.1:
# an instance of this "minimum ray covering" problem with 12 partially
# overlapping arcs, drawn at different distances for illustration, where
# six cameras — six rays — suffice.)
#
# Variant 2 (stated in the book; no solution given): There are a number of
# points in the plane that you want to observe. You are located at the
# point (0, 0). You can rotate about this point, and your field-of-view is a
# fixed angle. Which direction should you face to maximize the number of
# visible points?


# TEXTBOOK CODE COMPARISON
# ------------------------
# - Imports: the book uses `collections.namedtuple` and
#   `operator.attrgetter` via module imports; the file uses
#   `from collections import namedtuple` and `from operator import
#   attrgetter`, so the calls are written without the module prefix.
# - Interval: same fields ('left', 'right').
# - Book: `def find_minimum_visits(intervals):`; file adds type hints
#   `intervals: list[Interval]` and `-> int`.
# - Body: identical logic; the book's two inline comments ("Sort intervals
#   based on the right endpoints" and "The current right endpoint,
#   last_visit_time, will not cover any more intervals") are paraphrased in
#   the file's comments rather than reproduced as code comments.


# Python executes this block only when this source file is run directly.
# When pytest imports the file, this block is skipped automatically.
# Documentation: https://docs.python.org/3/library/__main__.html
if __name__ == '__main__':

    # The intervals from the problem statement; the book says two visits
    # (e.g. times 3 and 6) are enough.
    intervals=[Interval(0,3),Interval(2,6),Interval(3,4),Interval(6,9)]
    print('Minimum visits:',find_minimum_visits(intervals))

    # `assert` raises AssertionError if the condition is False (a quick
    # smoke check; pytest does the thorough testing). Calling the function
    # a second time is safe: the list is already sorted.
    assert find_minimum_visits(intervals)==2
