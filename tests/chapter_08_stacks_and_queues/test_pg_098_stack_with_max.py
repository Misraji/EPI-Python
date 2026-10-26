"""Independent tests for EPI 8.1.

pytest parameterization: https://docs.pytest.org/en/stable/how-to/parametrize.html
"""

# pytest enables one test function to run over several examples.
# Documentation: https://docs.pytest.org/en/stable/
import pytest

# Standard library: copies mutable inputs so tests do not share state.
# Documentation: https://docs.python.org/3/library/copy.html
import copy

from epi_python.chapter_08_stacks_and_queues.pg_098_stack_with_max import stack_max_history

@pytest.mark.parametrize(("args", "expected"), [
    (([1,3,2,5,4],), [1,3,3,5,5]),
    (([], ), []),
    (([-3,-1,-2],), [-3,-1,-1]),
])
def test_examples(args, expected):
    """Verify representative and boundary conditions independently."""
    assert stack_max_history(*copy.deepcopy(args)) == expected

from epi_python.chapter_08_stacks_and_queues.pg_098_stack_with_max import Stack


def test_max_after_popping_duplicate():
    stack = Stack()
    for x in (3, 5, 5, 1):
        stack.push(x)
    assert stack.pop() == 1 and stack.max() == 5
    assert stack.pop() == 5 and stack.max() == 5
    assert stack.pop() == 5 and stack.max() == 3
