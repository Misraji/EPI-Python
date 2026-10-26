"""Unit tests for EPI exercise 8.3."""

# pytest parametrization documentation:
# https://docs.pytest.org/en/stable/how-to/parametrize.html
import pytest

from epi_python.chapter_08_stacks_and_queues.pg_102_is_well_formed import is_well_formed


@pytest.mark.parametrize(("arguments", "expected"), [(('',), True), (('()[]{}',), True), (('([{}])',), True), (('([)]',), False), (('(',), False)])
def test_cases(arguments, expected):
    assert is_well_formed(*arguments) == expected
