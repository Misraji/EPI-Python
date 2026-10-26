# Exercise 9.1: Test if a binary tree is height-balanced

**Printed textbook page:** 114. **Reference transcription pages:** 114–115.

> **Unverified OCR transcription:** This section retains the supplied PDF text layer. It is not certified verbatim: code syntax, mathematical symbols, and page boundaries may be corrupted. When two exercises begin on the same page, their excerpts overlap. Do not paste extracted code into a `.py` file without manual verification.

#### Printed page 114 (PDF page 128)

```text
Binary treesboot caffip
A good way to get up to speed withbinary trees is to implement the three basic traversals-inordef,
preorder, and postorder.
def tree-traversal (root) :
if root:
# Pteorder: Processes the root before the traversaTs of Teft and right
# chiTdren.
print('Preorder: %d' % root.data)
tree-traversal (root . left)
# Inorder: Processes the root after the traversa-I of Teft chiTd and
# before the traversaT of right chiLd.
print ('Inorder : %d' % root . data)
tree-traversal (root . right)
# Postotder.' Processes the root after the traversa-Is of Teft and right
# chiTdren.
print ('Postorder : %d' % root . data)
The time complexity of each approach isO(n),where n is the number of nodes in the tree. Although
no memory is explicitly allocated, the function call stack reaches a maximum depth of h, the height
of the tree. Therefore, the space complexity is O(h). The minimum value for h is logn (complete
binary tree) and the maxirnum value for h is rz (skewed tree).
are
to
on trees.
to
sPace
itly allocated on the function call stack when doing space complexity analysis. Please read the
introduction to Chapter 15 if you need a refresher on recursion.
Some tree problems have simple brute-force solutions that use O(n) space,but subtler solutions
that use the existing tree nodes to reduce space comPlexity to O(1).
Consider left- and right-skewed trees when doing complexity analysis. Note that O(h) com-
plexity, where h is the tree height, translates into O(logn) complexity for balanced trees, but
O(n) complexity for skewed trees.
If each node has a parent field, use it to make your code simpler, and to reduce time and space
complexity.
!t's easy to make the mistake of treating a nodg th3!ha.s a single child as a leaf.
Table 9.1 : Top Tips for Binary Trees
9.7 Trsr rr A BTNARy rREE IS HEIGTm-BALANcED
A binary tree is said to be height-balanced if for each node in the tree, the difference in the height of
its left and right subtrees is at most one. A perfect binary tree is height-balanced, as is a complete
binary tree. A height-balanced binary tree does not have to be perfect or complete-see Figure 9.2
on the next page for an example.
Write a program that takes as input the root of a binary tree and checks whether the tree is height-
balanced.
Hlnf: Think of a classic binary tree algorithm.
114
```

#### Printed page 115 (PDF page 129)

```text
,,\
h
IJ
C
Lt
L
tl
l)
(;
I
I:
Flgure 9.2: A height-balanced binary tree of height 4.
Solution: Here is a brute-force algorithm. Compute the height for the tree rooted at each node r
recursively. The basic computation is to compute the height for each node starting from the leaves,
and proceeding upwards. For each node, we check if the difference in heights of the left and right
children is greater than one. We can store the heights in a hash table, or in a new field in the nodes.
This entails O(n ) storage and O(n) time, where n is the number of nodes of the tree.
We can solve this problem using less storage by observing that we do not need to store the
heights of all nodes at the same time. Once we are done with a subtree, all we need to know is
whether it is height-balanced, and if so, what its height is-we do not need any information about
descendants of the subtree's root.
def is-balanced-binary_tree (tree) :
BalancedStatusliithHeight = collections. namedtuple (
'BalancedStatusttithHeight', ('balanced','height'))
# First vaTue of the return value indicates i.f tree js baTanced, and if
# baTanced the second value of the return vaTue is tie height of tree,
def check-balanced(tree) 
:
if not tree:
return BalancedStatuswithHeight(True, -1) # Base case.
left-result 
= check-balanced(tree.left)
if not left-result.balanced:
# Left subtree is not balanced.
return BalancedStatusI{ithHeight(FaIse, 0)
right-result 
= check-balanced(tree,right)
if not right-result 
. balanced:
# Right subtree is not balanced.
return Balancedstatusl{ithfieight (FaIse, 0)
is_balanced = abs(left_result.height - right_result.height) <= I
height = nar(left-result.height, right_result.height) + 1
return BalancedStatusWithHeight(is_balanced, height)
return check_balanced (tree) . balanced
The program implements a postorder traversal with some calls possibly being eliminated because
of early terminafion. Specifically, if any left subtree is not height-balanced we do not need to visit
115
```
