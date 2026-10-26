"""EPI exercise 9.15, printed page 128: Compute the exterior of a binary tree.

EDUCATIONAL RECONSTRUCTION — not a verbatim verified code transcription.
Problem: Compute the exterior of a binary tree.
Method/complexity: Visit left boundary, leaves, right boundary; O(n) time, O(h) recursion plus output.
For the book's original explanation and variants, see:
    pg_128_exercise_09_15_compute_the_exterior_of_a_binary_tree.md

Run: python -m epi_python.chapter_09_binary_trees.pg_128_exterior_binary_tree
Test: python -m pytest tests/chapter_09_binary_trees/test_pg_128_exterior_binary_tree.py -v
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


def exterior_binary_tree(root: TreeNode | None) -> list[int]:
    """Return root, left boundary, leaves and reversed right boundary without duplicates."""
    if root is None:
        return []
    if root.left is None and root.right is None:
        return [root.data]
    exterior = [root.data]
    node = root.left
    while node is not None:
        if node.left is not None or node.right is not None:
            exterior.append(node.data)
        node = node.left if node.left is not None else node.right
    def leaves(node):
        if node is None:
            return
        if node.left is None and node.right is None:
            exterior.append(node.data)
            return
        leaves(node.left)
        leaves(node.right)
    leaves(root.left)
    leaves(root.right)
    right_boundary = []
    node = root.right
    while node is not None:
        if node.left is not None or node.right is not None:
            right_boundary.append(node.data)
        node = node.right if node.right is not None else node.left
    exterior.extend(reversed(right_boundary))
    return exterior


def exterior_values(tree) -> list[int]:
    return exterior_binary_tree(build_tree(tree))


if __name__ == "__main__":
    tree=(1,(2,(4,None,None),None),(3,None,(5,None,None)))
    print("exterior:", exterior_values(tree))
    assert exterior_values(tree)==[1,2,4,5,3]
