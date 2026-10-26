# Exercise 9.16: Compute the right sibling tree

**Printed textbook page:** 129. **Reference transcription pages:** 129–131.

> **Unverified OCR transcription:** This section retains the supplied PDF text layer. It is not certified verbatim: code syntax, mathematical symbols, and page boundaries may be corrupted. When two exercises begin on the same page, their excerpts overlap. Do not paste extracted code into a `.py` file without manual verification.

#### Printed page 129 (PDF page 143)

```text
We already know how to compute the leaves in left-to-right order (Solution 9.74 on the facing
Page). The path from root to leftmost leaf is computed by going left if a left child exists, and otherwise
going right. When we reach a leaf, it must be the leftmost leaf. A similar computation yields the
nodes on the path from the root to the rightmost leaf. The time complexity rs O(h + n + h) = O(n),
where n andh are the number of nodes and the height of the tree, respectively. The implementation
is a little tricky, because some nodes appear in multiple sequences. For example, in Figure 9.L on
PageLL2, the path from the root to the leftmost leaf is (A,B,C, D), the leaves in left-to-right order are
<D,E,H,M,N,P), and the path from the root to the rightmost leaf is (A,I,O,P). Note the leftmost
leaf , D, the rightmost leaf, P, and the root, A, appear in two sequences.
We can simplify the above approach by computing the nodes on the path from the root to the
leftmost leaf and the leaves in the left subtree in one traversal. After that, we find the leaves in
the right subtree followed by the nodes from the rightmost leaf to the root with another traversal.
This is the program shown below. For the tree in Figure 9.1 on Page 112, the first traversal refums
<B,C,D,E,H), and the second traversal retums <M,N,P,O,[. We append the first and then the
second sequences to (A).
def exterior-binary-tree (tree) :
def is_Ieaf(node):
return not node.left and not node.right
# Computes the nodes fron the root to the leftmost leaf foTTowed by a7l
# the Teaves in subtree,
def Ieft-boundary-and_leaves (subtree , is_boundary) :
if not subtree:
return []
return (([subtree] if is_boundary
or is_Ieaf(subtree) else []) + left_boundary_and_leaves(
subtree. left , is_boundary) + Ieft_boundary_and_leaves (
subtree. right , is-boundary and not subtree. left))
# Conputes the Ieaves in left-to-right order foTTowed by the rightnost
# Teaf to the root path in subtree.
def right-boundary-and-Ieaves(subtree, 
is_boundary) :
if not subtree:
return []
return (right_boundary_and_leaves (subtree . left , is_boundary
and not subtree.right) +
right_boundary_and_leaves (subtree. right, is_boundary) +
([subtree] if is_boundary or is_Ieaf(subtree) else []))
return ([tree] + Ieft_boundary_and_leaves(tree.left, is_boundary=True) +
right-boundary_and_leaves (tree. right, 
is_boundary=True)
if tree else [])
The time complexity isO(n).
9,1,6 CoMpurs rHE RrcHT srBLrNG TREE
For this Problem, assume that each binary tree node has a extra field, call it level-nex! that holds a
binary tree node (this field is distinct from the fields for the left and right children). The level-next
129
```

#### Printed page 130 (PDF page 144)

```text
.1
ll
L
(
14
I. 
(;
/Ji\
/N
I)
()
Figure 9.6: Assigning each node's level-next field to its right sibling in a perfect binary tree. A dashed arrow indicates
the value held by the level-next field after the update. No dashed arrow is shown for the nodes on the path trom the root
to the rightmost leaf, i.e., A,l,M, and O, since these nodes have no right siblings.
field will be used to compute a map from nodes to their right siblings. The input is assumed to be
perfect binary tree. See Figure 9.6 for an example.
Write a program that takes a perfect binary tree, and sets each node's level-next field to the node on
its right, if one exists.
Hlnt: Think of an appropriate traversal order.
Solution: A brute-force approach is to compute the depth of each node, which is stored in a hash
table. Next we order nodes at the same depth using inorder visit times. Then we set each node's
level-next field according to this order. The time and space complexity are O(n), where n is the
number of nodes.
The key insight into solving this problem with better space complexity is to use the structure of
the tree. Since it is a perfect binary tree, for a node which is a left child, its right sibling is just its
parent's right child. For a node which is a right child, its right sibling is its parent's right sibling's
left child. For example in Figure 9.6, since C is B's left child, C's right sibling is B's right child, i.e.,
F. Since Node F is B's right child, F's right sibling is B's right sibling's left child, i.e., /.
For this approach to work, we need to ensure that we process nodes level-byJevel, left-to-right.
Traversing a level in which the level-next field is set is trivial. As we do the traversal, we set the
level-next fields for the nodes on the level below using the principle outlined above. To get to the
next level, we record the starting node for each level. \A/hen we complete that level, the next level
is the starting node's left child.
def construct-right-sibling (tree) :
def populate-children-next-field(start-node) 
:
rhile start-node and start-node. left:
# PopuTate Teft chiTd's nert field.
start-node. left . next = start-node. right
# Popufate right child's next field if iter is not the Tast node of
# 7eve7.
start-node. right. next = start-node. next and start-node. next. Ieft
start-node = start-node.next
rhile tree and tree, Ieft:
popul ate-chi ldren-next-fi eI d ( tree )
tree = tree. Ieft
130
```

#### Printed page 131 (PDF page 145)

```text
.A
ti
C
(;
t
I1
Flgure 9.7: Assigning each node's level-next lield to its rlght sibling in a general binary tree. A dashed arrow indicates
the value held by the leveFnext field after the update.
Since we perform O(t) computation per node, the time complexity is O(n), The space complexity is
o(1).
Varianh Solve the same problem when there is no level-next field. Your result should be stored in
the right child field.
Variant Solve the same problem for a general binary hee. See Figure 9.7 for an example.
t)
131
```
