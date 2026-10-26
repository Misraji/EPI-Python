# Exercise 9.5: Sum the root-to-leaf paths in a binary tree

**Printed textbook page:** 119. **Reference transcription pages:** 119–119.

> **Unverified OCR transcription:** This section retains the supplied PDF text layer. It is not certified verbatim: code syntax, mathematical symbols, and page boundaries may be corrupted. When two exercises begin on the same page, their excerpts overlap. Do not paste extracted code into a `.py` file without manual verification.

#### Printed page 119 (PDF page 133)

```text
depth-diff = abs(depth-O - depth-1)
rhile depth-diff:
node-0 = node-O. parent
depth-diff -= 1
# Now ascends both nodes until we reach the LCA.
rhile node-O is not node-l:
node-O , node-l = node-O. parent , node-l . parent
return node_0
The time and space complexity are that of computing the depth, namely O(h) and O(1), respectively.
9.5 Suvr rup Roor-To-LEAF pATHS rN A BTNARy rREE
Consider a binary tree in which each node contains a binary digit. A root-to-leaf path can be
associated with a binary number-the MSB is at the root, As an example, the binary tree in
Figure 9.4 represents the numbers (1000)2, (1001)2, (10110)2, (110011)2, (11000)2, and (1100)2.
,\
li
C
()
l)
t:
(
ti
N
!\1
FIgure 9.4: Binary tree encoding integers.
Design an algorithm to compute the sum of the binary numbers represented by the root-to-leaf
paths.
Hint: Thtnk of an appropriate way of traversing the tree.
Solution: Here is a brute-force algorithm. We compute the leaves, and store the child-parent
mapping in a hash table, e.g., via an inorder walk. Afterwards, we traverse from each of the leaves
to the root using the child-parent map. Each leaf-to-root path yields a binary integer, with the leaf 's
bit being the LSB. We sum these integers to obtain the result. The time complexity is O(Lh), where
L is the number of root-to-leaf paths (which equals the number of leaves), and h is the tree height.
The space complexity is dominated by the hash table, namely O(m), where n is the number of nodes.
The insight to improving complexity is to recognize that paths share nodes and that it is not
necessary to repeat computations across the shared nodes. To compute the integer for the path from
the root to any node, we take the integer for the node's parent, double it, and add the bit at that
node. For examplg the integer for the path from A to L is 2 x (1100) z * 1 = (11001)2,
1,19
```
