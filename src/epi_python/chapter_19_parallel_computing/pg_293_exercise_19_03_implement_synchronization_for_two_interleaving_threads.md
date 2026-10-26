# Exercise 19.3: Implement synchronization for two interleaving threads

**Printed textbook page:** 293. **Reference transcription pages:** 293–293.

> **Unverified OCR transcription:** This section retains the supplied PDF text layer. It is not certified verbatim: code syntax, mathematical symbols, and page boundaries may be corrupted. When two exercises begin on the same page, their excerpts overlap. Do not paste extracted code into a `.py` file without manual verification.

#### Printed page 293 (PDF page 307)

```text
N-'l iterations
-LV\ A
t2
1
read
Itr
I
read
tt
write 
read
write
write
write
N-1 iterations
Figure 19.1 : Worst-case schedule for two unsynchronized threads.
which case the written value is at least 2. If the other thread now writes a 1, it has not yet completed,
so it will increment at least once mone. Otherwise, T's second read refums a value of L or more
(since the other thread has performed at least one write).
The lower bound of 2 is achieved according to the following thread schedule:
o 11 loads the value of the counter, which is 0.
r f2 executes the loop N - L times.
o f1 doesn't know that the value of the counter changed and writes 1 to it.
o t2loads the value of the counter, which is 1.
o ll. executes the loop for the remaining N - 1 iterations.
o f2 doesn't know that the value of the counter has changed, and writes 2 to the counter.
This schedule is depicted in Figure 19.1.
19.3 IvrprrrasNr syNcHRoNrzATroN FoR Two TNTERLEAVTNG THREADs
Thread f1 prints odd numbers from 1 to 100; Thread f2 prints even numbers from 1 to 100.
Write code in which the two threads, running concurrently, print the numbers from 1 to 100 in order.
Hint:The two threads need to noti$r each other when they are done.
Solution: A brute-force solution is to use a lock which is repeatedly captured by the threads. A
single variable, protected by the lock, indicates who went last. The drawback of this approach is
that it employs the busy waiting antipattem: processor time that could be used to execute a different
task is instead wasted on useless activity.
Below we present a solution based on the same idea, but one that avoids busy locking by using
class OddEvenllonitor(threading. Condition)
ODD-TURN = True
EVEN-TURN = FaIse
t1
293
```
