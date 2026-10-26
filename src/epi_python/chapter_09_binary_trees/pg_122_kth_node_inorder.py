"""EPI exercise 9.9, printed page 122: Compute the kth node in an inorder traversal.

EDUCATIONAL RECONSTRUCTION — not a verbatim verified code transcription.
Problem: Compute the kth node in an inorder traversal.
Method/complexity: Once subtree sizes are stored, O(h) time and O(1) traversal space.
For the book's original explanation and variants, see:
    pg_122_exercise_09_09_compute_the_kth_node_in_an_inorder_traversal.md

Run: python -m epi_python.chapter_09_binary_trees.pg_122_kth_node_inorder
Test: python -m pytest tests/chapter_09_binary_trees/test_pg_122_kth_node_inorder.py -v
"""

# dataclass creates an augmented node with subtree size metadata.
# Documentation: https://docs.python.org/3/library/dataclasses.html#dataclasses.dataclass
from dataclasses import dataclass


@dataclass
class SizeNode:
    data: int
    left: "SizeNode | None" = None
    right: "SizeNode | None" = None
    size: int = 1


def make_size_tree(tree) -> SizeNode | None:
    if tree is None:
        return None
    node = SizeNode(tree[0],make_size_tree(tree[1]),make_size_tree(tree[2]))
    node.size = 1 + (node.left.size if node.left else 0) + (node.right.size if node.right else 0)
    return node


def kth_node_inorder(root: SizeNode | None, k: int) -> SizeNode | None:
    """Find kth node in inorder traversal (1-based) using subtree sizes."""
    while root is not None:
        left_size = root.left.size if root.left else 0
        if k == left_size + 1:
            return root
        if k <= left_size:
            root = root.left
        else:
            k -= left_size + 1
            root = root.right
    return None


def kth_inorder_value(tree, k: int) -> int | None:
    node = kth_node_inorder(make_size_tree(tree), k)
    return None if node is None else node.data


if __name__ == "__main__":
    tree=(2,(1,None,None),(3,None,None))
    print("2nd inorder:", kth_inorder_value(tree,2))
    assert kth_inorder_value(tree,2)==2
