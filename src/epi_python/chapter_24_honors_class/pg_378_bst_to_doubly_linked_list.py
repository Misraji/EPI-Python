"""EPI Python 24.21, textbook printed page 378: Convert a BST to a sorted doubly linked list.

QUESTION: Convert BST nodes in place to ascending doubly linked list without allocating new nodes.

TEXTBOOK ALGORITHM: Join recursively generated left and right lists to the root and return the overall head.

The complete question, hints, solution development, and variants are in the
adjacent page-numbered reference Markdown, extracted from the supplied PDF.
This executable implementation restores syntax damaged by the PDF text layer;
minor type annotations, examples, and assertions are educational additions.

Run: python -m epi_python.chapter_24_honors_class.pg_378_bst_to_doubly_linked_list
Test: python -m pytest tests/chapter_24_honors_class/test_pg_378_bst_to_doubly_linked_list.py -v
"""

class BSTNode:
    def __init__(self,data: int,left=None,right=None):
        self.data,self.left,self.right=data,left,right


def bst_to_doubly_linked_list(tree: BSTNode | None) -> BSTNode | None:
    def helper(root):
        if root is None:return None,None
        left_head,left_tail=helper(root.left)
        right_head,right_tail=helper(root.right)
        root.left=left_tail
        if left_tail:left_tail.right=root
        root.right=right_head
        if right_head:right_head.left=root
        return left_head or root,right_tail or root
    return helper(tree)[0]


if __name__=='__main__':
    root=BSTNode(2,BSTNode(1),BSTNode(3))
    head=bst_to_doubly_linked_list(root)
    print('Inorder linked:',head.data,head.right.data,head.right.right.data)
    assert head.data==1 and head.right.right.left.data==2
