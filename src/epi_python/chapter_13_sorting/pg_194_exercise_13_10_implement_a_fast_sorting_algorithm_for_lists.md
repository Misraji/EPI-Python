# Exercise 13.10: Implement a fast sorting algorithm for lists

**Printed textbook page:** 194. **Reference transcription pages:** 194–194.

> **Unverified OCR transcription:** This section retains the supplied PDF text layer. It is not certified verbatim: code syntax, mathematical symbols, and page boundaries may be corrupted. When two exercises begin on the same page, their excerpts overlap. Do not paste extracted code into a `.py` file without manual verification.

#### Printed page 194 (PDF page 208)

```text
def valid-placement-exists (A, B) :
return all(a < b
for a, b in zip(sorted(A.-players), sorted(8.-players)))
The time complexity is that of sorting, i.e., O(nlogn)
13.10 INrprnNlsNr A FAST soRTING ALGoRITHM FoR LISTS
Implement a routine which sorts lists efficiently. It should be a stable sort, i.e., the relative positions
of equal elements must remain unchanged.
Hint: lnwhat respects are lists superior to arrays?
Solution: The brute-force approach is to repeatedly delete the smallest element in the list and add
it to the end of a new list. The time complexity is O(nzl andthe additional space complexity isO(n),
where n is the number of nodes in the list, We can refine the simple algorithm to run in O(1) space
by reordering the nodes, instead of creating new ones.
def insertion-sort (L) :
dummy-head = ListNode(0, L)
# The sub-list consisting of nodes up to and including iter is sorted in
# increasing order. We need to ensure that after we nove to L.next this
# property continues to ho7d. We do this by swapping L,next rith its
# predecessors in the list 
tiII 
it's 
in the right p7ace.
while L and L.next:
if L.data > L.next.data:
target, pre = L.next, dummy-head
rbile pre. next. data < target. data:
pre = pre. next
terdp, pre.next, L.next = pre.next, target, target.next
target.next = temp
else:
L = L.next
return dummy-head. next
The time complexity is O(nz),which corresponds to the case where the list is reverse-sorted to begin
with. The space complexity is O(1).
To improve on runtime, we can gain intuition from considering arrays. Quicksort is the best
all round sorting algorithm for arrays-it runs in time O(nlogn), and is in-place. However, it is
not stable. Mergesort applied to arrays is a stable O(nlogn) algorithm. However, it is not in-place,
since there is no way to merge two sorted halves of an array in-place in linear time.
Unlike arrays, lists can be merged in-place-conceptually, this is because insertion into the
middle of a list is an O(1) operation. The following program implements a mergesort on lists. We
decompose the list into two equal-sized sublists around the node in the middle of the list. We find
this node by advancing two iterators through the list, one twice as fast as the other. \llhen the fast
iterator reaches the end of the list, the slow iterator is at the middle of the list. We recurse on the
sublists, and use Solution 7.1. on Page 84 (merge two sorted lists) to combine the sorted sublists.
def stable-sort-1ist (L) :
# Base cases.' L is enpty or a singTe node, nothing to do
if not L or not L.next:
return L
194
```
