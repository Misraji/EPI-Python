# Exercise 7.1: Merge two sorted lists

**Printed textbook page:** 84. **Reference transcription pages:** 84–84.

> **Unverified OCR transcription:** This section retains the supplied PDF text layer. It is not certified verbatim: code syntax, mathematical symbols, and page boundaries may be corrupted. When two exercises begin on the same page, their excerpts overlap. Do not paste extracted code into a `.py` file without manual verification.

#### Printed page 84 (PDF page 98)

```text
linked lists, which are not a standard type i. Python. We define our own singly and doubly linked
list types. Some of the key methods on these lists include retuming the head/tail, adding an element
at the head/tail, retuming the value stored at the head/tail, and deleting the head, tail, or arbitrary
node in the list.
7.1 Msncr rwo soRTED Lrsrs
Consider two singly linked lists in which each node holds a number. Assume the lists are sorted,
i.e., numbers in the lists appear in ascending order within each list. The merge of the two lists is a
list consisting of the nodes of the two lists in which numbers appear in ascending order. Merge is
illustrated in Figure 7.3.
0x I SO0
0x 124$
0r1 830
Sx24l0
0x2 7S0
(a) Two sorted lists.
5
7
X
L1
2
11
X
L2
3
>
11
X
R
2
3
5
7
Ox 1OO0
ox2430 
0x1240
(b) The merge of the lists in (a).
Figure 7.3: Merging sorted lists.
0xl8J0
0x2 700
Write a program that takes two lists, assumed to be sorted, and returns their merge. The only field
your program can change in a node is its next field.
Hint: Two sorted arrays can be merged using two indices. For lists, take care when one iterator reaches the
end.
Solution: A naive approach is to append the two lists together and sort the resulting list. The
drawback of this approach is that it does not use the fact that the initial lists are sorted. The time
complexity is that of sorting, which is O((n + m)log(n + rz)), where n and m are the lengths of each
of the traro input lists.
A better approach, in terms of time complexity, is to traverse the two lists, always choosing the
node containing the smaller key to continue traversing from.
def merge-two-sorted-Iir." (lr , iil 
,
# Creates a pTaceholder for the result
dummy-head = tail = ListNodeo
while Ll and L2:
if L1. data < L2 . data:
taiI. next , L1 = L1, L1. next
else :
tail. next , L2 = L2 , L2 . next
tail = tail.next
# Appends the remaining nodes of Ll or L2
tail.next 
= L1 or L2
return dunmy-head. next
u
```
