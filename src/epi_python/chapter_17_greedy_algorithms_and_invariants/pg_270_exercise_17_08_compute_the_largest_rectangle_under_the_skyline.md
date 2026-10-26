# Exercise 17.8: Compute the largest rectangle under the skyline

**Printed textbook page:** 270. **Reference transcription pages:** 270–272.

> **Unverified OCR transcription:** This section retains the supplied PDF text layer. It is not certified verbatim: code syntax, mathematical symbols, and page boundaries may be corrupted. When two exercises begin on the same page, their excerpts overlap. Do not paste extracted code into a `.py` file without manual verification.

#### Printed page 270 (PDF page 284)

```text
Solution: Let A be the array, and n its length. There is a straightforward O(n2) brute-force
solution-for each pair of indices (i, j),i < 7, the water trapped by the corresponding lines is
(j - i) xmin(A[i], A[i]), which can easily be computed in O(1) time. The maximum of all these is the
desired quantity.
In an attempt to achieve a better time complexity, we can try divide-and-conquer. We find the
maximum water that can be trapped by the left half of A, the right half of A, and across the center
of A. Findhg the maximum water trapped by an element on the left half and the right half entails
considering combination s of the n I 2 entries from left half and n /2 entries on the right half . Therefore,
the time complexity T(n) of this divide-and-conquer approach satisfies T(n) = 2f(nP)+O(nzl+)
which solves to T(n) = O(n2). This is no better than the brute-force solution, and considerably
trickier to code.
A good starting point is to consider the widest pair, i.e.,0 and n- 1. We record the corresponding
amount of trapped water, i.e., ((n - 1) - 0) x min(A[0],A[n - 1]). Suppose A[0] > Aln - 1l- Then for
anyk > 0,thewatertrappedbetweenkand n-lislessthanthewatertrappedbetween0andn-t,
so going forward, we only need to focus on the maximum water that can be trapped between 0 and
n - 2. The converse is true if A[0] < Aln - 1]-we need never consider 0 again.
We use this approach iteratively to continuously reduce the subarray that must be explored,
while recording the most water trapped so far. In essence, we are exploring the best way in which
to trade-off width for height.
For the given example, we begin with (O,17), which has a capacity of 1 x 17 = 17. Since the
height of the left line is less than or equal to the height of the right line, we advance to (1,17). The
capacityislx16=16.Since2>l,weadvanceto(1,16).Thecapacityis2x15=30.Since2<4,
we advance to (2,16). The capacity is 1. x 14 = 14. Since 1 < 4, we advance to (3, 15). The capacity is
3 x 13 = 39. Since 3 < 4,we advance to (4, 16). The capacity is 4x12 = 48. Future iterations, which
we do not show, do not surpass 48, which is the result.
def get-max-trapped-water (heights) :
i, j, max-water = 0, len(heights) - 1, 0
while i < j:
width=j-i
max-wat€r = nal(max-water, width * nin(heightslil, heightslil))
if heishts Ii] > heights [j ] :
j -= 1
else : # heights [i] <= heights Ij] .
i+=1
return max_water
We iteratively eliminate one line or two lines at a time, and we spend O(1) time per iteration, so the
time complexity is O(z).
17.8 Coupurn rHE LARGEST RECTANGLE UNDER THE SKYLINE
You are given a sequence of adjacent buildings. Each has unit width and an integer height. These
buildings form the skyline of a city. An architect wants to know the area of a largest rectangle
contained in this skyline. See Figure 17.5 on the next page for an example.
Let A be an array representing the heights of adjacent buildings of unit width. Design an algorithm
to compute the area of the largest rectangle contained in this skyline.
Hint: How would you efficiently find the largest rectangle which includes the ith building, and has height A[l]?
270
```

#### Printed page 271 (PDF page 285)

