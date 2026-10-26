# Exercise 14.6: Find the closest entries in three sorted arrays

**Printed textbook page:** 206. **Reference transcription pages:** 206–206.

> **Unverified OCR transcription:** This section retains the supplied PDF text layer. It is not certified verbatim: code syntax, mathematical symbols, and page boundaries may be corrupted. When two exercises begin on the same page, their excerpts overlap. Do not paste extracted code into a `.py` file without manual verification.

#### Printed page 206 (PDF page 220)

```text
partially repeat this process for the root's left subtree. We can avoid repeated passes over nodes
by including the range of keys we want to reconstruct the subtrees over. For example, looking
at the preorder key sequence <43,23,37,29,31,41,47,53), instead of recursing on (23,37,29,31,41>
(which would involve an iteration to get the last element in this sequence). We can directly necur on
<23,37,29,31,41,47,53>, with the constraint that we are building the subtree on nodes whose keys
are less than 43.
def rebuild-bst-from-preorder (preorder-sequence) :
def rebuild-bst-from-preorder-on-vaIue-range (Iower-bound , upper-bound) :
if root-idxt0l == len(preorder-sequence) 
:
return None
root = preorder-sequence Iroot-idx [0] l
if not lower-bound <= root <= upper-bound:
return None
root-idx [0] +- 1
# Note that rebui-ld-bst-fron-preorder-on-va7ue-range 
updates root-idx[0]
# so the order of foTTowing two cal-ls are critical.
left-subtree = rebuild-bst-from-preorder-on-value-range 
(
lower-bound, root)
right-subtree = rebuild-bst-from-preorder-on-vaIue-range(
root, upper-bound)
return BSTNode(root, left-subtree, right-subtree)
root-idx = [0] 
# Tracks current subtree.
return rebuild-bst-from-preorder-on-value-range (float (' -inf ' ), float (' inf ' ) )
The worst-case time complexity is O(n), since it performs a constant amount of work per node.
Note the similarity to Solution 24.20 onPage377.
A postorder traversal sequence also uniquely specifies the BST, and the algorithm for recon-
structing the BST is very similar to that for the preorder case.
1,4.6 FrNo rrrs cLosEST ENTRIES IN THREE soRTED ARRAys
Design an algorithm that takes three sorted arrays and retums one entry from each such that the
minimum interval containing these three entries is as small as possible. For example, if the three
arraysare(5,10,15), <3,6,9,1,2,15),and(8,1,6,24>,then15,15,16lieinthesmallestpossibleinterval.
Hint:How would you proceed if you needed to pick three entries in a single sorted array?
Solution: The brute-force approach is to try all possible triples, e.9., with three nested for loops.
The length of the minimum interval containing a set of numbers is simply the diffurence of the
maximum and the minimum values in the triple. The time complexity is O(lmn), where l,m,n are
the lengths of each of the three arrays.
The brute-force approach does not take advantage of the sortedness of the input arrays. For
the example in the problem description, the smallest intervals containing (5,3,1.6) au-ld (5,3,24)
must be larger than the smallest interval containing (5,3,8) (since 8 is the maximum of 5,3,8, and
8<1.6<24).
Let's suppose we begin with the triple consisting of the smallest entries in each array. Let s be
the minimum value in the triple and f the maximum value in the triple. Then the smallest interval
206
```
