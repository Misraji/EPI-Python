"""EPI exercise 9.6, printed page 120: Find a root to leaf path with specified sum.

EDUCATIONAL RECONSTRUCTION — not a verbatim verified code transcription.
Problem: Find a root to leaf path with specified sum.
Method/complexity: Short-circuit DFS, O(n) time worst case and O(h) stack space.
For the book's original explanation and variants, see:
    pg_120_exercise_09_06_find_a_root_to_leaf_path_with_specified_sum.md

Run: python -m epi_python.chapter_09_binary_trees.pg_120_has_path_sum
Test: python -m pytest tests/chapter_09_binary_trees/test_pg_120_has_path_sum.py -v
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


def has_path_sum(root: TreeNode | None, target: int) -> bool:
    """Check for a complete root-to-leaf path whose values sum to target."""
    if root is None:
        return False
    remainder = target - root.data
    if root.left is None and root.right is None:
        return remainder == 0
    return has_path_sum(root.left, remainder) or has_path_sum(root.right, remainder)


def has_path_sum_values(tree, target: int) -> bool:
    return has_path_sum(build_tree(tree), target)


if __name__ == "__main__":
    tree=(5,(2,None,None),(3,None,None))
    print("has root-leaf path sum 8:", has_path_sum_values(tree, 8))
    assert has_path_sum_values(tree, 8)
