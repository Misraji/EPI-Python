from epi_python.chapter_14_binary_search_trees.bst_nodes import BSTNode
from epi_python.chapter_14_binary_search_trees.pg_211_pair_includes_ancestor_and_descendant_of_m import pair_includes_ancestor_and_descendant_of_m


def test_ancestor_descendant():
    leaf=BSTNode(1); middle=BSTNode(3,leaf); right=BSTNode(8); root=BSTNode(5,middle,right)
    assert pair_includes_ancestor_and_descendant_of_m(root,leaf,middle)
    assert pair_includes_ancestor_and_descendant_of_m(leaf,root,middle)
    assert not pair_includes_ancestor_and_descendant_of_m(root,right,middle)
    assert not pair_includes_ancestor_and_descendant_of_m(middle,leaf,middle)
    assert not pair_includes_ancestor_and_descendant_of_m(root,leaf,root)
