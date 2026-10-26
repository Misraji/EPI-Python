# Chapter 9: Binary Trees

**Starts at printed page 112.** [Repository overview](../../../README.md)

**Source:** user-supplied EPI Python PDF (2016/2017 edition). **Transcription warning:** PDF text extraction contains OCR errors, especially in code. Consult the original PDF for ambiguous expressions and diagrams.

## Original chapter introduction (unverified PDF text layer)

### Printed page 112

```text
Cueprsn
Binary Trees
The method of solution inooloes the detselopmmt of a theory of finite automata
operating on infinite trees,
- 
"Decidability of Second Order Theories and Automata on Tiees,"
M. O. RearN, 1969
Formally, a binary tree is either empty, or a roof node / together with a left binary tree and a right
binary tree. The subtrees themselves are binary trees. The left binary tree is sometimes referred to
as the left subtree of the root, and the right binary tree is referred to as the right subtree of the root.
Binary trees most commonly occur in the context of binary search trees, wherein keys are stored
in a sorted fashion (Chapter 14 on Page 197). However, *rere are many other applications of binary
trees: at a high level,binary tree are appropriate when dealing with hierarchies.
Figure 9.1 gives a graphical representation of a binary tree. Node A is the root. Nodes B and I
are the left and right children of A.
,l
depth 0
depth 1
depth 2
R
t
I
()
height = 5
/l
t.
\
(-i
(
.)
t1
depth 4
depth 5
Flgure 9.1 : Example of a binary tree. The node depths range from 0 to 5. Node M has the highest depth (5) of any
node in the tree, implying the height of the tree is 5.
Often the node stores additional data. Its prototype is listed as follows:
class BinaryTreeNode:
def --init--(self, 
data=None, left=None, right=None)
self.data = data
self.Ieft 
= left
self.right 
= right
Each node, except the root, is itself the root of a left subtree or a right subtree. If I is the root of
p's left subhee, we will say I is the left child of p, and p is the parent of l; the notion of right child is
r\1
1L2
```

### Printed page 113

```text
similar. If anodeisaleftorarightchildof p,wesayitisachildof p. Notethatwiththeexception
of the root, every node has a unique parent. Usually, but not universally, the node object definition
includes a parent field (which is null for the root). Observe that for any node there exists a unique
sequence of nodes from the root to that node with each node in the sequence being a child of the
previous node. This sequence is sometimes referred to as the search path from the root to the node.
The parent-child relationship defines an ancestor-descendant relationship on nodes in a binary
tree. Specifically, a node is an ancestor of d il it lies on the search path from the root to d. If a node is
an ancestor of d, we say d is a descendant of that node. Our convention is that a node is an ancestor
and descendant of itself. A node that has no descendants except for itself is called ateaf.
The depth of a node n is the number of nodes on the search path from the root to n, not including
nitself. Theheight of abinarytreeisthemaximumdepthof anynodeinthattree. Aleaelof atreeis
all nodes at the same depth. See Figure 9.1 on the preceding page for an example of the depth and
height concepts.
As concrete examples of these concepts, consider the binary tree in Figure 9.L on the facing page.
Node I is the parent of / and O. Node G is a descendant of B. The search path to Lis (A,l,l,K,L).
The depth of N is 4. Node M is the node of maximum depth, and hence the height of the tree is
5. The height of the subtree rooted at B is 3. The height of the subtree rooted at H is 0. Nodes
D,E,H,M,N, and P are the leaves of the tree.
A full binary tree is a binary tree in which every node other than the leaves has two children.
A perfect binary tree is a full binary tree in which all leaves are at the same depth, and in which
every parent has two children. A complete binary tree is a binary tree in which every level, except
possibly the last, is completely filled, and all nodes are as far left as possible. (This terminology is
not universal, e.9., some authors use complete binary tree where we write perfect binary tree.) It is
straightforward to prove using induction that the number of nonleaf nodes in a fulI binary tree is
one less than the number of leaves. A perfect binary tree of height ft contains exactly 2h+1 - 1 nodes,
of which 2h are leaves. A complete binary tree on n nodes has height llognl, A left-skewed tree is
a tree in which no node has a right child; a right-skewed tree is a tree in which no node has a left
child. In either case, we refer to the binary tree as being skewed.
A key computation on a binary tree is traaersing all the nodes in the tree. (Traversing is also
sometimes called walking.) Here are some ways in which this visit can be done.
I Traverse the left subtree, visit the root, then traverse the right subtree (an inorder traversal).
An inorder traversal of the binary tree in Figure 9.1 on the preceding page visits the nodes in
the following order: <D, C, E, B, F, H, G, A, I, L, M, K, N, l, O, P>.
o Visit the root, traverse the left subtree, then traverse the right subtree (apreorder haversal), A
preorder traversal of the binary tree in Figure 9.1 on the facing page visits the nodes in the
following order: (A, B, C, D, E, E, G, H, l, I, K, L, M, N, O, P>.
o Traverse the left subtree, traverse the right subtree, and then visit the root (a postorder traversal).
A postorder traversal of the binary tree in Figure 9.1 on the preceding page visits the nodes
in the following order: (D, E, C, H, G, F, B, M, L, N, K, I, P, O, l, A).
Let I be a binary tree of a nodes, with height h. Implemented recursively, these traversals have
O(n) time complexity md O(h) additional space complexity. (The space complexity is dictated by
the maximum depth of the function call stack.) If each node has a parent field, the traversals can be
done with O(1) additional space complexity.
The term tree is overloaded, which can lead to confusion; see Page 275 tor an overview of the
common variants.
113
```
