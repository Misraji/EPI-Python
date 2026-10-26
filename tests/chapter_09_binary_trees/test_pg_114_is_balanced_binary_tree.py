"""Parameterized checks of EPI 9.1 educational solution."""

# pytest API: https://docs.pytest.org/en/stable/how-to/parametrize.html
import pytest

from epi_python.chapter_09_binary_trees.pg_114_is_balanced_binary_tree import is_balanced_binary_tree


@pytest.mark.parametrize(("arguments", "expected"), [((None,), True), (((1, None, None),), True), (((1, (2, (3, None, None), None), None),), False), (((1, (2, None, None), (3, None, None)),), True)])
def test_examples(arguments, expected):
    assert is_balanced_binary_tree(*arguments) == expected
