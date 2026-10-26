# Exercise 15.2: Generate all nonattacking placements of n-Queens

**Printed textbook page:** 221. **Reference transcription pages:** 221–221.

> **Unverified OCR transcription:** This section retains the supplied PDF text layer. It is not certified verbatim: code syntax, mathematical symbols, and page boundaries may be corrupted. When two exercises begin on the same page, their excerpts overlap. Do not paste extracted code into a `.py` file without manual verification.

#### Printed page 221 (PDF page 235)

```text
Variank Find the minimum number of operations subject to the constraint that each operation must
involve P3.
Variant: Find the minimum number of operations subject to the constraint that each transfer must
be from P\ to P2, P2 to P3, or P3 to P1.
Variant Find the minimum number of operations subject to the constraint that a ring can never be
transferred directly from P1 to P2 (transfers from P2to Pl are allowed).
Varianh Find the minimum number of operations when the stacking constraint is relaxed to the
following-the largest ring on a peg must be the lowest ring on the peg. (The remaining rings on
the peg can be i. aoy order, e.g., it is fine to have the second-largest ring above the third-largest
ri.g.)
Variant: You have 2n disks of n different sizes, two of each size. You cannot place a larger disk on a
smaller disk, but can place a disk of equal size on top of the other. Compute the minimum number
of moves to transfer the 2n disks from P1. to P2.
Variant: You have 2n disks which are colored black or white. You cannot place a white disk directly
on top of a black disk. Compute the minimum number of moves to transfer the 2n disks from P1 to
P2,
Variant Find the minimum number of operations if you have a fourth peg, P4.
1,5.2 GnNrnanr ALL NoNATTACKTNc rLACEMENTS or n-QurrNs
A nonattacking placement of queens is one in which no two queens are in the same row column,
or diagonal. See Figure 15.4 for an example.
(a) Solution 1. 
(b) Soturion 2.
Figure 15.4: The only two ways in which four queens can be placed on a 4 x 4 chessboard.
Write a program which returns all distinct nonattacking placements of n queens on an n x n
chessboard, where n is an input to the program.
Hint: lf the first queen is placed at (i, j), where can the remaining queens definitely not be placed?
Solution: A brute-force approach is to consider all possible placements of the n queens-there are
(,') possiUte placements which grows very large with n.
Since we never would place two queens on the same row, a much faster solution is to enumerate
placements that use distinct rows. Such a placement cannot lead to conflicts on rows, but it may
221
```
