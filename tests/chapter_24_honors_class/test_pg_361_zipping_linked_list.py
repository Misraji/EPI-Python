# pytest parameterization: https://docs.pytest.org/en/stable/how-to/parametrize.html
import pytest

from epi_python.chapter_24_honors_class.pg_361_zipping_linked_list import ListNode,zipping_linked_list,as_list


@pytest.mark.parametrize('values',[[],[1],[1,2],[1,2,3],[0,1,2,3],[0,1,2,3,4],[0,1,2,3,4,5]])
def test_zip(values):
    h=None
    for x in reversed(values):h=ListNode(x,h)
    result=as_list(zipping_linked_list(h))
    desired=[]
    i,j=0,len(values)-1
    while i<=j:
        desired.append(values[i]);i+=1
        if i<=j:desired.append(values[j]);j-=1
    assert result==desired
