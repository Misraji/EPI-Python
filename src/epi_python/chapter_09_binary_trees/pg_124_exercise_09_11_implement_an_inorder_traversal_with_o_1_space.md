# Exercise 9.11: Implement an inorder traversal with O(1) space

**Printed textbook page:** 124. **Reference transcription pages:** 124–124.

> **Unverified OCR transcription:** This section retains the supplied PDF text layer. It is not certified verbatim: code syntax, mathematical symbols, and page boundaries may be corrupted. When two exercises begin on the same page, their excerpts overlap. Do not paste extracted code into a `.py` file without manual verification.

#### Printed page 124 (PDF page 138)

```text
# the rightnost node jn the tree
return node . parent
Since the number of edges followed cannot be more than the tree height, the time complexity is
O(h), where h is the height of the tree.
9.1,1 hupmlmNr AN INoRDER TRAvERSAL wrru O(1) sracE
The direct implementation of an inorder traversal using recursion has O(h) space comPlexity, where
h is the height of the tree. Recursion can be removed with an explicit stack, but the space complexity
remains O(h).
Write a nonrecursive program for computing the inorder traversal sequence for a binary tree.
Assume nodes have parent fields.
Hint: How can you tell whether a node is a left child or right child of its parent?
Solution: The standard idiom for an inorder traversal is traverse-Ieft, visit-root, traverse-right.
\Atrhen we complete traversing a subtree we need to retum to its parent. What we do after that
depends on whether the subtree we returned from was the left subtree or right subtree of the
parent. In the former, we visit the parent, and then its right subtree; in the latter, we refurn from
the parent itself.
One way to do this traversal without recursion is to record the parent node for each node
we begin a traversal from. This can be done with a hash table, and entails O(n) time and space
complexity for the hash table, where n is the number of nodes, and h the height of the tree. The
space complexity can be reduced to O(h) by evicting a node from the hash table when we complete
traversing the subtree rooted at it.
For the given problem, since each node stores its parent, we do not need the hash table, which
improves the space complexity to O(1).
To complete this algorithm, we need to know when we retum to a parent if the just completed
subtree was the parent's left child (in which case we need to visit the parent and then traverse
its right subtree) or a right subtree (in which case we have completed traversing the parent). We
achieve this by recording the subtree's root before we move to the parent. We can then compare the
subtree's root with the parent's left child. For example, for the tree in Figure 9.1 on Page 112, after
traversing the subtree rooted at C, when we retum to B, we record C. Since C is B's left child, we
still need to traverse B's right child. \Atrhen we return from F to B, we record F. Since F is not B's left
child, it must be B's right child, and we are done traversing B.
def inorder-traversal (tree) :
prev, result = None, []
while tree:
if prev is tree. parent:
# We came down to tree from prev,
if tree. left: 
# Keep going 7eft.
nert = tree. left
else:
result . append (tree . data)
# Done with left , so go right if right is not enpty
# go up.
nert = tree.right or tree.parent
124
0therlr'ise,
```
