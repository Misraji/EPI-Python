# Exercise 19.9: Test the Collatz conjecture in parallel

**Printed textbook page:** 298. **Reference transcription pages:** 298–300.

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

#### Printed page 299 (PDF page 313)

```text
Specifically, assume your program will run on a multicore machine, and threads in your program
will be distributed across the cores. Your program should check the Collatz conjecture for every
integer in [1, U] where U is an input to your program.
Design a multi-threaded program for checking the Collatz conjecture. Make full use of the cores
available to you. To keep your program from overloading the system, you should not have more
than r threads running at a time.
Hint:Use multithreading for performance-take care to minimize threading overhead.
Solution: Heuristics for pruning checks on individual integers are discussed in Solution 1.2.11 on
Page 176. The aim of this problem is implementing a multi-threaded checker. We could have
a master thread launch n threads, one per number, starting with7,2,...,r. The master thread
would keep hack of what number needs to be processed next, and when a thread refurned, it could
re-assign it the next unchecked number.
The problem with this approach is that the time spent executing the check in an individual
thread is very small compared to the overhead of communicating with the thread. The natural
solution is to have each thread process a subrange of [1, U]. We could do this by dividing [L, U] into
n equal sized subranges, and having Thread i handle the ith subrange.
The heuristics for checking the Collatz conjecture take longer on some integers than others, and
in the strategy above there is the potential of a situation arising where one thread takes much longer
to complete than the others, which leads to most of the cores being idle.
A good compromise is to have threads handle smaller intervals, which are still large enough to
offtet the thread overhead. We can maintain a work-queue consisting of unprocessed intervals, and
assigning these to returning threads.
# Perforns basic unit of work
de:f worker (lower , upper) :
for i in range(Iower, upper + 1):
assert collatz_check(i, setO)
print (' (%d,%d) ' fr (1ower , upper) )
# Checks an individuaT nunber
def collatz-check (x , visited) :
if x == 1;
return True
elif x in visited:
return FaIse
vi sited . add (x)
if x & 1: # odd nunber
return collatz_check(3 * x + 1, visited)
else: # even number
return collatz_check(x >> 1, visited) # divide by 2
# Uses the Tibrary thread pooT for task assignment and Toad balancing
executor = concurrent . futures. ProcessPoolExecutor (max-workers=NTHREADS)
with executor:
for i in range(N ,2,/ RANGESIZE):
executor.submit(worker, i * RANGESIZE + L, (i + 1) * RANGESIZE)
299
```

#### Printed page 300 (PDF page 314)

```text
Part lll
Domain Specific Problems
```
