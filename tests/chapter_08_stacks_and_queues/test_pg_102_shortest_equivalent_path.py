"""Unit tests for EPI exercise 8.4."""

# pytest parametrization documentation:
# https://docs.pytest.org/en/stable/how-to/parametrize.html
import pytest

from epi_python.chapter_08_stacks_and_queues.pg_102_shortest_equivalent_path import shortest_equivalent_path


@pytest.mark.parametrize(("arguments", "expected"), [(('/usr/./bin/../lib',), '/usr/lib'), (('a/b/../c',), 'a/c'), (('/',), '/'), (('a/./b',), 'a/b')])
def test_cases(arguments, expected):
    assert shortest_equivalent_path(*arguments) == expected
