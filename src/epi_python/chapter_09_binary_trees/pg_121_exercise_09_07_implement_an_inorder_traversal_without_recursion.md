# Exercise 9.7: Implement an inorder traversal without recursion

**Printed textbook page:** 121. **Reference transcription pages:** 121–121.

> **Unverified OCR transcription:** This section retains the supplied PDF text layer. It is not certified verbatim: code syntax, mathematical symbols, and page boundaries may be corrupted. When two exercises begin on the same page, their excerpts overlap. Do not paste extracted code into a `.py` file without manual verification.

#### Printed page 121 (PDF page 135)

```text
9.7 Iltpr,rlrcNr AN INoRDER TRAvERSAL wITHour RECURSToN
This problem is concemed with traversing nodes in a binary tree in an inorder fashion. See Page 113
for details and examples of these traversals. Generally speaking, a traversal computation is easy to
implement if recursion is allowed.
Write a program which takes as input a binary tree and performs an inorder traversal of the tree.
Do not use recursion. Nodes do not contain parent references.
Hinf: Simulate the function call stack.
Solution: The recursive solution is trivial-first traverse the left subtree, then visit the root, and
finally traverse the right subtree. This algorithm can be converted into a iterative algorithm by
using an explicit stack. Several implementations are possible; the one below is noteworthy in that
it pushes the current node, and not its right child. Furthermore, it does not use a visited field.
def inorder-traversal (tree) :
s, result = tl , tl
rhile s or tlee:
if tree:
s. append(tree)
# Going 7eft.
tree = tree. left
else ;
# Going up.
tree = s. pop o
result . append (tree . data)
# Going right,
tree = tree.right
return result
For the binary tree in Figure 9.1 on Page 772, the first few stack states are <A), <A,B>, <A,B,C>,
<A,B,C,D>, <A,B,C), <A,B,D>, <A,B), <A), <A,F>.
The time complexity is O(n ), since the total time spent on each node is O(1). The space complexity
is O(h), where h is the height of the tree. This space is allocated dynamically, specifically it is the
maximum depth of the function call stack for the recursive implementation. See Page 113 for a
definition of tree height.
9.8 IuprErrarNr A pREoRDER TRAvERSAL wITHour RECURSToN
This problem is concemed with traversing nodes in a binary tree in preorder fashion. See Page L13
for details and examples of these traversals. Generally speaking, a traversal computation is easy to
implement if recursion is allowed.
Write a program which takes as input a binary tree and performs a preorder traversal of the tree.
Do not use recursion. Nodes do not contain parent references.
Solution:
We can get intuition as to the best way to perform a preorder traversal without recursion by
noting that a preorder traversal visits nodes in a last in, first out order. We can perform the preorder
traversal using a stack of tree nodes. The stack is initialized to contain the root. We visit a node by
12'l
```
