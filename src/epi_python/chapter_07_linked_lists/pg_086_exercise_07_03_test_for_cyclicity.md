# Exercise 7.3: Test for cyclicity

**Printed textbook page:** 86. **Reference transcription pages:** 86–86.

> **Unverified OCR transcription:** This section retains the supplied PDF text layer. It is not certified verbatim: code syntax, mathematical symbols, and page boundaries may be corrupted. When two exercises begin on the same page, their excerpts overlap. Do not paste extracted code into a `.py` file without manual verification.

#### Printed page 86 (PDF page 100)

```text
Varianh Write a program which takes as input a singly linked list L and a nonnegative integer k,
and reverses the list k nodes at a time. If the number of nodes n in the list is not a multiple of k,
leave the last n mod k nodes unchanged. Do not change the data stored within a node.
0x2 700
0x1810
6x I2.10
0x24 30
0x1 000
Figure 7.5: The reversed list for the list in Figure 7.3(b) on Page 84. Note that no new nodes have been allocated.
7.3 Trsr ron cYCLICITY
Although a linked list is supposed to be a sequence of nodes ending in null, it is possible to create
a cycle in a linked list by making the next field of an element reference to one of the earlier nodes.
Write a program that takes the head of a singly linked list and retums null if there does not exist a
cycle, and the node at the start of the cycle, if a cycle is present, (You do not know the length of the
list in advance.)
Hirf; Consider using two iterators, one fast and one slow.
Solution: This problem has several solutions. If space is not an issue, the simplest approach is to
explore nodes via the next field starting from the head and storing visited nodes in a hash table-a
cycle exists if and only if we visit a node already in the hash table. If no cycle exists, the search ends
at the tail (often represented by having the next field set to null). This solution requires O(n) space,
where n is the number of nodes in the list.
A brute-force approach that does not use additional storage and does not modify the list is to
traverse the list in two loops-the outer loop traverses the nodes one-by-one, and the inner loop
starts from the head, and traverses as many nodes as the outer loop has gone through so far. If the
node being visited by the outer loop is visited twice, a loop has been detected. (If the outer loop
encounters the end of the list, no cycle exists.) This approach has O(n2) ttrne complexity.
This idea can be made to work in linear time-use a slow iterator and a fast iterator to traverse
the list. In each iteration, advance the slow iterator by one and the fast iterator by two. The list has
a cycle if and only if the two iterators meet. The reasoning is as follows: if the fast iterator jumps
over the slow iterator, the slow iterator will equal the fast iterator in the next step.
Now, assuming that we have detected a cycle using the above method, we can find the start
of the cycle, by first calculating the cycle length C. Once we know there is a cycle, and we have a
node on it, it is trivial to compute the cycle length. To find the first node on the cycle, we use two
iterators, one of which is C ahead of the other. We advance them in tandem, and when they meet,
that node must be the first node on the cycle.
The code to do this traversal is quite simple:
def has-cycIe (head) :
def cycle-len(end):
start , step = end, 0
rhile True:
step += 1
start = start.next
if start is end
return step
7
5
3
2
X
M
11
86
```
