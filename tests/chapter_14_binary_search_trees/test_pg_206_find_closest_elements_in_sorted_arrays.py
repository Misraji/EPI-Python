from itertools import product
from epi_python.chapter_14_binary_search_trees.pg_206_find_closest_elements_in_sorted_arrays import find_closest_elements_in_sorted_arrays


def test_book_example():
    assert find_closest_elements_in_sorted_arrays([[5,10,15],[3,6,9,12,15],[8,16,24]])==1


def test_bruteforce_comparison():
    data_sets=[[[1],[3],[7]],[[1,4],[2,8],[3,6]],[[0,0,6],[1,2],[4,9]],[[2,5],[2,5],[2,5]]]
    for arrays in data_sets:
        expected=min(max(t)-min(t) for t in product(*arrays))
        assert find_closest_elements_in_sorted_arrays(arrays)==expected


def test_bad_input():
    import pytest
    with pytest.raises(ValueError):
        find_closest_elements_in_sorted_arrays([[1],[]])
