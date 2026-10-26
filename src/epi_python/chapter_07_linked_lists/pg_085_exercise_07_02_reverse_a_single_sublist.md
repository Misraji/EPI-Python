# Exercise 7.2: Reverse a single sublist

**Printed textbook page:** 85. **Reference transcription pages:** 85–85.

> **Unverified OCR transcription:** This section retains the supplied PDF text layer. It is not certified verbatim: code syntax, mathematical symbols, and page boundaries may be corrupted. When two exercises begin on the same page, their excerpts overlap. Do not paste extracted code into a `.py` file without manual verification.

#### Printed page 85 (PDF page 99)

```text
The worst-case, from a runtime perspective, corresponds to the case when the lists are of comparable
length, so the time complexity is O(n + m). (In the best-case, one list is much shorter than the other
and all its entries appear at the beginning of the merged list.) Since we reuse the existing nodes, the
space complexity is O(1).
Variant: Solve the same problem when the lists are doubly linked.
7.2 Rsvnnsx A sTNGLE suBr,rsr
This problem is concemed with reversing a sublist within a list. See Figure 7.4 for an example of
sublist reversal.
0x2 700
0x2430
0x 12 40
0x 1810
0x 1000
Figure 7.4: The result of reversing the sublist consisting of the second to the fourth nodes, inclusive, in the list in
Figure 7.5 on the following page.
Write a program which takes a singly linked list L and two integers s and / as arguments, and
reverses the order of the nodes from the sth node to /th node, inclusive. The numbering begins at
1., i.e., the head node is the first node. Do not allocate additional nodes.
Hlnfr Focus on the successor fields which have to be updated.
Solution: The direct approach is to extract the sublist, neverse it, and splice it back in. The drawback
for this approach is that it requires two passes over the sublist.
The update can be performed with a single pass by combining the identification of the sublist
with its reversal. We identify the start of sublist by using an iteration to get the sth node and
its predecessor. Once we reach the sth node, we start the reversing process and keep counting.
When we reach the /th node, we stop the reversion process and link the reverted section with the
unreverted sections.
def reverse-sublist (L, start , finish) :
dummy-head = sublist-head = Listt{ode(0, L)
for - in range(l, start):
sublist-head = sublist_head.next
# Reverses sublist,
sublist-iter = sublist-head.next
for - in range(finish - start):
temp - sublist_iter.next
sublist-iter. next , temp. next , sublist_head. next = (temp. next ,
subli st-head . next ,
temp)
return dummy_head. next
The time complexity is dominated by the search for the /th node, i.e.,O(f).
Varianh Write a function that reverses a singly linked list. The function should use no more than
constant storage beyond that needed for the list itself. The desired transformation is illustrated in
Figure 7.5 on the next page.
M
11
J
5
7
2
X
85
```
