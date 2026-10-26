"""EPI exercise 9.14, printed page 128: Form a linked list from the leaves of a binary tree.

EDUCATIONAL RECONSTRUCTION — not a verbatim verified code transcription.
Problem: Form a linked list from the leaves of a binary tree.
Method/complexity: Traverse original tree and append leaves to linked list; O(n) time, O(number_of_leaves) output.
For the book's original explanation and variants, see:
    pg_128_exercise_09_14_form_a_linked_list_from_the_leaves_of_a_binary_tree.md

Run: python -m epi_python.chapter_09_binary_trees.pg_128_binary_tree_leaves_list
Test: python -m pytest tests/chapter_09_binary_trees/test_pg_128_binary_tree_leaves_list.py -v
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

# Reuse this chapter's existing singly linked list node for the output chain.
from epi_python.chapter_07_linked_lists.pg_084_merge_two_sorted_lists import ListNode


def create_list_of_leaves(root: TreeNode | None) -> ListNode | None:
    """Build a linked chain of leaf nodes, ordered left-to-right."""
    dummy = ListNode(0)
    tail = dummy
    def visit(node):
        nonlocal tail
        if node is None:
            return
        if node.left is None and node.right is None:
            tail.next = ListNode(node.data)
            tail = tail.next
            return
        visit(node.left)
        visit(node.right)
    visit(root)
    return dummy.next


def leaf_values(tree) -> list[int]:
    current = create_list_of_leaves(build_tree(tree))
    result = []
    while current:
        result.append(current.data)
        current = current.next
    return result


if __name__ == "__main__":
    tree=(2,(1,None,None),(3,None,None))
    print("leaf list:", leaf_values(tree))
    assert leaf_values(tree)==[1,3]
