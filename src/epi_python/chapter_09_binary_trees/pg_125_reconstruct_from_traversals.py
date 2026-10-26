"""EPI exercise 9.12, printed page 125: Reconstruct a binary tree from traversal data.

EDUCATIONAL RECONSTRUCTION — not a verbatim verified code transcription.
Problem: Reconstruct a binary tree from traversal data.
Method/complexity: Index inorder keys and reconstruct recursively; O(n) time and O(n) storage.
For the book's original explanation and variants, see:
    pg_125_exercise_09_12_reconstruct_a_binary_tree_from_traversal_data.md

Run: python -m epi_python.chapter_09_binary_trees.pg_125_reconstruct_from_traversals
Test: python -m pytest tests/chapter_09_binary_trees/test_pg_125_reconstruct_from_traversals.py -v
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


def reconstruct_from_preorder_inorder(preorder: list[int], inorder: list[int]) -> TreeNode | None:
    """Rebuild binary tree with distinct keys from matching preorder/inorder arrays."""
    if len(preorder) != len(inorder) or set(preorder) != set(inorder):
        raise ValueError("Traversals must contain the same unique keys")
    indices = {key: i for i,key in enumerate(inorder)}
    if len(indices) != len(inorder):
        raise ValueError("Distinct keys are needed for unambiguous reconstruction")
    position = 0
    def construct(lo, hi):
        nonlocal position
        if lo >= hi:
            return None
        key = preorder[position]
        position += 1
        mid = indices[key]
        node = TreeNode(key)
        node.left = construct(lo, mid)
        node.right = construct(mid + 1, hi)
        return node
    return construct(0, len(inorder))


def reconstruct_tree(preorder: list[int], inorder: list[int]):
    return nested_tree(reconstruct_from_preorder_inorder(preorder, inorder))


if __name__ == "__main__":
    result=reconstruct_tree([2,1,3],[1,2,3])
    print("reconstructed:", result)
    assert result==(2,(1,None,None),(3,None,None))
