"""EPI Python — Exercise 24.13: Implement a Postorder Traversal Without Recursion

Chapter 24: Honors Class
Textbook: pages 366–368 (printed page numbers; problem introduction on 366,
statement, hint, first program and discussion on 367, second program and
analysis on 368).

PROBLEM (from the textbook)
---------------------------
This problem is concerned with traversing nodes in a binary tree in
postorder fashion. See Page 113 for details and examples of these
traversals. Generally speaking, a traversal computation is easy to
implement if recursion is allowed.

Write a program which takes as input a binary tree and performs a postorder
traversal of the tree. Do not use recursion. Nodes do not contain parent
references.

HINT (from the textbook)
------------------------
Study the function call stack for the recursive versions.

SOLUTION DEVELOPMENT (following the textbook)
---------------------------------------------
The brute-force way to remove recursion is to imitate the function call
stack with an explicit stack; a difficulty is knowing where to "return to".

Roundabout approach first. An inverted preorder traversal visits the root,
then traverses the right subtree with inverted preorder, then the left
subtree. For the tree in Figure 9.1 on Page 112 it visits
<A, I, O, P, J, K, N, L, M, B, F, G, H, C, E, D>.
Because inverted preorder is "root, right, left", its reverse is "left,
right, root" — exactly postorder. So: do an inverted preorder traversal,
storing the nodes instead of outputting them, then read them back in
last-in, first-out order. The inverted preorder itself can be done
nonrecursively with the stack-based preorder technique, pushing the left
and right children in swapped order. This is the book's first program
(`postorder_traversal` with a nested `inverted_preorder_traversal`); here it
is `postorder_traversal_via_reverse`.

After the first program's analysis (see below), the book develops an O(h)
space method. A recursive postorder uses O(n) time and O(h) space, so a
stack imitating the call stack should achieve the same. The challenge is
knowing where to return to: there are two recursive calls, and a real call
stack stores a return address that user code cannot access. Instead,
decide where to continue by looking at where the previously visited node
lies relative to the current one:
  * keep a stack of nodes that evolves exactly like the sequence of nodes
    from which the recursive algorithm makes calls;
  * to know whether a nonleaf on top of the stack is ready to be visited,
    determine whether we are moving back up the tree and, if so, from which
    side;
  * coming up from the left: do not push the left child again, but do push
    the right child (imitating the second recursive call);
  * coming up from the right: both children are done, so pop the stack and
    visit the nonleaf.
This is the book's second program, `postorder_traversal`, implemented here
under the same name.

ADDITIONAL EXAMPLES (added for learning; not printed in this exercise)
---------------------------------------------------------------------
        1
       / \\
      2   3        postorder: [4, 2, 3, 1]
     /
    4
"""


class BinaryTreeNode:
    """Binary tree node (helper; the book defines it in its trees chapter).

    __init__ is the initializer run by BinaryTreeNode(...). Tuple assignment
    stores all three fields in one statement; `left=None, right=None` are
    default arguments meaning "no child".
    """
    def __init__(self,data,left=None,right=None):
        self.data,self.left,self.right=data,left,right


def postorder_traversal_via_reverse(tree: BinaryTreeNode | None) -> list[int]:
    """Textbook solution 1: inverted preorder traversal, then reversed.

    O(n) time and O(n) space. The hint `BinaryTreeNode | None` means "a node
    or None" (`|` in annotations needs Python 3.10+); Python does not
    enforce type hints.
    """

    # The list is used as a stack (append/extend push to the end, pop
    # removes from the end). It starts with the root, which may be None.
    path_stack,result=[tree],[]
    while path_stack:
        curr=path_stack.pop()

        # Skip missing children (None is falsy). `continue` jumps to the next
        # loop iteration. A one-statement body may follow the colon.
        if not curr:continue
        result.append(curr.data)

        # list.extend(iterable) appends each item in order. Pushing left
        # THEN right means right is popped first: root, right, left — the
        # inverted preorder.
        path_stack.extend([curr.left,curr.right])

    # Slicing with step -1, `[::-1]`, returns a reversed copy of the list:
    # reversing inverted preorder yields postorder.
    return result[::-1]


