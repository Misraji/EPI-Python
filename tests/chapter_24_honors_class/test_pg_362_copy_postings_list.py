# pytest documentation: https://docs.pytest.org/en/stable/
from epi_python.chapter_24_honors_class.pg_362_copy_postings_list import PostingListNode,copy_postings_list


def test_copy_and_restore():
    a,b,c=[PostingListNode(i) for i in range(3)]
    a.next=b;b.next=c
    a.jump=c;b.jump=a;c.jump=b
    copied=copy_postings_list(a)
    ca,cb,cc=copied,copied.next,copied.next.next
    assert [ca.order,cb.order,cc.order]==[0,1,2]
    assert ca.jump is cc and cb.jump is ca and cc.jump is cb
    assert all(x is not y for x,y in zip((a,b,c),(ca,cb,cc)))
    assert a.next is b and b.next is c and a.jump is c


def test_empty():
    assert copy_postings_list(None) is None
