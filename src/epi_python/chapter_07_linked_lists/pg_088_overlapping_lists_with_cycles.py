"""EPI Python — Exercise 7.5: Test for Overlapping Lists—Lists May Have Cycles

Chapter 7: Linked Lists
Textbook: pages 88–90 (printed page numbers; problem on 88, Figure 7.7,
hint, solution and program on 89, program end and complexity on 90).

PROBLEM (from the textbook)
---------------------------
"Solve Problem 7.4 on the previous page for the case where the lists may
each or both have a cycle. If such a node exists, return a node that
appears first when traversing the lists. This node may not be unique—if
one node ends in a cycle, the first cycle node encountered when traversing
it may be different from the first cycle node encountered when traversing
the second list, even though the cycle is the same. In such cases, you may
return either of the two nodes."

"For example, Figure 7.7 on the facing page shows an example of lists
which overlap and have cycles. For this example, both A and B are
acceptable answers."

Figure 7.7: L2 runs A -> B -> ... and its last node links back to A, so A
is where L2 enters the cycle; L1's second node links into B, so B is where
L1 enters the same cycle.

HINT (from the textbook)
------------------------
"Use case analysis. What if both lists have cycles? What if they end in a
common cycle? What if one list has cycle and the other does not?"

SOLUTION DEVELOPMENT (following the textbook)
---------------------------------------------
With the hash-table approach of Solution 7.4 the problem is easy in O(n)
time and O(n) space, n being the total number of nodes. Space improves by
splitting into cases:

1. Neither list is cyclic (determined with Solution 7.3). Then overlap is
   checked with the technique of Solution 7.4.
2. Exactly one list is cyclic: they cannot overlap; answer "none".
3. Both lists are cyclic: if they overlap, their cycles must be the same
   cycle. Two subcases:
   a. The paths join before reaching the cycle: there is a unique first
      common node, found with the approach of Solution 7.4 (align by the
      lengths of the parts before the cycle, then step together).
   b. The paths reach the cycle at different nodes: use the technique of
      Solution 7.3 (walking around a cycle) to confirm the cycle is
      shared; any node on the cycle is then an acceptable answer.

The book's program: get each list's cycle start (root1, root2). Handle the
no-cycle and one-cycle cases. Otherwise walk around the cycle from root2;
if root1 is never met, the cycles are disjoint. Then measure each list's
distance from its head to its cycle start, advance the longer one by the
difference, and step both until they meet or one reaches its cycle start.
If they met first, that node is the answer; otherwise return root1.

Implementation in this file: overlapping_lists_with_cycles() follows this
case analysis, reusing has_cycle_nodes() from Exercise 7.3's module and
overlapping_no_cycle_lists() from Exercise 7.4's module. build_nodes() and
node_values() are helpers added in this repository (not in the book).

ADDITIONAL EXAMPLES (added for learning; not printed in this exercise)
---------------------------------------------------------------------
    A two-node cycle 1 <-> 2: starting one list at node 1 and the other at
    node 2 gives two lists that share the whole cycle but enter it at
    different nodes; the function returns node 1 (entry of the first list).
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

    Helper added in this repository (not in the book). Do not call it on a
    cyclic list: the loop would never end.
    """
    result = []
    while head is not None:
        result.append(head.data)
        head = head.next
    return result

# Repository import (placed mid-file in this module): the two-pointer
# cycle-start finder from Exercise 7.3's module. It returns the node where
# a list's cycle begins, or None (O(1) additional memory).
# Python import system: https://docs.python.org/3/reference/import.html
# `from ... import` statement: https://docs.python.org/3/reference/simple_stmts.html#the-import-statement
from epi_python.chapter_07_linked_lists.pg_086_has_cycle import has_cycle_nodes

# Repository import: the acyclic overlap algorithm from Exercise 7.4's
# module, used for the case where neither list has a cycle.
# Python import system: https://docs.python.org/3/reference/import.html
# `from ... import` statement: https://docs.python.org/3/reference/simple_stmts.html#the-import-statement
from epi_python.chapter_07_linked_lists.pg_087_overlapping_no_cycle_lists import overlapping_no_cycle_lists


