# pytest documentation: https://docs.pytest.org/en/stable/
from epi_python.chapter_24_honors_class.pg_378_bst_to_doubly_linked_list import BSTNode,bst_to_doubly_linked_list


def test_tree_to_linked():
    left=BSTNode(2,BSTNode(1),BSTNode(3))
    root=BSTNode(4,left,BSTNode(6,BSTNode(5),BSTNode(7)))
    h=bst_to_doubly_linked_list(root)
    seen=[];prev=None
    while h:
        seen.append(h.data)
        assert h.left is prev
        prev,h=h,h.right
    assert seen==list(range(1,8))


def test_empty():
    assert bst_to_doubly_linked_list(None) is None
