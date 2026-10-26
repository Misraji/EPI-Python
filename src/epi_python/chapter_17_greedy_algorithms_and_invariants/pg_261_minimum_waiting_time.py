"""EPI Python — Exercise 17.2: Schedule to Minimize Waiting Time

Chapter 17: Greedy Algorithms and Invariants
Textbook: pages 261–262 (printed page numbers; problem and solution start
on 261, program and complexity on 262).

PROBLEM (from the textbook)
---------------------------
A database has to respond to a set of client SQL queries. The service time
required for each query is known in advance. For this application, the
queries must be processed by the database one at a time, but can be done in
any order. The time a query waits before its turn comes is called its
waiting time.

Given service times for a set of queries, compute a schedule for processing
the queries that minimizes the total waiting time. Return the minimum
waiting time. For example, if the service times are <2, 5, 1, 3>, if we
schedule in the given order, the total waiting time is
0 + (2) + (2 + 5) + (2 + 5 + 1) = 17. If however, we schedule queries in
order of decreasing service times, the total waiting time is
0 + (5) + (5 + 3) + (5 + 3 + 2) = 23. As we will see, for this example, the
minimum waiting time is 10.

HINT (from the textbook)
------------------------
Focus on extreme values.

SOLUTION DEVELOPMENT (following the textbook)
---------------------------------------------
Brute force: try every possible schedule (every permutation of the
queries) and keep the best. With n queries there are n! schedules, so this
is O(n!) — far too slow.

Intuition: serve short queries first. Justification (an exchange
argument): each query's service time is added to the waiting time of every
query still waiting behind it. Suppose a slow query is scheduled before a
fast one. Swapping them:
  - improves the waiting time of every query lying between them (they now
    wait behind the fast query instead of the slow one);
  - leaves the waiting time of all other queries unchanged;
  - increases the slow query's waiting time, but by exactly as much as the
    fast query's waiting time decreases, so these two effects cancel.
So no schedule can beat processing the queries in order of nondecreasing
service time: sort the service times, then process them in that order.

Book worked example: for <2, 5, 1, 3>, the increasing order 1, 2, 3, 5 has
total waiting time 0 + (1) + (1 + 2) + (1 + 2 + 3) = 10. Processing longest
first (the 23 above) is in fact the worst approach.

The book's program is named minimum_total_waiting_time; this file's
function minimum_waiting_time implements the same sort-then-sum idea with a
different accumulation (see TEXTBOOK CODE COMPARISON below).

ADDITIONAL EXAMPLES (added for learning; not printed in this exercise)
---------------------------------------------------------------------
    []          -> 0  (no queries, nobody waits)
    [3]         -> 0  (a single query never waits)
    [2, 5, 1]   -> 4  (order 1, 2, 5: waits 0, 1, 3)
    [2, 2, 2]   -> 6  (waits 0, 2, 4)
    [3, 1, 2]   -> 4  and the list itself becomes [1, 2, 3]
"""


# The annotations `list[int]` and `-> int` are type hints: they document the
# expected argument and result types. Python does NOT check or enforce them
# at run time. (list[int] syntax requires Python 3.9 or newer.)
def minimum_waiting_time(service_times: list[int]) -> int:
    """Minimum total wait when one server handles jobs sequentially.

    Implements the textbook's sort-by-service-time solution (book name:
    minimum_total_waiting_time). Sorts the caller's list in place.
    """

    # list.sort() changes the caller's list in place and returns None.
    # The printed textbook explicitly sorts the supplied list directly.
    # Sorting into nondecreasing order is the whole greedy decision: short
    # queries go first. This step costs O(n log n).
    # Documentation: https://docs.python.org/3/tutorial/datastructures.html#more-on-lists
    service_times.sort()

    # `ordered` is just a second name for the SAME (now sorted) list; no
    # copy is made.
    ordered = service_times

    # elapsed: total service time of all queries already processed, i.e. how
    # long the NEXT query must wait.
    # waiting: running sum of the waiting times seen so far.
    elapsed=0
    waiting=0
    for duration in ordered:

        # The current query waits for everything processed before it; then
        # its own service time is added to what later queries must wait.
        waiting+=elapsed
        elapsed+=duration
    return waiting


# TEXTBOOK POST-SOLUTION DISCUSSION (page 262)
# --------------------------------------------
# The time complexity is dominated by the time to sort, i.e., O(n log n).
# (The summation pass after sorting is O(n).)
#
# VARIANTS
# --------
# The book states no variants for this exercise.


# TEXTBOOK CODE COMPARISON
# ------------------------
# - Name: book `def minimum_total_waiting_time(service_times):`; file
#   `def minimum_waiting_time(service_times: list[int]) -> int:` (function
#   renamed, type hints added; parameter name the same).
# - Both sort the input list in place (the book keeps its comment "Sort the
#   service times in increasing order.").
# - Accumulation differs: the book uses enumerate and adds
#   service_time * num_remaining_queries, where num_remaining_queries =
#   len(service_times) - (i + 1) (each service time delays every later
#   query). The file instead keeps a running `elapsed` prefix sum and adds
#   it to `waiting` before each query. Both compute the same total; the file
#   also introduces the alias `ordered`.


# Python executes this block only when this source file is run directly.
# When pytest imports the file, this block is skipped automatically.
# Documentation: https://docs.python.org/3/library/__main__.html
if __name__ == "__main__":

    # Demonstrations check representative input/output behavior: an empty
    # schedule, a single query, a small unsorted list and equal times.
    # (These are added examples; the book's own <2, 5, 1, 3> -> 10 is not
    # among them.)
    #
    # `assert` stops the program with an AssertionError if the condition is
    # False; these are quick smoke checks, pytest does the thorough testing.
    observed = minimum_waiting_time([])
    print("minimum_waiting_time:", observed)
    assert observed == 0
    observed = minimum_waiting_time([3])
    print("minimum_waiting_time:", observed)
    assert observed == 0
    observed = minimum_waiting_time([2, 5, 1])
    print("minimum_waiting_time:", observed)
    assert observed == 4
    observed = minimum_waiting_time([2, 2, 2])
    print("minimum_waiting_time:", observed)
    assert observed == 6

    # Show the side effect: the function sorts the caller's list in place,
    # so `tasks` itself is reordered after the call.
    tasks = [3, 1, 2]
    assert minimum_waiting_time(tasks) == 4
    assert tasks == [1, 2, 3]
    print("In-place schedule sorting: passed")
