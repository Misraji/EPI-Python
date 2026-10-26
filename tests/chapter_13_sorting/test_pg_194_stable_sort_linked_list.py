"""Pytest verification for EPI 13.10 (printed page 194)."""

# pytest parameterization: https://docs.pytest.org/en/stable/how-to/parametrize.html
import pytest

from epi_python.chapter_13_sorting.pg_194_stable_sort_linked_list import ListNode, stable_sort_list, to_linked, to_list


@pytest.mark.parametrize('values', [[],[1],[3,2,1],[1,2,3],[4,1,3,1,2],[-2,-9,3,0,0]])
def test_sort(values):
    assert to_list(stable_sort_list(to_linked(values))) == sorted(values)


def test_sort_is_stable():
    a,b,c=ListNode(2),ListNode(1),ListNode(2)
    a.next=b; b.next=c
    result=stable_sort_list(a)
    assert result is b and result.next is a and result.next.next is c
