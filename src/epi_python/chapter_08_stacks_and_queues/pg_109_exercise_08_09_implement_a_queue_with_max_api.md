# Exercise 8.9: Implement a queue with max API

**Printed textbook page:** 109. **Reference transcription pages:** 109–111.

> **Unverified OCR transcription:** This section retains the supplied PDF text layer. It is not certified verbatim: code syntax, mathematical symbols, and page boundaries may be corrupted. When two exercises begin on the same page, their excerpts overlap. Do not paste extracted code into a `.py` file without manual verification.

#### Printed page 109 (PDF page 123)

```text
def --init--(self):
self.-enq, seIf.-deq = il, tl
def enqueue (self, x) :
seIf. -enq. append (x)
def dequeue(self):
if not seIf. _deq:
# Transfers the elerents in _enq to _deq
rhile seIf.-enq:
seJ. f. _deq. append ( seIf. _enq . pop O )
if not seIf.-deq: # _deq is still 
empty!
raise IndexError('empty queue')
return self.-deq.popo
This approach takes O(m) time for m operations, which can be seen from the fact that each element
is pushed no more than twice and popped no more than twice.
8.9 lN,rprntirsrvr A euEUE wrrH MAx API
Implement a queue with enqueue, dequeue, and max operations. The max operation refurns the
maximum element currently stored in the queue.
Hint: When can an element never be returned by max, regardless of future updates?
Solution: A brute-force approach is to track the current maximum. The current maximum has to
be updated on both enqueue and dequeue, Updating the current maximum on enqueue is trivial
and fast-just compare the enqueued value with the current maximum. However, updating the
current maximum on dequeue is slow-we must examine every single remaining element, which
takes O(n) time, where n is the size of the queue.
Consider an element s in the queue that has the property that it entered the queue before a later
element, b, which is greater than s. Since s will be dequeued before b, s can never in the future
become the maximum element stored in the queue, regardless of the subsequent enqueues and
dequeues.
The key to a faster implementation of a queue-with-max is to elirninate elements like s from
consideration. We do this by maintaining the set of entries in the queue that have no later entry in
the queue greater than them in a separate deque. Elements in the deque will be ordered by their
position in the queue, with the candidate closest to the head of the queue appearing first. Since
each entry in the deque is greater than or equal to its successors, the largest element in the queue is
at the head of the deque.
We now briefly describe how to update the deque on queue updates. If the queue is dequeued,
and if the element just dequeued is at the deque's head, we pop the deque from its head; otherwise
the deque remains unchanged. When we add an entry to the queue, we iteratively evict from the
deque's tail until the element at the tail is greater than or equal to the entry being enqueued, and
then add the new entry to the deque's tail. These operations are illustrated in Figure 8.4 on the
following page.
109
```

#### Printed page 110 (PDF page 124)

```text
o lairi3i2lo
olffi,r
,lffi
p lriai2ioil
o ls2JF
olffi
o lt',2lo i1l2l4 i4
D
p lsiziolll2
tr-
^ l-r^r.
u L!_!_
o lelzt,o',1t,2t,L
o fzio',tt,zt,4
oW 
o@ 
o@ 
oW
Flgure 8.4: The queue with max for the following operations: enqueue 1, dequeue, dequeue, enqueue 2, enqueue 4,
dequeue, enqueue 4. The queue initially contains3,1,3,2, and 0 in that order. The deque D corresponding to queue Q
is immediately below Q. The progression is shown from left-to-right, then top{o-bottom. The head of each queue and
deque is on the left. Observe how the head ol the deque holds the maximum element in the queue.
class Queuelf i thl{ax :
def --init--(self):
self .-entries = collections.deque()
self. -candidates-for-max = collecti.ons. deque o
def enqueue(self, x):
self . -entries . append (x)
# ETininate doninated elements in -candidates-for-max.
while seIf.-candidates-for-max and self .-candidates-for-max[-1] < x
seIf. -candidates-for-max 
. pop o
self . -candidates-for-max. append(x)
def dequeue(se1f):
if se1f. -entries :
result = self. -entries. popleft o
if result == self.-candidates-for-max[0] :
seIf. -candidates-for-max . popleft o
return result
raise IndexError ('empty queue')
def max(seIf):
if self . -candidates-for-max 
:
return self . -candidates-for-max [0]
raise IndexError ('empty queue')
Each dequeue operation has time O(1) complexity. A single enqueue operation may entail many
ejections from the deque. However, the amortized time complexity of n enqueues and dequeues
is O(n), since an element can be added and removed from the deque no more than once. The max
operation is O(1) since it consists of returning the element at the head of the deque.
An altemate solution that is often presented is to use reduction. Specifically, we know how to
solve the stack-with-max problem efficiently (Solution 8.1 on Page 98) and we also know how to
efficiently model a queue with two stacks (Solution 8.8 on Page 108), so we can solve the queue-
with-max design by modeling a queue with two stacks-with-max. This approach feels unnatural
compared to the one presented above.
class QueueWithllax:
def --init--(self):
110
```

#### Printed page 111 (PDF page 125)

```text
self,-enqueue = Stacko
sel:f.-dequeue = Stacko
def enqueue (self, x) :
self. -enqueue . push (x)
def dequeue(self):
if self. -dequeue. empty O :
while not seIf. -enqueue. enptyO :
seLf. -dequeue . push ( seIf. _enqueue . pop O )
if not self. -dequeue. enpty() :
leturn self . -dequeue.popo
raise IndexError ('enpty queue ' )
def rnax(self):
lf not seIf._enqueue, enptyO ;
return seIf._enqueue.max() if se1f._dequeue.empty() else max(
self. _enqueue . max O , self. _dequeue , max O )
if not self, -dequeue . empty O :
retur[ self , _dequeue,naro
raise fndexError('empty queue')
Since thestack-with-maxhasO(1) amortized timecomplexityforpush, pop, andmax/ and the queue
from two stacks has O(1) amortized time complexity for enqueue and dequeue, this approach has
O(1) amortized time complexity for enqueug dequeue, and max.
111.
```
