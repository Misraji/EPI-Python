# pytest documentation: https://docs.pytest.org/en/stable/
from epi_python.chapter_24_honors_class.pg_376_build_bst_from_sorted_doubly_list import DoublyNode,build_bst_from_sorted_doubly_list


def inorder(tree):
    return [] if tree is None else inorder(tree.prev)+[tree.data]+inorder(tree.next)


def test_list_to_tree():
    nodes=[DoublyNode(i) for i in range(7)]
    for a,b in zip(nodes,nodes[1:]):a.next=b;b.prev=a
    root=build_bst_from_sorted_doubly_list(nodes[0],7)
    assert inorder(root)==list(range(7))
    assert root.data==3


def test_empty():
    assert build_bst_from_sorted_doubly_list(None,0) is None
