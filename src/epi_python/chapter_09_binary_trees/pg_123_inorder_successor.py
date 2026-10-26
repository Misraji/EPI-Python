"""EPI exercise 9.10, printed page 123: Compute the successor.

EDUCATIONAL RECONSTRUCTION — not a verbatim verified code transcription.
Problem: Compute the successor.
Method/complexity: Find leftmost right-descendant or upward left turn; O(h) time, O(1) space.
For the book's original explanation and variants, see:
    pg_123_exercise_09_10_compute_the_successor.md

Run: python -m epi_python.chapter_09_binary_trees.pg_123_inorder_successor
Test: python -m pytest tests/chapter_09_binary_trees/test_pg_123_inorder_successor.py -v
"""

# Reuse parent-pointer tree builder from exercise 9.4.
from epi_python.chapter_09_binary_trees.pg_118_lca_with_parent import ParentNode, build_parent_tree, find_node


def inorder_successor(node: ParentNode | None) -> ParentNode | None:
    """Find next node of inorder traversal without inspecting node keys."""
    if node is None:
        return None
    if node.right is not None:
        node = node.right
        while node.left is not None:
            node = node.left
        return node
    while node.parent is not None and node.parent.right is node:
        node = node.parent
    return node.parent


def inorder_successor_value(tree, key: int) -> int | None:
    root = build_parent_tree(tree)
    candidate = inorder_successor(find_node(root,key))
    return None if candidate is None else candidate.data


if __name__ == "__main__":
    tree=(2,(1,None,None),(3,None,None))
    print("successor of 1:", inorder_successor_value(tree,1))
    assert inorder_successor_value(tree,1) == 2
