# Exercise 13.7: Compute the union of intervals

**Printed textbook page:** 189. **Reference transcription pages:** 189–190.

> **Unverified OCR transcription:** This section retains the supplied PDF text layer. It is not certified verbatim: code syntax, mathematical symbols, and page boundaries may be corrupted. When two exercises begin on the same page, their excerpts overlap. Do not paste extracted code into a `.py` file without manual verification.

#### Printed page 189 (PDF page 203)

```text
in [0,8], so we proceedtolT,9l.It intersects [1,8]but is not completely contained in it, so we update
the most recently added interval to the result, [1,8] to [0,9]. Next we proceed to [L1, 12]. It does
not intersect the most recently added interval to the result, 10,9), so we are in Stage 3. We add it
and all subsequent intervals to the result, which is now l-4,-U,f0,9f, 111,1.27,174,17]. Note how
the algorithm operates "locally"-"ortedness guarantees that we do not miss any combinations of
intervals.
The program implementing this idea is given below,
Interval = collections.namedtuple('Interval', 
('left','right'))
def add-interval (disjoint-intervals, 
new-interval)
i, result = 0, []
# Processes intervals in disjoint-intervals 
which cone before new_interval
rhile (i < Ien(disjoint-intervals)
and new-interval . left > disjoint_intervals Ii] . right) :
result . append(di sj oint-intervals 
I i ] )
i+=1
# Processes intervals in disjoint-interva.ls 
which overTap with new-intervaT
rbile (i < len(disjoint-intervals)
and new_interval right >= disjoint_intervals Ii] .1eft) :
# If [a, b] and [c, d] overTap, unjon is [nin(a, c), nax(b, d)].
new-interval = Interval(
nin(new-interval . Ieft , disjoint-intervals 
Ii] . Ieft) 
,
nar(new-interval.right, 
disjoint-intervals 
Ii]. right))
i+=1
# Processes intervals in disjoint-interya.ls 
which cone after new_intervaT.
return result + [new_interval] + disjoint_intervalsIi:]
Since the program spends O(1) time per entry, its time complexity isO(n).
13.7 Coupuru rlrE uNroN oF TNTERvALS
L:I this problem we consider sets of intervals with integer endpoints; the intervals may be open
or closed at either end. We want to compute the union of the intervals in such sets. A concrete
example is given in Figure 13.2.
Iz,al o 
. 
,u,rD o 
",rr,r9o #.:lx
[1,1] 
13,4)
OH
(0,3)
H
17,8)
H
(t2,161
(9, 111
H
L12,r4l
t5,n
H
H
0 1 2 3 4 5 6 7 8 9 10 11 12 13 1.4 15 t6 t7
(0lI
lt11l
{-
189
ll2,l7)
Union of intervals
Figure 13.2: A set of intervals and their union
```

#### Printed page 190 (PDF page 204)

```text
Design an algorithm that takes as input a set of intervals, and outputs their union expressed as a
set of disjoint intervals.
Hint: Do a case analysis.
Solution: The brute-force approach of considering every number from the minimum left endpoint
to the maximum right endpoint described at the start of Solution 13.6 on Page 188 will work for this
problem too. As before, its time complexity is O(Dn), where D is the difference between the two
extreme values and n is the number of intervals, which is rmacceptable when D is large.
We can improve the run time by focusing on intervals instead of individual values. We perform
the following iteratively: select an interval arbitrarily, and find all intervals it intersects with. If it
does not intersect any interval, nemove it from the set and add it to the result. Otherwise, take its
union with all the intervals it intersects with (the union must itself be an interval), remove it and
all the intervals it intersects with from the result, and add the union to the set. Since we remove at
least one interval from the set each time, and the time to process each interval (test intersection and
form unions) rs O(n), the time complexity is O(nz).
A faster implementation of the above approach is to process the intervals in sorted order, so that
we can limit our attention to a subset of intervals as we proceed. Specifically, we begin by sorting
the intervals on their left endpoints. The idea is that this allows us to not have to revisit intervals
which are entirely to the left of the interval currently being processed.
We refer to an interval which does not include its left endpoint as being left-open. Left<losed,
right-open, and right-closed are defined similarly. lrVhen sorting, if two intervals have the same left
endpoint, we put intervals which are left-closed first. We break ties arbitrarily.
As we iterate through the sorted array of intervals, we have the following cases:
o The interval most recently added to the result does not intersect the current interval, nor does
its right endpoint equal the left endpoint of the current interval. In this case/ we simply add
the current interval to the end of the result array as a new interval.
o The interval most recently added to the result intersects the current interval. In this case, we
update the most recently added interval to the union of it with the current interval.
o The interval most recently added to the result has its right endpoint equal to the left endpoint
of the current interval, and one (or both) of these endpoints are closed. In this case too, we
update the most recently added interval to the union of it with the current interval.
For the example in Figure 13.2 on the preceding page,the result array updates in the following
way: ((0,3)) , <(0,4)), <(0,4),15,7)>, <(0,41, [5,8)), <(0,41, [5, 11)), <(0,4], [5, 11]), ((0,4], [5, 11], 11,2,1.41),
<(0, 41, [5, 1 1 ], 112, 16)>, <(0, 41, [5, 1 1 ], 112, 17 )) .
Endpoint = collections.namedtuple('Endpoint', ('is-closed','val'))
class Interval:
def _-init--(se1f, 
left, 
right)
self.Ieft 
= Ieft
self.right 
= right
def --1t--(self, 
other):
if self.Ieft.val 
!= other.left.val:
return self. left . vaI < other . Ieft . vaI
# Left endpoints are equa7, so now see if one is closed and the other open
# - cTosed intervals should appear first.
190
```
