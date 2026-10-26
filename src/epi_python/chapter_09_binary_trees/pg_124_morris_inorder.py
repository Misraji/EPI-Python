"""EPI exercise 9.11, printed page 124: Implement an inorder traversal with O(1) space.

EDUCATIONAL RECONSTRUCTION — not a verbatim verified code transcription.
Problem: Implement an inorder traversal with O(1) space.
Method/complexity: Threaded inorder traversal O(n) time, O(1) traversal memory; restores all temporary links.
For the book's original explanation and variants, see:
    pg_124_exercise_09_11_implement_an_inorder_traversal_with_o_1_space.md

Run: python -m epi_python.chapter_09_binary_trees.pg_124_morris_inorder
Test: python -m pytest tests/chapter_09_binary_trees/test_pg_124_morris_inorder.py -v
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


def inorder_constant_space(root: TreeNode | None) -> list[int]:
    """Morris traversal: temporary predecessor threads avoid an explicit stack."""
    result = []
    current = root
    while current is not None:
        if current.left is None:
            result.append(current.data)
            current = current.right
        else:
            predecessor = current.left
            while predecessor.right is not None and predecessor.right is not current:
                predecessor = predecessor.right
            if predecessor.right is None:
                predecessor.right = current
                current = current.left
            else:
                predecessor.right = None
                result.append(current.data)
                current = current.right
    return result


def morris_values(tree) -> list[int]:
    return inorder_constant_space(build_tree(tree))


if __name__ == "__main__":
    tree=(2,(1,None,None),(3,None,None))
    print("Morris inorder:", morris_values(tree))
    assert morris_values(tree)==[1,2,3]
