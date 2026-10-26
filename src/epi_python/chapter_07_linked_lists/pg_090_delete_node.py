"""EPI Python — Exercise 7.6: Delete a Node from a Singly Linked List

Chapter 7: Linked Lists
Textbook: page 90 (printed page number; problem, solution, program and
complexity all on 90).

PROBLEM (from the textbook)
---------------------------
"Given a node in a singly linked list, deleting it in O(1) time appears
impossible because its predecessor's next field has to be updated.
Surprisingly, it can be done with one small caveat—the node to delete
cannot be the last one in the list and it is easy to copy the value part
of a node."

"Write a program which deletes a node in a singly linked list. The input
node is guaranteed not to be the tail node."

HINT (from the textbook)
------------------------
"Instead of deleting the node, can you delete its successor and still
achieve the desired configuration?"

SOLUTION DEVELOPMENT (following the textbook)
---------------------------------------------
Holding only a reference to a node, you cannot unlink it without changing
its predecessor's next field, and the only way to find the predecessor is
to walk from the head: O(n) time for n nodes.

Deleting a node's successor, however, is easy: just change the current
node's next field. So copy the successor's value into the current node and
then delete the successor. The list now looks exactly as if the current
node had been removed. This takes O(1) time.

Implementation in this file: delete_node() is the textbook program.
build_nodes(), node_values() and delete_at_index() are helpers added in
this repository (not in the book).

ADDITIONAL EXAMPLES (added for learning; not printed in this exercise)
---------------------------------------------------------------------
    [1, 2, 3], delete the node at index 1 (value 2)   -> [1, 3]
    (Afterwards the node object that held 2 holds 3; the object that
    originally held 3 is no longer in the list.)
"""

# Repository import (not the standard library): reuse the ListNode
# dataclass defined in this chapter's Exercise 7.1 module.
# Python import system: https://docs.python.org/3/reference/import.html
# `from ... import` statement: https://docs.python.org/3/reference/simple_stmts.html#the-import-statement
from epi_python.chapter_07_linked_lists.pg_084_merge_two_sorted_lists import ListNode


# Type hints such as `list[int]` and `ListNode | None` ("a node or None")
# document intended types; Python does not enforce them. The `|` form
# between types needs Python 3.10+.
def build_nodes(values: list[int]) -> ListNode | None:
    """Construct nodes in input order for the standalone examples and tests.

    Helper added in this repository (not in the book).
    """
    head = None

    # reversed(sequence) yields items from last to first without copying,
    # so prepending leaves `head` at values[0].
    for value in reversed(values):
        head = ListNode(value, head)
    return head


def node_values(head: ListNode | None) -> list[int]:
    """Read an acyclic chain into a convenient Python list.

    Helper added in this repository (not in the book).
    """
    result = []
    while head is not None:
        result.append(head.data)
        head = head.next
    return result


# `-> None` documents that the function returns nothing useful; it works
# by changing the node in place.
def delete_node(node: ListNode) -> None:
    """Delete a non-tail node given only its pointer, by copying its successor.

    This is the textbook's deletion_from_list(node_to_delete) program
    (page 90), plus a guard that the book does not have.
    """

    # Added guard: `raise ValueError(...)` stops with an exception instead
    # of failing later with AttributeError on `None.data`. The book simply
    # assumes the node is not the tail.
    if node.next is None:
        raise ValueError("Cannot delete a tail node this way")

    # Copy the successor's value in, then bypass the successor.
    node.data = node.next.data
    node.next = node.next.next


def delete_at_index(values: list[int], index: int) -> list[int]:
    """Adapter: delete a non-tail node and return the resulting linked-list data.

    Helper added in this repository (not in the book); `index` is 0-based.
    """

    # Chained comparison: 0 <= index and index < len(values) - 1, i.e. a
    # valid position that is not the last one (the tail).
    if not 0 <= index < len(values) - 1:
        raise ValueError("Index must refer to a non-tail node")
    head = build_nodes(values)
    node = head
    for _ in range(index):
        node = node.next
    delete_node(node)
    return node_values(head)


# TEXTBOOK POST-SOLUTION DISCUSSION (page 90)
# -------------------------------------------
# The time complexity is O(1). (The book states this just before the
# program; no further discussion follows it.)
#
# VARIANTS
# --------
# None printed for this exercise.


# TEXTBOOK CODE COMPARISON
# ------------------------
# - Function name: book `deletion_from_list(node_to_delete)` (with the
#   comment "Assumes node_to_delete is not tail."); file
#   `delete_node(node: ListNode) -> None`.
# - File adds a check that raises ValueError when node.next is None; the
#   book has no check.
# - The two assignment statements match the book's.
# - Node class: file imports the @dataclass ListNode from
#   pg_084_merge_two_sorted_lists instead of the book's class (page 82).
# - build_nodes, node_values and delete_at_index are helpers not in the
#   book.


# Python executes this block only when this source file is run directly.
# When pytest imports the file, this block is skipped automatically.
# Documentation: https://docs.python.org/3/library/__main__.html
if __name__ == "__main__":

    # Delete the middle node of 1 -> 2 -> 3. `assert` raises AssertionError
    # if the result is different from the expected value.
    print("delete node:", delete_at_index([1, 2, 3], 1))
    assert delete_at_index([1, 2, 3], 1) == [1, 3]
