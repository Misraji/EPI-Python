# Exercise 19.8: Implement a Timer class

**Printed textbook page:** 298. **Reference transcription pages:** 298–298.

> **Unverified OCR transcription:** This section retains the supplied PDF text layer. It is not certified verbatim: code syntax, mathematical symbols, and page boundaries may be corrupted. When two exercises begin on the same page, their excerpts overlap. Do not paste extracted code into a `.py` file without manual verification.

#### Printed page 298 (PDF page 312)

```text
This motivates the second readers-writers problem: protect s with "writer-preference", i.e., no
writer, once added to the queue, is to be kept waiting longer than absolutely necessary.
Implement a synchronization mechanism for the second readers-writers problem.
Hint:Force readers to acquire a write lock.
Solution: We want to give writers the preference. We achieve this by modifying Solution 19.6 on
the previous page to have a reader start by locking the write lock and then immediately releasing
it. Irr this way, a writer who acquires the write lock is guaranteed to be ahead of the subsequent
readers.
Variant The specifications to Problems 19.6 on Page 296 and 19.7 on the previous page allow
starvation-the first may starve writers, the second may starve readers. The third readers-writers
problem adds the constraint that neither readers nor writers should starve. Implement a slmchro-
nization mechanism for the third readers-writers problem.
19.8 lvrprrurNr a Trurn cress
Consider a web-based calendar in which the server hosting the calendar has to perform a task when
the next calendar event takes place. (The task could be sending an email or a Short Message Service
(SMS).) Your job is to design a facility that manages the execution of such tasks.
Develop a timer class that manages the execution of deferred tasks. The timer constructor takes as
its argument an object which includes a flln method and a string-valued name field. The class must
support-(1.) starting a thread, identified by name, at a given time in the future; and (2.) canceling
a thread, identified by name (the cancel request is to be ignored if the thread has already started).
Hint: There are two aspects-data structure design and concurrency.
Solution: The two aspects to the design are the data structures and the locking mechanism.
We use two data structures. The first is a min-heap in which we insert key-value pairs: the keys
are run times and the values are the thread to run at that time. A dispatch thread runs these threads;
it sleeps from call to call and may be woken up if a thread is added to or deleted from the pool. If
woken up, it advances or retards its remaining sleep time based on the top of the min-heap. On
waking up, it looks for the thread at the top of the min-heap-if its larlnch time is the current time,
the dispatch thread deletes it from the min-heap and executes it. It then sleeps till the launch time
for the next thread in the min-heap. (Because of deletions, it may happen that the dispatch thread
wakes up and finds nothing to do.)
The second data structure is a hash table with thread ids as keys and entries in the min-heaP as
values. If we need to cancel a thread, we go to the min-heap and delete it. Each time a thread is
added, we add it to the min-heap; if the insertion is to the top of the min-heap, we interrupt the
dispatch thread so that it can adjust its wake up time.
Since the min-heap is shared by the update methods and the dispatch thread, we need to lock it.
The simplest solution is to have a single lock that is used for all read and writes into the min-heap
and the hash table.
19.9 Trsr rHr Cor,r.erz coNTECTURE IN rARALLEL
In Problem 12.11 on Page 776 and its solution we introduced the Collatz conjecture and heuristics
for checking it. In this problem, you are to build a parallel checker for the Collatz conjecture.
298
```
