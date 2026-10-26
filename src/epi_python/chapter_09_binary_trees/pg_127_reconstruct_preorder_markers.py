"""EPI exercise 9.13, printed page 127: Reconstruct a binary tree from a preorder traversal with markers.

EDUCATIONAL RECONSTRUCTION — not a verbatim verified code transcription.
Problem: Reconstruct a binary tree from a preorder traversal with markers.
Method/complexity: Consume preorder once; O(n) time and O(h) recursion space.
For the book's original explanation and variants, see:
    pg_127_exercise_09_13_reconstruct_a_binary_tree_from_a_preorder_traversal_with_markers.md

Run: python -m epi_python.chapter_09_binary_trees.pg_127_reconstruct_preorder_markers
Test: python -m pytest tests/chapter_09_binary_trees/test_pg_127_reconstruct_preorder_markers.py -v
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


def reconstruct_preorder_with_null(preorder: list[int | None]) -> TreeNode | None:
    """Deserialize preorder sequence where None represents each empty child."""
    cursor = iter(preorder)
    def read():
        try:
            value = next(cursor)
        except StopIteration:
            raise ValueError("Truncated preorder sequence") from None
        if value is None:
            return None
        node = TreeNode(value)
        node.left = read()
        node.right = read()
        return node
    root = read()
    if next(cursor, None) is not None:
        raise ValueError("Extraneous trailing values")
    return root


def reconstruct_marked_tree(preorder: list[int | None]):
    return nested_tree(reconstruct_preorder_with_null(preorder))


if __name__ == "__main__":
    example=[1,2,None,None,3,None,None]
    print("preorder with null markers:", reconstruct_marked_tree(example))
    assert reconstruct_marked_tree(example) == (1,(2,None,None),(3,None,None))
