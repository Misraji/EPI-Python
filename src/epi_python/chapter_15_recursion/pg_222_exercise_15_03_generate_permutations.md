# Exercise 15.3: Generate permutations

**Printed textbook page:** 222. **Reference transcription pages:** 222–223.

> **Unverified OCR transcription:** This section retains the supplied PDF text layer. It is not certified verbatim: code syntax, mathematical symbols, and page boundaries may be corrupted. When two exercises begin on the same page, their excerpts overlap. Do not paste extracted code into a `.py` file without manual verification.

#### Printed page 222 (PDF page 236)

```text
lead to conflicts on columns and diagonals. It can be represented by an array of length n, where the
Ith entry is the location of the queen on Row l.
As an example, if n = 4, begin by placing the first row's queen at Column 0. Now we enumerate
all placements of the form (0,-,-,-). Placing the second row's queen at Column 0leads to a
column conflict, so we skip all placements of the form (0,0, -, -). Placing the second row's queen
at Column 1 leads to a diagonal conflict, so we skip all placements of the form (0, '1, -, -). Now we
tum to placements of the form (0,2,0, -). Such placements are conflicting because of the conflict on
Column 0. Now we tum to placements of the form (0,2,1, -) and (0,2,2, -). Such placements are
conflicting because of the diagonal conflict between the queens at Row 1 and Column 2 and Row 2
and Column 1, and the column conflict between the queens at Row 1 and Column 2 and Row 2
and Column 2, respectively, so we move on to (O,2,3,-), which also violates a diagonal constraint.
Now we advance to placements of the form (0,3, -, -). Both (0,3,7,-) and (0,3,2, -) lead to conflicts,
implying there is no nonattacking placement possible with a queen placed at Row 0 and Column 0.
The first nonattacking placement is (1.,3,0,2); the only other nonattacking placement is (2,0,3,1).
def n-queens (n) :
def solve-n-queens (row) :
if row == n:
# A77 queens are 1ega77y placed.
result . append (list (col-placement) )
return
for co1 in range(n):
# Test if a newly pTaced queen rill 
confTict any earlier queens
# placed before.
if aII(
abs(c - col) not in (0, row - i)
for i, c in enunerate(c01-placement[:row])):
col-placementIrow] - col
solve-n-queens(row + 1)
result, col-placement = [] , [0] * n
solve-n-queens (0)
return result
The time complexity is lower bounded by the number of nonattacking placements. No exact form
is known for this quantity as a function of n, but it is conjectured to tend to nlf cn, where c x 2.54,
which is super-exponential.
Varianh Compute the number of nonattacking placements of n queens on an n x n chessboard.
Varianh Compute the smallest number of queens that can be placed to attack each uncovered
square.
Variant Compute a placement of 32 knights, or 14 bishops, 16 kings or 8 rooks on an 8 x 8 chessboard
in which no two pieces attack each other.
15.3 GTNnneTTPERMUTATIoNS
This problem is concemed with computing all permutations of an array. For example, if the array
is \2,3,5,7) one output could be <2,3,5,7), <2,3,7,5>, <2,5,3,7>, <2,5,7,3>, <2,7,3,5>, <2,7,5,3>,
222
```

#### Printed page 223 (PDF page 237)

```text
<3,2,5,7>, <3,2,7,5>, <3,5,2,7>, <3,.5,7,2>, <3,7,2,5>, <3,7,5,2>, <5,2,3,7>, <5,2,7,3), <5,3,2,7>,
<5,3,7,2>, <5,7,2,3>, <5,7,2,3), <7,2,3,5), <7,2,5,3>, <7,3,2,5), <7,3,5,2), <7,5,2,3>, (7,5,3,2). (Any
other ordering is acceptable too.)
Write a program which takes as input an array of distinct integers and generates all permutations
of that array. No permutation of the array may appear more than once.
Hint: How many possible values are there for the first element?
Solution: Let the input array be A. Suppose its length is n. A truly brute-force approach would be
to enumerate all arrays of length n whose entries are from A, and check each such array for being a
permutation. This enumeration can be performed recursively, e.g., enumerate all arrays of length
n - 1 whose entries are from A, and then for each array, consider the n arrays of length n which is
formed by adding a single entry to the end of that array. Since the number of possible anays is nn,
the time and space complexity are staggering.
A better approach is to recognize that once a value has been chosen for an entry, we do not want
to repeat it. Specifically, every permutation of A begins with one of A[0],A[1] ,. . . ,Aln - 11. The
idea is to generate all permutations that begin with A[0], then all permutations that begin with A[1],
and so on. Computing all permutations beginning with A[0] entails computing all permutations of
Al1,,n - 1], which suggests the use of recursion. To compute all permutations beginning with A[1]
we swap A[0] with A[1] and compute all permutations of the updated Al1.,n - 11. We then restore
the original state before embarking on computing all permutations beginning with A[2], and so on.
For example, for the artay (7,3,5), we would first generate all permutations starting with7.
This entails generating all permutations of (3,5), which we do by finding all permutations of (3,5)
begiruring with 3. Since (5) is an array of length 1, it has a single permutation. This implies (3,5)
has a single permutation beginning with 3. Next we look for permutations of (3,5) beginning with
5. To do this, we swap 3 and 5, and find, as before, there is a single permutation of (3,5) beginning
with5,namely,(5,3). Hence,therearetwopermutationsofAbeginningwithT,narrrely(7,3,5)and
(7,5,3). We swap 7 with 3 to find all permutations beginning with 3, namely <3,7,5> and (3,5,7).
The last two permutations we add are (5,3, 7) and <5,7,3).In all there are six permutations.
def permutations (A) :
def directed-permutations (i) :
if i == Ien(A) - 1:
result . append (A. copy O )
return
# Try every possibility for Atil.
for j in range(i, len(A)):
Atil, Atjl = Atjl, Atil
# Generate a-lJ pernutations for A[i + 1:]
directed_permutations(i + 1)
AIil, Atjl = Atjl, AIi]
result = []
directed-permutations (0)
return result
The time complexity is determined by the number of recursive calls, since within each function
the time spent is O(1), not including the time in the subcalls. The number of function calls, C(n)
223
```
