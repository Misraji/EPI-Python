# Exercise 21.1: Garbage Collection

**Printed textbook page:** 319. **Reference transcription pages:** 319–319.

> **Unverified OCR transcription:** This section retains the supplied PDF text layer. It is not certified verbatim: code syntax, mathematical symbols, and page boundaries may be corrupted. When two exercises begin on the same page, their excerpts overlap. Do not paste extracted code into a `.py` file without manual verification.

#### Printed page 319 (PDF page 333)

```text
Cneprnn
Language Questions
The limits of my language means the limits of my world.
- L. WrrrcsNsrrrr.I
21,.1, Gennecr CorrscrroN
What is garbage collection? Explain it in the context of Python.
Solution: Garbage collection is the process of finding data objects in a running program that cannot
be accessed in the future, and to reclaim the resources, particularly memory, used by those objects.
A garbage-collected language is one in which the garbage collection happens automatically-Java,
C#, Python, and most scripting languages are examples. C is a notable example of a nongarbage-
collected language-the programmer is responsible for knowing when to allocate and deallocate
memory.
o Most garbage-collected languages used either reference counting (track the number of refer-
ences to an object) or tracing (finding objects that are reachable by a sequence of references
from certain "root" objects, and considering the rest as " garbage" and collecting them). Python
uses reference counting, which has the benefit that it can immediately reclaim objects when
the reference count goes to 0; the cost for this is the need for storing an additional integer-value
per object. Tracing, which is used in Java, has the benefit that it can be performed in a separate
thread, which makes it higher performance. A weakness of tracing is that when the garbage
collector runs, it pauses all threads-this leads to nondeterministic performance (sporadic
pauses).
o A challenge with reference counting is "reference cycles"-objects A and B reference each
other, e.g., A .u = B andB.a = A. The reference count never drops below 1-, even if nothing else
references A and B. The garbage collector periodically looks for these, and removes them.
o Garbage collectors used heuristics for speed. For example, empirically, recently created objects
are more likely to be dead. Therefore, as objects are created, they are assigned to generations,
and younger generations are examined first.
21.2 Crosunn
\A/hat does the following program print, and why?
increment-by_i = [Iaubda x: x + i for i in range(lO)]
print (incrernent-by-i t3l (4) )
319
```
