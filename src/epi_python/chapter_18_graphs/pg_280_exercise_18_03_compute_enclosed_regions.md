# Exercise 18.3: Compute enclosed regions

**Printed textbook page:** 280. **Reference transcription pages:** 280–280.

> **Unverified OCR transcription:** This section retains the supplied PDF text layer. It is not certified verbatim: code syntax, mathematical symbols, and page boundaries may be corrupted. When two exercises begin on the same page, their excerpts overlap. Do not paste extracted code into a `.py` file without manual verification.

#### Printed page 280 (PDF page 294)

```text
Variant: Design an algorithm for computing the black region that contains the most points.
Varianh Design an algorithm that takes a point (a,b), sets A(a,b) to black, and returns the size of
the black region that contains the most points. Assume this algorithm will be called multiple times,
and you want to keep the aggregate run time as low as possible.
18.3 CoMpurs ENCLosED REGIoNS
This problem is concemed with computing regions within a 2D grid that are enclosed. See Fig-
ure'1,8.7 for an illustration of the problem.
mtr
ffi
r---l
II
tl
ffi
t-r
LJ
(a) 
(b)
Figure 18.7: Three of the four white squares in (a) are enclosed, i.e., there is no path from any of them to the boundary
that only passes through white squares. (b) shows the white squares that are not enclosed.
The computational problem can be formalized using 2D arrays of Bs (blacks) and Ws (whites)
Figure 1"8.7(a) is encoded by
^[?
Figure 18.7(b) is encoded by
Let A be a2D array whose entries are either W or B. Write a program that takes A, and replaces all
Ws that cannot reach the boundary with a B.
Hint: lt is easier to compute the complement of the desired result.
Solution: It is easier to focus on the inverse problem, namely identifying Ws that can reach the
boundary. The reason that the inverse is simpler is that if a W is adjacent to a W that is can reach the
boundary, then the first W can reach it too. The Ws on the boundary are the initial set. Subsequently,
we find Ws neighboring the boundary Ws, and iteratively grow the set. Whenever we find a new
W that can reach the boundary, we need to record it, and at some stage search for new Ws from
it. A queue is a reasonable data structure to track Ws to be processed. The approach amounts to
breadth-first search starting with a set of vertices rather than a single vertex.
B B Bl
BWBI
wwBl
B BB]
IB B B B1
l, BB Bl
l; ;i')
280
```
