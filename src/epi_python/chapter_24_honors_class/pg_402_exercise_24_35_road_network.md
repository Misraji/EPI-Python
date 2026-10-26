# Exercise 24.35: Road network

**Printed textbook page:** 402. **Reference transcription pages:** 402–402.

> **Unverified OCR transcription:** This section retains the supplied PDF text layer. It is not certified verbatim: code syntax, mathematical symbols, and page boundaries may be corrupted. When two exercises begin on the same page, their excerpts overlap. Do not paste extracted code into a `.py` file without manual verification.

#### Printed page 402 (PDF page 416)

```text
a+= 1
return max-length
Now we argue the correctness of the program. Let Ala.,b-] be a maximum length subarray
that satisfies the sum constraint. Note that we increment b until Mr,a ) k. Lr particulat when we
increment a to a + 1, Afa,b - 1] does satisfy the sum constraint, but Ala, b] does not. This implies
Afa,b - 1] is the longest subarray starting at a that satisfies the sum constraint.
The iteration ends when b = n. At this point, we claim a > a". If not, then Afa,n - 1] satisfies
thesumconstraint,sinceweincrementedbton,and(n-1)-a+1>b.-a*+l.,contradictingthe
optimality o f Ala. ,b.f . Therefore, a must be assigned to a. at some iteration. At this point, b ( b- since
A[a- -1,,b- 1] satisfies the sum constraint. For,if b > b*, then (b-l)-(a- -1)+1. = b-a. +1 > b- -a. +1',
violating the maximality of Ala.,b.). Since b < b. and a = a*, the algorithm will increment b till
it becomes b- (since Ala- ,b.j satisfies the sum constraint), and thus will identify b* - a* + L as the
optimum solution.
Varianh Design an algorithm for finding the longest subarray of a given array such that the average
of the subarray elements is < k.
24.35 Roeo NrrwoRK S
The Califomia Department of Transportation is considering adding a new section of highway to the
California Highway System. Each highway section connects two cities. City officials have submitted
proposals for the new highway----each proposal includes the pair of cities being connected and the
length of the section.
Write a program which takes the existing highway network (specified as a set of highway sections
between pairs of cities) and proposals for new highway sections, and retums the proposed highway
section which leads to the most improvement in the total driving distance. The total driving distance
is defined to be the sum of the shortest path distances between all pairs of cities. All sections, existing
and proposed, allow for bidirectional traffic, and the original network is connected.
Hln fr Suppose we add a new section from b, tobl.ll the shortest path from il to ? Passes through this section,
what must be true of the part of the path trom u to b'?
Solution: Note that we cannot add more than one proposal to the existing network and run a
shortest path algorithm-we may end up with a shortest path which uses multiple proposals.
The brute-force approach would be to first compute the shortest path distances for all pairs in
the original network. Then consider the new sections, one-at-a-time, and then compute the new
shortest path distances for all pairs, recording the total improvement. The all-pairs shortest path
problem can be solved in time O(r3) using the Floyd-Warshall algorithm, leading to an overall
O(kn3) time complexity.
We can improve upon this by running the all pairs shortest paths algorithm just once. Let S(u,o)
be the 2D array of shortest path distances for each pair of cities. Each proposal p is a pair of cities
(r,y). Forthepairof cities(a,b),thebestwecandobyusingproposalpismin(S(a,b),5(a,x)+d(x,y)+
S(y,b),5(a,y)+d(y,x)+S(r,b))where d(x,y)isthedistanceof theproposedhighwaypbetweenrand
y. This computation is O(1) time, so we can evaluate all the proposals in time proportional to the
402
```
