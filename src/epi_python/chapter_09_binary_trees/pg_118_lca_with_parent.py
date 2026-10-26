"""EPI exercise 9.4, printed page 118: Compute the LCA when nodes have parent pointers.

EDUCATIONAL RECONSTRUCTION — not a verbatim verified code transcription.
Problem: Compute the LCA when nodes have parent pointers.
Method/complexity: Find node depths, align, walk; O(h) time, O(1) additional memory after nodes are identified.
For the book's original explanation and variants, see:
    pg_118_exercise_09_04_compute_the_lca_when_nodes_have_parent_pointers.md

Run: python -m epi_python.chapter_09_binary_trees.pg_118_lca_with_parent
Test: python -m pytest tests/chapter_09_binary_trees/test_pg_118_lca_with_parent.py -v
"""

# dataclass generates a simple binary tree record with parent links.
# Documentation: https://docs.python.org/3/library/dataclasses.html#dataclasses.dataclass
from dataclasses import dataclass


@dataclass
class ParentNode:
    data: int
    left: "ParentNode | None" = None
    right: "ParentNode | None" = None
    parent: "ParentNode | None" = None


def build_parent_tree(tree, parent=None):
    """Build a binary tree with reciprocal child/parent links."""
    if tree is None:
        return None
    node = ParentNode(tree[0], parent=parent)
    node.left = build_parent_tree(tree[1], node)
    node.right = build_parent_tree(tree[2], node)
    return node


def find_node(root, key):
    if root is None or root.data == key:
        return root
    return find_node(root.left, key) or find_node(root.right, key)


def lca_with_parent(a: ParentNode, b: ParentNode) -> ParentNode | None:
    """Align ancestor depths, then walk upwards together."""
    def depth(node):
        d = 0
        while node is not None:
            d += 1
            node = node.parent
        return d
    depth_a, depth_b = depth(a), depth(b)
    if depth_a < depth_b:
        a, b = b, a
        depth_a, depth_b = depth_b, depth_a
    for _ in range(depth_a - depth_b):
        a = a.parent
    while a is not b:
        a, b = a.parent, b.parent
    return a


def lca_parent_value(tree, a: int, b: int) -> int | None:
    root = build_parent_tree(tree)
    left, right = find_node(root, a), find_node(root, b)
    if left is None or right is None:
        return None
    node = lca_with_parent(left, right)
    return None if node is None else node.data


if __name__ == "__main__":
    tree=(4,(2,(1,None,None),(3,None,None)),(6,None,None))
    print("parent LCA:", lca_parent_value(tree, 1, 3))
    assert lca_parent_value(tree, 1, 3) == 2
