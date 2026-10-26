# Exercise 7.4: Test for overlapping lists - lists are cycle-free

**Printed textbook page:** 87. **Reference transcription pages:** 87–87.

> **Unverified OCR transcription:** This section retains the supplied PDF text layer. It is not certified verbatim: code syntax, mathematical symbols, and page boundaries may be corrupted. When two exercises begin on the same page, their excerpts overlap. Do not paste extracted code into a `.py` file without manual verification.

#### Printed page 87 (PDF page 101)

```text
fast=slow=head
rhile fast and fast. next and fast. next, next:
slow, fast = slow.next, fast.next.next
if slow is fast:
# Finds the start of the cycle.
cycle_Ien_advanced_iter = head
for - in range(cycIe-len(slow)):
cycle_len_advanced_iter = cycle_Ien_advanced_iter. next
it = head
# Both iterators 
advance in tandem.
rhile it is not cycle_Len_advanced_iter:
it = it, next
cycle_1en_advanced_iter = cycle_Ien_advanced_iter. next
return it 
# iter is the start of cycle.
return None # No cycle.
Let F be the number of nodes to the start of the cycle, C the number of nodes on the cycle, and ,x the
total number of nodes. Then the time complexity is O(F) + O(C) = O(n)-4(F) for both pointers to
reach the cycle, and O(C) for them to overlap once the slower one enters the cycle.
Variant The following pro$am purports to compute the beginning of the cycle without determining
the length of the cycle; it has the benefit of being more succinct than the code listed above. Is the
program correct?
def has-cycle (head) :
fast=slow=head
while fast and fast. next and fast. next. next:
slow, fast = slow.next, fast.next.next
if slow is fast: 
# There is a cyc7e.
# Tries to find the start of the cyc7e.
slow = head
# Both pointers advance at the sane time,
rhile slow is not fast:
slow , fast = sIow. next , fast . next
return slow # sTow is the start of cycle
return None # No cyc7e.
7,4 Trsr ron ovERLApprNG Lrsrs-Lrsrs ARE cycLE-FREE
Given two singly linked lists there may be list nodes that are common to both. (This may not be a
bug-it may be desirable from the perspective of reducing memory footprint, as in the flyweight
pattem, or maintaining a canonical form.) For example, the lists in Figure 7.6 on the following page
overlap at Node I.
Write a Program that takes two cycle-free singly linked lists, and determines if there exists a node
that is corunon to both lists.
Hint: Solve the simple cases first.
Solution: A brute-force approach is to store one list's nodes in a hash table, and then iterate through
the nodes of the otheq, testing each for presence in the hash table. This takes O(n) tirrre and O(n)
space, where n is the total number of nodes.
87
```
