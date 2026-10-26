"""EPI exercise 9.5, printed page 119: Sum the root-to-leaf paths in a binary tree.

EDUCATIONAL RECONSTRUCTION — not a verbatim verified code transcription.
Problem: Sum the root-to-leaf paths in a binary tree.
Method/complexity: DFS over binary digit path values; O(n) time, O(h) recursion space.
For the book's original explanation and variants, see:
    pg_119_exercise_09_05_sum_the_root_to_leaf_paths_in_a_binary_tree.md

Run: python -m epi_python.chapter_09_binary_trees.pg_119_sum_root_to_leaf_paths
Test: python -m pytest tests/chapter_09_binary_trees/test_pg_119_sum_root_to_leaf_paths.py -v
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


def sum_root_to_leaf(root: TreeNode | None, partial: int = 0) -> int:
    """Interpret each path of binary digits as a base-2 integer, sum paths."""
    if root is None:
        return 0
    if root.data not in (0, 1):
        raise ValueError("Binary paths require node values 0 or 1")
    partial = (partial << 1) | root.data
    if root.left is None and root.right is None:
        return partial
    return sum_root_to_leaf(root.left, partial) + sum_root_to_leaf(root.right, partial)


def sum_root_to_leaf_paths(tree) -> int:
    return sum_root_to_leaf(build_tree(tree))


if __name__ == "__main__":
    tree=(1,(0,None,None),(1,None,None))
    print("sum of binary paths:", sum_root_to_leaf_paths(tree))
    assert sum_root_to_leaf_paths(tree) == 5
