"""Unit tests for EPI exercise 8.8."""

# pytest parametrization documentation:
# https://docs.pytest.org/en/stable/how-to/parametrize.html
import pytest

from epi_python.chapter_08_stacks_and_queues.pg_108_queue_from_stacks import queue_from_stacks


@pytest.mark.parametrize(("arguments", "expected"), [(([],), []), (([1],), [1]), (([1, 2, 3],), [1, 2, 3])])
def test_cases(arguments, expected):
    assert queue_from_stacks(*arguments) == expected
