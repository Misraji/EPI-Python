# pytest documentation: https://docs.pytest.org/en/stable/
from epi_python.chapter_24_honors_class.pg_366_postorder_traversal import BinaryTreeNode,postorder_traversal,postorder_traversal_via_reverse


def test_tree():
    tree=BinaryTreeNode(1,BinaryTreeNode(2,BinaryTreeNode(4),BinaryTreeNode(5)),BinaryTreeNode(3))
    for fn in (postorder_traversal,postorder_traversal_via_reverse):
        assert fn(tree)==[4,5,2,3,1]
        assert fn(None)==[]


def test_single():
    assert postorder_traversal(BinaryTreeNode(7))==[7]
