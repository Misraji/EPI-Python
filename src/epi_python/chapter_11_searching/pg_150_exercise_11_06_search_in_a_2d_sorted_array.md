# Exercise 11.6: Search in a 2D sorted array

**Printed textbook page:** 150. **Reference transcription pages:** 150–151.

> **Unverified OCR transcription:** This section retains the supplied PDF text layer. It is not certified verbatim: code syntax, mathematical symbols, and page boundaries may be corrupted. When two exercises begin on the same page, their excerpts overlap. Do not paste extracted code into a `.py` file without manual verification.

#### Printed page 150 (PDF page 164)

```text
else :
left = mid
return left
The time complexity is O(log f ), where s is the tolerance.
Variant Given two positive floating point numbers r and /, how would you compute f to within a
specified tolerance e if the division operator cannot be used? You cannot use any library functions,
such as log and exp; addltion and multiplication are acceptable.
Generalized search
Now we consider a number of search problems that do not use the binary search principle. For
example, they focus on tradeofft between RAM and computation time, avoid wasted comparisons
when searching for the minimum and maximum simultaneously, use randomization to perform
elimination efficiently, use bitJevel manipulations to identify missing elements, etc.
71.6 Srancn lu a 2D soRrED ARRAY
Calla2D array sorted if its rows and its columns are nondecreasing. See Figure 11.3 for an example
of a 2D sorted array.
RO
R1
R2
R3
R4
R5
CO C1
-1 2
15
36
35
68
C2 C3 C4
21
22
24
25
40
4
5
6
8
9
4
9
9
10
72
L0 t2 13
8
Figure 11 .3: A 2D sorted array.
Design an algorithm that takes a 2D sorted array and a number and checks whether that number
appears in the array. For example, if the input is the 2D sorted array in Figure 1.1.3, and the number
is 7, your algorithm should retum false; if the number is 8, your algorithm should return true.
Hint: Can you eliminate a row or a column per comparison?
Solution: Let the 2D array be A and the input number be x. We can perform binary search on each
row independently, which has a time complexity O(mlogn), where m is the number of rows and n
is the number of columns. (If searching on columns, the time complexity isO(nlogm).)
Note that the above approach fails to take advantage of the fact that both rows and columns are
sorted-it treats separate rows independently of each other. For example, if r < A[0][0] then no row
or column can contain r-the sortedness property guarantees that A[0][0] is the smallest element
inA.
150
```

#### Printed page 151 (PDF page 165)

```text
Howeve4 if r > A[0][0], we cannot eliminate the first row or the first column of A. Searching
along both rows and columns will lead to a O(mn) solution, which is far worse than the previous
solution. The same problem arises if r < Alm - 1l[n - 1].
A good rule of design is to look at extremal cases. We have already seen that there is nothing to
be gained by comparing with At0ltO] and Alm - l|ln - 11. However, there are some more extremal
cases. For example, suppose we compare x with AlDlln - U. If x = Al})ln - 1], we have found the
desired value. Otherwise:
o x > Al1lln - 11, in which case r is greater than all elements in Row 0.
o x < Al}lln - 11, in which case r is less than all elements in Column n - 1.
In either case, we have a 2D aruay with one fewer row or column to search. The other extremal case,
namely comparing withA[m - 1]t0l yields a very similar algorithm.
CO Cl. C2 C3 C4
CO Cl C2 C3 C4
R0-'t24
RO
R1
R2
R3
R4
R5
10 12 13 40
45
-1 2446
155921
366
922
10 24
R1
R236
R336
R468
15s
6
8
9
R58
6 8 9 1225
810121340
(b) Search for 8 (pres6nt)
(a) Search lor 7 (not present)
Flgure 11.4: Sample searches in a 2D array.
In Figure 77.4(a), we show how the algorithm proceeds when the input number is 7. It compares
the top-right entry, AIOlt4] = 6 with 7. Since 7 > 6, we know 7 cannot be present in Row 0. Now
we comPare with A[1][al = 21.. Since 7 < 2L, we know 7 cannot be present in Column 4. Now
we comPare with A[1][3] = 9. Since 7 < 9, we know 7 cannot be present in Column 3, Now we
comPare with A[1][2] = 5. Since 7 > 5, we know 7 cannot be present in Row 1. Now we compare
with A[2][2] = 6. Since 7 > 6, we know 7 cannot be present in Row 2. Now we compare with
At3ll21 = 8. Since 7 < 8, we know 7 cannot be present in Column 2. Now we compare with
At3llll = 6. SinceT > 6,weknowTcannotbepresentinRow3. NowwecomparewithA[4][1] = 8.
Since 7 < 8, we know 7 cannot be present in Column 1. Now we compare with A[a][0] = 6. Since
7 > 6,we knowTcannotbepresentinRow4. NowwecomparewithA[5][0] = 8. Since 7 <8,we
know 7 cannot be present in Column 0. There are no remaining entries, so we retum false.
In Figure 11.4(b), we show how the algorithm proceeds when the input number is 8. We
eliminate Row 0, then Column 4, then Column 3, then Row L, then Row 2. When we compare with
At3lt2] we have a match so we retum true.
def matrix-search (A, x) :
row, col = 0, Ien(Atol) - 1 # Start fron the top-right corner.
# Keeps searching whiTe there are uncl.assified rows and colunns
rhile row < len(A) and col >= 0:
if A[row][col] == x;
151
```
