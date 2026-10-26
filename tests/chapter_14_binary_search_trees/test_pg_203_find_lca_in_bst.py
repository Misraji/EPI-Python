from epi_python.chapter_14_binary_search_trees.bst_nodes import BSTNode
from epi_python.chapter_14_binary_search_trees.pg_203_find_lca_in_bst import find_lca_in_bst


def test_lca():
    a,b,c,d=BSTNode(2),BSTNode(7),BSTNode(12),BSTNode(19)
    left,right=BSTNode(5,a,b),BSTNode(15,c,d)
    root=BSTNode(10,left,right)
    assert find_lca_in_bst(root,a,b) is left
    assert find_lca_in_bst(root,a,d) is root
    assert find_lca_in_bst(root,c,d) is right
    assert find_lca_in_bst(root,left,b) is left


def test_empty():
    assert find_lca_in_bst(None,BSTNode(1),BSTNode(2)) is None
