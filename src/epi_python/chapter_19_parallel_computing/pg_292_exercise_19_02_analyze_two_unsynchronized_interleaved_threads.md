# Exercise 19.2: Analyze two unsynchronized interleaved threads

**Printed textbook page:** 292. **Reference transcription pages:** 292–292.

> **Unverified OCR transcription:** This section retains the supplied PDF text layer. It is not certified verbatim: code syntax, mathematical symbols, and page boundaries may be corrupted. When two exercises begin on the same page, their excerpts overlap. Do not paste extracted code into a `.py` file without manual verification.

#### Printed page 292 (PDF page 306)

```text
SpellCheckService. closest-to-last-word = result
resp . encode-into-response (result)
Varianh Threads 1 to n execute a method called criticalo. Before this, they execute a method called
rendezoous). The synchronization constraint is that only one thread can execute critical) at a time,
and all threads must have completed executing rsndezuous) before critical) can be called. You can
assume n is stored in a variable n that is accessible from all threads. Design a synchronization
mechanism for the threads. All threads must execute the same code. Threads may call critical)
multiple times, and you should ensure that a thread cannot call critical) a (k + 1)th time until all
other threads have completed their kth calls to critical).
19.2 ANrarvzr rwo uNSyNcHRoNlzED INTERLEAVED THREADS
Threads f 1 and t2 each increment an integer variable N times, as shown in the code below. This
program yields nondeterministic results. Usually, it prints 2N but sometimes it prints a smaller
value. The problem is more pronounced for large N. As a concrete example, on one run the program
output 1320209 when N = 1000000 was specified at the cornmand line.
N = 1000000
counter = 0
def increment-thread O :
global counter
for - in range (N) :
counter=counter+1
t1 = threading.Thread(target=increment-thread)
t2 = threading.Thread(target=increment-thread)
t1. start o
t2. start o
t1. join()
t2 . join o
print (counter)
\Atrhat are the maximum and minimum values that could be printed by the program as a function
of N?
Hint: Be as perverse as you can when scheduling the threads.
Solution: First, note that the increment code is unguarded, which opens up the possibility of its
value being determined by the order in which threads that write to it are scheduled by the thread
scheduler.
The maximumvalue is 2N. This occurs when the thread scheduler runs one thread to comPletion,
followed by the other thread.
When N = 1, the minimum value for the count variable is 1: f1 reads, t2 reads, fl. increments
and writes, then f2 increments and writes. lzVhen N > 1, the final value of the count variable must
be at least 2. The reasoning is as follows. There are two possibilities. A thread, call it T, performs
a read-increment-write-read-increment-write without the other thread writing between reads, in
292
```
