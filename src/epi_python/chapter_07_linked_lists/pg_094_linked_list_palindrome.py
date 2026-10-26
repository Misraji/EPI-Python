"""EPI exercise 7.11, printed page 94: Test whether a singly linked list is palindromic.

EDUCATIONAL RECONSTRUCTION — not a verbatim verified code transcription.
Problem: Test whether a singly linked list is palindromic.
Method/complexity: Reverse second half, compare, restore; O(n) time and O(1) additional space.
For the book's original explanation and variants, see:
    pg_094_exercise_07_11_test_whether_a_singly_linked_list_is_palindromic.md

Run: python -m epi_python.chapter_07_linked_lists.pg_094_linked_list_palindrome
Test: python -m pytest tests/chapter_07_linked_lists/test_pg_094_linked_list_palindrome.py -v
"""

# Reuse this chapter's singly linked ListNode, rather than a list-backed mock.
from epi_python.chapter_07_linked_lists.pg_084_merge_two_sorted_lists import ListNode


def build_nodes(values: list[int]) -> ListNode | None:
    """Construct nodes in input order for the standalone examples and tests."""
    head = None
    for value in reversed(values):
        head = ListNode(value, head)
    return head


def node_values(head: ListNode | None) -> list[int]:
    """Read an acyclic chain into a convenient Python list."""
    result = []
    while head is not None:
        result.append(head.data)
        head = head.next
    return result


def is_linked_list_a_palindrome(head: ListNode | None) -> bool:
    """Compare first half to reversed second half; restore original links."""
    def reverse(node):
        previous = None
        while node is not None:
            node.next, node, previous = previous, node.next, node
        return previous
    slow = fast = head
    while fast is not None and fast.next is not None:
        fast = fast.next.next
        slow = slow.next
    second_half = reverse(slow)
    first, second = head, second_half
    answer = True
    while second is not None:
        if first.data != second.data:
            answer = False
            break
        first, second = first.next, second.next
    reverse(second_half)
    return answer


def palindrome_values(values: list[int]) -> bool:
    return is_linked_list_a_palindrome(build_nodes(values))


if __name__ == "__main__":
    for values in ([1, 2, 1], [1, 2, 3]):
        print("linked palindrome:", values, palindrome_values(values))
