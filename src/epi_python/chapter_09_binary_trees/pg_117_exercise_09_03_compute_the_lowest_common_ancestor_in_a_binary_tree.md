# Exercise 9.3: Compute the lowest common ancestor in a binary tree

**Printed textbook page:** 117. **Reference transcription pages:** 117–117.

> **Unverified OCR transcription:** This section retains the supplied PDF text layer. It is not certified verbatim: code syntax, mathematical symbols, and page boundaries may be corrupted. When two exercises begin on the same page, their excerpts overlap. Do not paste extracted code into a `.py` file without manual verification.

#### Printed page 117 (PDF page 131)

```text
and check_symnetric (subtree_0. left , subtree_l . right)
and check_symmetric(subtree_0.right, subtree_1. Ieft))
# One subtree is empty, and the other is not.
return FaIse
return not tree or check_symmetric (tree. Ieft , tree. right)
The time complexity and space complexity are O(n) and O(h), respectively, where n is the number
of nodes in the tree and h is the height of the tree.
9.3 Coupurr rHE LowEsr coMMoN ANCESToR rN A BTNARy rREE
Any two nodes in a binary tree have a corunon ancestor, namely the root. The lowest corunon
ancestor (LCA) of any two nodes in a binary tree is the node furthest from the root that is an ancestor
of both nodes. For example, the LCA of M and N in Figure 9.1 on Page 112 is K.
Computing the LCA has important applications. For example, it is an essential calculation
when rendering web pages/ specifically when computing the Cascading Style Sheet (CSS) that is
applicable to a particular Document Object Model (DOM) element.
Design an algorithm for computing the LCA of two nodes in a binary tree in which nodes do not
have a parent field.
Hinf: lAlhen is the root the LCA?
Solution: A brute-force approach is to see if the nodes are in different immediate subtrees of the
root, or if one of the nodes is the root. Lr this case, the root must be the LCA. If both nodes are in
the left subtree of the root, or the right subtree of the root, we recurse on that subtree. The time
complexity is O(n2), where n is the number of nodes. The worst-case is a skewed tree with the two
nodes at the bottom of the tree.
The insight to a better time complexity is that we do not need to perform multiple passes. If the
two nodes are in a subtree, we can compute the LCA directly, instead of simply retuming a Boolean
indicating that both nodes are in that subtree. The program below retums an object with two
fields-the first is an integer indicating how many of the two nodes were present in that subtree,
and the second is their LCA, if both nodes were present.
def lca(tree, node0, nodel):
Status = colLections . namedtuple ('Status ' , ('num_target_nodes , , ,ancestor ') )
# Returns an object consisting of an int and a node. The int field js 0,
# 7, or 2 depending on how nany of {node0, nodeT} are present in tree. If
# both are present in tree, when ancestor is assigned to a non-null va7ue,
# it is the LCA.
def lca-helper(tree, node0, nodel):
if not tree:
return Status (0, None)
left-result 
= Ica-helper (tree. Ieft , node0, nodel)
if Ieft-result.num-target-nodes == 2:
# Found both nodes in the left subtree.
return left_result
right-result 
= lca-helper(tree.right, 
node0, nodel)
if right-result.num-target-nodes == 2:
117
```
