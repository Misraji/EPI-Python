"""EPI Python 24.20, textbook printed page 376: Convert a sorted doubly linked list into a BST.

QUESTION: Convert sorted doubly linked list into balanced BST without allocating replacement nodes.

TEXTBOOK ALGORITHM: Recursively build left subtree, consume the next list node as root, and build right subtree.

The complete question, hints, solution development, and variants are in the
adjacent page-numbered reference Markdown, extracted from the supplied PDF.
This executable implementation restores syntax damaged by the PDF text layer;
minor type annotations, examples, and assertions are educational additions.

Run: python -m epi_python.chapter_24_honors_class.pg_376_build_bst_from_sorted_doubly_list
Test: python -m pytest tests/chapter_24_honors_class/test_pg_376_build_bst_from_sorted_doubly_list.py -v
"""

class DoublyNode:
    def __init__(self,data: int,prev=None,next=None):
        self.data,self.prev,self.next=data,prev,next


def build_bst_from_sorted_doubly_list(head: DoublyNode | None,n: int) -> DoublyNode | None:
    current=[head]
    def build(start: int,end: int) -> DoublyNode | None:
        if start>=end:return None
        mid=(start+end)//2
        left=build(start,mid)
        root=current[0]
        if root is None:raise ValueError('List shorter than indicated length')
        current[0]=root.next
        root.prev=left
        root.next=build(mid+1,end)
        return root
    return build(0,n)


if __name__=='__main__':
    a,b,c=DoublyNode(1),DoublyNode(2),DoublyNode(3)
    a.next=b;b.prev=a;b.next=c;c.prev=b
    tree=build_bst_from_sorted_doubly_list(a,3)
    print('BST root:',tree.data)
    assert tree is b and tree.prev is a and tree.next is c
