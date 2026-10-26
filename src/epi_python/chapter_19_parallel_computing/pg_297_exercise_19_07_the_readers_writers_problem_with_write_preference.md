# Exercise 19.7: The readers-writers problem with write preference

**Printed textbook page:** 297. **Reference transcription pages:** 297–297.

> **Unverified OCR transcription:** This section retains the supplied PDF text layer. It is not certified verbatim: code syntax, mathematical symbols, and page boundaries may be corrupted. When two exercises begin on the same page, their excerpts overlap. Do not paste extracted code into a `.py` file without manual verification.

#### Printed page 297 (PDF page 311)

```text
Solution: We want to keep track of whether the string is being read from, as well as whether the
string is being written to. Additionally, if the string is being read from, we want to know the number
of concurrent readers. We achieve this with a pair of locks-a read lock and a write lock-and a
read counter locked by the read lock.
A reader proceeds as follows. It locks the read lock, increments the counter, and releases the
read lock. After it performs its reads, it locks the read lock, decrements the counter, and releases
the read lock. A writer locks the write lock, then performs the following in an infinite loop. It locks
the read lock, checks to see if the read counter is 0; if so, it performs its write, releases the read lock,
and breaks out of the loop. Finally, it releases the write lock. As in Solution 19.3 on Page 293, we
use wait-notify primitives to avoid busy waiting.
# LR and LW are c-lass attributes in the Rf class.
# They serve as read and write locks, The integer
# variabTe read_count in R[ tracks tfie nunber of readers
class Reader (threading. Thread) :
def run(seIf):
while True:
with RI{.LR:
RIl.read_count += 1
print (RW. data)
with RW.LR:
RW. read-count -=
RW. LR. noti fy o
do-something_eIse o
class Writer (threading . Thread) :
def run(self):
while True:
Hith Rtl .LI{:
done = False
rhile not done:
with RW.LR:
if RI{.read_count == 0:
Rll . data += 1
done = True
else:
# use wait/notify to avoid busy waiting
while RW. read-count ! = 0:
RI{.LR.wait()
do-something-e1se o
19.7 THs nsannns-wRrrERs pRoBLEM wrrH wRrrE pREFERENcE
Suppose we have an object s as in Problem 19.6 on the preceding page. In the solution to Problem 19.6
on the facing Page, a reader R1 may have the lock; if a writer W is waiting for the lock and then a
reader R2 requests access, R2 will be given priority over W. If this happens often enough, W will
starve. Instead, suppose we want W to start as soon as possible.
297
```
