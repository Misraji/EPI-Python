# Exercise 9.2: Test if a binary tree is symmetric

**Printed textbook page:** 116. **Reference transcription pages:** 116–116.

> **Unverified OCR transcription:** This section retains the supplied PDF text layer. It is not certified verbatim: code syntax, mathematical symbols, and page boundaries may be corrupted. When two exercises begin on the same page, their excerpts overlap. Do not paste extracted code into a `.py` file without manual verification.

#### Printed page 116 (PDF page 130)

```text
the corresponding right subtree. The function call stack corresponds to a sequence of calls from the
root through the unique path to the current node, and the stack height is therefore bounded by the
height of the tree, leading to an O(h) space bound. The time complexity is the same as that for a
postorder traversal, namely O(n).
Variant: Write a program that retums the size of the largest subtree that is complete.
Varianh Define a node in a binary tree to be k-balanced if the difference in the number of nodes in
its left and right subtrees is no more than k. Design an algorithm that takes as input a binary tree
and positive integer k, and retums a node in the binary tree such that the node is not k-balanced,
but all of its descendants are k-balanced. For example, when applied to the binary tree in Figure 9.1
on Page 1,1,2, if k = 3, your algorithm should retum Node /.
9.2 Tssr rr A BTNARy rREE IS syMMETRIC
A binary tree is symmetric if you can draw a vertical line through the root and then the left subtree
is the mirror image of the right subtree. The concept of a symmetric binary tree is illustrated in
Figure 9.3.
t\
j,,
t.
ll
L
t_
/l
('
(.
/)
ir
a;
/)
(a) A symmetric binary tree. 
(b) An asymmetric binary tree. 
(c) An asymmetric binary tree.
Figure 9.3: Symmetric and asymmetric binary trees. The tree in (a) is symmetric. The tree in (b) is structurally
symmetric, but not symmetric, because symmetry requires that conesponding nodes have the same keys; here C and
F as well as D and G break symmetry. The tree in (c) is asymmetric because there is no node conesponding to D.
Write a program that checks whether a binary tree is symmetric.
Hint:The definition of symmetry is recursive.
Solution: We can test if a tree is symmetric by computing its mirror image and seeing if the mirror
image is equal to the original tree. Computing the mirror irnage of a tree is as simple as swapping
the left and right subtrees, and recursively continuing. The time and space complexity are both
O(n),where n is the number of nodes in the tree.
The insight to a better algorithm is that we do not need to construct the mirrored subtrees. All
that is important is whether a pair of subtrees are mirror images. As soon as a pair fails the test, we
can short circuit the check to false. This is shown in the code below.
def is_symmetric (tree) :
def check-symmetric (subtree-0 , subtree-1) :
if not subtree-0 and not subtree-l:
return True
elif subtree-0 and subtree-1:
return (subtree-0. data == subtree-1. data
314
6
6
561
561
3
11,6
```
