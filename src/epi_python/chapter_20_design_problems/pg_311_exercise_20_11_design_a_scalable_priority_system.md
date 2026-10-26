# Exercise 20.11: Design a scalable priority system

**Printed textbook page:** 311. **Reference transcription pages:** 311–311.

> **Unverified OCR transcription:** This section retains the supplied PDF text layer. It is not certified verbatim: code syntax, mathematical symbols, and page boundaries may be corrupted. When two exercises begin on the same page, their excerpts overlap. Do not paste extracted code into a `.py` file without manual verification.

#### Printed page 311 (PDF page 325)

```text
o Since we usually download one file in one request, if a file is greater than D bytes, there is no
way we can meet the constraint of serving fewer than b bytes every minute, unless we can
work with the lower layers of the network stack such as the transport layer or the network
layer. Often the system designer could look at the distribution of file sizes and conclude that
this problem happens so infrequently that we do not care. Alternatively, we rrtay choose to
download no more than the first b bytes of any file.
o Given that the host's bandwidth is a resource for which there could be contention, one
important design choice to be made is how to resolve a contention. Do we let requests get
served in first-come first-served order or is there a notion of priority? Often crawlers have a
built-in notion of priority based on how irnportant the document is to the users or how fresh
the current copy is.
One way of doing this could be to maintain a permission server with which each crawler checks
to see if it is okay to hit a particular host. The server can keep an account of how many bytes
have been downloaded from the server in the last minute and not permit any crawler to hit the
server if we are already close to the quota. If we do not care about priority, then we cEU:r keep the
interface synchronous where a server requests permission to download a file and it immediately
gets approved or denied. If we care about priorities, then the server may enqueue the request and
inform the crawler when the file is available for download. The queues at the permission server
may be based on priorities.
If the permission server becomes a bottleneck, we can use multiple permission servers such
that the responsibility of a given host is decided by applying a hash function to the host name and
assigning it to a particular server based on the hash code.
20.77 DrsrcN A scALABLE pRroRrry sysrEM
Maintaining a set of prioritized jobs in a distributed system can be tricky. Applications include a
search engine crawling web pages in some prioritized order, as well as event-driven simulation in
molecular dynamics. In both cases the number of jobs is in the billions and each has its own priority.
Designa system formaintaininga setof prioritized jobs that implements the followingAPl: (1.) insert
a new job with a given priority; (2.) delete a job; (3.) find the highest priority job. Each job has a
unique ID. Assume the set cannot fit into a single machine's memory.
Hint: How would you partition jobs across machines? Is it always essential to operate on the highest priority
job?
Solution: If we have enough RAM on a single machine, the most simple solution would be to
maintain a min-heap where entries are ordered by their priority. An additional hash table can be
used to map jobs to their corresponding entry in the min-heap to make deletions fast.
A more scalable solution entails partitioning the problem across multiple machines. One ap-
proach is to apply a hash function to the job ids and partition the resulting hash codes into ranges,
one Per machine. Insert as well as delete require communication with just one server. To do extract-
min, we send a lookup minimum message to all the machines, infer the min from their responses,
and then delete it.
At a given time many clients may be interested in the highest priority event, and it is challenging
to distribute this problem well. If many clients are trying to do this operation at the same time, we
311
```