def postorder_traversal(tree: BinaryTreeNode | None) -> list[int]:
    """Textbook solution 2: explicit stack plus previous-node pointer, O(h) space.

    We use stack and previous node pointer to simulate postorder traversal.
    """

    # Empty tree.
    if not tree:return []

    # Tuple assignment: the stack starts with the root; prev is the node
    # handled in the previous iteration.
    path_stack,prev,postorder_sequence=[tree],None,[]
    while path_stack:

        # Index -1 reads the top of the stack without removing it.
        curr=path_stack[-1]

        # We came down to curr from prev (or curr is the root).
        # `is` tests object identity: is curr exactly prev's child object?
        if not prev or prev.left is curr or prev.right is curr:

            # Traverse left if possible, otherwise right; a leaf is visited
            # and popped.
            # `a;b` puts two simple statements on one line; after `else:`
            # BOTH belong to the else branch.
            if curr.left:path_stack.append(curr.left)
            elif curr.right:path_stack.append(curr.right)
            else:postorder_sequence.append(curr.data);path_stack.pop()

        # Done with left, now traverse right (or visit curr if there is no
        # right child).
        elif curr.left is prev:
            if curr.right:path_stack.append(curr.right)
            else:postorder_sequence.append(curr.data);path_stack.pop()

        # Finished traversing left and right, so visit curr.
        else:
            postorder_sequence.append(curr.data);path_stack.pop()
        prev=curr
    return postorder_sequence


# TEXTBOOK POST-SOLUTION DISCUSSION (pages 367–368)
# -------------------------------------------------
# Solution 1: time and space are both O(n), n the number of nodes. Besides
# being unintuitive, it needs O(n) additional space. That is unavoidable if
# the result must be returned as an array, but if the nodes only need to be
# printed the space can be reduced to O(h), h the height of the tree —
# which motivates solution 2.
#
# Solution 2: O(n) time, constant work per node (a push and a pop). O(h)
# space, since the stack always holds a path starting at the root.
#
# VARIANTS
# The book gives no variants for this exercise.


# TEXTBOOK CODE COMPARISON
# ------------------------
# Solution 1 — book: `def postorder_traversal(tree)` containing a nested
#   `def inverted_preorder_traversal(tree)`, returning
#   `inverted_preorder_traversal(tree)[::-1]`.
#   file: renamed `postorder_traversal_via_reverse(tree: BinaryTreeNode |
#   None) -> list[int]`; the nested function is inlined into the body;
#   `if not curr: continue` written on one line. Same algorithm.
# Solution 2 — book: `def postorder_traversal(tree)` with each statement on
#   its own line and explanatory comments.
#   file: same name, type hints added; the same branches compressed onto
#   single lines (`if ...: stmt`, `else: stmt; stmt`). Statements otherwise
#   match the book.
# Helper: class `BinaryTreeNode` is defined in the file (the book defines it
#   in its binary trees chapter, not here).


# Python executes this block only when this source file is run directly.
# When pytest imports the file, this block is skipped automatically.
# Documentation: https://docs.python.org/3/library/__main__.html
if __name__=='__main__':

    # Tree 1 with children 2 (whose left child is 4) and 3; postorder is
    # 4, 2, 3, 1.
    # A chained comparison `x == y == z` means `x == y and y == z`, so the
    # assert checks that both implementations agree with the expected list.
    # `assert` raises AssertionError on mismatch; the tests/ folder holds
    # the thorough pytest suite.
    tree=BinaryTreeNode(1,BinaryTreeNode(2,BinaryTreeNode(4)),BinaryTreeNode(3))
    print('Postorder:',postorder_traversal(tree))
    assert postorder_traversal(tree)==postorder_traversal_via_reverse(tree)==[4,2,3,1]
