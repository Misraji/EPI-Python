"""Parameterized checks of EPI 9.7 educational solution."""

# pytest API: https://docs.pytest.org/en/stable/how-to/parametrize.html
import pytest

from epi_python.chapter_09_binary_trees.pg_121_inorder_traversal import inorder_traversal


@pytest.mark.parametrize(("arguments", "expected"), [((None,), []), (((1, None, None),), [1]), (((2, (1, None, None), (3, None, None)),), [1, 2, 3])])
def test_examples(arguments, expected):
    assert inorder_traversal(*arguments) == expected
