# Exercise 5.18: Compute the spiral ordering of a 2D array

**Printed textbook page:** 61. **Reference transcription pages:** 61–63.

> **Unverified OCR transcription:** This section retains the supplied PDF text layer. It is not certified verbatim: code syntax, mathematical symbols, and page boundaries may be corrupted. When two exercises begin on the same page, their excerpts overlap. Do not paste extracted code into a `.py` file without manual verification.

#### Printed page 61 (PDF page 75)

```text
def is-vaIid-sudoku(partial_assignment) 
:
# Return True if subarray
# partiaT-assignnent Istart-row:end_row][start-col:end_coL] contains any
# dupTicates in {1, 2, ..., 
7en(partial_assignnent)}; ot}rerwjse return
# Fa7se.
def has-duplicate (block) :
block = list(filter(lanbda 
x: x l= 0, block))
return len(block) != len(set(block))
n = len(partial-assignment)
# Check row and column constraints.
if any(
has_duplicate([partial_assignmentti] [j] for j in range(n)l)
or has_duplicate([partial_assignmentIj] [i] for j in range(n)l)
for i in range(n)):
return False
# Check region constraints.
region-size = int(math. sqrt(n))
return all(not has_duplicate([
partial-assi gnment tal tbl
for a in range(region-size * I, region-size t (I + 1))
for b in range(region-size * J, region-size * (l + 1))
l) for I in range(region-size) for J in range(region_size))
# Pythonic so-Iution that exploits the poiler of list compreiension.
def is-valid-sudoku-pythonic (partial-assignment) :
region-size = int(math. sqrt(Ien(partial_assignment)))
return nar(
collections . Counter (k
for i, row in enu[erate(partial-assignment)
for j, c in enumerate(row)
if c != 0
for k in ((i, str(c)), (strqcl , i;,
(i ,/ region-size, j / region-size,
str(c)))).valueso,
default=0) <= 1
The time complexity of this algorithm for an n x r Sudoku grid with fi x ,,ln subgrids is O(n2) +
O(nz) + O(n2l(,,|i)'x ,1la\ = O(n2); the terms correspond to the complexity to check n row
constraints, the n column constraints, and the n subgrid constraints, respectively. The memory
usage is dominated by the bit array used to check the constraints, so the space complexity is O(n).
Solution 15.9 on Page 230 describes how to solve Sudoku instances.
5.18 Coupurr rHE sprRAL oRDERTNG oF A 2D ARRAy
A 2D array can be written as a sequence in several orders-the most natural ones being row-
by-row or colurnn-by-column. L:r this problem we explore the problem of writing the 2D array
in spiral order. For example, the spiral ordering for the 2D array in Figure 5.3(a) on the fol-
61,
```

#### Printed page 62 (PDF page 76)

