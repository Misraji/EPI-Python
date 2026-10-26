# Chapter 20: Design Problems

**Starts at printed page 301.** [Repository overview](../../../README.md)

**Source:** user-supplied EPI Python PDF (2016/2017 edition). **Transcription warning:** PDF text extraction contains OCR errors, especially in code. Consult the original PDF for ambiguous expressions and diagrams.

## Original chapter introduction (unverified PDF text layer)

### Printed page 301

```text
CueprrR
Design Problems
Don't be fooled by the many books on complexity or by the many
complex and arcane algorithms you find in this book or elsewhere.
Although there are no textbooks on simplicity, simple systems
work and complex don't.
- 
"Transaction Processing: ConcEts and Techni4ues,"
l. Gxrt,1992
You may be asked in an interview how to go about creating a set of services or a larger system,
possibly on top of an algorithm that you have designed. These problems are fairly open-ended,
and many can be the starting point for a large software project.
In an interview setting when someone asks such a question, you should have a conversation in
which you demonstrate an ability to think creatively, understand design trade-offr, and attack un-
familiar problems. You should sketch key data structures and algorithms, as well as the technology
stack (programming language, libraries, OS, hardware, and services) that you would use to solve
the problem.
The answers in this chapter are presented in this context-they are meant to be examples of
good responses in an interview and are not comprehensive state-of-the-art solutions.
We review pattems that are useful for designing systems in Table 20.1. Some other things to
keep in mind when designing a system are implementation time, extensibility, scalability, testability,
security, intemationalization, and IP issues.
Table 20.1 : System design patterns.
Algorithms and Data Struc-
tures
Decomposition
Identify the basic algorithms and data structures
ftalability
Split the functionality, architecture, and code into manageable,
reusable components.
Break the problem into subproblems that can be solved rela-
tively independently on different machines, Shard data across
machines to make it fit. Decouple the servers that handle writes
from those that handle reads. Use replication across the read
servers to gain more performance. Consider caching computa-
tion and later look it up to save work.
Decomposition
Good decompositions are critical to successfully solving system-level design problems. Function-
ality, architecture, and code all benefit from decomposition.
301
```
