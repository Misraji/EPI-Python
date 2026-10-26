# Exercise 4.11: Rectangle intersection

**Printed textbook page:** 35. **Reference transcription pages:** 35–36.

> **Unverified OCR transcription:** This section retains the supplied PDF text layer. It is not certified verbatim: code syntax, mathematical symbols, and page boundaries may be corrupted. When two exercises begin on the same page, their excerpts overlap. Do not paste extracted code into a `.py` file without manual verification.

#### Printed page 35 (PDF page 49)

```text
number-of_outcomes = upper-bound - lower_bound + 1
rhile True:
result,i=0,0
while (1 << i) < number_of_outcomes:
# zero-one_randonO is the provided randon nunber generator
result - (result << 1) | zero_one_randomo
i+= I
if result < number-of-outcomes:
break
return result + Iower_bound
Toanalyzethetimecomplexity,lett=b-a+1. Theprobabilitythatwesucceedinthefirsttryistl2i.
Since 2' is the smallest power of 2 greater than or equal to f, it must be less than 2f. (An easy way
to see this is to consider the binary representation of t and 2f.) This implies that tl2i > tl2t = (112).
Hence the probability that we do not succeed on the first try is 1- tl2i < 712. Since successive
tries are independent, the probability that more than k tries are needed is less than or equal to
112k. Hence, the expected number of tries is not more than 1 + 2(1.12)r + 3$12)2 + .... The series
converges/ so the number of tries is O(1). Each try makes flog(b - a + 1)l calls to the 0/1-valued
random number generator. Assuming the O/1-valued random number generator takes O(1) time,
the time complexity is O(log(b - a + 1)).
4.11 RrcraNcrnrNTERSECrroN
This problem is concemed with rectangles whose sides are parallel to the X-axis and Y-axis. See
Figure 4.2 for examples.
F
H
B
D
A
E
Flgure 4.2: Examples of XY-aligned rectangles.
Write a Program which tests if two rectangles have a nonempty intersection. If the intersection is
nonempty, retum the rectangle formed by their intersection.
Hln f: Think of the X and Y dimensions independently.
Solution: Since the problem leaves it unspecified, we will treat the boundary as part of the rectangle.
This implies, for example, rectangles A and B in Figure 4.2 intersect.
There are many qualitatively different ways in which rectangles can intersect, 8.g., they have
partial overlap (D and F), one contains the other (F and G), they share a corunon side (D and E),
they share a corunon comer (,4 and B), they form a cross (B and C), they form a tee (F and H), etc.
The case analysis is quite tricky.
A better approach is to focus on conditions under which it can be guaranteed that the rectangles
do not intersect. For example, the rectangle with left-most lower point (1,2), width 3, and height 4
35
```

#### Printed page 36 (PDF page 50)

```text
cannot possibly intersect with the rectangle with left-most lower point (5,3), width 2, and height 4,
since the X-values of the first rectangle range from 1 to 1 + 3 = 4, inclusive, and the X-values of the
second rectangle range from 5 to 5 + 2 = 7, inclusive.
Similarly, if the Y-values of the first rectangle do not intersect with the Y-values of the second
rectangle, the two rectangles cannot intersect.
Equivalently, if the set of X-values for the rectangles intersect and the set of Y-values for the
rectangles intersect, then all points with those X- and Y-values are common to the two rectangles,
so there is a nonempty intersection.
Rectangle = collections.namedtuple('Rectangle', ('x', 
'y', 
'width', 
'height'))
def intersect-rectangle(Rl, R2):
def is-intersect(R1, R2) :
return (Rl.x <= R2.x + R2.width and Rl.x + Rl.width >= R2.x
and R1.y <= R2.y + R2.height and R1.y + Rl.height >= R2.y)
if not is-intersect(R1, R2):
return Rectangle(0, 0, -1, -1) # IVo intersection.
return Rectangle(
nar(R1. x , R2. x) ,
nar(R1.y, R2.y),
nin(Rl.x + Rl.width, R2.x + R2.width) - nax(Rl.x, R2.x),
nin(Rl.y + Rl.height, R2.y + R2.height) - nar(Rl.y, R2.y))
The time complexity is O(1), since the number of operations is constant.
Variant: Given four points in the plane, how would you check if they are the vertices of a rectangle?
Variant How would you check if two rectangles, not necessarily aligned with the X and Y axes,
intersect?
36
```
