from epi_python.chapter_14_binary_search_trees.pg_210_build_min_height_bst_from_sorted_array import build_min_height_bst_from_sorted_array


def inorder(root):
    return [] if root is None else inorder(root.left)+[root.data]+inorder(root.right)


def height(root):
    return 0 if root is None else 1+max(height(root.left),height(root.right))


def test_sorted_and_height():
    for n in range(64):
        root=build_min_height_bst_from_sorted_array(list(range(n)))
        assert inorder(root)==list(range(n))
        assert height(root).bit_length() <= 9
        if n>0:
            assert 2**(height(root)-1) <= n < 2**height(root)
