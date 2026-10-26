# Exercise 8.8: Implement a queue using stacks

**Printed textbook page:** 108. **Reference transcription pages:** 108–108.

> **Unverified OCR transcription:** This section retains the supplied PDF text layer. It is not certified verbatim: code syntax, mathematical symbols, and page boundaries may be corrupted. When two exercises begin on the same page, their excerpts overlap. Do not paste extracted code into a `.py` file without manual verification.

#### Printed page 108 (PDF page 122)

```text
if self.-num-queue-elements == len(self.-entries): 
# IVeeds to resize
# Itakes the queue elerents appear consecutiveJy.
seIf.-entries 
= (
self .-entriesIself .-head:] + seIf.-entries[: self .-head])
# Resets head and tail.
seIf.-head, seLf.-tail 
= 0, self.-num-queue-elements
self.-entries 
+= [None] * (
len(self.-entries) 
* Queue.SCALE-FACTOR - Ien(self.-entries))
self .-entriesIse1f.-tail] 
= x
seIf.-taiL 
= (self.-tail 
+ 1) % len(self.-entries)
self .-num-queue-elements += 1
def dequeue (se1f) :
if not self. -num-queue-elements 
:
raise IndexError ('empty queue ')
self .-num-queue-elements -= 1
ret = self .-entriesIseIf .-head]
seIf.-head = (seIf.-head + 1) % len(seIf.-entries)
return ret
def size (self) :
return self . -num-queue-elements
The time complexity of dequeue is O(1), and the amortized time complexity of enqueue is O(1).
8.8 hupr,uurNr A eUEUE usrNc sTACKS
Queue insertion and deletion follows first-in, first-out semantics; stack insertion and deletion is
last-in, first-out.
How would you implement a queue given a library implementing stacks?
Hint: lt is impossible to solve this problem with a single stack.
Solution: A straightforward implementation is to enqueue by pushing the element to be enqueued
onto one stack. The element to be dequeued is then the element at the bottom of this stack, which
can be achieved by first popping all its elements and pushing them to another stack, then popping
the top of the second stack (which was the bottom-most element of the first stack), and finally
popping the remaining elements back to the first stack.
The primary problem with this approach is that every dequeue takes two pushes and two pops
of eaery element, i.e., dequeue has O(n) time complexity, where r is the number of stored elements.
(Enqueue takes O(1) time.)
The intuition for improving the time complexity of dequeue is that after we move elements
from the first stack to the second stack, any further dequeues are trivial, until the second stack is
empty. This is true even if we need to enqueue, as long as we enqueue onto the first stack. When
the second stack becomes empty, and we need to perform a dequeue, we simply repeat the process
of transferring from the first stack to the second stack. ln essence, we are using the first stack for
enqueue and the second for dequeue.
class Queue
108
```