def overlapping_lists_with_cycles(a: ListNode | None, b: ListNode | None) -> ListNode | None:
    """Return shared node, or any node on common cycle when ambiguity exists.

    This follows the textbook's overlapping_lists(L1, L2) program
    (pages 89–90), with the cases handled in a different order (see the
    TEXTBOOK CODE COMPARISON below).
    """

    # Store the start of each cycle, if any (None means acyclic).
    entry_a, entry_b = has_cycle_nodes(a), has_cycle_nodes(b)

    # Both lists don't have cycles: use the Exercise 7.4 algorithm.
    if entry_a is None and entry_b is None:
        return overlapping_no_cycle_lists(a, b)

    # One list has a cycle, one has no cycle. Comparing the two booleans
    # with `!=` acts as an exclusive or: True exactly when one is None and
    # the other is not. Such lists cannot overlap.
    if (entry_a is None) != (entry_b is None):
        return None

    # Both lists have cycles and enter them at the same node, so they share
    # the cycle and possibly some nodes before it.
    if entry_a is entry_b:

        # Calculates the number of steps from `head` to `stop`.
        def distance(head, stop):
            length = 0
            while head is not stop:
                length += 1
                head = head.next
            return length

        # Align the two stems (the parts before the cycle) so that both
        # pointers are the same distance from the shared cycle start.
        na, nb = distance(a, entry_a), distance(b, entry_b)
        if na > nb:
            a, b = b, a
            na, nb = nb, na
        for _ in range(nb - na):
            b = b.next

        # Step together until the pointers meet or one reaches the cycle.
        while a is not b and a is not entry_a and b is not entry_b:
            a, b = a.next, b.next

        # If they met before the cycle start, that is the first common
        # node; otherwise the cycle start itself is returned.
        # `A if condition else B` is a conditional expression.
        return a if a is b else entry_a

    # Different cycle entries: walk once around list a's cycle. If entry_b
    # is met, both lists end in the same cycle and either entry is an
    # acceptable answer; if we get back to entry_a, the cycles are disjoint.
    cursor = entry_a.next
    while cursor is not entry_a and cursor is not entry_b:
        cursor = cursor.next
    return entry_a if cursor is entry_b else None


# TEXTBOOK POST-SOLUTION DISCUSSION (page 90)
# -------------------------------------------
# Time complexity O(n + m), where n and m are the lengths of the two input
# lists; space complexity O(1).
#
# VARIANTS
# --------
# None printed for this exercise.


# TEXTBOOK CODE COMPARISON
# ------------------------
# - Function name: book `overlapping_lists(L1, L2)`; file
#   `overlapping_lists_with_cycles(a, b)` with type hints.
# - Cycle detection: book calls its Solution 7.3 `has_cycle` (the main,
#   cycle-length program); file calls `has_cycle_nodes`, which is the
#   shorter program the book prints as the 7.3 variant question.
# - Book tests `if not root1 and not root2` / `elif (root1 and not root2)
#   or (not root1 and root2)`; file uses `is None` tests and the `!=`
#   comparison of two booleans.
# - Order of the both-cyclic logic differs: the book first walks around the
#   cycle from root2 (`temp`, `while True ... break`) to rule out disjoint
#   cycles, then ALWAYS computes stem lengths with `distance(a, b)`, aligns,
#   and returns `L1 if L1 is L2 else root1`. The file performs the
#   alignment only when `entry_a is entry_b`; when the entries differ it
#   walks around entry_a's cycle looking for entry_b and returns entry_a or
#   None directly.
# - Book names `stem1_length`, `stem2_length`, `dis`; file `na`, `nb`,
#   `length`. Book swaps lists and roots and advances
#   `abs(stem1_length - stem2_length)`; file swaps lists and lengths (the
#   entries are identical in that branch) and advances `nb - na`.
# - The file imports ListNode, has_cycle_nodes and
#   overlapping_no_cycle_lists from other repository modules;
#   build_nodes and node_values are helpers not in the book.


# Python executes this block only when this source file is run directly.
# When pytest imports the file, this block is skipped automatically.
# Documentation: https://docs.python.org/3/library/__main__.html
if __name__ == "__main__":

    # Build a two-node cycle 1 -> 2 -> back to 1. Treating cycle_a and
    # cycle_b as two list heads, the lists share the cycle but enter it at
    # different nodes, so the function returns the first list's entry,
    # cycle_a. (`.data` is printed rather than the node, because printing
    # a node on a cycle would recurse forever in the dataclass __repr__.)
    # `assert ... is cycle_a` checks identity: the very same node object.
    cycle_a = ListNode(1)
    cycle_b = ListNode(2, cycle_a)
    cycle_a.next = cycle_b
    print("overlap (cycles):", overlapping_lists_with_cycles(cycle_a, cycle_b).data)
    assert overlapping_lists_with_cycles(cycle_a, cycle_b) is cycle_a
