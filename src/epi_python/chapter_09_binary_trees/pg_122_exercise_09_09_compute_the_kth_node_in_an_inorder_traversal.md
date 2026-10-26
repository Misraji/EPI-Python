# Exercise 9.9: Compute the kth node in an inorder traversal

**Printed textbook page:** 122. **Reference transcription pages:** 122–122.

> **Unverified OCR transcription:** This section retains the supplied PDF text layer. It is not certified verbatim: code syntax, mathematical symbols, and page boundaries may be corrupted. When two exercises begin on the same page, their excerpts overlap. Do not paste extracted code into a `.py` file without manual verification.

#### Printed page 122 (PDF page 136)

```text
popping it, adding first its right child, and then its left child to the stack. (We add the left child after
the right child, since we want to continue with the left child.)
ForthebinarytreeinFigureg.lonPage772, thefirstfewstackstatesare <A>,<l,B),<l,E,C>,
<I,F,E,D), <l,F,E>, <I,F>, <l,G>, <l,H>, and (I). (The top of the stack is the rightmost node in the
sequences.)
def preorder-traversal (tree) :
path, result = [tree], []
rhile path:
curr = path.popo
if curr:
result . append (curr. data)
path += [curr. right , curr. left]
return result
Since we push and pop each node exactly once, the time complexity is O(n),where n is the number
of nodes. The space complexity is O(h), where h is the height of the tree, since, with the possible
exception of the top of the stack, the nodes in the stack correspond to the right children of the nodes
on a path beginning at the root.
9.9 CoNrpurs rrm krH NoDE IN AN TNoRDER TRAvERsAL
It is trivial to find the kth node that appears in an inorder traversal wtthO(n) time complexity, where
r is the number of nodes. However, with additional information on each node, you can do better.
Write a program that efficiently computes the kth node appearing in an inorder traversal. Assume
that each node stores the number of nodes in the subtree rooted at that node.
Hint: Use the divide and conquer principle.
Solution: The brute-force approach is to perform an inorder walk, keeping track of the number of
visited nodes, stopping when the node being visited is the kth one. The time complexity is O(r).
(Consider for example, a left-skewed tree-to get the first node (k = 1) we have to pass through all
the nodes.)
Looking carefully at the brute-force algorithm, observe that it does not take advantage of the
information present in the node. For example, if k is greater than the number of nodes in the left
subtree, the kth node carurot lie in the left subtree. More precisely, if the left subtree has L nodes,
then the kth node in the original tree is the (k - L)th node when we skip the left subtree. Conversely,
if k < L, the desired node lies in the left subtree. For example, the left subtree in Figure 9.1 on
Page L12 has seven nodes, so the tenth node cannot be in the left subtree. Instead it is the third node
if we skip the left subtree. This observation leads to the following program.
def find-kth-node-binary-tree (tree , k) :
while tree:
Ieft-size = tree.left.size 
if tree.left 
else 0
if left-size + 1 < k: # k-th node must be in tight subtree of tree
k -= left-size 
+ 1
tree = tree.right
elif left-size 
== k - 1: # k-th is iter itself.
return tree
else: 
# k-th node fiust be in Teft subtree of iter.
tree = tree. left
122
```
