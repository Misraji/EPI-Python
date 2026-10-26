# Exercise 7.9: Implement cyclic right shift for singly linked lists

**Printed textbook page:** 92. **Reference transcription pages:** 92–92.

> **Unverified OCR transcription:** This section retains the supplied PDF text layer. It is not certified verbatim: code syntax, mathematical symbols, and page boundaries may be corrupted. When two exercises begin on the same page, their excerpts overlap. Do not paste extracted code into a `.py` file without manual verification.

#### Printed page 92 (PDF page 106)

```text
L
5
3
2
EE EX
0x2200
Sx 1 000
0x2 1 10
0x1354
0x1 200
Figure 7.9: The result of applying a right cyclic shift by 3 to the list in Figure 7.1 on Page 82. Note that no new nodes
have been allocated.
the candidate value already is present. If the length of the list is r, the first approach requires O(n)
additional space for the hash table, and the second requires O(/,2; time to perform the lookups. Both
allocate n nodes for the new list.
A better approach is to exploit the sorted nature of the list. As we traverse the list, we remove
all successive nodes with the same value as the current node.
def remove-duplicates (L) :
it=L
while it:
# Ilses next-distinct 
to find the next distinct 
value.
next-distinct = it,next
rhile next-distinct 
and next-distinct.data 
== it.data
next-di stinct = next-di stinct . next
it.next = next-distinct
it = next-distinct
return L
Determining the time complexity requires a little amortized analysis. A single node may take
more than O(1) time to process if there are many successive nodes with the same value. A clearer
justification for the time complexity is that each link is traversed once, so the time complexity is
O(n). The space complexity is O(1).
Varianh Letmbe a positive integer and L a sorted singly linked list of integers. For each integer k,
if k appears more than rx times in L, remove all nodes from L containing k.
7.9 IuplrurNr cyclrc RIGHT sHIFT FoR SINGLy LINKED LISTs
This problem is concemed with performing a cyclic right shift on a list.
Write a program that takes as input a singly linked list and a nonnegative integer k, and retums the
list cyclically shifted to the right by k. See Figure 7.9 for an example of a cyclic right shift.
Hint:How does this problem differ from rotating an array?
Solution: A brute-force strategy is to right shift the list by one node k times. Each right shift by a
single node entails finding the tail, and its predecessor. The tail is prepended to the current head,
and its original predecessor's successor is set to null to make it the new tail. The time complexity
is O(kn), and the space complexity is O(1), where n is the number of nodes in the list.
Note that k may be larger than n. If so, it is equivalent to shift by k mod r,, so we assume k < ,4.
The key to improving upon the brute-force approach is to use the fact that linked lists can be cut
and the sublists reassembled very efficiently. First we find the tail node l. Since the successor of the
tail is the original head, we update f's successor. The original head is to become the kth node from
the start of the new list. Therefore, the new head is the (ra - k)th node in the initial list.
def cyclically-right-shift-list 
(L, k)
if not L:
92
```
