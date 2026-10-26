from epi_python.chapter_14_binary_search_trees.bst_nodes import BSTNode
from epi_python.chapter_14_binary_search_trees.pg_202_find_k_largest_in_bst import find_k_largest_in_bst


def test_k_largest():
    root=BSTNode(8,BSTNode(3,BSTNode(1),BSTNode(6)),BSTNode(10,None,BSTNode(14)))
    for k in range(0,8):
        assert find_k_largest_in_bst(root,k)==[14,10,8,6,3,1][:k]


def test_empty():
    assert find_k_largest_in_bst(None,3)==[]
