# Exercise 9.14: Form a linked list from the leaves of a binary tree

**Printed textbook page:** 128. **Reference transcription pages:** 128–128.

> **Unverified OCR transcription:** This section retains the supplied PDF text layer. It is not certified verbatim: code syntax, mathematical symbols, and page boundaries may be corrupted. When two exercises begin on the same page, their excerpts overlap. Do not paste extracted code into a `.py` file without manual verification.

#### Printed page 128 (PDF page 142)

```text
The time complexity is O(n), where n is the number of nodes in the tree.
Variant: Solve the same problem when the sequence corresponds to a postorder traversal sequence.
Is this problem solvable when the sequence corresponds to an inorder traversal sequence?
9,1,4 Fonlr a LINKED LIST FRoM THE LEAVES oF A BINARY TREE
In some applications of a binary tree, only the leaf nodes contain actual information. For example,
the outcomes of matches in a tennis toumament can be represented by a binary tree where leaves
are players. The internal nodes correspond to matches, with a single winner advancing. For such a
tree, we can link the leaves to get a list of participants.
Given a binary tree, compute a linked list from the leaves of the binary tree. The leaves should
appear in left-to-right order. For example, when applied to the binary tree in Figure 9.1 on Page 112,
your function should retum <D,E,H,M,N,P>.
Hint: B:ulld the list incrementally-it's easy if the partial list is a global.
Solution: A fairly direct approach is to use two passes-one to compute the leaves, and the other
to assign ranks to the leaves, with the left-most leaf getting the lowest rank. The final result is the
leaves sorted by ascending order of rank.
In fact, it is not necessary to make two passes-if we process the tree from left to right, the leaves
occur in the desired order, so we can incrementally add them to the result. This idea is shown
below.
def create-list-of-leaves (tree) :
if not tree:
return []
if not tree. Ieft and not tree. right:
return Itree]
# Fitst do the left subtree, and then do the right subtree.
return create_Iist-of-Ieaves(tree.left) + create-Iist-of-leaves(tree.right)
The time complexity is O(n), where rz is the number of nodes.
9.75 CoMpure rHE ExTERIoR oF A BINARY TREE
The exterior of a binary tree is the following sequence of nodes: the nodes from the root to
the leftmost leaf, followed by the leaves in left-to-right order, followed by the nodes from the
rightmost leaf to the root. (By leftmost (rightmost) leaf, we mean the leaf that appears first (last)
in an inorder traversal.) For example, the exterior of the binary tree in Figure 9.1 on Page 1L2 is
<A, B, C, D, E, H, M,N, P, O, I>,
Write a program that computes the exterior of a binary tree.
Hlnt; Handle the root's left child and right child in mirror fashion.
Solution: A brute-force approach is to use a case analysis. We need the nodes on the path from the
root to the leftmost leaf, the nodes on the path from the root to the rightmost leaf, and the leaves in
left-to-right order.
128
```
