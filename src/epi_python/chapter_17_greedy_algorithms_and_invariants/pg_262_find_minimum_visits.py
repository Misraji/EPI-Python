"""EPI Python 17.3, textbook printed page 262: The interval covering problem.

QUESTION: Find the smallest set of time instants intersecting every closed interval.

TEXTBOOK ALGORITHM: Sort intervals by right endpoint, and visit only when the previous visit no longer covers the next interval.

The complete question, hints, solution development, and variants are in the
adjacent page-numbered reference Markdown, extracted from the supplied PDF.
This executable implementation restores syntax damaged by the PDF text layer;
minor type annotations, examples, and assertions are educational additions.

Run: python -m epi_python.chapter_17_greedy_algorithms_and_invariants.pg_262_find_minimum_visits
Test: python -m pytest tests/chapter_17_greedy_algorithms_and_invariants/test_pg_262_find_minimum_visits.py -v
"""

# collections.namedtuple documentation: https://docs.python.org/3/library/collections.html#collections.namedtuple
from collections import namedtuple

# operator.attrgetter documentation: https://docs.python.org/3/library/operator.html#operator.attrgetter
from operator import attrgetter


Interval = namedtuple('Interval',('left','right'))


def find_minimum_visits(intervals: list[Interval]) -> int:

    # attrgetter extracts an object's named field as the sort key.
    intervals.sort(key=attrgetter('right'))
    last_visit_time, num_visits = float('-inf'), 0
    for interval in intervals:
        if interval.left > last_visit_time:
            last_visit_time = interval.right
            num_visits += 1
    return num_visits


if __name__ == '__main__':
    intervals=[Interval(0,3),Interval(2,6),Interval(3,4),Interval(6,9)]
    print('Minimum visits:',find_minimum_visits(intervals))
    assert find_minimum_visits(intervals)==2
