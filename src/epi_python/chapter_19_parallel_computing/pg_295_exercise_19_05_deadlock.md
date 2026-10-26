# Exercise 19.5: Deadlock

**Printed textbook page:** 295. **Reference transcription pages:** 295–295.

> **Unverified OCR transcription:** This section retains the supplied PDF text layer. It is not certified verbatim: code syntax, mathematical symbols, and page boundaries may be corrupted. When two exercises begin on the same page, their excerpts overlap. Do not paste extracted code into a `.py` file without manual verification.

#### Printed page 295 (PDF page 309)

```text
Suppose you find that the program has poor performance because it frequently blocks on I/O. What
steps could you take to improve the program's performance? Feel free to use €my utilities from the
standard library, including concurrency classes.
Hint:Use multithreading, but control the number of threads.
Solution: The first attempt to solve this problem mightbe to launch a new thread per request rather
than process the request itself:
SERVERPORT = 8080
serversock = socket. socket (socket. AF_INET, socket. S0CK_STREAI.I)
serversock.bind(( ", 
SERVERPORT))
serversock. listen(5)
rbile True:
sock, addr = serversock.accepto
threading. Thread(target=process_req , args=(sock, )) . starto
The problem with this approach is that we do not control the number of threads launched. A
thread consurnes a nontrivial amount of resources, such as the time taken to start and end the thread
and the memory used by the thread. For a lightly-loaded serveL this may not be an issue but under
load, it can result in exceptions that are challenging, if not impossible, to handle.
The right trade-off is to use a thread pool. As the name implies, this is a collection of threads,
the size of which is bounded. A thread pool can be implemented relatively easily using a blocking
queue/ i.e., a queue which blocks the writing thread on a put until the queue is empty. However,
since the problem statement explicitly allows us to use library routines, we can use
SERVERPoRT = 8080
NTHREADS = 2
executor = concurrent . futures . ThreadPoorExecutor (max_workers=NTHREADs)
serversock = socket. socket (socket. AF_IilET , socket. SOCK_STREAII)
serversock.bind(( ", 
SERVERPORT))
serversock. listen(5)
rhile True:
sock , addr = serversock. accept o
executor. submit (process_req , sock)
19.5 Dsaorocr
\A/hen threads need to acquire multiple locks to enter a critical section, deadlock can result. As an
example, suPPose both T1 andTzneed to acquire locks L and M. If 11 first acquires L, and then T2
then acquires M, they end up waiting on each other forever.
Identify a concurrency bug in the program below, and modify the code to resolve the issue.
class Account
-global-id = 0
def --init--(self 
, balance) :
self._balance = balance
self. -id = Account. -globaI_id
Account.-global-id += 1
self. -1ock = threading . Rlock o
29s
```
