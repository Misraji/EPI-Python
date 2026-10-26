# Exercise 7.12: Implement list pivoting

**Printed textbook page:** 95. **Reference transcription pages:** 95–95.

> **Unverified OCR transcription:** This section retains the supplied PDF text layer. It is not certified verbatim: code syntax, mathematical symbols, and page boundaries may be corrupted. When two exercises begin on the same page, their excerpts overlap. Do not paste extracted code into a `.py` file without manual verification.

#### Printed page 95 (PDF page 109)

```text
Variant Solve the same problem when the list is doubly linked and you have pointers to the head
and the tail.
7.12 IuprEvmNr Lrsr prvorrNc
For any integer k, the pivot of a list of integers with respect to k is that list with its nodes reordered so
that all nodes containing keys less than k appear before nodes containing k, and all nodes containing
keys greater than k appear after the nodes containing k. See Figure 7.11 for an example of pivoting.
0x 18 l0
0x2 1 10
0x 1000
0x1200
0x2 200
0x1 2 40
0x1354
(a) A list to be pivoted.
L
J
2
2
,7
5
rx
rE
L
3
2
,)
5
7
11
11
X
0x1830
0x2 1 10
0x 1 200
0xi 354
0x1000 
l$x1240 
0x2200
(b) The result of pivoting the list in (a) with k = 7
Flgure 7.11 : List pivoting.
Implement a function which takes as input a singly linked list and an integer k and performs a pivot
of the list with respect to k. The relative ordering of nodes that appear before k, and after k, must
remain unchanged; the same must hold for nodes holding keys equal to k.
Hint: Form the three regions independently.
Solution: A brute-force approach is to form three lists by iterating through the list and writing
values into one of the three new lists based on whether the current value is less than, equal to, or
greater than k. We then traverse the list from the head, and overwrite values in the original list from
the less than, then equal to, and finally greater than lists. The time and space complexity are O(n),
where n is the number of nodes in the list.
A key observation is that we do not really need to create new nodes for the three lists. Instead
we reorganize the original list nodes into these three lists in a single traversal of the original list.
Since the traversal is in order, the individual lists preserve the ordering. We combine these three
lists in the final step.
def list-pivoting 
(L , x) :
less-head = Iess_iter = ListNodeo
equal-head = equal-iter = ListNodeo
greater_head = greater_iter = ListNodeo
# PopuTates the tfiree lists.
rhile L:
if L. data < x;
less_iter.next = L
Iess-iter = Iess_iter.next
elif 
L. data == x:
equal-iter.next = L
equal_iter = equal_iter.next
else: #L.data>x.
greater-iter.next 
= L
greater_iter = greater_iter,next
L = L.next
95
```
