# Exercise 15.1: The Towers of Hanoi problem

**Printed textbook page:** 219. **Reference transcription pages:** 219–220.

> **Unverified OCR transcription:** This section retains the supplied PDF text layer. It is not certified verbatim: code syntax, mathematical symbols, and page boundaries may be corrupted. When two exercises begin on the same page, their excerpts overlap. Do not paste extracted code into a `.py` file without manual verification.

#### Printed page 219 (PDF page 233)

```text
Recursion is especially suitable when
computer granunar.
recursive rules such as a
P3
Recursion is a good choice for search, enumeration, and divide-and-conquer.
IJse recursion as alternative to deeply nested iteration loops. For example, recursion is much
better when youhave an undefined number of levels, such as the IP address problem generalized
to k substrings.
If you are asked to remove recursion from a program, consider mimicking call stack with the
stack data structure.
Recursion can be easily removed from a tail-recursive program by using a while-loop-no stack
is needed. (Optimizing compilers do this.)
If a recursive function may end up being called with the same arguments more than once, cache
the results-this is the idea_b9h4d Dynamic Plogr_amming (Chapter 16)
Table 15.1 : Top Tips lor Recursion
15,1 THs Townns or HlNor pRoBLEM
A peg contains rings in sorted orde1, with the largest ring being the lowest. You are to transfer these
rings to another peg, which is initially empty. This is illustrated in Figure 15.2.
P7
P2 
P3 
P1 
P2
(a) lnitial configuration. 
(b) Desired configuration.
Figure 15.2: Tower of Hanoi with 5 pegs.
Write a program which prints a sequence of operations that transfers n rings from one peg to
another. You have a third peg, which is initially empty. The only operation you can perform is
taking a single ring from the top of one peg and placing it on the top of another peg. You must
never place a larger ring above a smaller ring.
Hint: lf you know how to transfer the top n - 1 rings, how does that help move the n th ring?
Solution: The insight to solving this problem can be gained by trying examples. The three ring
transfer can be achieved by moving the top two rings to the third peg, then moving the lowest ring
(which is the largest) to the second peg, and then transferring the two rings on the third peg to the
second peg, using the first peg as the intermediary. To transfer four rings, move the top three rings
to the third peg, then moving the lowest ring (which is the largest) to the second peg, and then
transfer the three rings on the third peg to the second peg, using the first peg as an intermediary.
For both the three ring and four ring transfers, the first and third steps are instances of the same
219
```

#### Printed page 220 (PDF page 234)

```text
problem, which suggests the use of recursion. This approach is illustrated in Figure 15.3. Code
implementing this idea is given below.
PI
P2
P3
(a) Move all but the lowest ring from PL to P3 using P2 as an
intermediary.
(b) Move the lowest ring lrom Pl to P2.
P3
P2
P1
P1 
P2 
P3 
P1 
P2
(c) Move the rings to PS lo P2 using Pl. 
(d) Solvedl
Figure 15.3: A recursive solution to the Tower of Hanoi tor n = 6.
P3
NUM-PEGS = 3
def compute-tower-hanoi (num-rings) :
def compute-tower-hanoi-steps(num-rings-to-move, from-peg, to-peg, use-peg)
if num-rings-to-move > 0:
compute-tower-hanoi-steps(num-rings-to-move 
- 1, from-peg, use-peg,
to-peg )
pegs Ito_peg] . append(pegs Ifrom_peg] . pop())
result. append([from-peg, to-peg])
compute-tower-hanoi-steps(num-rings-to-move 
- 1, use-peg, to-peg,
from-peg )
# Initialize 
pegs.
result = []
pegs = [list(reversed(range(1, num-rings + 1)))
I + ttl for _ in range(l, NUll-PEGS)l
compute-tovrer-hanoi-steps(num-rings, 0, 1, 2)
return result
The number of moves, T(n), satisfies the following recurrencet T(n) = T(n - 1) + 1 + T(n - 1) =
1 + 2T(n - 1). The first T(n - 1) corresponds to the transfer of the top fl - 1 rings from P1 to P3, and
the second T(n-L) corresponds to the transfer from P3 to P2. This recurrence solves toT(n) = 2n -'1.
One way to see this is to "unwrap" the recurrence: T(n) = 1. +2+4+ "'+2kT(n -k). Printing a
single move takes O(1) time, so the time complexity is O(2").
Variant: Solve the same problem without using recursion.
220
```
