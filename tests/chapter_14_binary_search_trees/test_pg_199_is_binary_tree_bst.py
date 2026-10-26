"""Parameterized checks of EPI 14.1 educational solution."""

# pytest API: https://docs.pytest.org/en/stable/how-to/parametrize.html
import pytest

from epi_python.chapter_14_binary_search_trees.pg_199_is_binary_tree_bst import is_binary_tree_bst


@pytest.mark.parametrize(("arguments", "expected"), [((None,), True), (((2, (1, None, None), (3, None, None)),), True), (((2, (3, None, None), (1, None, None)),), False), (((10, (5, None, (12, None, None)), (15, None, None)),), False)])
def test_examples(arguments, expected):
    assert is_binary_tree_bst(*arguments) == expected


def test_pdf_breadth_first_alternative_against_recursive_bounds():
    """Verify both PDF implementations over balanced and invalid trees."""
    from epi_python.chapter_14_binary_search_trees.pg_199_is_binary_tree_bst import (
        TreeNode,
        is_bst_nodes,
        is_bst_nodes_bfs,
    )

    roots = (
        None,
        TreeNode(3, TreeNode(1), TreeNode(5)),
        TreeNode(3, TreeNode(4), TreeNode(5)),
        TreeNode(10, TreeNode(5, right=TreeNode(12)), TreeNode(15)),
        TreeNode(4, TreeNode(4), TreeNode(4)),
    )
    for root in roots:
        assert is_bst_nodes_bfs(root) is is_bst_nodes(root)


def test_pdf_breadth_first_alternative_randomized():
    import random

    from epi_python.chapter_14_binary_search_trees.pg_199_is_binary_tree_bst import (
        TreeNode, is_bst_nodes, is_bst_nodes_bfs,
    )

    generator = random.Random(194199)
    for _ in range(200):
        nodes = [TreeNode(generator.randrange(-20, 21)) for _ in range(15)]
        for i, node in enumerate(nodes):
            left, right = i * 2 + 1, i * 2 + 2
            node.left = nodes[left] if left < len(nodes) else None
            node.right = nodes[right] if right < len(nodes) else None
        assert is_bst_nodes_bfs(nodes[0]) is is_bst_nodes(nodes[0])
