"""Independent tests for EPI 8.7.

pytest parameterization: https://docs.pytest.org/en/stable/how-to/parametrize.html
"""

# pytest enables one test function to run over several examples.
# Documentation: https://docs.pytest.org/en/stable/
import pytest

# Standard library: copies mutable inputs so tests do not share state.
# Documentation: https://docs.python.org/3/library/copy.html
import copy

from epi_python.chapter_08_stacks_and_queues.pg_107_circular_queue import circular_queue_roundtrip

@pytest.mark.parametrize(("args", "expected"), [
    (([], ), []),
    (([1,2,3,4],), [1,2,3,4]),
    (([9],), [9]),
])
def test_examples(args, expected):
    """Verify representative and boundary conditions independently."""
    assert circular_queue_roundtrip(*copy.deepcopy(args)) == expected

from epi_python.chapter_08_stacks_and_queues.pg_107_circular_queue import CircularQueue


def test_wraparound_and_growth():
    queue = CircularQueue(2)
    queue.enqueue(1)
    queue.enqueue(2)
    assert queue.dequeue() == 1
    queue.enqueue(3)
    queue.enqueue(4)
    assert [queue.dequeue() for _ in range(3)] == [2,3,4]
