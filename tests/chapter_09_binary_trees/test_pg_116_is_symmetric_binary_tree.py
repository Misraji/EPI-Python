"""Parameterized checks of EPI 9.2 educational solution."""

# pytest API: https://docs.pytest.org/en/stable/how-to/parametrize.html
import pytest

from epi_python.chapter_09_binary_trees.pg_116_is_symmetric_binary_tree import is_symmetric_binary_tree


@pytest.mark.parametrize(("arguments", "expected"), [((None,), True), (((1, None, None),), True), (((1, (2, None, None), (2, None, None)),), True), (((1, (2, None, None), (3, None, None)),), False)])
def test_examples(arguments, expected):
    assert is_symmetric_binary_tree(*arguments) == expected
