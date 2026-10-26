# Exercise 24.7: Identify positions attacked by rooks

**Printed textbook page:** 359. **Reference transcription pages:** 359–359.

> **Unverified OCR transcription:** This section retains the supplied PDF text layer. It is not certified verbatim: code syntax, mathematical symbols, and page boundaries may be corrupted. When two exercises begin on the same page, their excerpts overlap. Do not paste extracted code into a `.py` file without manual verification.

#### Printed page 359 (PDF page 373)

```text
i %= len(A)
A[:] = A[::-1] 
# revetse whole ]ist
A[:i] = A[:i] [:: -1] # reverse A[:i] 
part
AIi: ] = AIi: ] [: : -1] 
# reverse A[i:] 
part
We note in passing that a completely different approach is to perform the rotation in blocks of k,
reusing freed space for temporary storage. It can be made to work, but the final rotation has to be
performed very carefully, and the resulting code is complex.
24.7 IprN'rrry posrrroNs ATTACKED By RooKS S
This problem is concemed with computing squares in a chessboard which can be attacked by rooks
that have been placed at arbitrary locations. The scenario is illustrated in Figure 2a.1@).
11111
11. 111
11111
11, 101
10111
11111
0
0
01011
00000
0000
010L
000
010
11101
71111
0000
011
0
1,
0
1
(a) lnitial placement ol 5 rooks on an
8 x 8 chessboard.
(b) Rook placemenl trom (a) en-
coded using an 8 x 8 2D anay-a 0
indicales a rook is placed at that po-
sition.
(c) 2D anay encoding positions that
can be attacked by rooks placed as
in (a)-a 0 indlcates an attacked po-
sition.
Flgure 24.1 : Flook attack.
Write a program which takes as input a 2D array A of 1s and 0s, where the 0s encode the positions
of rooks on an /! x m chessboard, as show in Figure 24.1,b) and updates the array to contain 0s at all
locations which can be attacked by rooks, as shown in Figure zaJ,@).
Hint: Make use of the first row and the first column.
Solution: This problem is trivial with an additional n-bit array R and an additional ffi-bit array C.
We simply initialize R and C to 1s. Then we iterate through all entries of A, and for each (1, fl such
that A[i][i] = 0, we set R[f] and C[i] to 0. Consequently, a 0 in RU] indicates that Row I should be set
to 0; columns are analogous. A second iteration through all entries can be used to set the 0s in A.
The drawback with the above approach is the use of O(n + m) additional storage. The solution
is to use storage in A itself. The reason we c€u:r do this is because if a single 0 appears in a row,
the entire row is cleared. Consequently, we can store a single extra bit r denoting whether Row 0
has a 0 within it. Now Row 0 can play the role of C in the algorithm in the previous paragraph. If
we record a 0 in RU], that is the value we would be writing at that location, so the original entry is
not lost. If R[l] holds a 1 after the first pass, it retains that value, unless r indicates Row 0 is to be
cleared. Columns are handled in exactly the same way.
359
```
