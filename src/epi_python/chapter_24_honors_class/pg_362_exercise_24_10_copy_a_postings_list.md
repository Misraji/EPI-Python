# Exercise 24.10: Copy a postings list

**Printed textbook page:** 362. **Reference transcription pages:** 362–363.

> **Unverified OCR transcription:** This section retains the supplied PDF text layer. It is not certified verbatim: code syntax, mathematical symbols, and page boundaries may be corrupted. When two exercises begin on the same page, their excerpts overlap. Do not paste extracted code into a `.py` file without manual verification.

#### Printed page 362 (PDF page 376)

```text
The O(nz) complexity comes from having to repeatedly traverse the list to identify the tail. Note
that getting the head of a singly linked list is an O(1) time operation. This suggests paying a one-time
cost of O(n) to reverse the second half of the original list. Now all we need to do is interleave this
with the first half of the original list.
def zipping-Iinked-Iist (L) :
if not L or not L.next:
return L
# Finds the second haTf of L.
slow=fast=L
while fast and fast.next:
slow , fast = slow, next , fast . next , next
first-haIf-head = L
second-half-head = slow.next
slow.next = None # splits the Iist into tr,vo -lists
second-haI f-head = reverse-I inked-li st ( second-ha1 f-head)
# Interleave the first 
haTf and the reversed of the second ha7f.
first-ha1f-iter, 
second-half-iter = first-half-head, 
second-half-head
rhile second-half-iter :
second-half-iter . next , first-ha1f-iter. 
next , second-ha1f-iter = (
first-half-iter.next, 
second-half-iter, second-haIf-iter.next)
first-half-iter 
= first-half-iter. 
next . next
return fir st-haIf-head
The time complexity is O(n). The space complexity is O(1)
24.10 Copv e PosrlNcs LIST I
A postings list is a singly linked list with an additional"jump" field at each node. The jump field
points to any other node. Figure 24.3 illustrates a postings list with four nodes.
Flgure 24.3: A postings list.
Implement a ftrnction which takes a postings list and retums a copy of it. You can modify the
original list, but must restore it to its initial state before retuming.
Hint: Copy the jump field and then copy the next field.
Solution: Here is a brute-force algorithm. First, create a copy of the postings list, without assiSning
values to the jump field. Next, use a hash table to store the mapping from nodes in the original
postings list to nodes in the copied list. Finally, traverse the original list and the new list in tandem,
,
d
, X
L
a
I
b
I
c
362
```

#### Printed page 363 (PDF page 377)

```text
using the maPPing to assign each jump field. The time and space complexity are O(n), where n is
the number of nodes in the original postings list.
The key to improving space complexity is to use the next field for each node in the original
list to record the mapping from the original node to its copy. To avoid losing the structure of the
original list, we use the next field in each copied node to point to the successor of its original node.
See Figure 24.4b) for an example. Now we can proceed like we did in the brute-force algorithm.
We assign the jump field in the copied nodes, using the next field in the original list to get the
corresponding nodes in the copy. See Figure 24.4(c). Finally, we undo the changes made to the
original list and update the next fields of the copied list, as in Figure 24.4(d) for an example.
(a) lnitial list.
(b) Copy with cross-referencing.
(c) Assign jump field. 
(d) Undo changes.
Flgwe24.4:, Duplicating a postings list.
def copy-postings-Ii st (L)
if not L:
return None
# Stage 1
#
#
it=L
rhile it:
new-node = PostinglistNode(it.order, 
it.next, 
None)
it.next = new-node
it = new-node. next
# Stage 2: Assigns the junp field in the copied J.jst
it=L
rhile it:
if it. jump:
it. next . jump = it. jump. next
it = it. next . next
I{akes a copy of the original list rjthout assigning the junp
field, and creates the napping for each node in the original
list to the copied list.
# Stage 3
#
it=1
Reverts the original list, 
and assigns t}e next field of
the copied list.
Eltx
363
```
