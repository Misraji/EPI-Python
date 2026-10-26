"""EPI Python — Exercise 17.1: Compute an Optimum Assignment of Tasks

Chapter 17: Greedy Algorithms and Invariants
Textbook: pages 260–261 (printed page numbers; problem and solution start
on 260, program and complexity on 261).

PROBLEM (from the textbook)
---------------------------
We consider the problem of assigning tasks to workers. Each worker must be
assigned exactly two tasks. Each task takes a fixed amount of time. Tasks
are independent, i.e., there are no constraints of the form "Task 4 cannot
start before Task 3 is completed." Any task can be assigned to any worker.

We want to assign tasks to workers so as to minimize how long it takes
before all tasks are completed. For example, if there are 6 tasks whose
durations are 5, 2, 1, 6, 4, 4 hours, then an optimum assignment is to give
the first two tasks (i.e., the tasks with duration 5 and 2) to one worker,
the next two (1 and 6) to another worker, and the last two tasks (4 and 4)
to the last worker. For this assignment, all tasks will finish after
max(5 + 2, 1 + 6, 4 + 4) = 8 hours.

Design an algorithm that takes as input a set of tasks and returns an
optimum assignment.

HINT (from the textbook)
------------------------
What additional task should be assigned to the worker who is assigned the
longest task?

SOLUTION DEVELOPMENT (following the textbook)
---------------------------------------------
Brute force: list every way of splitting the tasks into pairs and keep the
best. This is infeasible because there are far too many pairings. The book
gives the exact count as the product C(n,2) * C(n-2,2) * ... * C(4,2) *
C(2,2), which equals n! / 2^(n/2), where n is the number of tasks.

Instead, study the structure of the problem. Extreme values matter: the
longest task "needs the most help", so it is natural to pair the longest
task with the shortest one. To see why, take any assignment in which a
longest task is NOT paired with a shortest task. Swap the partner of the
longest task with the shortest task; the resulting assignment is at least
as good as the original (an exchange argument).

The book warns against a tempting misreading: the optimum completion time
is NOT necessarily (longest + shortest). If the two longest tasks are close
in length and the shortest task is much shorter than the second shortest,
another pair dominates. Book example: durations 1, 8, 9, 10 give pairs
(1, 10) and (8, 9), so the optimum delay is 8 + 9 = 17, not 1 + 10 = 11.

Summary of the algorithm:

1. Sort the task durations.
2. Pair the shortest with the longest, the second shortest with the second
   longest, the third shortest with the third longest, and so on.

Book worked example: 5, 2, 1, 6, 4, 4 sorts to 1, 2, 4, 4, 5, 6, giving the
pairs (1, 6), (2, 5) and (4, 4).

The function optimum_task_assignment below is the textbook's single
implementation; it returns a list of PairedTasks named tuples.
"""

# Python standard library: specialized container types.
# Module documentation: https://docs.python.org/3/library/collections.html
# namedtuple API: https://docs.python.org/3/library/collections.html#collections.namedtuple
import collections


# collections.namedtuple(typename, field_names) creates a NEW CLASS: a
# subclass of tuple whose positions also have names. Here PairedTasks(a, b)
# is still an ordinary 2-tuple (it can be indexed, unpacked, compared), but
# you may also write pair.task_1 and pair.task_2, which makes the returned
# assignment self-describing. Instances are immutable like plain tuples.
# The first argument 'PairedTasks' is the class name shown by repr(), e.g.
# PairedTasks(task_1=1, task_2=6).
PairedTasks = collections.namedtuple('PairedTasks', ('task_1','task_2'))


# The annotations `list[int]` and `-> list[PairedTasks]` are type hints:
# they document that the argument is a list of ints and the result is a list
# of PairedTasks. Python stores them but does NOT enforce them at run time.
# (Built-in generic syntax such as list[int] needs Python 3.9 or newer.)
def optimum_task_assignment(task_durations: list[int]) -> list[PairedTasks]:
    """Pair shortest with longest task (the textbook's implementation).

    As in the textbook, the input list is sorted IN PLACE, so the caller's
    list order is changed. Assumes an even number of tasks.
    """

    # list.sort() sorts the list in place in ascending order and returns
    # None (unlike sorted(), which builds a new list). Sorting puts the
    # shortest tasks at the front and the longest at the back, which is
    # what the greedy pairing needs. This step costs O(n log n).
    task_durations.sort()

    # This is a list comprehension that builds one PairedTasks per worker.
    #
    # `~i` is Python's bitwise NOT. For integers, ~i equals -i - 1, so
    # ~0 == -1, ~1 == -2, ~2 == -3, ... Used as an index, task_durations[~i]
    # is therefore the i-th element counted from the END of the list
    # (the largest, the second largest, ...). This neatly mirrors
    # task_durations[i], the i-th smallest.
    #
    # `//` is floor division, so range(len(...) // 2) visits the first half
    # of the indices, producing exactly n/2 pairs for n tasks. With an odd
    # number of tasks the middle task would simply be left out.
    return [PairedTasks(task_durations[i], task_durations[~i])
            for i in range(len(task_durations)//2)]


# TEXTBOOK POST-SOLUTION DISCUSSION (page 261)
# --------------------------------------------
# The running time is dominated by sorting the task durations, so the time
# complexity is O(n log n). (The pairing pass itself is O(n).)
#
# VARIANTS
# --------
# The book states no variants for this exercise.


# TEXTBOOK CODE COMPARISON
# ------------------------
# - PairedTasks: identical to the book's namedtuple definition.
# - Book: `def optimum_task_assignment(task_durations):` with no type hints.
#   File: same name and parameter name, with added hints
#   `task_durations: list[int]` and return type `list[PairedTasks]`.
# - Body: same algorithm (in-place sort, then a list comprehension pairing
#   task_durations[i] with task_durations[~i]); the file writes the
#   comprehension on two lines instead of the book's bracketed layout and
#   omits spaces around `//`. No functional difference.
# - The book's "Greedy algorithms boot camp" function change_making (page
#   260) is not part of this file.


# Python executes this block only when this source file is run directly.
# When pytest imports the file, this block is skipped automatically.
# Documentation: https://docs.python.org/3/library/__main__.html
if __name__ == '__main__':

    # The textbook's example: durations 5, 2, 1, 6, 4, 4 hours. The optimum
    # pairing is (1, 6), (2, 5), (4, 4), and the latest finish time is 8.
    assignments=optimum_task_assignment([5,2,1,6,4,4])
    print('Optimal pairing:',assignments)

    # max(...) here receives a generator expression: it computes each
    # worker's total (a.task_1 + a.task_2) on the fly and returns the
    # largest, i.e. the time when all tasks are complete.
    #
    # `assert` stops the program with an AssertionError if the condition is
    # False. It is a quick smoke check; pytest provides thorough testing.
    assert max(a.task_1+a.task_2 for a in assignments)==8
