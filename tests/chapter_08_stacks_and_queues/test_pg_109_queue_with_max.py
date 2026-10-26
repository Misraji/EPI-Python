"""Independent tests for EPI 8.9.

pytest parameterization: https://docs.pytest.org/en/stable/how-to/parametrize.html
"""

# pytest enables one test function to run over several examples.
# Documentation: https://docs.pytest.org/en/stable/
import pytest

# Standard library: copies mutable inputs so tests do not share state.
# Documentation: https://docs.python.org/3/library/copy.html
import copy

from epi_python.chapter_08_stacks_and_queues.pg_109_queue_with_max import queue_max_history

@pytest.mark.parametrize(("args", "expected"), [
    (([1,2,3,2],), [1,2,3,3]),
    (([], ), []),
    (([4,1,4],), [4,4,4]),
])
def test_examples(args, expected):
    """Verify representative and boundary conditions independently."""
    assert queue_max_history(*copy.deepcopy(args)) == expected

from epi_python.chapter_08_stacks_and_queues.pg_109_queue_with_max import QueueWithMax


def test_max_after_dequeues():
    q = QueueWithMax()
    for x in [4, 1, 4, 3, 2]:
        q.enqueue(x)
    assert q.max() == 4
    q.dequeue()
    assert q.max() == 4
    q.dequeue()
    q.dequeue()
    assert q.max() == 3
