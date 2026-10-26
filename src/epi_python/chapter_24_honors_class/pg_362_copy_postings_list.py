"""EPI Python 24.10, textbook printed page 362: Copy a postings list.

QUESTION: Deep next and arbitrary jump pointers while deep-copying a posting list in O(1) additional space.

TEXTBOOK ALGORITHM: Interleave copies, rewire jump pointers, and separate copies while restoring the source.

The complete question, hints, solution development, and variants are in the
adjacent page-numbered reference Markdown, extracted from the supplied PDF.
This executable implementation restores syntax damaged by the PDF text layer;
minor type annotations, examples, and assertions are educational additions.

Run: python -m epi_python.chapter_24_honors_class.pg_362_copy_postings_list
Test: python -m pytest tests/chapter_24_honors_class/test_pg_362_copy_postings_list.py -v
"""

class PostingListNode:
    def __init__(self,order: int,next: 'PostingListNode | None'=None,jump: 'PostingListNode | None'=None):
        self.order=order
        self.next=next
        self.jump=jump


def copy_postings_list(head: PostingListNode | None) -> PostingListNode | None:
    if head is None:
        return None
    it=head
    while it:
        copy=PostingListNode(it.order,it.next,None)
        it.next=copy
        it=copy.next
    it=head
    while it:
        if it.jump:
            it.next.jump=it.jump.next
        it=it.next.next
    it=head
    new_head=head.next
    while it:
        copy=it.next
        it.next=copy.next
        copy.next=it.next.next if it.next else None
        it=it.next
    return new_head


if __name__=='__main__':
    a,b=PostingListNode(1),PostingListNode(2)
    a.next=b;a.jump=b;b.jump=a
    cloned=copy_postings_list(a)
    print('Copied postings:',cloned.order,cloned.jump.order)
    assert cloned is not a and cloned.jump is cloned.next and a.next is b
