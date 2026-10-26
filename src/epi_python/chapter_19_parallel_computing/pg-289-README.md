# Chapter 19: Parallel Computing

**Starts at printed page 289.** [Repository overview](../../../README.md)

**Source:** user-supplied EPI Python PDF (2016/2017 edition). **Transcription warning:** PDF text extraction contains OCR errors, especially in code. Consult the original PDF for ambiguous expressions and diagrams.

## Original chapter introduction (unverified PDF text layer)

### Printed page 289

```text
Cueprsn
Parallel Computing
The actiaity of a computer must include the proper reacting to a possibly
great oaiety of messages that can be sent to it at unpredictable mommts,
a situation which occurs in all information systems in which a number of
computers are coupled to uch other,
- 
" Cooperating sequential processes,"
E. W. Dryxsrna, 1965
Parallel computation has become increasingly corunon. For example, laptops and desktops come
with multiple processors which communicate through shared memory. High-end computation is
often done using clusters consisting of individual computers communicating through a network.
Parallelism provides a number of benefits:
o High performance-more processors working on a task (usually) means it is completed faster.
o Better use of resources-a program can execute while another waits on the disk or network.
o Fairness-letting different users or programs share a machine rather than have one program
run at a time to completion.
o Convenience-it is often conceptually more straightforward to do a task using a set of con-
current Programs for the subtasks rather than have a single program manage all the subtasks.
o Fault tolerance-if a machine fails in a cluster that is serving web pages, the others can take
over.
Concrete applications of parallel computing include graphical user interfaces (GUI) (a dedicated
thread handles UI actions while other threads are, for example, busy doing network communication
and passing results to the UI thread, resulting in increased responsiveness), java virtual machines (a
seParate thread handles garbage collection which would otherr,rrise lead to blocking, while another
thread is busy running the user code), web servers (a single logical thread handles a single client
request), scientific computing (a large matrix multiplication can be split across a cluster), and web
search (multiple machines crawl, index, and retrieve web pages).
The two primary models for parallel computation are the shared memory model, in which
each processor can access any location in memory, and the distributed memory model, in which a
Processor must explicitly send a message to another processor to access its memory. The former is
more appropriate in the multicore setting and the latter is more accurate for a cluster. The questions
in this chapter are focused on the shared memory model.
Writing correct parallel programs is challenging because of the subtle interactions between
parallel components. One of the key challenges is races-two concurrent instruction sequences
access the same address in memory and at least one of them writes to that address. Other challenges
to correctness are
o starvation (a processor needs a resource but never gets it; e.g., Problem 19.6 on Page 296),
o deadlock (Thread A acquires Lock L1 and Thread B acquires LockL2,following which A tries
to acquire L2 and B tries to acquire L1), and
289
```

### Printed page 290

```text
o livelock (a processor keeps retrying an operation that always fails)'
Bugs caused by these issues are difficult to find using testing. Debugging them is also difficult
because they may not be reproducible since they are usually load dependent. It is also often true
that it is not possible to realize the performance implied by parallelism-sometimes a critical task
cannot be parallelized, making it impossible to improve performance, regardless of the number
of processors added. Similarly, the overhead of communicating intermediate results between
processors can exceed the performance benefits.
The problems in this chapter focus on threadJevel parallelism. Problems concemed with par-
allelism on distributed memory architecturesl e.g., cluster computing, are usually not meant to be
coded; they are popular design and architecture problems. Problems 20.9 on Page 310, 20.10 on
Page 310, 20.11 on Page 311, and20.77 on Page 316 cover some aspects of cluster-level parallelism.
P arullel coffiputing b o ot camp
A semaphore is a very powerful synchronization construct. Conceptually, a semaphore maintains
a set of permits. A thread calling acquire) on a semaphore waits, if necessary until a permit is
available, and then takes it. A thread calling release) on a semaphore adds a permit and notifies
threads waiting on that semaphore, potentially releasing a blocking acquirer.
iuport threading
class Semaphore O :
def --init-- 
(self , max-available) :
self. cv = threading . condition o
self . UAX-AVAILABLE = max-available
self.taken = 0
def acquire (self) :
self. cv . acquire o
while (se1f. taken == self. I{AX-AVAILABLE)
seIf. cv . wait o
self.taken += 1
self. cv . release o
def release (self) :
self. cv. acquire o
self.taken -= 1
self, cv . notify o
self. cv. release o
an algorithm that
IS
seen tobe correct. Then
concurrency, while ensuring the critical parts are locked.
When analyzing parallel code, assume a worst-case thread scheduler. In particular, it may
choose to schedule the same thread repeatedly, it may altemate between two threads, it may
starve a thread, etc.
Try to work at a higher level of abstraction. In particular, know the concurrency libraries-
don't implement your own semaphores, thread pools, deferred execution/ etc. (You should
implemented, and implement them if asked to.)
Table 19.1 l Top Tips for Concurrency
know how these features are
290
```
