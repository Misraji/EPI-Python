# Exercise 20.1: Design a spell checker

**Printed textbook page:** 302. **Reference transcription pages:** 302–302.

> **Unverified OCR transcription:** This section retains the supplied PDF text layer. It is not certified verbatim: code syntax, mathematical symbols, and page boundaries may be corrupted. When two exercises begin on the same page, their excerpts overlap. Do not paste extracted code into a `.py` file without manual verification.

#### Printed page 302 (PDF page 316)

```text
For example, in our solution to designing a system for online advertising (Problem 20.15 on
Page 315), we decompose the goals into categories based on the stake holders. We decompose the
architecture itself into a front-end and a back-end. The front-end is divided into user management,
web page design, reporting functionality, etc. The back-end is made up of middleware, storage,
database, cron services, and algorithms for ranking ads. The design of Tg[ (Problem 20.6 on
Page 307) and Connexus (Problem 20.1.4 on Page 314) also illustrate such decompositions.
Decomposing code is a hallmark of object-oriented programming. The subject of design pattems
is concemed with finding good ways to achieve code-reuse. Broadly speaking, design pattems
are grouped into creational, structural, and behavioral pattems. Many specific patterns are very
natural-strategy objects, adapters, builders, etc., appear in a number of places in our codebase.
Freeman et al.'s "Head First Design Patterns" is, in our opinion, the right place to study design
pattems.
Scalability
In the context of interview questions parallelism is useful when dealing with scale, i.e., when the
problem is too large to fit on a single machine or would take an unacceptably long time on a single
machine. The key insight you need to display is that you know how to decompose the problem so
that
o each subproblem can be solved relatively independently, and
o the solution to the original problem can be efficiently constructed from solutions to the sub-
problems.
Efficiency is typically measured in terms of central processing unit (CPU) time, random access
memory (RAM), networkbandwidth, number of memory and database accesses, etc.
Consider the problem of sorting a petascale integer array. If we know the distribution of the
numbers, thebest approachwouldbe to define equal-sized ranges of integers and send one range to
one machine for sorting. The sorted numbers would just need to be concatenated in the correct order.
If the distribution is not known then we can send equal-sized arbitrary subsets to each machine and
then merge the sorted results, e.g., using a min-heap. Details are given in Solution 20.9 on Page 310.
The solutions to Problems 20.8 on Page 308 and 20.17 on Page 316 also illustrate the use of
parallelism.
Caching is a great tool whenever computations are repeated. For example, the central idea
behind dynamic programming is caching results from intermediate computations. Caching is
also extremely useful when implementing a service that is expected to respond to many requests
over time, and many requests are repeated. Workloads on web services exhibit this property.
Solution 19.1 on Page 2gl sketches the design of an online spell correction service; one of the key
issues is performing cache updates in the presence of concurrent requests. Solution 19.9 onPage299
shows how multithreading combines with caching in code which tests the Collatz hypothesis.
20.L DssrcN A sPELL cHEcKER
Designing a good spelling correction system can be challenging. We discussed spelling correction
in the context of edit distance (Problem '1.6.2 on Page 239). However, in that problem, we only
computed the Levenshtein distance between a pair of strings. A spell checker must find a set of
words that are closest to a given word from the entire dictionary. Furthermore, the Levenshtein
302
```
