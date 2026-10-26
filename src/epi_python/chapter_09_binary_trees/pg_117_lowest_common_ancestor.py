"""EPI exercise 9.3, printed page 117: Compute the lowest common ancestor in a binary tree.

EDUCATIONAL RECONSTRUCTION — not a verbatim verified code transcription.
Problem: Compute the lowest common ancestor in a binary tree.
Method/complexity: Bottom-up recursion with found-count; O(n) time and O(h) recursion space.
For the book's original explanation and variants, see:
    pg_117_exercise_09_03_compute_the_lowest_common_ancestor_in_a_binary_tree.md

Run: python -m epi_python.chapter_09_binary_trees.pg_117_lowest_common_ancestor
Test: python -m pytest tests/chapter_09_binary_trees/test_pg_117_lowest_common_ancestor.py -v
"""

# Reuse a simple dataclass-backed binary tree node for linked-node algorithms.
from epi_python.chapter_09_binary_trees.pg_114_is_balanced_binary_tree import TreeNode


def build_tree(tree: tuple | None) -> TreeNode | None:
    """Turn nested (value, left, right) tuples into binary tree nodes."""
    if tree is None:
        return None
    return TreeNode(tree[0], build_tree(tree[1]), build_tree(tree[2]))


def nested_tree(root: TreeNode | None):
    return None if root is None else (root.data, nested_tree(root.left), nested_tree(root.right))


def lowest_common_ancestor(root: TreeNode | None, a: int, b: int) -> TreeNode | None:
    """Find lowest node whose subtree contains two distinct target keys."""
    def descend(node):
        if node is None:
            return 0, None
        left_count, left_match = descend(node.left)
        if left_count == 2:
            return left_count, left_match
        right_count, right_match = descend(node.right)
        if right_count == 2:
            return right_count, right_match
        found = left_count + right_count + (node.data in (a, b))
        return (found, node if found == 2 else None)
    return descend(root)[1]


def lca_value(tree: tuple | None, a: int, b: int) -> int | None:
    match = lowest_common_ancestor(build_tree(tree), a, b)
    return None if match is None else match.data


if __name__ == "__main__":
    tree = (4,(2,(1,None,None),(3,None,None)),(6,None,None))
    print("LCA(1,3):", lca_value(tree, 1, 3))
    assert lca_value(tree,1,3) == 2
