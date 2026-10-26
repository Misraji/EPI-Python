"""Parameterized checks of EPI 7.3 educational solution."""

# pytest API: https://docs.pytest.org/en/stable/how-to/parametrize.html
import pytest

from epi_python.chapter_07_linked_lists.pg_086_has_cycle import has_cycle


@pytest.mark.parametrize(("arguments", "expected"), [(([],), False), (([1, 2, 3],), False), (([1, 2, 3], 0), True), (([1, 2, 3], 2), True)])
def test_examples(arguments, expected):
    assert has_cycle(*arguments) == expected
