"""EPI exercise 9.8, printed page 121: Implement a preorder traversal without recursion.

EDUCATIONAL RECONSTRUCTION — not a verbatim verified code transcription.
Problem: Implement a preorder traversal without recursion.
Method/complexity: Explicit depth-first stack; O(n) time and O(h) stack for balanced trees.
For the book's original explanation and variants, see:
    pg_121_exercise_09_08_implement_a_preorder_traversal_without_recursion.md

Run: python -m epi_python.chapter_09_binary_trees.pg_121_preorder_without_recursion
Test: python -m pytest tests/chapter_09_binary_trees/test_pg_121_preorder_without_recursion.py -v
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


def preorder_traversal(root: TreeNode | None) -> list[int]:
    """Visit root, left, right by pushing right before left onto a stack."""
    if root is None:
        return []
    stack = [root]
    result = []
    while stack:
        node = stack.pop()
        result.append(node.data)
        if node.right is not None:
            stack.append(node.right)
        if node.left is not None:
            stack.append(node.left)
    return result


def preorder_values(tree) -> list[int]:
    return preorder_traversal(build_tree(tree))


if __name__ == "__main__":
    tree=(2,(1,None,None),(3,None,None))
    print("preorder:", preorder_values(tree))
    assert preorder_values(tree)==[2,1,3]
