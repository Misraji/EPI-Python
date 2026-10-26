"""EPI Python 24.22, textbook printed page 379: Merge two BSTs.

QUESTION: Merge two BSTs into a balanced BST using the existing nodes and constant list bookkeeping.

TEXTBOOK ALGORITHM: Convert both BSTs to sorted doubly lists, merge, then rebuild a balanced BST from sorted nodes.

The complete question, hints, solution development, and variants are in the
adjacent page-numbered reference Markdown, extracted from the supplied PDF.
This executable implementation restores syntax damaged by the PDF text layer;
minor type annotations, examples, and assertions are educational additions.

Run: python -m epi_python.chapter_24_honors_class.pg_379_merge_two_bsts
Test: python -m pytest tests/chapter_24_honors_class/test_pg_379_merge_two_bsts.py -v
"""

class BSTNode:
    def __init__(self,data: int,left=None,right=None):
        self.data,self.left,self.right=data,left,right


def merge_two_bsts(a: BSTNode | None,b: BSTNode | None) -> BSTNode | None:
    def to_list(tree):
        if not tree:return None,None
        lh,lt=to_list(tree.left)
        rh,rt=to_list(tree.right)
        tree.left=lt
        if lt:lt.right=tree
        tree.right=rh
        if rh:rh.left=tree
        return lh or tree,rt or tree

    a_head,_=to_list(a)
    b_head,_=to_list(b)
    merged_head=merged_tail=None
    n=0
    while a_head or b_head:
        if not b_head or (a_head is not None and a_head.data<=b_head.data):
            node=a_head;a_head=a_head.right
        else:
            node=b_head;b_head=b_head.right
        node.left=merged_tail
        if merged_tail:merged_tail.right=node
        else:merged_head=node
        merged_tail=node
        n+=1
    if merged_tail:merged_tail.right=None
    cursor=[merged_head]
    def build(size):
        if size==0:return None
        left=build(size//2)
        root=cursor[0]
        cursor[0]=root.right
        root.left=left
        root.right=build(size-size//2-1)
        return root
    return build(n)


if __name__=='__main__':
    a=BSTNode(2,BSTNode(1),BSTNode(3));b=BSTNode(5,BSTNode(4),BSTNode(6))
    merged=merge_two_bsts(a,b)
    print('Merged BST root:',merged.data)
    assert merged.data in (3,4)
