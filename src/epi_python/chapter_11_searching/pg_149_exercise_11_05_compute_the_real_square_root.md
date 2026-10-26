# Exercise 11.5: Compute the real square root

**Printed textbook page:** 149. **Reference transcription pages:** 149–149.

> **Unverified OCR transcription:** This section retains the supplied PDF text layer. It is not certified verbatim: code syntax, mathematical symbols, and page boundaries may be corrupted. When two exercises begin on the same page, their excerpts overlap. Do not paste extracted code into a `.py` file without manual verification.

#### Printed page 149 (PDF page 163)

```text
mid = (left + risht) //
mid-squared=mid*mid
if mid-squared <= k:
left=mid+1
else:
right=nid-1
return left - 1
The time complexity is that of binary search over the interval l},kf, i.e., O(logk)
11.5 Coupurn rHE REAL seuARE Roor
Square root computations can be implemented using sophisticated numerical techniques involving
iterative methods and logarithms. However, if you were asked to implement a square root function,
you would not be expected to know these techniques.
Implement a function which takes as input a floating point value and retums its square root.
Hint: Iteratively compute a sequence of intervals, each contained in the previous interval, that contain the
result.
Solution: Let r be the input. One approach is to find an integerx such thatnz < r and (n + 1)2 > x,
using, for example, the approach in Solution 11.4 on the preceding page. We can then search within
ln,n + 1] to find the square root of .r to any specified tolerance.
We can avoid decomposing the computation into an integer computation followed by a floating
point computation by directly performing binary search. The reason is that if a number is too big
to be the square root of r, then any number bigger than that number can be eliminated. Similarly,
if a number is too small to be the square root of x, then any number smaller than that number can
be eliminated.
Trivial choices for the initial lower bound and upper bound are 0 and the largest floating point
number that is representable. The problem with this is that it does not play well with finite precision
arithmetic-the first midpoint itself will overflow on squaring.
We cannot start with [0,r] because the square root may be larger than x, e.g., l4 = 112.
However, if x > L.0, we can tighten the lower and upper bounds to 1.0 and r, respectively, since
if 1.0 < x then x < x2. On the other hand, if x <'J..0, we cEU:r use r and 1.0 as the lower and upper
bounds respectively, since then the square root of x is greater than x but less than 1.0. Note that
the floating point square root problem differs in a fundamental way from the integer square root
(Problem 11.4 on the facing page). In that problem, the initial interval containing the solution is
always [0,r].
def square-root (x) :
# Decides the search range according to x's val.ue relative to 1.0
left, 
right = (x, 1.0) if x < 1.0 else (1.0, x)
# Keeps searching as Tong as left != right
rhile not nath. isclose (1eft , right) :
mid=0.5o(left+right)
mid-squared=mid*mid
if mid-squared > x:
right = mid
1.49
```
