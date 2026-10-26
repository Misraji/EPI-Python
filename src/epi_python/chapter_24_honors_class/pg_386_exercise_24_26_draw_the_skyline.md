# Exercise 24.26: Draw the skyline

**Printed textbook page:** 386. **Reference transcription pages:** 386–387.

> **Unverified OCR transcription:** This section retains the supplied PDF text layer. It is not certified verbatim: code syntax, mathematical symbols, and page boundaries may be corrupted. When two exercises begin on the same page, their excerpts overlap. Do not paste extracted code into a `.py` file without manual verification.

#### Printed page 386 (PDF page 400)

```text
rhile left-start 
< mid and right-start 
< end:
if AIleft-start] 
<= AIright-start]:
sorted-A. append (A I left-start 
] )
left-start 
+= 1
else :
# A[7eft-start:nid] 
are the inversions of A[right-start]
inversion-count += mid - left-start
sort e d-A . append (A I ri ght-st art ] )
right-start 
+= 1
# Updates A with sorted-A.
Atstart: endl = sorted-A + AIleft-start:mid] 
+ AIright-start: 
end]
return inversion-count
if end - start <= 1:
return 0
mid - (start + end,) // 
2
return (
count-subarray-inversions ( start, rnid) + count-subarray-inversions (
mid, end) + merge-sort-and-count-inversions-across-subarrays (
start , mid, end) )
return count-subarray-inversions (0, len(A))
The time complexity satisfies T(n) = O(n) + ZT(n - L), which solves to O(nlogn), where n is the
length of the array.
Varianh Runners numbered from 0 ton-L race on a straight one-way road to a colrlrnon finish line.
The runners have different (constant) speeds and start at different distances from the finish line.
Specifically, Runner I has a speed s; and begins at a distance d; from the finish line. Each runner
stops at the finish line, and the race ends when all runners have reached the finish line. How many
times does one runner pass another?
24.26 Dnaw rue sxvrrNr $
A number of buildings are visible from a point. A building appears as a rectangle, with the bottom
of each building lying on a fixed horizontal line. A building is specified using its left and right
coordinates, and its height. One building may partly obstruct anothe(, as shown in Figure 24.8(a) on
the facing page. The skyline is the list of coordinates and corresponding heights of what is visible.
For example, the skyline corresponding to the buildings in Figure 2a.8@) on the next page is
given in Figure 24.80) on the facing page. (The patterned rectangles within the skyline are used to
describe Problem 17.8 on Page270; they are not relevant to the current problem.)
Design an efficient algorithm for computing the skyline.
Hlaf: Think of an efficient way of merging skylines.
Solution: The simplest solution is to compute the skyline incrementally. For one building, the
skyline is trivial. Suppose we know the skyline for some buildings, and need to compute the
skyline when another building is added. Let the new building's left and right coordinates be L and
R, and its height H. To add it, we iterate through the existing skyline from left to right to see where
386
```

#### Printed page 387 (PDF page 401)

```text
7
6
5
4
3
2
1
0 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 1,5 1,6 L7 L8
(a) A set of buildings.
3 4 5 6 7 8 9 1011127374',t5L6771,8
(b) Skyline lor the buildings in (a).
Flgure 24.8: Buildings, their skyline, and the largest contained rectangle. The text label identifying the building is just
below and to the right of its upper left-hand corner.
L should be added. Then we move through the existing skyline until we pass R, increasing any
heights that are less than H to H.
This algorithm is simple, but has O(n2) complexity if there are n buildings, since adding the nth
building may entail O(n) comparisons. The key to improving efficiency is the observation that it
takes linear time to merge two skylines (if they are represented in left-to-right order), which is the
same as the time to merge a single skyline, but gets much more done.
Now it is clear what the textbook solution is: use divide-and-conquer to compute skylines for
one half of the buildings, the other half of the buildings, and then merge the results. The merge is
similar to the procedure for adding a single building, described above, and can be performed nO(n)
time. We iterate through the two skylines together from left-to-right, matching their X coordinates,
and updating heights appropriately. Our website has a link to a program based on the algorithm
above. The time complexity T(r) satisfies the recurrence T(n) = 2T(nl2) + O(n), where the latter
term comes from the merge step. This solves to T(n) = O(nlogn).
As an example, consider merging the skyline for Buildings A,B,C, D with the skyiine for Build-
ings E, d, G, H. From 0 to 7 , the skyline for A, B, C, D determines the height, because these are the
only buildings present. At 7, since the skyline for A,B,C,D is taller, than that for E,F,G,H, we use
its height, 4, going forward. At 8, since the skyline for E,F,G,H is talleq, so we use its height, 3,
going forward. After 9, the skyline for E,F,G,H determines the height, because these are the only
buildings going forward.
6
5
4
3
2
1,
0
0
2
F
c
G
D
H
B
I
387
```
