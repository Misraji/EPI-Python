"""Parameterized checks of EPI 7.2 educational solution."""

# pytest API: https://docs.pytest.org/en/stable/how-to/parametrize.html
import pytest

from epi_python.chapter_07_linked_lists.pg_085_reverse_sublist import reverse_sublist


@pytest.mark.parametrize(("arguments", "expected"), [(([1, 2, 3, 4], 2, 3), [1, 3, 2, 4]), (([1, 2, 3], 1, 3), [3, 2, 1]), (([1], 1, 1), [1])])
def test_examples(arguments, expected):
    assert reverse_sublist(*arguments) == expected
