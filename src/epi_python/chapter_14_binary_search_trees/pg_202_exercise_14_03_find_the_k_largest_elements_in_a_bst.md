# Exercise 14.3: Find the k largest elements in a BST

**Printed textbook page:** 202. **Reference transcription pages:** 202–202.

> **Unverified OCR transcription:** This section retains the supplied PDF text layer. It is not certified verbatim: code syntax, mathematical symbols, and page boundaries may be corrupted. When two exercises begin on the same page, their excerpts overlap. Do not paste extracted code into a `.py` file without manual verification.

#### Printed page 202 (PDF page 216)

```text
a key that is greater than the input value, we search in the left subtree, updating the candidate to
the current root. Correctness follows from the fact that whenever we first set the candidate, the
desired result must be within the tree rooted at that node.
For example, when searching for the first node whose key is greater than 23 in the BST in
Figure 14.1 on Page 198, the node sequence is A,l,J,KL. Since L has no left child, its key, 29, is the
result.
def find-first-greater-than-k(tree, k) :
subtree, first-so-far = tree, None
rhile subtree:
if subtree.data > k:
first-so-far , subtree = subtree , subtree. left
else: # Root and a77 keys in Ieft subtree are <= k, so skip thera
subtree = subtree.right
return first-so-far
The time complexity is O(h), where h is the height of the tree. The space complexity is O(1).
Variant: Write a program that takes as input a BST and a value, and retums the node whose key
equals the input value and appears first in an inorder traversal of the BST. For example, when
applied to the BST in Figure 14.2,your program should retum Node B for 108, Node G for 285, and
null for 143.
4
(;
B
('
I
U
I)
Flgure 14.2: A BST with duplicate keys.
14.3 FrNo rns k r.lncssr ELEMENTS rN a BST
A BST is a sorted data structure, which suggests that it should be possible to find the k largest keys
easily.
Write a program that takes as input a BST and an integer k, and retums the k largest elements in the
BST in decreasing order. For example, if the input is the BST in Figure 14.1 on Page 198 and k = 3,
your program should retum (53,47,43>.
Hint: rNhat does an inorder traversal yield?
Solution: The brute-force approach is to do an inorder traversal, which enumerates keys in ascend-
ing order, and return the last k visited nodes. A queue is ideal for storing visited nodes, since it
makes it easy to evict nodes visited more than k steps previously. A drawback of this approach is
202
```
