"""EPI Python 24.13, textbook printed page 366: Implement a postorder traversal without recursion.

QUESTION: Return a tree postorder traversal without recursion.

TEXTBOOK ALGORITHM: Preserve book inverted-preorder-plus-reverse and stack-with-previous-pointer alternatives.

The complete question, hints, solution development, and variants are in the
adjacent page-numbered reference Markdown, extracted from the supplied PDF.
This executable implementation restores syntax damaged by the PDF text layer;
minor type annotations, examples, and assertions are educational additions.

Run: python -m epi_python.chapter_24_honors_class.pg_366_postorder_traversal
Test: python -m pytest tests/chapter_24_honors_class/test_pg_366_postorder_traversal.py -v
"""

class BinaryTreeNode:
    def __init__(self,data,left=None,right=None):
        self.data,self.left,self.right=data,left,right


def postorder_traversal_via_reverse(tree: BinaryTreeNode | None) -> list[int]:
    path_stack,result=[tree],[]
    while path_stack:
        curr=path_stack.pop()
        if not curr:continue
        result.append(curr.data)
        path_stack.extend([curr.left,curr.right])
    return result[::-1]


def postorder_traversal(tree: BinaryTreeNode | None) -> list[int]:
    if not tree:return []
    path_stack,prev,postorder_sequence=[tree],None,[]
    while path_stack:
        curr=path_stack[-1]
        if not prev or prev.left is curr or prev.right is curr:
            if curr.left:path_stack.append(curr.left)
            elif curr.right:path_stack.append(curr.right)
            else:postorder_sequence.append(curr.data);path_stack.pop()
        elif curr.left is prev:
            if curr.right:path_stack.append(curr.right)
            else:postorder_sequence.append(curr.data);path_stack.pop()
        else:
            postorder_sequence.append(curr.data);path_stack.pop()
        prev=curr
    return postorder_sequence


if __name__=='__main__':
    tree=BinaryTreeNode(1,BinaryTreeNode(2,BinaryTreeNode(4)),BinaryTreeNode(3))
    print('Postorder:',postorder_traversal(tree))
    assert postorder_traversal(tree)==postorder_traversal_via_reverse(tree)==[4,2,3,1]
