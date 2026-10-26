# Exercise 14.4: Compute the LCA in a BST

**Printed textbook page:** 203. **Reference transcription pages:** 203–203.

> **Unverified OCR transcription:** This section retains the supplied PDF text layer. It is not certified verbatim: code syntax, mathematical symbols, and page boundaries may be corrupted. When two exercises begin on the same page, their excerpts overlap. Do not paste extracted code into a `.py` file without manual verification.

#### Printed page 203 (PDF page 217)

```text
that it potentially processes many nodes that cannot possibly be in the result, e.g., if k is small and
the left subtree is large.
A better approach is to begin with the desired nodes, and work backwards. We do this by
recursing first on the right subtree and then on the left subtree. This amounts to a reverse-
inorder traversal. For the BST in Figure 14.1 on Page 198, the reverse inorder visit sequence is
<P, O, I, N, K, M, L, I, A, G, H, F, B, E, C, D>.
As soon as we visit k nodes, we can halt. The code below uses a dynamic array to store the
desired keys. As soon as the array has k elements, we refum. We store newer nodes at the end of
the array, as per the problem specification.
To find the five biggest keys in the tree in Figure 14.1 on Page198,we would recurse onA,l,O,P,
in that order. Returning from recursive calls, we would visit P,O,I, in that order, and add their keys
to the result. Then we would recurse on , K N, in that order. Finally, we would visit N and then K,
adding their keys to the result. Then we would stop, since we have five keys in the array.
def find-k-Iargest-in-bst (tree , k) :
def find_k_largest_in_bst_helper(tree) :
# Perform reverse inorder ttaversaT.
if tree and 1en(k-Iargest_elements) < k:
find_k_largest_in_bst_helper (tree . right)
if len(k-largest_elements) < k:
k_Iargest_elements . append(tree . data)
find_k_Iargest_in_bst_helper (tree . Ieft)
k-largest-elements = []
f ind-k-Iarge st-in_bst-helper (tree)
return k-Iargest_elements
The time complexity is O(h + k), which can be much better than performing a conventional inorder
walk, e.g., when the tree is balanced and k is small. The complexity bound comes from the
observation that the number of times the program descends in the tree can be at most h more than
the number of times it ascends the tree, and each ascent happens after we visit a node in the result.
After k nodes have been added to the result, the program stops.
14.4 Corrpurr rnp LCA rN e BST
Since a BST is a specialized binary tree, the notion of lowest corunon ancestor, as expressed in
Problem 9.4 on Page 118, holds for BSTs too.
In general, computing the LCA of two nodes in a BST is no easier than computing the LCA in
a binary tree, since structurally a binary tree can be viewed as a BST where all the keys are equal.
However, when the keys are distinct, it is possible to improve on the LCA algorithms for binary
trees.
Design an algorithm that takes as input a BST and two nodes, and retums the LCA of the two
nodes. For example, for the BST in Figure 14.L on Page 198, and nodes C and G,your algorithm
should retum B. Assume all keys are distinct. Nodes do not have references to their parents.
Hint:Take advantage of the BST property.
Solution: In Solution 9.3 on Page 117 we presented an algorithm for this problem in the context of
binary trees. The idea underlying that algorithm was to do a postorder traversal-the LCA is the
203
```