```text
lowing page is <1.,2,3,6,9,8,7,4,5>. For Figure 5.3(b) on the next page, the spiral ordering is
<1, 2, 3, 4, 8, 72, 1.6, 1.5, L4, 13, 9, 5, 6, 7, 11., 1.0>.
C6 
Cr 
C2 
C3
R6 1234
Ce 
Cl 
Cz
R0 123
567
8
91011
t2
13 14 ls 
t6
(a) Spiralorderingfora3x3array. (b) Spiral ordering lor a4x4array.
FIgure 5.3: Spiral orderings. Column and row ids are specified above and to the lett of the matrix. The value 1 is at
entry R6, C6.
Write a program which takes an n x n 2D array and retums the spiral ordering of the array.
Hint: U se case analysis and divide-and-conquer.
Solution: It is natural to solve this problem starting from the outside, and working to the center.
The naive approach begins by adding the first row, which consists of n elements. Next we add the
n - 1 remaining elements of the last column, then the n - 1 remaining elements of the last row, and
then the n - 2 remaining elements of the first column. The lack of uniformity makes it hard to get
the code right.
Here is a uniform way of adding the boundary. Add the first n - 1 elements of the first row.
Then add the first n - 1 elements of the last column. Then add the last n - 1 elements of the last row
in reverse order, Finally, add the last r - 1 elements of the first column in reverse order.
After this, we are left with the problem of adding the elements of an (n - 2) x (n - 2) 2D
array in spiral order. This leads to an iterative algorithm that adds the outermost elements of
nxn,(n-2)x(n-2),(n-{)x(n-4),...2D arrays. Notethatamatrixof odddimensionhasa
corner-case/ namely when we reach its center.
As an example, for the 3 x 3 array in Figure 5.3(a), we would add7,2 (first two elements of the
first row), then 3,6 (first two elements of the last column), then 9,8 (last two elements of the last
row), then 7,4 (last two elements of the first column). We are now left with the 1, x 1 array, whose
sole element is 5. After processing it, all elements are processed.
Forthe 4x4anay inFigure5.3(b),wewould add1,2,3 (firstthreeelementsof thefirstrow),
then 4,8,12 (first three elements of the last column), then 16,15,14 (last three elements of the last
row), then 13,9,5 (last three elements of the first column). We are now left with a 2 x 2 matrix,
which we process similarly in the order 6,7,71,10, afler which all elements are processed.
def matrix-in-spiral-order(square-matrix) 
:
def matrix-Iayer-in-clockwise (offset) :
if offset == len(square-matrix) - offset - 1:
# square-natrix has odd dinension, and we are at the center of the
Rr
R2
4
7
5
8
5
9
Rr
Rz
R3
62
```

#### Printed page 63 (PDF page 77)

```text
# natrix square-rnatrix.
spiral_ordering. append(square-matrix Ioffset] [offset] )
return
spiral-ordering . extend(square-matrix Ioffset] [offset : -1 - offset] )
spiral-ordering . extend (
list(zip(+square_matrix)) [-1 - offset] [offset: -1 - offset])
spiral-ordering . extend (
square-matrix[-1 - offset] [-1 - offset:offset: -1])
spiral-ordering . extend (
Iist(zip(*square-natrix)) 
[offset] [-1 - offset: offset: -1])
spiral-ordering = 11
for offset in range((Ien(square-matrix) +
matri x-I ayer_in_clockwi se (off set )
return spiral-ordering
r) // 2)
The time complexity isO(nz).
The above solution uses four iterations which are almost identical. Now we present a
solution that uses a single iteration. We start at the entry at Ro, Co. We process entries
in the sequence Ro,Co,R0,Cr,...,R0,Cn-2, i.e., we are moving to the right. Then we pro-
cess entries Ro,Cr-t,R1,Cn-7,...,Rn-2,Cn-.1., i.@., we are moving down. Then we process en-
tries Rr-1,Cn-7,Rn-t,Cn-z,.,.,Rn-1.,Ct, i.e., we are moving to the left. Then we process entries
Rn-1,Cs,Rn-2,C0,. .. ,R1.,C0, i.e., we are moving up. We record that an element has already been
processed by setting it to 0, which is assumed to be a value that is not already present in the ar-
ray. (Any value not in the array works too.) After processing the entry R1, C6 we start the same
Process from R1,C1. This method is applied until all elements are processed. Conceptually, we are
processing the array in "shells" from the outside moving to the center.
def matrix-in-spiral-order(square-matrix) 
:
sHrFr = ((0, 1), (1, 0), (0, -r), (-1, 0))
direction-x-y=0
spiral-ordering = 11
for - in range(len(square-matrix)**2) 
:
spiral-ordering. append(square-matrix txl Iy])
square-natrixlxlIy] = O
next-x, next-y = x + SHIFTldirectionll0l, y + SHIrTIdirection][1]
if (next-x not in range(Ien(square_matrix))
or next_y not in range(1en(square_matrix))
or square-matrixInext-x] [next-y] == 0) :
direction = (direction + 1) & 3
next-x, next-y = x + SHIFTIdirection]t01, y + SHIFTIdirection][1]
x, y = next-x, next-y
return spiral_ordering
The time complexity is O(n2) and the space complexity is O(1),
Variant Given a dimension d,write a program to generate adxd2D anay which in spiral order is
63
```
