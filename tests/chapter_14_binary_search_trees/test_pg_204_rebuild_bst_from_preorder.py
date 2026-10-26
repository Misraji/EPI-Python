from epi_python.chapter_14_binary_search_trees.pg_204_rebuild_bst_from_preorder import rebuild_bst_from_preorder


def preorder(node):
    return [] if node is None else [node.data]+preorder(node.left)+preorder(node.right)


def test_reconstruction():
    for values in [[],[5],[10,5,2,7,15,12,20],[5,4,3,2,1],[1,2,3,4,5]]:
        assert preorder(rebuild_bst_from_preorder(values))==values
