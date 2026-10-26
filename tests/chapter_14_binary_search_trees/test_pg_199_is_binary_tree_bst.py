"""Parameterized checks of EPI 14.1 educational solution."""

# pytest API: https://docs.pytest.org/en/stable/how-to/parametrize.html
import pytest

from epi_python.chapter_14_binary_search_trees.pg_199_is_binary_tree_bst import is_binary_tree_bst


@pytest.mark.parametrize(("arguments", "expected"), [((None,), True), (((2, (1, None, None), (3, None, None)),), True), (((2, (3, None, None), (1, None, None)),), False), (((10, (5, None, (12, None, None)), (15, None, None)),), False)])
def test_examples(arguments, expected):
    assert is_binary_tree_bst(*arguments) == expected
