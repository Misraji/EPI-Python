# Exercise 9.6: Find a root to leaf path with specified sum

**Printed textbook page:** 120. **Reference transcription pages:** 120–120.

> **Unverified OCR transcription:** This section retains the supplied PDF text layer. It is not certified verbatim: code syntax, mathematical symbols, and page boundaries may be corrupted. When two exercises begin on the same page, their excerpts overlap. Do not paste extracted code into a `.py` file without manual verification.

#### Printed page 120 (PDF page 134)

```text
][
-rtrtt 
Therefore, we can compute the sum of all root to leaf node as follows. Each time we visit a node,
we compute the integer it encodes using the number for its parent. If the node is a leaf we retum
its integer. If it is not a leaf, we retum the sum of the results from its left and right children.
def sum-root-to-leaf (tree, partial-path-sum=0)
if not tree:
return 0
partial_path-sun = partial-path-sum * 2 + tree.data
if not tree.left and not tree.right: # Leaf.
return partial-path-sum
# Non-7eaf.
return (sum-root-to-Ieaf(tree.Ieft, partial-path-sum) + sum-root-to-leaf(
tree . right , partial-path-sum) )
The time complexity and space complexity areO(n) andO(h), respectively.
9.6 FrNo e Roor ro LEAF pATH wITH spECIFIED suM
You are given a binary tree where each node is labeled with an integer. The path weight of a node in
such a tree is the sum of the integers on the unique path from the root to that node. For the example
shown in Figure 9.1 on Page 1.1.2, the path weight of E is 591.
Write a program which takes as input an integer and a binary tree with integer node weights, and
checks if there exists a leaf whose path weight equals the given integer.
Hint: V,lhatdo you need to know about the rest of the tree when checking a specific subtree?
Solution: The brute-force algorithm in Solution 9.5 on the preceding page can be directly applied
to this problem, and it has the same time complexity, namely, O(Lh), where L is the number of root-
to-leaf paths (which equals the number of leaves), and /z is the tree height. The space complexity is
dominated by the hash table, namely O(ra), where n is the number of nodes.
The inefficiency in the brute-force algorithm stems from the fact that we have overlapping paths,
and we do not share the summation computation across those overlaps.
A better approach is to traverse the tree, keeping track of difference of the root-to-node path
sum and the target value-call this the remaining weight. As soon as we encounter a leaf and the
remaining weight is equal to the leaf 's weight, we retum true. Short circuit evaluation of the check
ensures that we do not process additional leaves.
def has-path-sum(tree, remaining-weight) 
:
if not tree:
return False
if not tree.left and not tree.righti 
# Leaf.
return remaining-weight == tree. data
# Non-7eaf.
return (has-path-sun(tree. Ieft , remaining-weight - tree. data)
or has-path-sum(tree. right , remaining-weight - tree. data))
The time complexity and space complexity areO(n) arrdO(h), respectively.
Variant: Write a program which takes the same inputs as in Problem 9.6 and returns all the paths to
leaveswhoseweightequalss. Forexample,if s = 619,youshouldretum <<A,B,C,D>,<A,l,O,P>>.
1,20
```
