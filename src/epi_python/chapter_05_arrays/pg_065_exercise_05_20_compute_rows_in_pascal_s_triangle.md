# Exercise 5.20: Compute rows in Pascal's Triangle

**Printed textbook page:** 65. **Reference transcription pages:** 65–66.

> **Unverified OCR transcription:** This section retains the supplied PDF text layer. It is not certified verbatim: code syntax, mathematical symbols, and page boundaries may be corrupted. When two exercises begin on the same page, their excerpts overlap. Do not paste extracted code into a `.py` file without manual verification.

#### Printed page 65 (PDF page 79)

```text
Since we are not explicitly required to allocate a new array, it is natural to ask if we can perform
the rotation in-place, i.e., with O(1) additional storage. The first insight is that we c.rn perform the
rotation in a layer-by-layer fashion-different layers canbe processed independently. Furthermore,
within a layer, we can exchange groups of four elements at a time to perform the rotation, e.g.,
send L to 4's location, 4 to 16's location,16 to 13's location, and L3 to 1's location, then send 2 to 8's
location, 8 to 15's location, 15 to 9's location, and 9 to 2's location, etc. The program below works
its way into the center of the array from the outermost layers, performing exchanges within a layer
iteratively using the four-way swap just described.
def rotate-matrix ( square-matrix) :
natrix-size = len(square_rnatrix) - 1
for i in range(len(square-matrix) // 2):
for j in range(i, matrix-size - i):
# Perform a 4-way exchange. I{ote that A[-i] for i in [0, len(A) - 1]
# is A[-(i + 1)].
(square-matrix til t j l, square_natrix [-j ] [i], 
square_matrix t-il t-jl,
square-matrixtjl t-il) = (square-matrix[-j] [i],
square_matrix t-il i-jl ,
square_matrix tjl t-il, 
square_matrix til tjl)
The time complexity isO(nz) and the additional space complexity is O(1).
Interestingly, we can get the effect of a rotation with O(1) space and time complexity, albeit with
some limitations. Specifically, we retum an object r that composes the original matrix A. A read
of the element at indices i and i in r is converted into a read from A at index [n - 1- l]ft1. Writes
are handled similarly. The time to create r is constant, since it simply consists of a reference to A.
The time to perform reads and writes is unchanged. This approach breaks when there are clients
of the original A object, since writes to r change A. Even if A is not written to, if methods on the
stored objects change their state, the system gets corrupted. Copy-on-write can be used to solve
these issues.
class Rotatedl{atrix:
def --init--(self , square-matrix) :
seIf.-square-matrix = square-matrix
def read-entry(self, i , j) ,
# Note that A[-i] for i in [0, len(A) - tJ is A[-(i + 1)]
return se1f. _square_matrix t-j I til
def write-entry(se1f, i, j, v):
self. -square-matrix t-j I til = v
Variant: Implement an algorithm to reflect A, assumed to be an n x n 2D array, about the horizontal
axis of symmetry. Repeat the same for reflections about the vertical axis, the diagonal from top-left
to bottom-right, and the diagonal from top-right to bottom-left.
5.20 Coupurr Rows rN Pascer's TnlaNcrr
Figure 5.5 on the following page shows the first five rows of a graphic that is known as Pascal's
triangle. Each row contains one more entry than the previous one. Except for entries in the last
65
```

#### Printed page 66 (PDF page 80)

```text
1
1
1
1
2
1
1
J
3
1
1
4
6
4
1
Flgure 5.5: A Pascal triangle.
row, each entry is adjacent to one or two numbers in the row below it. The first row holds 1, Each
entry holds the sum of the numbers in the adjacent entries above it.
Write a program which takes as input a nonnegative integer n and returns the first n rows of Pascal's
triangle.
Hint: Write the given fact as an equation.
Solution: A brute-force approach might be to organize the arrays in memory similar to how they
appear in the figure. The challenge is to determine the correct indices to range over and to read
from.
A better approach is to keep the arrays left-aligned, that is the first entry is at location 0. Now it
is simple: the 7thentry in the lthrow is lif j= 0 or i = l, otherwise itis the sum of tn" (l - 1)thand
7th entries in the (l - 1)th row. The first row Ro is (1). The second row R1 is (1, 1). The third row R2
is(1,Rr[0]+Rr[1] =2,1). ThefourthrowR3is(1,R2[0]+Rz[U =3,R2[1]+R2[2] =3,1).
def generate-pascal-triangle (n) :
result = [[1] o (i + 1) for i in range(n)l
for i in range(n):
for j in range(l, i):
# Sets this entry to the sun of the two above adjacent entries
resulttiltjl 
= resultti - lltj - 1l + resultti - lltjl
return result
Since each element takes O(L) time to compute, the time complexity is O(1 + 2 + "' + n) = O(n(n +
1)12) = O(nz).Similarly, the space complexity is O(nz).
It is a fact that the lth entry in the nth row of Pascal's triangle is (l). This in itself does not
trivialize the problem, since computing (l) itself is tricky. (In fact, Pascal's triangle can be used to
compute (l).)
Varianh Compute the nth row of Pascal's triangle using O(n) space.
66
```
