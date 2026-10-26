"""EPI Python — Exercise 13.5: Render a Calendar

Chapter 13: Sorting
Textbook: pages 186–188 (printed page numbers; problem and solution start on 186).

PROBLEM (from the textbook)
---------------------------
"Consider the problem of designing an online calendaring application. One
component of the design is to render the calendar, i.e., display it
visually."

"Suppose each day consists of a number of events, where an event is
specified as a start time and a finish time. Individual events for a day are
to be rendered as nonoverlapping rectangular regions whose sides are
parallel to the X- and Y-axes. Let the X-axis correspond to time. If an
event starts at time b and ends at time e, the upper and lower sides of its
corresponding rectangle must be at b and e, respectively. Figure 13.1 on the
facing page represents a set of events."

"Suppose the Y-coordinates for each day's events must lie between 0 and L
(a pre-specified constant), and each event's rectangle must have the same
"height" (distance between the sides parallel to the X-axis). Your task is
to compute the maximum height an event rectangle can have. In essence, this
is equivalent to the following problem."

"Write a program that takes a set of events, and determines the maximum
number of events that take place concurrently."

Figure 13.1 (page 187): "A set of nine events. The earliest starting event
begins at time 1; the latest ending event ends at time 17. The maximum
number of concurrent events is 3, e.g., {E1, E5, E8} as well as others."
(The figure draws events E1–E9 as closed intervals on a time axis 0–17.)

HINT (from the textbook)
------------------------
"Focus on endpoints."

SOLUTION DEVELOPMENT (following the textbook)
---------------------------------------------
Brute force: the number of events in progress changes only at an event's
start or end time. So for every endpoint, count how many events contain it;
the answer is the largest such count. With n intervals there are 2n
endpoints, and counting the events that contain one endpoint is O(n) (each
containment check is O(1)), giving O(2n x n) = O(n^2) time.

Improvement: the brute force ignores locality, i.e. what changes as we move
from one endpoint to the next. Sort all endpoints in ascending order of
time. When a start time and an end time are equal, the start comes first
(intervals are closed, so two events touching at one instant overlap); when
two starts or two ends are equal, ties are broken arbitrarily.

Then sweep the sorted endpoints, maintaining a counter of events in
progress: add 1 at each start, subtract 1 at each end. The maximum value the
counter reaches is the maximum number of overlapping intervals.

Worked example from the book (Figure 13.1): the first seven endpoints are
1(start), 2(start), 4(start), 5(end), 5(end), 6(start), 7(end), and the
counter takes the values 1, 2, 3, 2, 1, 2, 1.

The function below implements the book's single sorted-endpoint sweep.

ADDITIONAL EXAMPLES (added for learning; not printed in this exercise)
---------------------------------------------------------------------
    [Event(1,5), Event(2,7), Event(4,5), Event(8,9)] -> 3
        (at time 4 the first three events all overlap)
"""

# Python standard library: specialized container types.
# Module documentation: https://docs.python.org/3/library/collections.html
# namedtuple API: https://docs.python.org/3/library/collections.html#collections.namedtuple
from collections import namedtuple


# collections.namedtuple(typename, field_names) creates a new tuple
# subclass whose positions also have names. `Event(1, 5)` is still a tuple
# (1, 5), but its items can be read as `event.start` and `event.finish`,
# which makes the algorithm easier to read. Like tuples, instances are
# immutable.
# Documentation: https://docs.python.org/3/library/collections.html#collections.namedtuple
Event = namedtuple('Event', ('start', 'finish'))


