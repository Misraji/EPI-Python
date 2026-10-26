"""EPI Python 24.9, textbook printed page 361: Implement list zipping.

QUESTION: Reorder a singly-linked list 0,n-1,1,n-2,... without allocating new list nodes.

TEXTBOOK ALGORITHM: Find midpoint, reverse second half, and weave node pointers together.

The complete question, hints, solution development, and variants are in the
adjacent page-numbered reference Markdown, extracted from the supplied PDF.
This executable implementation restores syntax damaged by the PDF text layer;
minor type annotations, examples, and assertions are educational additions.

Run: python -m epi_python.chapter_24_honors_class.pg_361_zipping_linked_list
Test: python -m pytest tests/chapter_24_honors_class/test_pg_361_zipping_linked_list.py -v
"""

class ListNode:
    def __init__(self,data: int,next: 'ListNode | None'=None):
        self.data=data
        self.next=next


def reverse_linked_list(head: ListNode | None) -> ListNode | None:
    prev=None
    while head:
        nxt=head.next
        head.next=prev
        prev,head=head,nxt
    return prev


def zipping_linked_list(head: ListNode | None) -> ListNode | None:
    if not head or not head.next:
        return head
    slow=fast=head
    while fast and fast.next:
        slow,fast=slow.next,fast.next.next
    first_half_head=head
    second_half_head=slow.next
    slow.next=None
    second_half_head=reverse_linked_list(second_half_head)
    first_iter,second_iter=first_half_head,second_half_head
    while second_iter:
        second_iter.next,first_iter.next,second_iter=(first_iter.next,second_iter,second_iter.next)
        first_iter=first_iter.next.next
    return first_half_head


def as_list(head: ListNode | None) -> list[int]:
    out=[]
    while head:
        out.append(head.data)
        head=head.next
    return out


if __name__=='__main__':
    h=ListNode(0,ListNode(1,ListNode(2,ListNode(3,ListNode(4)))))
    result=as_list(zipping_linked_list(h))
    print('Zipped:',result)
    assert result==[0,4,1,3,2]
