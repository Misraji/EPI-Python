# Exercise 19.6: The readers-writers problem

**Printed textbook page:** 296. **Reference transcription pages:** 296–296.

> **Unverified OCR transcription:** This section retains the supplied PDF text layer. It is not certified verbatim: code syntax, mathematical symbols, and page boundaries may be corrupted. When two exercises begin on the same page, their excerpts overlap. Do not paste extracted code into a `.py` file without manual verification.

#### Printed page 296 (PDF page 310)

```text
def get-balance(self) :
return self.-balance
@s t at i cme thod
def transfer (acc-from , acc-to , amount) :
th = threading.Thread(target=acc_from._move, args=(acc-to, amount))
th. start o
def -move (self, acc-to , amount) :
with self. -1ock:
if amount > self.-balance
return False
acc-to.-balance += amount
self.-balance -= amount
print('returning 
True')
return True
Solution: Suppose U1 initiates a transfer toU2, and immediately afterwards, U2 initiates a transfer
to UL. Since each transfer takes place in a separate thread, it's possible for the first thread to lock
U1 and then the second thread to be scheduled in and take the lock U2. The program is now
deadlocked--each of the two threads is waiting for the lock held by the other thread.
One solution is to have a global lock which is acquired by the transfer method. The drawback is
that it blocks transfers that are unrelated, e.g., U3 cannot transfer to U4 if there is a pending transfer
from U5 to U6.
The canonical way to avoid deadlock is to have a global ordering on locks and acquire them in
that order. Since accounts have a unique integer id, the update below is all that is needed to solve
the deadlock.
lock1 = self.-lock if seIf.-id < acc-to.-id else acc-to.-lock
lock2 = acc-to.-lock if self.-id < acc-to.-id else se1f.-lock
# Does not ratter if Lockl equals 7ock2: since recursive-mutex locks
# are reentrant, we wi77 re-acquire 7ock2,
with lock1, 1ock2:
79.6 Trlr nuprns-wRrrERS PRoBLEM
Consider an object s which is read from and written to by many threads. (For example, s could
be the cache from Problem 19.1 on Page 297.) You need to ensure that no thread may access s for
reading or writing while another thread is writing to s. (TWo or more readers may access s at the
same time.)
One way to achieve this is by protecting s with a mutex that ensures that two threads cannot
access s at the same time. However, this solution is suboptimal because it is possible that a reader
R1 has locked s and another reader R2 wants to access s. Reader R2 does not have to wait until R1
is done reading; instead, R2 should start reading right away.
This motivates the first readers-writers problem: protect s with the added constraint that no
reader is to be kept waiting if s is currently opened for reading.
Implement a synchronization mechanism for the first readers-writers problem.
Hint: Track the number of readers.
296
```
