# Exercise 24.27: Measure with defective jugs

**Printed textbook page:** 388. **Reference transcription pages:** 388–389.

> **Unverified OCR transcription:** This section retains the supplied PDF text layer. It is not certified verbatim: code syntax, mathematical symbols, and page boundaries may be corrupted. When two exercises begin on the same page, their excerpts overlap. Do not paste extracted code into a `.py` file without manual verification.

#### Printed page 388 (PDF page 402)

```text
Here is an altemative to the textbook solution that is hugely simpler, and, except for degenerate
inputs, performs much better. It is based on "digitizing" the problem. Let's say the left-most
coordinate for any building is I and the right-most coordinate for any building is r. Then the
final skyline will start at I and end at r. We draw the the skyline building by building as follows.
We represent the skyline with an array, where the lth element of the array hold the height of
coordinate i of the current skyline. This array is initialized to 0s. For each building, we iterate over
the coordinates, and update the skyline-if the current skyline's height at coordinate I is less than
the height of the building, we update the skyline at i to the building's height.
Rectangle = collections.namedtuple('Rectangle', ('left', 
'right', 'height'))
def compute-skyline (buildings) :
min-left = nin(buildings , key=lanbda b: b. left) . left
max-right = nar(buildings, key=laubda b: b.right).right
heights = [0] o (max-right - min-left + 1)
for building in buildings:
for i in range(building.Ieft, 
building.right 
+ 1):
heightsIi - min-left] = nax(heightsIi - min-left], 
building.height)
result = []
left = 0
for i in range(1, Ien(heights)):
if heishtstil 
!= heightsli - 1l:
result. append(
Rectangle(left + min-Ieft, i - 1 + min-left, heightsIi -
left = i
return result + [Rectangle(left + min-left, max-right, heightst-1])l
1l ) )
The time complexity is O(nW), where W is the width of the widest building. In theory, W could
be very large, making this approach much worse than the textbook solution. In practice, W will be
a constarlt, and the digitized solution will be much faster. It is also vastly simpler to code and to
understand.
Varianh Solve the skyline problem when each building has the shape of an isosceles triangle with
a 90 degree angle at its apex.
24.27 Mnnsunr wrrH DEFECTTvE JUcs I
You have three measuring jugs, A, B, and C. The measuring marks have worn out, making it
impossible to measure exact volumes. Specifically, each time you measure with A, all you can be
sure of is that you have a volume that is in the range 1230,240] mL. (The next time you use A,
you may get a different volume-all that you know with certainty is that the quantity will be in
l23O,24Ol mL.) Jugs B and C can be used to measure a volume in [290,310] mL and in [500,515] mL,
respectively. Your recipe for chocolate chip cookies calls for at least 2100 mL and no more than 2300
mL of milk.
Write a program that determines if there exists a sequence of steps by which the required amount of
milk can be obtained using the wom-out jugs. The milk is being added to a large mixing bowl, and
388
```

#### Printed page 389 (PDF page 403)

```text
hence cannot be removed from the bowl. Furthermore, it is not possible to pour one jug's contents
into another. Your scheme should always work, i.e., return between 2100 and 2300 mL of milk,
independent of how much is chosen in each individual step, as long as that quantity satisfies the
given constraints.
Hlnf; Solve the z jugs case.
Solution: It is natural to solve this problem using recursion-if we use jug A for the last step,
we need to correctly measure a volume of milk that is at least 2100 - 230 = 1870 ml-the last
measurement may be as little as 230 mL, and anything less than 1870 mL rtrns the risk of being too
little. Similarly, the volume must be at most 2300 - 240 = 2060 mL. The volume is not achievable if it
is not achievable with any of the three jugs as ending points. We cache intermediate computations
to reduce the number of recursive calls.
In the following code, we implement a general purpose function which finds the feasibility
among n jugs.
Jug = collections.namedtuple('JuS', ('1ow','high'))
def check-feasible(juSS, L, H, c=setO):
VolumeRange = collections.namedtuple('VolumeRange', ('Iow','high,))
if L > H or VoluneRange(L, H) in c or (L < 0 and H < 0):
return False
# Checks the voTune for each jug to see jf it js possible.
if any((L <- j.low and j.high <= 11;
or check_feasible(jugs, L - j.low, H - j.high) for j in jugs)
return True
c.add(Volum€Range(L, H)) # ltarks this as impossible,
return False
The time complexity is O((L + 1)(H + 1)n). The time directly spent within each call to
CheckFeasibleHelper, except for the recursive calls, is O(n), and because of the cache, there are at
most (L + 1)(H + 1) calls to CheckFeasibleHelper. The space complexity is O((L + 1)(H + 1)), which
is the upper bound on the size of the cache.
Note that it is possible to formulate this problem using Integer Linear Programming (ILP).
F{owever, typically interviewers will not be satisfied with a reduction to ILP since such a solution
does not demonstrate any programming skills.
Variant: Suppose jug I can be used to measure any quantity tnpi,ul exactly. Determine if it is
possible to measure a quantity of milk between L and U.
24.28 Coururu rHE MAxTMUM suBARRAy suM rN A cTRCULAR ennav $
Finding the maximum subarray sum in an array can be solved in linear time, as described on
Page 235. However, if the given array A is circular, which means the first and last elements of the
array are to be treated as being adjacent to each other, the algorithm yields suboptimum solutions.
For example, if A is the array in Figure 76.2 on Page 235, the maximum subarray sum starts at index
7 and ends at index 3, but the algorithm described on Page 236 returns the subarray from index 0
to index 3.
389
```
