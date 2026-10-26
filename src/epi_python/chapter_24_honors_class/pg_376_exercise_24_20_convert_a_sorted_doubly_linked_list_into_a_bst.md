# Exercise 24.20: Convert a sorted doubly linked list into a BST

**Printed textbook page:** 376. **Reference transcription pages:** 376–377.

> **Unverified OCR transcription:** This section retains the supplied PDF text layer. It is not certified verbatim: code syntax, mathematical symbols, and page boundaries may be corrupted. When two exercises begin on the same page, their excerpts overlap. Do not paste extracted code into a `.py` file without manual verification.

#### Printed page 376 (PDF page 390)

```text
The design of a hash function appropriate for lines is more challenging than it may seem at first.
The equation of the line through (xr,yi and (x2,y) is
!/z' At 
xzAt - xtAz
Y= x2-xlr- rr-n 
'
One idea would be to compute a hash code from the slope and the Y-intercept of this line as an
ordered pair of floating-point numbers. However, because of finite precision arittrmetic, we may
have three points that are collinear map to distinct buckets.
A more robust hash fr.rnction treats the slope and the Y-intercept as rationals. A rational is an
ordered pair of integers: the numerator and the denominator. We need to bring the rational into a
canonical form before applying the hash function. One canonical form is to make the denominator
always nonnegative, and relatively prime to the numerator. Lines parallel to the Y-axis are a special
case. For such lines, we use the X-intercept in place of the Y-intercept, and use f, as the slope.
Point = collections.namedtuple("Point", ("x", "y"))
def find-line-with-most-points (points) :
result = 0
for i, pl in enunerate(points):
slope-table = collections . defaultdict (int)
overlap-points = 1
for p2 in points[i + 1:]:
if Pl == P2:
overlaP-Points += 1
elif PI . x == P2. x:
# A vertical line with slope 1/0.
slope-tablet(0, 1)l += 1
else:
x-diff, y-diff = pl.x - p2.\, pl.y - p2.y
gcd = fractions.gcd(x-diff, y-diff)
x-diff, y-diff = x-diff / scd, y-diff / gcd
slope-table [ (x-diff , y-diff) ] += r
result = nar(resu1t,
overlap-points + nax(slope-table.valuesO, default=0))
return result
24.20 CoNvEnr A soRrED DouBLy LINKED LISr INro ,c. BST I
Lists and BSTs are both examples of "linked" data strucfures, i.e., some fields are references to other
objects of the same type. Since nodes in a doubly linked list and in a BST both have a key field and
two references, it's natural to consider the following problem.
Write a program that takes as input a doubly linked list of sorted numbers and builds a height-
balanced BST on the entries in the list. Reuse the nodes of the list for the BSI using the previous
and next fields for the left and right children, respectively. See Figure 24.6(b) on the next page for
an example of a doubly linked list, and Figure 2a.6@) on the facing page for the BST on the same
nodes.
Hint: Update reference fields, not node contents.
376
```

#### Printed page 377 (PDF page 391)

```text
0x 1000
Ox1 I 40
0x 14 3O
0x2 0 50
0x2460
(a) A BST on five nodes-edges that do not terminate in nodes denot€ empty sub-
trees. The numbor in hex adjacent to each node represenls its address in memory.
0x2050 
0x1840 
0xi460 
0x1000 
0x14to
(b) The sorted doubly linked list corresponding to the BST In (a). Note how the tree nodes have been used for the list nodes.
Flgure 24.6: BST and sorted doubly linked list interconversion.
Solution: If the list nodes were in an array, we could index directly into the array to obtain the
midpoint, and the time complexity would satisfy T(n) = O(1) + zf(r), where n is the number of
nodes in the list, which solves to T(n) = O(n).This is the approach of Solution 14.8 on Page 210. We
can recycle the list nodes, but creating the array entails O(n) additional space.
A direct approach to the construction which does not allocate new nodes is to find the midpoint
of the list, and use it as the root, recursing on the first half and the second half of the list. The time
complexity satisfies the recurrence T(n) = O(n) + zf($)-the O(n) term comes from the traversal
required to find the midpoint of the list, which itself entails computing the length of the list. This
solves to T(n) = O(nlogn). The added time complexity compared to the array-based approach
comes from the inability to find a midpoint in a list in O(1) time.
The key insight to improving the time complexity without adding to the space complexity is
noting that since we have to spend O(n) trrne to find the midpoint, we should do more than just get
the midpoint. Specifically, we can first create a balanced BST on the first Lf J nodes. Then we use
the (Ltl + t)th node as the root of the final BST and set its left child to the BST just created.
Since we are changing the links in the list, we need to be careful to ensure we can recover the
root. We can do this by keeping a reference to the head of the list being processed, and advancing
this reference inside the recursive calls. This allows us to compute the root while computing the
left subtree.
Finally we create a balanced BST on the remainin gn - til - 1 nodes, and set it as the root's right
child.
# Returns the root of the corresponding Bsr. The prev and next fields of the
# List nodes are used as the 8sr nodes Teft and right fields, respectively.
# The Tength of the ]ist is given.
def build-bst_from_sorted_doubly_tist(L, n) :
# BuiTds a BST fron the (start + 1)-th to the end-th node, inclusive, in L,
# and returns the root.
B
X
2
]-
{
J
F
5
-{
7
>
11 X
J//
```
