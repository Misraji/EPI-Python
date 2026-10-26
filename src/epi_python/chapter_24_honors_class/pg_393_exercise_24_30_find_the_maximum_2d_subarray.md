# Exercise 24.30: Find the maximum 2D subarray

**Printed textbook page:** 393. **Reference transcription pages:** 393–394.

> **Unverified OCR transcription:** This section retains the supplied PDF text layer. It is not certified verbatim: code syntax, mathematical symbols, and page boundaries may be corrupted. When two exercises begin on the same page, their excerpts overlap. Do not paste extracted code into a `.py` file without manual verification.

#### Printed page 393 (PDF page 407)

```text
Solution: A brute-force approach is to examine all 2D subarrays. Since a 2D subarray is character-
izedby two diagonally opposite comers the total number of such arrays is O(m2n2). Each 2D sub-
array canbe checked by examining the corresponding entries, so the overall complexity isO(m3n3).
This can be easily reduced to O(mznz) by processing 2D subarrays by size, and reusing results-the
2Dsubarray A[i,i+a)lj,j+ b]isfeasibleif andonlyif the2Dsubarrays Afi,i+a-lllj,j+b-l],
Afi+ a,i+ allj, j+b -1), A[i,i + a - ll|j+b, j+b], md Ali+ a,i+ al[j+b, j+ b] are feasible. This
is an O(1) time operation, assuming that feasibility of the smaller 2D subarrays has already been
computed and stored. (Note that this solution requires O(mznz) storage.)
The following approach lowers the time and space complexity. For each feasible entry A[i][l]
we record (hi,j,wi,), where hi,iis the largest L such that all the entries rn Afi,i + L -ll[j, j) arc feasible,
and wi,i is the largest L such that all the entries n Ali,illj, j+ L - 1l are feasible. This computation
can be performed nO(mn) time, and requires O(mn) storage.
Now for each feasible entry Alilli) we calculate the largest 2D subarray that has AUIIj] as its
bottom-left corner. We do this by processing each entry in Aft, i+h;,i-1)U, il.As we iterate through
the entries in vertical ordeq, we update zp to the smallest ar;,, amongst the entries processed so far.
The largest 2D subarray that has Ali)ljl as its bottom-left comer and A[i'][jl as its top-left comer
has area (i' - i + 1)w. We track the largest 2D subarray seen so far across all Alillil processed.
def max-rectangle-submatrix (A) :
llaxHW = collections.namedtuple('llaxHl{', ('h',
# DP tabTe stores (h, w) for each (i, jl.
table = [[None] * len(A[O]) for _ in Al
'w') )
for i, row in reversed(list(enunerate(A))):
for j, v in reversed(list(enunerate(row))):
# Find the Targest h such that (j, j) to (i + h - 1, jl are feasible
# Find the largest r such that (i , j) to (i, j + w - 1) are feasjble
tableIi] [j] = (uaxHw(tableli + 1l tjl.h + t
if i + 1 < Ien(A) else t, tabletiltj + 1l.w + 1
ifj+1<len(row)else1)
if v else UaxHW(O, 0))
rnax_rect_area = 0
for i, row in enunerate(A):
for j, v in enunerate(row):
# Process (i, j) if it js feasible and is possibie to update
# nax-rect_area.
if v and table [i] [j ] .w o table [i] tjl . h > max_rect_area:
min_width = float('inf ')
for a in range(tabletil tjl.h):
min-width = nin(min-width , table [i + a] tj I . w)
max_rect_area = nax(max_rect_area, min_width * (a + 1))
return max_rect_area
The time complexity per Alilljl is proportional to the number of rows, i.e., O(n), yielding an overall
time complexity of O(mnz), and space complexity of O(mn).
If we are looking for the largest feasible square region, we ctu:r improve the complexity as
follows-we compute the (h;,i,w;,) values as before. Suppose we know the length s of the largest
square region that has Ali + ll[j+ 1] as its bottom-left corner. Then the length of the side of the
largest square with A[,][] as its bottom-left corner is at most s + 1, which occurs if and only if
393
```

#### Printed page 394 (PDF page 408)

```text
hi,i >s+1andwi,j 2s+l.Thegeneralexpressionforthelengthismin(s+1.,hi,i,wi,).Notethatthis
is an O(1) time computation. L:r total, the run time is O(mn), a factor of n better than before.
The calculations above can be sped up by intelligent pruning. For example, if we already have
a feasible 2D subarray of dimensions H x W, there is no reason to process an entry Alilljl for which
hr,j.Handwi,i <W.
def max-square-submatrix (A) :
HaxHW = collections.namedtuple('uaxHw', ('h','w'))
# DP table stores (h, w) for each (i, jl.
table = [[None] * 1en(A[0]) for - in Al
for i, row in reversed(Iist(enunerate(A))):
for j, v in reversed(Iist(enunerate(row))):
# Finds the largest h such that (i, i) to (i + h - 1, i) are feasibTe.
# Finds the largest w such that (i,j) 
to (i, i + w - 1) are feasible.
tablelil [j] = (uaxHw(table[i + 1] tjl.h + 1
if i + I < len(A) else 1, tabletiltj + 1l.w + 1
ifj+1<len(row)e1seI)
if v else UaxHw(0, 0))
# A table stores the length of the Targest square for each (i, j).
s = tt0l * len(A[0]) for - in Al
maI-Square-area = 0
for i, row in reversed(Iist(enunerate(A))):
for j, v in reversed(Iist(enunerate(row))):
if v:
side = nin(tabletil Ijl.h, tabletil tjl.w)
# Gets the length of Targest square with botton-7eft cotnet (i,
# j) '
if i + t < Ien(A) and j + I < len(Ali + 1]):
side = nin(sIi + 1]tj + 1l + 1, side)
slil tjl = side
max-square-area = nal(nax-square-area, side**2)
return max-square-area
The largest 2D subarray can be found n O(nm) time using a qualitatively different apProach.
Essentially, we reduce our problem to n instances of the largest rectangle under the skyline problem
described in Problem 17.8 on Page 270. First, for each AU][l] we determine the largest h;,7 such that
Ali,i+hi,i-7l[j,i]isfeasible.(IfAtilljl=0thenhi,j=0.)Thenforeachofthenrows,startingwith
the topmost one, we compute the largest 2D subarray whose bottom edge is on that row in time
O(m), ustng Solution 17.8 on Page 271.. This computation can be performed in time O(r) once the
hi,,, values have been computed. The final solution is the maximum of the n instances.
The time complexity for each row is O(m) for computing the h values, assuming we record the
k values for the previous row and O(m) for computing the largest rectangle under the skyline, i.e.,
O(m)rntotal per row. Therefore the total time complexity isO(mn). The additional space comPlexity
is O(m)-this is the space for recording the h values and running the largest rectangle under the
skyline computation.
def max-rectangle-submatrix (A) :
table=[0]*Ien(A[0])
max-rect-area = 0
# Find the maxinur anong a77 instances of the Targest rectangTe
for row in A:
394
```
