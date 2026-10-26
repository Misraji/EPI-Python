# Exercise 24.21: Convert a BST to a sorted doubly linked list

**Printed textbook page:** 378. **Reference transcription pages:** 378–378.

> **Unverified OCR transcription:** This section retains the supplied PDF text layer. It is not certified verbatim: code syntax, mathematical symbols, and page boundaries may be corrupted. When two exercises begin on the same page, their excerpts overlap. Do not paste extracted code into a `.py` file without manual verification.

#### Printed page 378 (PDF page 392)

```text
def build-bst-from-sorted-doubly-list-helper (start, end)
if start >= end:
return None
mid - (start + end) // 
2
Ieft = build-bst-from-sorted-doubly-list*helper(start, 
mid)
# The Tast function call sets t to the successor of the naxinun node in
# the tree rooted at left.
curr , head [0] = head [0] , head [0] . next
curr.prev = left
curr.next = build-bst-from-sorted-doubly-list-helper(mid 
+ 1, end)
return curr
head = [L]
return build-bst-from-sorted-doubly-list-helper(0, 
n)
The algorithms spends O(1) time per node, leading to an O(n) time complexity. No dynamic memory
allocation is required. The maximum number of call frames in the function call stack is flogrl,
yielding an O(logn) space comPlexity,
24.21 CoNvsnr a BST ro A soRTED DouBLY LINKED r,Isr $
A BST node has two references, left and right. A doubly linked list node has two references/
previous and next. If we interpret the BST's left pointer as previous and the BST's right pointer as
next, a BST's node can be used as a node in a doubly linked list. Also, the inorder traversal of a BST
represents an ordered set just like a doubly linked list. Therefore it is natural to ask if is possible to
take a BST and rewrite its node reference fields so that it represents a doubly linked list such that
the resulting list represents the inorder traversal sequence of the tree'
Design an algorithm that takes as input a BST and returns a sorted doubly linked list on the same
elements. Your algorithm should not do any dynamic allocation. The original BST does not have
to be preservedi use its nodes as the nodes of the resulting list, as shown in Figure 24.6 on the
Preceding Page.
Hint:The tricky part is attaching the root to its subtrees.
Solution: In the absence of the allocation constraint, the problem can be easily solved using a
dynamic array to write nodes to a list as we perforrn an inorder traversal. The time complexity is
O(n ), where n is the number of nodes, but the space comPlexity is also O(n)'
Speaking generally, a key benefit of lists is that we can easily apPend one list to another. ln
particular, if we have lists for the left and right subtrees, we can easily splice them in with the root
in O(1) time.
def bst-to-doubly-Iinked-l,i st (tree) :
HeadAndTait = collections . namedtuple ('HeadAndTail ' , ('head' , 'tail '))
# Transforns a BSI into a sorted doubTy linked list 
in-place,
# and return the head and taiT of the list.
def bst-to-doubly-linked-list-helper(tree) 
:
# Enpty subtree.
if not tree:
378
```
