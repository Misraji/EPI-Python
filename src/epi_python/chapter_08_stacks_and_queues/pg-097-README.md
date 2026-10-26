# Chapter 8: Stacks And Queues

**Starts at printed page 97.** [Repository overview](../../../README.md)

**Source:** user-supplied EPI Python PDF (2016/2017 edition). **Transcription warning:** PDF text extraction contains OCR errors, especially in code. Consult the original PDF for ambiguous expressions and diagrams.

## Original chapter introduction (unverified PDF text layer)

### Printed page 97

```text
Cneprsn
Stacks and Queues
Linear lists in which insertions, deletions, and accesses to aal-
ues occut alfiost always at the flst or the last node are oery
frequmtly encountered, and we gioe them specinl names . . .
- "The Art of Computer Programming, Volume 1.,"
D. E. KNurn,1997
Stacks support last-in, first-out semantics for inserts and deletes, whereas queues are first-in,
first-out. Stacks and queues are usually building blocks in a solution to a complex problem. As we
will soon see, they can also make for stand-alone problems.
Stacks
A stack suPports two basic operations-push and pop. Elements are added (pushed) and removed
(popped) in last-in, first-out order, as shown in Figure 8.1. If the stack is empty, pop typically
retums null or throws an exception.
When the stack is implemented using a linked list these operations have O(1) time complexity.
If it is implemented using an array, there is maximum number of entries it can have-push and pop
are still O(1). If the array is dynamically resized, the amortized time for both push and pop is O(1).
A stack can support additional operations such as peek, which retums the top of the stack without
popping it.
push 3
4
3
I
L
L
2
2
2
(a) lnitial configuration.
(b) Popping (a).
Flgure 8.1 : Operations on a stack.
(c) Pushing 3 on to (b)
Stacks boot camp
The last-in, first-out semantics of a stack make it very useful for creating reverse iterators for
sequences which are stored in a way that would make it difficult or impossible to step back from
a given element. This a prograrn uses a stack to print the entries of a singly-linked list in reverse
order.
pop
97
```
