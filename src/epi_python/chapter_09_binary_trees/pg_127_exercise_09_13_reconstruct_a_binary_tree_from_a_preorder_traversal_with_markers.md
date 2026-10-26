# Exercise 9.13: Reconstruct a binary tree from a preorder traversal with markers

**Printed textbook page:** 127. **Reference transcription pages:** 127–127.

> **Unverified OCR transcription:** This section retains the supplied PDF text layer. It is not certified verbatim: code syntax, mathematical symbols, and page boundaries may be corrupted. When two exercises begin on the same page, their excerpts overlap. Do not paste extracted code into a `.py` file without manual verification.

#### Printed page 127 (PDF page 141)

```text
len(preorder) , 0,
1en(inorder) )
The time comPlexity is O(n)-building the hash table takes O(n) time and the recursive reconstruc-
tion spends O(1) time per node. The space complexity is O(n + h) = O(n)-the size of the hash table
plus the maximum depth of the function call stack.
Varian* Solve the same problem with an inorder traversal sequence and a postorder traversal
sequence.
Varianh Let A be an affay of n distinct integers. Let the index of the maximum element of Abe
m. Define the max-tree on A to be the binary tree on the entries of A in which the root contains
the maximum element of A, the left child is the max-tree on AlO,m - 1] and the right child is the
max-tree onAlm+1.,n- 1]. Design ano(n) algorithmforbuildingthemax-treeof A.
9.13 RscoNsrnucr A BTNARy rREE FRoM A pREoRDER TRAVERSAL wrrH MARKERS
M*y different binary trees have the same preorder traversal sequence.
In this problem, the preorder traversal computation is modified to mark where a left or right
child is empty. For example, the binary tree in Figure 9.5 on Page 125 yields the following preorder
traversal sequence:
(H, B, E, nul1 ,nuLL,E,A,nuI1, nulI, nul1, C null, D, nulI, G, I, nulI, nu1l, nul1)
Design an algorithm for reconstructing a binary tree from a preorder traversal visit sequence that
uses null to mark empty children.
Hint: lt's difficult to solve this problem by examining the preorder traversal visit sequence from left-to-right.
Solution: One brute-force approach is to enumerate all binary trees and compare the resulting
preorder sequence with the given one. This approach will have unacceptable time complexity.
The intuition for a better algorithm is the recognition that the first node in the sequence is the
root, and the sequence for the root's left subtree appears before all the nodes in the root's right
subtree. It is not easy to see where the left subtree sequence ends. F{owever, if we solve the problem
recursively, we can assume that the routine correctly computes the left subtree, which will also tell
us where the right subtree begins.
def reconstruct-preorder (preorder) :
def reconstruct-preorder_helper(preorder_iter) :
subtree-key = nert (preorder-iter)
if subtree_key is None:
return None
# Note that reconstruct_preorder_helper updates preorder_iter. So the
# order of foTTowing two ca77s are criticaT.
Ieft-subtree = reconstruct_preorder_helper(preorder_iter)
right-subtree = reconstruct_preorder_hetper(preorder_iter)
return BinaryTreeNode(subtree_key, left_subtree, right_subtree)
return reconstruct_preorder_helper(iter(preorder))
127
```
