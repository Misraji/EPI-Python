# Exercise 24.15: Search a sorted array of unknown length

**Printed textbook page:** 370. **Reference transcription pages:** 370–371.

> **Unverified OCR transcription:** This section retains the supplied PDF text layer. It is not certified verbatim: code syntax, mathematical symbols, and page boundaries may be corrupted. When two exercises begin on the same page, their excerpts overlap. Do not paste extracted code into a `.py` file without manual verification.

#### Printed page 370 (PDF page 384)

```text
min-heap = [EmpIoyeeData(p,
heapq. heapi fy (min-heap)
'index') )
i) for i, p in enunerate(productivity)l
# Initially 
assigns ore ticket to everyone.
tickets = [1] o Ien(productivity)
# Fi77s tickets fron Towest rating to highest rating.
rhile min-heap:
next-dev = heapq. heappop(min-heap) [1]
# Handles the .left neighbor.
if next-dev > 0 and productivityInext-dev] > productivityInext-dev
ticketsInext-dev] = ticketsInext-dev - 1] + 1
# HandTes tle right neighbor.
if (next-dev + I < len(tickets)
and productivityInext-dev] > productivityInext-dev + 1]):
tickets Inext-dev] = nar(ticketsInext-dev],
ticketsInext-dev + 1] + 1)
return su[(tickets)
1l
Since each extraction from a min-heap takes time O(logn), the time complexity isO(nlogn).
The approach presented above is in the spirit of a brute-force solution. On some reflection, a
total ordering on the developers is overkill, since the specified constraint is very local. lndeed, we
can improve the time complexity toO(n) by making two passes over the array.
We start by giving each developer a single ticket. Then we make a left-to-right Pass in which
we give each developer who has more productivity than the developer on his left one ticket more
than the developer on his left. We then do the same in a right-to-left pass.
Any amount added is required, so we cannot getby with fewer tickets. Note that every developer
who is more productive than his right neighbor has more tickets than that neighbor. Furthermore,
if a developer is more productive than his left neighbor, in the left-to-right pass we already give
him more tickets than his left neighbor, and we can only increase his ticket count in the right-to-left
Pass.
def calculate-bonus (productivity) :
# InitiaTTy assigns one ticket to everyone.
tickets = [1] o len(productivity)
# Fron Teft to right.
for i in range(1, len(productivity)):
if productivityIi] > productivityli - 1l:
ticketsIi] = ticketsIi - 1] + 1
# Fron right to Left.
for i in reversed(range(Ien(productivity) - 1)):
if productivityIi] > productivityli + 1l:
ticketsIi] = nax(ticketsIi], ticketsli + 1l + 1)
return sun(tickets)
24.75 SrancHA soRTED ARRAv oF uNKNowN LENGTH S
Binary search is usually applied to an array of known length. Sometimes, the array is "virtual", i.e.,
it is an abstraction of data that is spread across multiple machines. In such cases, the length is not
known in advance; accessing elements beyond the end results in an exception.
370
```

#### Printed page 371 (PDF page 385)

```text
Design an algorithm that takes a sorted array whose length is not known, and a key, and returns an
index of an array element which is equal to the key. Assume that an out-of-bounds access throws
an exception.
Hint: Can diwide and conquer be used to find the end of the array?
Solution: The brute-force approach is to iterate through the array, one element at a time, stopping
when either the key is found or an exception is thrown (in which case the key is not present). The
time complexity is O(n),where n is the length of the input array.
A better approach is to take advantage of sortedness. If we know the array length, we can use
binary search to search for the key. We can compute the array length by testing whether indices
0,'J.,3,7,15,. . . are valid. As soon as we find an invalid index, say 2i - 1, we can use binary search
over the interval l2i-1,2i - 2] to find the first invalid index, which is the length of the array.
We can improve on the above approach by comparing the value of the element at index 2, - 1
with the key, since if it is greater than the key, we can do binary search over indices 12i-t,2i - 2j
for the key. Conceptually, we can treat out-of-bounds indices in the same way as valid indices by
treating an out-of-bounds index as holding infinity.
For example, consider the array in Figure 11.1 on Page 145. Suppose we are searching for
thekey243.WeexamineindicesO,L,3,7. SinceAl71 =285>24S,wenowperformconventional
binary search over the interval 14, 6l for 243. If instead, we were searching for the key 400, we would
examine indices 0,1,3,7, 15. Since L5 is not a valid index, we would stop, and perform conventional
binary search over the interval [8,14]. The first midpoint is 11, which is out-of-bounds and treated
as holding infinity, so we update the interval to [8,10]. The next interval is [8,8], followed by 18,71
which is empty, indicating that the key 400 is not present.
def binary-search-unknown_length(A, k) :
# Find the possib-le range where k exists.
P=0
rhile True:
try:
idx=(1<<p)-l 
#2^p-1.
if A[idx] == k:
return idx
elif A[idx] > k:
break
ercept IndexError:
break
p+- 1
# Binary search between jndices 2^(p - 1) and 2^p - 2, inclusive
left, right = | 14 nar(O, 1p - 1)), (1 << p) - Z
rhile left <= right:
mid = left + (risht - left) // z
try:
if Almidl == k:
return mid
elif A[mid] > k:
right=nid-1
else: #A[nid]<k
left=mid+1
ercept IndexError:
371,
```
