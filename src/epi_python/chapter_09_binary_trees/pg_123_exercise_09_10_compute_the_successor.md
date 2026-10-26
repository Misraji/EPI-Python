# Exercise 9.10: Compute the successor

**Printed textbook page:** 123. **Reference transcription pages:** 123–123.

> **Unverified OCR transcription:** This section retains the supplied PDF text layer. It is not certified verbatim: code syntax, mathematical symbols, and page boundaries may be corrupted. When two exercises begin on the same page, their excerpts overlap. Do not paste extracted code into a `.py` file without manual verification.

#### Printed page 123 (PDF page 137)

```text
return None # If k is between 1 and the tree size, thjs is unreachable
Since we descend the tree in each iteration, the time complexity is O(h), where h is the height of the
tree
9.1,0 Cor"rpurr rr{E succEssoR
The successor of a node in a binary tree is the node that appears immediately after the given node
in an inorder traversal. For example, in Figure 9.1 on Page 112, the successor of G is A, and the
successor of Ais l.
Design an algorithm that computes the successor of a node in a binary tree. Assume that each node
stores its parent.
Hint: Stady the node's right subtree. What if the node does not have a right subtree?
Solution: The brute-force algorithm is to perform the inorder walk, stopping immediately at the
first node to be visited after the given node. The time complexity is that of an inorder walk, namely
O(n),where r is the number of nodes.
Looking more carefully at the structure of the tree, observe that if the given node has a nonempty
right subtree, its successor must lie in that subtree, and the rest of the nodes are immaterial. For
example, in Figure 9.1 on Page l1,Z,regardless of the structure of A's left subtree, A's successor must
lie in the subtree rooted at L Similarly, B's successor must lie in the subtree rooted at F. Furthermore,
when a node has a nonempty right subtree, its successor is the first node visited when performing
an inorder traversal on that subtree. This node is the "left-most" node in that subtree, and can be
computed by following left children exclusively, stopping when there is no left child to continue
from.
The challenge comes when the given node does not have a right subtree, e.g., H in Figure 9.1 on
Page 712. If the node is its parent's left child, the parent will be the next node we visit, and hence
is its successor, e.9., G is H's successor, If the node is its parent's right child, e.g., G, then we have
already visited the parent. We can determine the next visited node by iteratively following parents,
stopping when we move up from a left child. For example, from G we traverse F, then B, then A.
We stop at A, since B is the left child of A-the successor of G is A.
Note that we may reach the root without ever moving up from a left child. This happens when
the given node is the last node visited in an inorder traversal, and hence has no successor. Node P
in Figure 9.1 on Page 172 illustrates this scenario.
def find-successor (node) :
if node. right:
# Successor is the leftnost el.enent in node 's right subtree
node = node. right
rhile node. left:
node = node.Ieft
return node
# Find the closest ancestor nhose left subtree contains node
rhile node. parent and node . parent . right is node:
node = node. parent
# A teturn value of lVone fieans node does not have successor, i.e,, 
node is
123
```
