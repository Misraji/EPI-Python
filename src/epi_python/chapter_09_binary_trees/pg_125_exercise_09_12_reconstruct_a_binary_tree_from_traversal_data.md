# Exercise 9.12: Reconstruct a binary tree from traversal data

**Printed textbook page:** 125. **Reference transcription pages:** 125–126.

> **Unverified OCR transcription:** This section retains the supplied PDF text layer. It is not certified verbatim: code syntax, mathematical symbols, and page boundaries may be corrupted. When two exercises begin on the same page, their excerpts overlap. Do not paste extracted code into a `.py` file without manual verification.

#### Printed page 125 (PDF page 139)

```text
elif tree.left 
is prev:
# lle cane up to tree fron its TeIt child.
result . append(tree. data)
# Done with 7eft, so go right if right is not enpty
# up.
next = tree.right or tree.parent
else: # Done with both children, so nove up,
nelt = tree. parent
Otherwise, go
prev, tree = tree, nelt
return result
The time complexity is O(n) and the additional space complexity is O(1).
Alternatively, since the successor of a node is the node appearing after it in an inorder visit
sequence, we could start with the left-most node, and keep calling successor. This enables us to
reuse Solution 9.10 on Page 123.
Variant: How would you perform preorder and postorder traversals iteratively using O(1) addi-
tional space? Your algorithm cannot modify the tree. Nodes have an explicit parent field.
9.1,2 RrcoNsrnucr A BTNARy rREE FRoM TRAVERSAL DATA
Maoy different binary trees yield the same sequence of keys in an inorder/ preorder, or postorder
traversal. However, given an inorder traversal and one of any two other traversal orders of a binary
tree, there exists a unique binary tree that yields those orders, assuming each node holds a distinct
key. For example, the unique binary tree whose inorder traversal sequence is <F, B , A, E, H, C, D , I , G>
and whose preorder traversal sequence is (H,B,F,E,A,C,D,G, I) is given in Figure 9.5.
Flgure 9.5: A binary tree-edges that do not terminate in nodes denote empty subtrees.
Given an inorder traversal sequence and a preorder traversal sequence of a binary tree write a
program to reconstruct the tree. Assume each node has a unique key.
Hlnf; Focus on the root.
125
```

#### Printed page 126 (PDF page 140)

```text
Solution: A truly brute-force approach is to enumerate every binary tree on the inorder traversal
sequence, and check if the preorder sequence from that tree is the given one. The complexity is
enormous.
Looking more carefully at the example, the preorder sequence gives us the key of the root
node-it is the first node in the sequence. This in turn allows us to split the inorder sequence into
an inorder sequence for the left subtree, followed by the root, followed by the right subtree.
The next insight is that we can use the left subtree inorder sequence to compute the preorder
sequence for the left subtree from the preorder sequence for the entire tree. A preorder traversal
sequence consists of the root, followed by the preorder traversal sequence of the left subtree,
followed by the preorder traversal sequence of the right subtree. We know the number k of nodes
in the left subtree from the location of the root in the inorder traversal sequence. Therefore, the
subsequence of k nodes after the root in the preorder traversal sequence is the preorder traversal
sequence for the left subtree.
As a concrete example, for the inorder traversal sequence <F,B,A,E,H,C,D,I,G> and preorder
traversal sequence <H,B,F,E,A,C,D,G,I> (in Figure 9.5 on the preceding page) the root is the
first node in the preorder traversal sequence/ namely H. From the inorder traversal sequence,
we know the inorder traversal sequence for the root's left subtree is (F,B,A,E). Therefore the
sequence <B,F,E,A>, which is the four nodes after the root, H, in the preorder traversal sequence
<H,B,F,E,A,C,D,G,I> is the preorder traversal sequence for the root's left subtree. A similar
construction applies to the root's right subtree. This construction is continued recursively till we
get to the leaves.
Implemented naively, the above algorithm has a time complexity of O(n2). The worst-case
corresponds to a skewed tree. Finding the root within the inorder sequences takes time O(n). We
can improve the time complexity by initially building a hash table from keys to their positions in
the inorder sequence. This is the approach described below
def binary-tree-from-preorder-inorder(preorder, inorder) :
node-to-inorder-idx = {data: i for i, data in enunerate(inorder)}
# Builds the subtree with preorder[preorder-start :preorder-end] and
# inorder Iinorder-start: inorder-end] .
def binary-tree-from-preorder-inorder-helper (preorder-start , preorder-end
inorder-start, inorder-end) :
if preorder-end <= preorder-start or inorder-end <= inorder-start:
return None
root-inorder-idx = node-to-inorder-idx Ipreorder Ipreorder-start] l
Ieft-subtree-size = root-inorder-idx - inorder-start
return BinaryTreeNode (
preorder Ipreorder-start],
# RecursiveTy buiTds the Teft subtree.
binary-tree-from-preorder-inorder-helper (
preorder-start + 1, preorder-start + 1 + left-subtree-size,
inorder-start, root-inorder-idx),
# RecursiveTy buiTds the right subtree.
b inary-tr e e-from-pre orde r-i norder-he 1p er (
preorder-start + 1 + Ieft-subtree-size, preorder-end,
root-inorder-idx + 1, inorder-end))
return binary-tree-from-preorder-inorder-helper (0
126
```
