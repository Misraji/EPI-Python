# Exercise 9.4: Compute the LCA when nodes have parent pointers

**Printed textbook page:** 118. **Reference transcription pages:** 118–118.

> **Unverified OCR transcription:** This section retains the supplied PDF text layer. It is not certified verbatim: code syntax, mathematical symbols, and page boundaries may be corrupted. When two exercises begin on the same page, their excerpts overlap. Do not paste extracted code into a `.py` file without manual verification.

#### Printed page 118 (PDF page 132)

```text
# Found both nodes in the right subtree.
r€turn right-result
num-target-nodes = (
left-result.num-target-nodes + right-result,num-target-nodes + int(
tree is nodeO) + int(tree is nodel))
return Status(num-target-nodes, tree if num-target-nodes == 2 else None)
return lca-helper(tree, node0, nodel).ancestor
The algorithm is structurally similar to a recursive postorder traversal, and the complexities are the
same. Specifically, the time complexity and space complexity areO(n) andO(h), respectively, where
h is the height of the tree.
9.4 Cor,rpurr rnr LCA wHEN NoDES HAVE pARENT poINTERS
Given two nodes in a binary tree, design an algorithm that computes their LCA. Assume that each
node has a parent pointer.
Hint: The problem is easy if both nodes are the same distance from the root.
Solution: A brute-force approach is to store the nodes on the search path from the root to one of the
nodes in a hash table. This is easily done since we can use the parent field. Then we go up from the
second node, stopping as soon as we hit a node in the hash table. The time and space complexity
are both O(h), where h is the height of the tree.
We know the two nodes have a corunon ancestor, namely the root. If the nodes are at the same
depth, we can move up the tree in tandem from both nodes, stopping at the first common node,
which is the LCA. However, if they are not the same depth, we need to keep the set of traversed
nodes to know when we find the first common node. We can circumvent having to store these
nodes by ascending from the deeper node to get the same depth as the shallower node, and then
performing the tandem upward movement.
For example, for the tree in Figure 9.1 on Page 112, nodes M and P are depths 5 and 3, respectively.
Their search paths are <A,l,l,K,L,Ml and <A,I,O,P>. If we ascend to depth 3 from M,we get to K.
Now when we move upwards in tandem, the first corunon node is I, which is the LCA of M and P.
Computing the depth is straightforward since we have the parent field-the time complexity is
O(h) arrd the space complexity is O(1). Once we have the depths we can perform the tandem move
to get the LCA.
def lca(node-O, node-l):
def get-depth(node):
dePth = 0
rhile node:
dePth += 1
node = node.parent
return depth
depth-O, depth-l = get-depth(node-O), get-depth(node-1)
# Ilakes node-O as the deeper node in order to sinplify the code.
if depth-l > depth-O:
node-0, node-l = node*l, node-0
# Ascends fron the deeper node
118
```