# Type hints: `events: list[Event]` and `-> int` document the expected
# types; Python does not enforce annotations at run time.
def find_max_simultaneous_events(events: list[Event]) -> int:
    """Count overlapping *closed* time intervals; starts precede ties at ends.

    This is the textbook's implementation (sort endpoints, then sweep with
    a counter), using plain tuples instead of an Endpoint namedtuple.
    """
    endpoints = []
    for event in events:

        # Added input check (not in the book): `raise ValueError(...)` stops
        # with an exception for an event that ends before it starts.
        if event.start > event.finish:
            raise ValueError("start cannot be later than finish")

        # Each endpoint is a plain tuple (time, kind). kind 0 marks a start
        # and 1 marks an end, so that when times are equal the start sorts
        # first, which is the book's tie-breaking rule for closed intervals.
        endpoints.append((event.start, 0))  # 0 = start; sorts ahead of 1 = end.
        endpoints.append((event.finish, 1))

    # list.sort() sorts the list in place (O(n log n)). With no `key`, tuples
    # are compared lexicographically: first by time, then, for equal times,
    # by the 0/1 marker, so starts precede ends at the same time.
    # Documentation: https://docs.python.org/3/library/stdtypes.html#list.sort
    endpoints.sort()

    # Chained assignment: both counters start at 0.
    active = maximum = 0

    # Tuple unpacking in the loop header. `_` is a conventional name for a
    # value that is deliberately unused (here the time, which no longer
    # matters once the endpoints are in order).
    for _, endpoint_type in endpoints:

        # Conditional expression `X if condition else Y`: +1 for a start,
        # -1 for an end.
        # Documentation: https://docs.python.org/3/reference/expressions.html#conditional-expressions
        active += 1 if endpoint_type == 0 else -1

        # Built-in max() returns the larger of its arguments; this records
        # the highest number of simultaneous events seen so far.
        # Documentation: https://docs.python.org/3/library/functions.html#max
        maximum = max(maximum, active)
    return maximum


# TEXTBOOK POST-SOLUTION DISCUSSION (pages 187–188)
# -------------------------------------------------
# Sorting the endpoint array is O(n log n) and iterating over it is O(n), so
# the time complexity is O(n log n). Space is O(n), the size of the endpoint
# array.
#
# VARIANTS
# --------
# Variant (stated in the book; no solution given): Users 1, 2, ..., n share
# an Internet connection. User i uses b_i bandwidth from time s_i to f_i,
# inclusive. What is the peak bandwidth usage?


# TEXTBOOK CODE COMPARISON
# ------------------------
# - Book: `Event = collections.namedtuple('Event', ('start', 'finish'))`
#   (with `import collections`). File: same Event, but imported with
#   `from collections import namedtuple`.
# - Book also defines `Endpoint = collections.namedtuple('Endpoint',
#   ('time', 'is_start'))`; the file has no Endpoint type and uses plain
#   tuples `(time, 0)` for starts and `(time, 1)` for ends.
# - Book: `def find_max_simultaneous_events(A):` builds `E` with two list
#   comprehensions of Endpoint objects, sorts with
#   `E.sort(key=lambda e: (e.time, not e.is_start))`, and tracks
#   `max_num_simultaneous_events, num_simultaneous_events`, updating the
#   maximum only after a start. File: parameter `events: list[Event]` with
#   `-> int`, builds the list with a loop and `append`, adds a ValueError
#   check for start > finish, sorts with plain `endpoints.sort()` (the 0/1
#   marker gives the same tie order), and uses `active`/`maximum` with a
#   conditional expression, updating the maximum after every endpoint.
#   Results are the same.


# Python executes this block only when this source file is run directly.
# When pytest imports the file, this block is skipped automatically.
# Documentation: https://docs.python.org/3/library/__main__.html
if __name__ == "__main__":

    # An added example (not from the book): three events overlap at time 4.
    # Note Event(1, 5) and Event(4, 5) share the end time 5.
    sample = [Event(1, 5), Event(2, 7), Event(4, 5), Event(8, 9)]
    result = find_max_simultaneous_events(sample)
    print("Peak concurrent events:", result)

    # `assert` stops the program with an AssertionError if the condition is
    # false; a quick smoke check, with full tests in the tests/ folder.
    assert result == 3
