# Exercise 11.4: Compute the integer square root

**Printed textbook page:** 148. **Reference transcription pages:** 148–148.

> **Unverified OCR transcription:** This section retains the supplied PDF text layer. It is not certified verbatim: code syntax, mathematical symbols, and page boundaries may be corrupted. When two exercises begin on the same page, their excerpts overlap. Do not paste extracted code into a `.py` file without manual verification.

#### Printed page 148 (PDF page 162)

```text
Note that this problem cannot, in general, be solved in less than linear time when elements may
be repeated. For example, if A consists of n - 1 1s and a single 0, that 0 cannot be detected in the
worst-case without inspecting every element.
Variant: A sequence is strictly ascending if each element is greater than its predecessor. Suppose it
is known that an array A consists of a strictly ascending sequence followed by a strictly descending
sequence. Design an algorithm for finding the maximum element in A.
Variant: Design anO(logn) algorithm for finding the position of an element k in a cyclically sorted
array of distinct elements.
17.4 Coupurn rHE TNTEcER seuARE Roor
Write a program which takes a nonnegative integer and retums the largest integer whose square is
less than or equal to the given integer. For example, if the input is 16, return 4; if the input is 300,
return L7, since 172 = 289 < 300 and L82 = 324 > 300.
Hint: Look out for a comer-case.
Solution: A brute-force approach is to square each number from 1 to the key, k, stopping as soon
as we exceed k. The time complexity is O(k). For a 32 bit integel, this algorithm may take over one
billion iterations.
Looking more carefully at the problem, it should be clear that it is wasteful to take unit-sized
increments. For example, \f x2 < k, then no number smaller than r can be the result, and if x2 > k,
then no number Breater than or equal to r can be the result.
This ability to eliminate large sets of possibilities is suggestive of binary search. Specifically, we
can maintain an interval consisting of values whose squares are unclassified with respect to k, i.e.,
might be less than or greater than k.
We initialize the interval to [0,k]. We compare the square of m = L(l + r)l2l with k, and use the
elimination rule to update the interval. If m2 < k, we know all integers less than or equal to rn have
a square less than or equal to k. Therefore, we update the interval to lm + 1,,r1. If mz > k, we know
all numbers greater than or equal to m have a square greater than k, so we update the candidate
interval to fl,m - 1]. The algorithm terminates when the interval is empty, in which case every
number less than I has a square less than or equal to k and l's square is greater than k, so the result
isl-1.
Forexample,ifk=2T,weinitializetheintervalto[0,21]. Themidpointm=L(0+21)12)=10;
since 102 > 27,we update the interval to [0,9]. Now m = L(0 + 9)12) = 4; since 42 < 21, we update
the interval to [5,9]. Now m = L(5 + 8)12) = 7; since 72 > 2l,we update the interval to [5,6]. Now
m = L(5 + 6)12) = 5; since 52 > 21, we update the interval to [5,4]. Now the right endpoint is less
than the left endpoint, i.e., the interval is empty, so the result is 5 - 1 = 4, which is the value retumed.
For k = 25, the sequence of intervals is [0,25], [0,11], 16,11,1,16,71,16,51. The retumed value is
6-1=5.
def square-root (k) :
left, 
right = 0, k
# Candidate interval [7eft, right] where everything before Teft has square
# <= k, everything after right has square > k.
rhile left <= right:
1,48
```