```text
B
C
D
E
F
C
H
J
K
L
M
6
5
4
3
2
0
01234567891011.1213
Flgure 17.5: A collection of unit-width buildings, and the largest contained rectangle. The te)d label identifying the
building is just below and to the right of its upper left-hand corner. The shaded area is the largest rectangle under the
skyline. lts area is 2 x (11 - 1). Note that the tallest rectangle is from 7 to 9, and the widest rectangle is from 0 to 1., but
neither of these are the largest rectangle under the skyline.
Solution: A brute-force approach is to take each (i,l) pair, find the minimum of subarray Ali, jl, and
multiply that by j - i + 1. This has time complexity O(n3), where n is the length of A. This can be
improved to O(n2) by iterating over I and then I > I and tracking the minimum height of buildings
from f to 7, inclusive. However, there is no reasonable way to further refine this algorithm to get
the time complexity below O(n2).
Another brute-force solution is to consider for each i the furthest left and right we can go without
dropping below Aft] in height. In essence, we want to know the largest rectangle that is "supported"
by Building i, which can be viewed as acting like a "pillar" of that rectangle. For the given example,
the largest rectangle supported by G extends from 1 to 11, and the largest rectangle supported by F
extends from 3 to 6.
We can easily determine the largest rectangle supported by Building I with a single forrvard
and a single backward iteration from l. Since I ranges from 0 to n - 7, the time complexity of this
approach isO(n2).
This brute-force solution can be refined to get a much better time complexity. Specifically,
suPPose we iterate overbuildings from left to right. When we process Building i, we do not know
how far to the right the largest rectangle it supports goes. Howevet we do know that the largest
rectangles supported by earlier buildings whose height is greater than A[i] cannot extend past l,
since Building I "blocks" these rectangles. For example, when we get to F in Figure 17.5, we know
that the largest rectangles supported by Buildings B, D, and E (whose heights are greater than F's
height) cannot extend past 5.
Lookingmore carefully at the example, we see that there's no need to consider B when examining
F, since C has already blocked the largest rectangle supported by B. In addition, there's no reason
to consider C: since G's height is the same as C's height, and C has not been blocked yet, G and C
will have the same largest supported rectangle. Generalizing, aswe advance through the buildings,
all we really need is to keep track of is buildings that have not been blocked yet. Additionally, we
can replace existing buildings whose height equals that of the current building with the current
building. Call these buildings the set of active pillars.
Initially there are no buildings in the active pillar set. As we iterate from 0 to 12, the active pillar
sets are {Al,lA,Bl,lA,Cl, {A,C,Dl, {A,C,D,El,lA,C,Fl, {A,G},lA,G,Hl, {A,G,ll, {A,G,ll,IA,KI, {Ll,
and{.L,Ml.
\A/henever a building is removed from the active pillar set, we know exactly how far to the right
the largest rectangle that it supports goes to. For example, when we reach C we know B's supported
rectangle ends at 2, and when we reach F, we know that D and E's largest supported rectangles end
271
```

#### Printed page 272 (PDF page 286)

```text
at 5.
\Atrhen we remove a blocked building from the active pillar set, to find how far to the left its
largest supported rectangle extends we simply look for the closest active pillar that has a lower
height. For example, when we reach F, the active pillars are {A,C,D,E!. We remove E and D from
the set, since both are taller than F. The largest rectangle supported by E has height 6 and begins
after D, i.e., at 4; its area is 6 x (5 - 4) = 6. The largest rectangle supported by D has height 5 and
begins after C, i.e., at 3; its area is 5 x (5 - 3) = 10.
There are a number of data structures that can be used to store the active pillars and the right data
structure is key to making the above algorithm efficient. When we process a new building we need
to find the buildings in the active pillar set that are blocked. Because insertion and deletion into the
active pillar set take place in last-in first-out order, a stack is a reasonable choice for maintaining
the set. Specifically, the rightmost building in the active pillar set appears at the top. Using a stack
also makes it easy to find how far to the left the largest rectangle that's supported by a building
in the active pillar set extends-we simply look at the building below it in the stack. For example,
when we process F, the stack is A,C,D, E, with E at the top. Comparing F's height with E, we see E
is blocked so the largest rectangle under E ends at where F begins, i.e., at 5. Since the next building
in the stack is D, we know that the largest rectangle under E begins where D ends, i.e., at 4.
The algorithm described above is almost complete. The missing piece is what to do when we
get to the end of the iteration. The stack will not be empty when we reach the end-at the very
least it will contain the last building. We deal with these elements just as we did before, the only
difference being that the largest rectangle supported by each building in the stack ends at n,where
n is the number of elements in the array. For the given example, the stack contains L and M when
we get to the end, and the largest supported rectangles for both of these end at 13.
def calculate-Iargest-rectangle (hei ghts) :
pillar-indices, max-rectangle-area = [] , 0
# By appending [0] to heights , we can unifornly ftandle the couputation for
# rectangTe area here.
for i, h in enunerate(heights + [0]):
while pillar-indices and heights IpiIlar-indices [-1] I >= h:
height = heights [piIlar-indices. popO ]
width = i if not pillar-indices else i - pillar-indicest-11 - 1
max-rectangle-area = nar(max-rectangle-area, height * width)
piIlar-indice s . append (i)
return max-rectangle-area
The time complexity is O(n). When advancing through buildings, the time spent for building is
proportional to the number of pushes and pops performed when processing it. Although for some
buildings, we may perform multiple pops, in total we perform at most /, pushes and at most n pops.
This is because in the advancing phase, an entry I is added at most once to the stack and cannot
be popped more than once. The time complexity of processing remaining stack elements after the
advancing is complete is also O(n) since there are at most n elements in the stack, and the time to
process each one is O(1). Thus, the overall time complexity is O(n). The space complexity is O(n),
which is the largest the stack can grow to, e.g., if buildings appear in ascending order.
Variant: Find the largest square under the skyline.
272
```
