"""EPI 13.5, printed page 186: Render a calendar.

Problem: Render a calendar. See pg_186_exercise_13_05_render_a_calendar.md for the full
original problem, hint, development, and variants from the PDF text layer.

Approach and complexity: O(n log n) time, O(n) endpoint storage; starts sort before finishes at equal times.

EDUCATIONAL RECONSTRUCTION: source and comments are not claimed verbatim.
Run directly: python -m epi_python.chapter_13_sorting.pg_186_find_max_simultaneous_events
Test: python -m pytest tests/chapter_13_sorting/test_pg_186_find_max_simultaneous_events.py -v
"""

# TEXTBOOK PROBLEM (exercise 13.5, printed page 186):
# Find the maximum number of simultaneous events in a calendar.
# HINT: Represent starts and finishes as sortable endpoints.

# namedtuple builds tuple-like objects with readable field names.
# Documentation: https://docs.python.org/3/library/collections.html#collections.namedtuple
from collections import namedtuple


Event = namedtuple('Event', ('start', 'finish'))


def find_max_simultaneous_events(events: list[Event]) -> int:
    """Count overlapping *closed* time intervals; starts precede ties at ends."""
    endpoints = []
    for event in events:
        if event.start > event.finish:
            raise ValueError("start cannot be later than finish")
        endpoints.append((event.start, 0))  # 0 = start; sorts ahead of 1 = end.
        endpoints.append((event.finish, 1))

    # sorted() compares tuples lexicographically: time, then start/end marker.
    # Documentation: https://docs.python.org/3/library/functions.html#sorted
    endpoints.sort()
    active = maximum = 0
    for _, endpoint_type in endpoints:
        active += 1 if endpoint_type == 0 else -1
        maximum = max(maximum, active)
    return maximum


if __name__ == "__main__":
    sample = [Event(1, 5), Event(2, 7), Event(4, 5), Event(8, 9)]
    result = find_max_simultaneous_events(sample)
    print("Peak concurrent events:", result)
    assert result == 3
