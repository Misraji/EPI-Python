# Exercise 5.17: The Sudoku checker problem

**Printed textbook page:** 60. **Reference transcription pages:** 60–60.

> **Unverified OCR transcription:** This section retains the supplied PDF text layer. It is not certified verbatim: code syntax, mathematical symbols, and page boundaries may be corrupted. When two exercises begin on the same page, their excerpts overlap. Do not paste extracted code into a `.py` file without manual verification.

#### Printed page 60 (PDF page 74)

```text
Multi dimensi o n al an ay s
Thus far we have focused our attention in this chapter on one-dimensional arrays. We now turn our
attention to multidimensional arrays. A2D array in an array whose entries are themselves arraysi
the concept generalizes naturally to k dimensional arrays.
Multidimensional arrays arise in image processing, board games, graphs, modeling spatial
phenomenon, etc. Often, but not always, the arrays that constitute the entries of a 2D array A have
the same length, in which case we refer to A as being anmx n rectangular array (or sometimes
just an m x n array), where ln is the number of entries in A, and n the number of entries in A[0].
The elements within a2D array A are often referred to by their row and column indices i and 7, and
written as AUI[l].
5.17 Tsr Suooxu cHECKER PRoBLEM
Sudoku is a popular logic-based combinatorial number placement puzzle. The objective is to fill
a 9 x 9 grid with digits subject to the constraint that each column, each row, and each of the nine
3 x 3 sub-grids that compose the grid contains unique integers in [1,9]. The grid is initialized with
a partial assignment as shown in Figure 5.2(a); a complete solution is shown in Figure 5.2(b).
(a) Partial assignment. 
O) A complete solution.
Figure 5.2: Sudoku configurations.
Check whether a 9 x9 2D arcay representing a partially completed Sudoku is valid. Specifically,
check that no row, column, or 3 x 3 2D subarray contains duplicates. A O-value in the 2D array
indicates that entry is blank; every other entry is in [1,9].
Hint: Directly test the constraints. Use an array to encode sets.
Solution: There is no real scope for algorithm optimization in this problem-it's all about writing
clean code.
We need to check nine row constraints, nine column constraints, and nine sub-grid constraints.
It is convenient to use bit arrays to test for constraint violations, that is to ensure no number in [1,9]
appears more than once.
# Check if a partiaTTy fi77ed natrix has any con-fl.icts
5
3
7
6
I
9
5
I
8
6
8
6
3
4
8
3
1
7
2
6
5
2
8
4
1
9
5
8
7
9
5
3
4
6
7
8
9
1
2
6
7
2
1
9
5
3
4
8
1
9
8
J
4
2
5
6
7
8
5
9
7
6
1
4
2
3
4
2
6
8
5
3
7
9
1
7
1
J
9
2
4
8
5
6
9
6
1:
5
3
7
2
8
4
2
8
7
4
't
9
6
3
5
3
4
5
2
I
6
1"
7
9
60
```
