# Exercise 24.22: Merge two BSTs

**Printed textbook page:** 379. **Reference transcription pages:** 379–379.

> **Unverified OCR transcription:** This section retains the supplied PDF text layer. It is not certified verbatim: code syntax, mathematical symbols, and page boundaries may be corrupted. When two exercises begin on the same page, their excerpts overlap. Do not paste extracted code into a `.py` file without manual verification.

#### Printed page 379 (PDF page 393)

```text
return HeadAndTail(None, None)
# RecursiveTy builds the list fron Teft and right subtrees
left = bst_to_doubly_linked_list_helper(tree. Ieft)
right = bst_to_doubly_linked_list_helper(tree. right)
# Appends tree to tfie list fron Teft subtree
if left. tail:
left. tail . right = tree
tree. left = left. tail
# Appends the list fron right subtree to tree
tree. right = right. head
if right.head:
right. head. left = tree
return HeadAndTail(left.head or tree, right.tail or tree)
return bst-to_doubly_linked_li st_helper (tree) . head
Since we do a constant amount of work per tree node, the time complexity is O(n). The space
comPlexity is the maximum depth of the function call stack, i.e., O(h),where fu is the height of the
BST. The worst-case is for a skewed tree-m activation records are pushed on the stack.
24.22 Mrncr rwo BSTs $
Given two BSTs, it is straightforward to create a BST containing the union of their keys: traverse
one, and insert its keys into the other.
Design an algorithm that takes as input two BSTs and merges them to form a balanced BST. For any
node, you can update its left and right subtree fields, but cannot change its key. See Figure 24.7 on
the next page for an example. Your solution can dlmamically allocate no more than a few bytes.
Hint: Can you relate this problem to Problems 24.21 onthe facing page and 24.20 onPage376?
Solution: A brute-force approach is to traverse one tree and add its keys to the second tree. The
time complexity depends on how balanced the second tree is, and how we perfonn the insert. In
the best-case, we start with the second free being balanced, and preserve balance as we perform
additions,yieldingatimecomplexityofO(nlogn),wherenisthetotalnumberofnodes. Performing
the updates while reusing existing nodes is tricky if we do an inorder walk since the links change.
However, it is fairly simple if we do a post-order walk, since when we visit the node, we do not
need any information from its original left and right subtrees.
Looking more carefully at the brute-force approach, it is apparent that it does not exploit the
fact that both the sources of data being merged are sorted. In particular, if memory was not a
constraint, we could perform an inorder walk on each tree, writing the result of each to a sorted
array. Then we could put the union of the two arrays into a third sorted array. Finally, we could
build a balanced BST from the union array using recursion, e.g., using Solution 14.8 on Page 210.
The time complexity would be o(n), but the additional space complexity is o(n).
It is good to remember that a list can be viewed as a tree in which each node's left child is empty.
It is relatively simple to create a list of the same nodes as a tree (Solution 24.21on Page 328). We
379
```
