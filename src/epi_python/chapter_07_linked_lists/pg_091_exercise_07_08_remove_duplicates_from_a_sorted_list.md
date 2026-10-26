# Exercise 7.8: Remove duplicates from a sorted list

**Printed textbook page:** 91. **Reference transcription pages:** 91–91.

> **Unverified OCR transcription:** This section retains the supplied PDF text layer. It is not certified verbatim: code syntax, mathematical symbols, and page boundaries may be corrupted. When two exercises begin on the same page, their excerpts overlap. Do not paste extracted code into a `.py` file without manual verification.

#### Printed page 91 (PDF page 105)

```text
Hint: lI you know the length of the list, can you find the kth last node using two iterators?
Solution: A brute-force approach is to compute the length with one pass, and then use that to
determine which node to delete in a second pass. A drawback of this approach is that it entails two
Passes over the data, which is sloW e.9., if traversing the list entails disc accesses.
We use two iterators to traverse the list. The first iterator is advanced by k steps, and then the
two iterators advance in tandem. When the first iterator reaches the tail, the second iterator is at
the (k + 1)th last node, and we can remove the kth node.
# Assumes I has at least k nodes, del.etes the k-th l.ast node in I
def remove-kth-Iast (L, k) :
dummy-head = ListNode(0, L)
first = dummy-head.next
for - in range (k) :
first = first.next
second = dummy-head
while first:
first , second = first. next , second. next
# second points to the (k + l)-th last node, deletes jts successor
second. next = second. next . next
return dummy_head. next
The time complexity is that of list traversal, i.e., O(n), wheren is the length of the list. The space
complexity is O(1), since there are only two iterators.
Compared to the brute-force approach, if k is small enough that we can keep the set of nodes
between the two iterators in memory but the list is too big to fit in memory, the two-iterator
approach halves the number of disc accesses.
7.8 Rruovr DUpLICATES FRoM A soRTED Lrsr
This problem is concemed with removing duplicates from a sorted list of integers. See Figure 7.8
for an example.
0x 1000
0x2 1 16)
0x1 8 3S
0x 1240
SxZ 200
0x1200
0x1 3 54
(a) List before removing duplicates.
L
2
2
3
7
11
rX
EE
L
2
J
5
7
11
X
0x i000
0x1830 
0x1240 
0x2200
(b) The list in (a) alter removing duplicates.
Figure 7.8: Example of duplicate removal.
0x 1200
Write a program that takes as input a singly linked list of integers in sorted order, and removes
duplicates from it. The list should be sorted.
Hfuf: Focus on the successor fields which have to be updated.
Solution: A brute-force algorithm is to create a new list, using a hash table to test if a value has
already been added to the new list. Altematively, we could search in the new list itself to see if
91
```
