"""Independent tests for EPI 7.11.

pytest parameterization: https://docs.pytest.org/en/stable/how-to/parametrize.html
"""

# pytest enables one test function to run over several examples.
# Documentation: https://docs.pytest.org/en/stable/
import pytest

# Standard library: copies mutable inputs so tests do not share state.
# Documentation: https://docs.python.org/3/library/copy.html
import copy

from epi_python.chapter_07_linked_lists.pg_094_linked_list_palindrome import palindrome_values

@pytest.mark.parametrize(("args", "expected"), [
    (([1,2,3,2,1],), True),
    (([1,2,2,1],), True),
    (([1,2,3],), False),
    (([], ), True),
    (([7],), True),
])
def test_examples(args, expected):
    """Verify representative and boundary conditions independently."""
    assert palindrome_values(*copy.deepcopy(args)) == expected

from epi_python.chapter_07_linked_lists.pg_094_linked_list_palindrome import build_nodes, node_values, is_linked_list_a_palindrome


def test_check_does_not_destroy_list():
    for values in ([1,2,3,2,1], [1,2,2,1], [4,5,6], [1,2]):
        head = build_nodes(values)
        is_linked_list_a_palindrome(head)
        assert node_values(head) == values
