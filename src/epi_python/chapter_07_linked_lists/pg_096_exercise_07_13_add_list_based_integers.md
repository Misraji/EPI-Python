# Exercise 7.13: Add list-based integers

**Printed textbook page:** 96. **Reference transcription pages:** 96–96.

> **Unverified OCR transcription:** This section retains the supplied PDF text layer. It is not certified verbatim: code syntax, mathematical symbols, and page boundaries may be corrupted. When two exercises begin on the same page, their excerpts overlap. Do not paste extracted code into a `.py` file without manual verification.

#### Printed page 96 (PDF page 110)

```text
# Conbines the three ]ists.
greater-iter.next = None
equal-iter. next = greater-head. next
less-iter. next = equal-head. next
return less-head. next
The time to compute the three lists is O(r). Combining the lists takes O(1) time, yielding an overall
O(n) time complexity. The space complexity is O(1).
7.73 Aoo rrsr-nnsED TNTEGERs
A singly linked list whose nodes contain digits can be viewed as an integer, with the least significant
digit coming first. Such a representation can be used to represent unbounded integers. This problem
is concerned with adding integers represented in this fashion, See Figure 7.12 for an example.
(a) Two lists.
(b) The sum of the two lists in (a).
Flgure 7.12: List-based interpretation ot 413 + 907 = 1320
Write a program which takes two singly linked lists of digits, and returns the list corresponding to
the sum of the integers they represent. The least significant digit comes first.
Hint: First, solve the problem assuming no pair of corresponding digits sum to more than 9.
Solution: Note that we cannot simply convert the lists to integers, since the integer word length is
fixed by the machine architecture, and the lists can be arbitrarily long.
Instead we mimic the grade-school algorithm, i.e., we compute the sum of the digits in corre-
sponding nodes in the two lists. A key nuance of the computation is handling the carry-out. The
algorithm continues processing input until both lists are exhausted and there is no remaining carry.
def add-two-numbers (L1 , L2) :
place-iter = dummy-head = ListNodeo
carr! = $
while L1 or L2 or carry:
val = carry + (Ll.data if L1 else 0) + (Lz.data if L2 else 0)
LI = Ll.next if Ll else None
L2 = L2. next if L2 else l{one
place-iter.next = ListNode(val % 10)
carry, place-iter = vaL // 10, place-iter.next
return dummy-head.next
The time complexity is O(n + m) Nrd the space complexity is O(max(n,m)), where n and m are the
lengths of the two lists.
Varianh Solve the same problem when integers are represented as lists of digits with the most
significant digit comes first.
L
3
1
EX
7
0
9
L
0
2
J
1
X
96
```
