"""Parameterized checks of EPI 7.3 educational solution."""

# pytest API: https://docs.pytest.org/en/stable/how-to/parametrize.html
import pytest

from epi_python.chapter_07_linked_lists.pg_086_has_cycle import has_cycle


@pytest.mark.parametrize(("arguments", "expected"), [(([],), False), (([1, 2, 3],), False), (([1, 2, 3], 0), True), (([1, 2, 3], 2), True)])
def test_examples(arguments, expected):
    assert has_cycle(*arguments) == expected

def test_two_pdf_cycle_entry_methods_return_identical_node_objects():
    from epi_python.chapter_07_linked_lists.pg_086_has_cycle import ListNode,has_cycle_nodes,has_cycle_nodes_via_cycle_length
    for n in range(20):
        nodes=[ListNode(v) for v in range(n)]
        for a,b in zip(nodes,nodes[1:]):
            a.next=b
        head=nodes[0] if nodes else None
        assert has_cycle_nodes(head) is None
        assert has_cycle_nodes_via_cycle_length(head) is None
        for entry in range(n):
            nodes[-1].next=nodes[entry]
            assert has_cycle_nodes(head) is nodes[entry]
            assert has_cycle_nodes_via_cycle_length(head) is nodes[entry]
        if nodes: nodes[-1].next=None
