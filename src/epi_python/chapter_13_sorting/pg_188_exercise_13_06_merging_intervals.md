# Exercise 13.6: Merging intervals

**Printed textbook page:** 188. **Reference transcription pages:** 188–188.

> **Unverified OCR transcription:** This section retains the supplied PDF text layer. It is not certified verbatim: code syntax, mathematical symbols, and page boundaries may be corrupted. When two exercises begin on the same page, their excerpts overlap. Do not paste extracted code into a `.py` file without manual verification.

#### Printed page 188 (PDF page 202)

```text
Sorting the endpoint array takes O(n log n) time; iterating through the sorted array takes O(n) time,
yielding an O(nlogn) time complexity. The space complexity is O(n), which is the size of the
endpoint array.
Variant Users L,2,. . .,n share an Intemet cormection. User I uses b; bandwidth from time s; to fi,
inclusive. \,Vhat is the peak bandwidth usage?
1,3.6 Muncrxc INTERvALS
Suppose the time during the day that a person is busy is stored as a set of disjoint time intervals. If
an event is added to the person's calendar, the set of busy times may need to be updated.
ln the abstract, we want a way to add an interval to a set of disjoint intervals and rep-
resent the new set as a set of disjoint intervals. For example, if the initial set of inter-
vals is l-4,-7),10,2f,I3,67,I7,97,171,72f,174,171, and the added interval is [1,8], the result is
l- 4, -77, 10, 91, 11.1., 72), 17 4, 77).
Write a program which takes as input an array of disjoint closed intervals with integer endpoints,
sorted by increasing order of left endpoint, and an interval to be added, and returns the union of
the intervals in the array and the added interval. Your result should be expressed as a union of
disjoint intervals sorted by left endpoint.
Hint:tNhat is the union of two closed intervals?
Solution: Abrute-force approach is to find the smallest left endpoint and the largest right endpoint
in the set of intervals in the array and the added interval. We then form the result by testing every
integer between these two values for membership in an interval. The time complexity is O(Dn),
where D is the difference between the two extreme values and n is the number of intervals. Note
that D may be much larger than n. For example, the brute-force approach will iterate over all
integers from 0 to 1000000 if the array is ([0, 1], 1999999,10000001) and the added interval is [10,20].
The brute-force approach examines values that are not endpoints, which is wasteful, since if an
integer point p is not an endpoint, it must lie in the same interv al as p - 1 does. A better approach
is to focus on endpoints, and use the sorted property to quickly process intervals in the array.
Specifically, processing an interval in the array takes place in three stages:
(1.) First, we iterate through intervals which appear completely before the interval to be added-
all these intervals are added directly to the result.
(2.) As soon as we encounter an interval that intersects the interval to be added, we compute
its union with the interval to be added. This union is itself an interval. We iterate through
subsequent intervals, as long as they intersect with the union we are forming. This single
union is added to the result.
(3.) Finally, we iterate through the remaining intervals. Because the array was originally sorted,
none of these can intersect with the interval to be added, so we add these intervals to the
result.
Suppose the sorted array of intervals is I-4, -11,10,21,13,61,17,91,11'1,121,1L4,17l, md the added
interval is [1,8]. We begin in Stage 1. Interval I-4, -L|does not intersect [1,8], so we add it directly
to the result. Next we proceed to [0,2]. Since [0,2] intersects [1,8], we are now in Stage 2 of the
algorithm. We add the union of the two, [0,8], to the result. Now we process [3,6]-it lies completely
188
```
