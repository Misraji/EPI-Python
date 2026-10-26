"""EPI exercise 9.16, printed page 129: Compute the right sibling tree.

EDUCATIONAL RECONSTRUCTION — not a verbatim verified code transcription.
Problem: Compute the right sibling tree.
Method/complexity: For perfect binary trees, link children using already-linked parent level; O(n) time, O(1) workspace.
For the book's original explanation and variants, see:
    pg_129_exercise_09_16_compute_the_right_sibling_tree.md

Run: python -m epi_python.chapter_09_binary_trees.pg_129_right_sibling_tree
Test: python -m pytest tests/chapter_09_binary_trees/test_pg_129_right_sibling_tree.py -v
"""

# deque provides FIFO level traversal to verify sibling pointers.
# Documentation: https://docs.python.org/3/library/collections.html#collections.deque
from collections import deque

# dataclass generates node initialization with a next-sibling reference.
# Documentation: https://docs.python.org/3/library/dataclasses.html#dataclasses.dataclass
from dataclasses import dataclass


@dataclass
class SiblingNode:
    data: int
    left: "SiblingNode | None" = None
    right: "SiblingNode | None" = None
    next: "SiblingNode | None" = None


def make_sibling_tree(tree):
    if tree is None:
        return None
    return SiblingNode(tree[0], make_sibling_tree(tree[1]), make_sibling_tree(tree[2]))


def construct_right_sibling(root: SiblingNode | None) -> SiblingNode | None:
    """Link immediate neighbors at each depth in a perfect binary tree."""
    level = root
    while level is not None and level.left is not None:
        current = level
        while current is not None:
            current.left.next = current.right
            if current.next is not None:
                current.right.next = current.next.left
            current = current.next
        level = level.left
    return root


def sibling_pairs(tree) -> list[tuple[int, int | None]]:
    root = construct_right_sibling(make_sibling_tree(tree))
    if root is None:
        return []
    queue = deque([root])
    pairs = []
    while queue:
        node = queue.popleft()
        pairs.append((node.data, node.next.data if node.next else None))
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return pairs


if __name__ == "__main__":
    tree=(1,(2,None,None),(3,None,None))
    print("right siblings:", sibling_pairs(tree))
    assert sibling_pairs(tree)==[(1,None),(2,3),(3,None)]
