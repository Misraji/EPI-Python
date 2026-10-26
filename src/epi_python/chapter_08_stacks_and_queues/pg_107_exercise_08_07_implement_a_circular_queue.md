# Exercise 8.7: Implement a circular queue

**Printed textbook page:** 107. **Reference transcription pages:** 107–107.

> **Unverified OCR transcription:** This section retains the supplied PDF text layer. It is not certified verbatim: code syntax, mathematical symbols, and page boundaries may be corrupted. When two exercises begin on the same page, their excerpts overlap. Do not paste extracted code into a `.py` file without manual verification.

#### Printed page 107 (PDF page 121)

```text
Since each node is enqueued and dequeued exactly once, the time complexity is O(n). The space
complexity is O(m), where m is the maximum number of nodes at any single depth.
Varianh Write a program which takes as input a binary tree and retums the keys in top
down, alternating left-to-right and right-to-left order, starting from left-to-right. For ex-
ample, if the input is the tree in Figure 9.1 on Page 7\2, your program should retum
<<31,4>, <6, 6>, <27 7, 561., 2, 27 1), <29, 1., 3, O, 2g>, <77, 401., 257>, (eD) .
Varianh Write a program which takes as input a binary tree and retums the keys in a bottom up,
leftto-right order. For example, if the input is the tree in Figure 9.1 on Page 112, your program
should retum <<641>,<17,407,257>,<28,0,3,1.,28>,<271,561,,2,271>,<6,6>,<31,4>>.
Variant: Write a program which takes as input a binary tree with integer keys, and retums the
average of the keys at each level. For example, if the input is the tree in Figure 9,L on Page 11.2, your
program should retum <31, 4, 6, 27 6.25, 12, 225, 641)l .
8.7 Iuptnr"rnNt A CTRCULAR euEUE
A queue can be implemented using an array and two additional fields, the beginning and the end
indices. This structure is sometimes referred to as a circular queue. Both enqueue and dequeue
have O(1) time complexity. If the array is fixed, there is a maximum number of entries that can be
stored. If the array is dlmamically resized, the total time for rn combined enqueue and dequeue
operations is O(m).
Implement a queue API using an array for storing elements. Your API should include a constructor
functioru which takes as argument the initial capacity of the queue, enqueue and dequeue functions,
and a function which retums the number of elements stored. Implement dynamic resizing to
support storing an arbitrarily large number of elements.
Hint:Trackthe head and tail. How can you diffurentiate a full queue from an empty one?
Solution: A brute-force approach is to use ar.arrayt with the head always at index 0. An additional
variable tracks the index of the tail element. Enqueue has O(1) time complexity. However dequeue's
time complexity is O(n), where r is the number of elements in the queue, since every element has
to be left-shifted to fill up the space oeated at index 0.
A better approach is to keep one more variable to track the head. This way, dequeue can also
be performed in O(1) time. lAIhen performing an enqueue into a full array, we need to resize the
array. We cannot only resize, because this results in queue elements not appearing contiguously.
For example, if the array is (e,b,c,d), with e being the tail and b the head, if we resize to get
(e,b,c,d,-, -, -, -), we cannot enqueue without overwriting or moving elements.
class Queue:
SCALE-FACTOR = 2
def --init--(self 
, capacity) :
self.-entries 
- [None] * capacity
seIf.-head = se1f.-tail 
= self._num_queue_elements = 0
def enqueue(self, x)
107
```
