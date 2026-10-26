"""EPI exercise 8.6, printed page 106: Compute binary tree nodes in order of increasing depth.

EDUCATIONAL RECONSTRUCTION — not a verbatim verified code transcription.
Problem: Compute binary tree nodes in order of increasing depth.
Method/complexity: Breadth-first traversal; O(n) time, O(max_level_width) queue memory.
For the book's original explanation and variants, see:
    pg_106_exercise_08_06_compute_binary_tree_nodes_in_order_of_increasing_depth.md

Run: python -m epi_python.chapter_08_stacks_and_queues.pg_106_binary_tree_depth_order
Test: python -m pytest tests/chapter_08_stacks_and_queues/test_pg_106_binary_tree_depth_order.py -v
"""

# deque is a double-ended queue; popleft() runs in O(1) time.
# Documentation: https://docs.python.org/3/library/collections.html#collections.deque
from collections import deque

# Reuse the chapter 9 example node with left and right child fields.
from epi_python.chapter_09_binary_trees.pg_114_is_balanced_binary_tree import TreeNode


def binary_tree_depth_order(root: TreeNode | None) -> list[list[int]]:
    """Return level-order lists using breadth-first traversal."""
    if root is None:
        return []
    queue = deque([root])
    result: list[list[int]] = []
    while queue:
        level = []
        for _ in range(len(queue)):
            node = queue.popleft()
            level.append(node.data)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(level)
    return result


def depth_order_values(tree: tuple | None) -> list[list[int]]:
    def build(t):
        return None if t is None else TreeNode(t[0], build(t[1]), build(t[2]))
    return binary_tree_depth_order(build(tree))


if __name__ == "__main__":
    tree = (1, (2, None, None), (3, None, None))
    print("tree levels:", depth_order_values(tree))
    assert depth_order_values(tree) == [[1], [2, 3]]
