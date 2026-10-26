"""Parameterized checks of EPI 18.4 educational solution."""

# pytest API: https://docs.pytest.org/en/stable/how-to/parametrize.html
import pytest

from epi_python.chapter_18_graphs.pg_281_is_deadlocked import is_deadlocked


@pytest.mark.parametrize(("arguments", "expected"), [(([],), False), (([[1], [2], []],), False), (([[1], [2], [0]],), True), (([[0]],), True)])
def test_examples(arguments, expected):
    assert is_deadlocked(*arguments) == expected
