# Exercise 17.4: The 3-sum problem

**Printed textbook page:** 264. **Reference transcription pages:** 264–265.

> **Unverified OCR transcription:** This section retains the supplied PDF text layer. It is not certified verbatim: code syntax, mathematical symbols, and page boundaries may be corrupted. When two exercises begin on the same page, their excerpts overlap. Do not paste extracted code into a `.py` file without manual verification.

#### Printed page 264 (PDF page 278)

```text
variables of the program, or on the control logic. A well-chosen invariant can be used to rule out
potential solutions that are suboptimal or dominated by other solutions.
For example, binary search, maintains the invariant thatthe space of candidate solutions contains
all possible solutions as the algorithm executes.
Sorting algorithms nicely illustrate algorithm design using invariants. Intuitively, selection sort
is based on finding the smallest element, the next smallest element, etc. and moving them to their
right place. More precisely, we work with successively larger subarrays beginning at index 0, and
preserve the invariant that these subarrays are sorted, their elements are less than or equal to the
remaining elements, and the entire array remains a permutation of the original array.
As a more sophisticated example, consider Solution 147 on Page 208, specifically the O(k)
algorithm for generating the first k numbers of the form a + b,'lr. The key idea there is to process
these numbers in sorted order. The queues in that code maintain multiple invariants: queues are
sorted, duplicates are never present, and the separation between elements is bounded.
Inoariants boot camp
Suppose you were asked to write a program that takes as input a sorted array and a given target
value and determines if there are two entries in the array that add up to that value. For example, if
the array is (-2,1,2,4,7,1.1), then there are entries adding to 6, to 0, and to 13, but not to 10'
The brute-force algorithm for this problem consists of a pair of nested for loops. Its complexity
is O(nz), where n is the length of the input array. A faster approach is to add each element of the
array to a hash table, and test for each elemente if K- e, where K is the target value, is present in the
hash table. While reducing time complexity to O(n), this approach rcquires O(n) additional storage
for the hash.
The most efficient approach uses invariants: maintain a subarray that is guaranteed to hold a
solution, if it exists. This subarray is initialized to the entire array, and iteratively shrunk from one
side or the other. The shrinking makes use of the sortedness of the array. Specifically, if the sum of
the leftmost and the rightmost elements is less than the target, then the leftmost element can never
be combined with some element to obtain the target. A similar observation holds for the rightmost
element.
def has-two-sum(A, t):
i,j=0,Ien(A)-1
nhile i <= j:
if Atil + A[j] == 1;
return True
elif Atil + A[j] < t:
i+=l
else: #Atil+A[j]>t
j -= 1
return FaIse
The time complexity is O(n), where n is the length of the array. The space complexity is O(1), since
the subarray can be represented by two variables.
17.4 THs 3-suNa PRoBLEM
Design an algorithm that takes as input an array and a number, and determines if there are three
entries in the array (not necessarily distinct) which add up to the specified number. For example,
if the array is \1,7,2,5,7,3) then there are three entries in the array which add up to 21. (3,7,1.1 and
264
```

#### Printed page 265 (PDF page 279)

```text
invariant is an art.
strategy to
whether to use an invari-
ant when designing an algorithm is to work on small examples to hypothesize the invariant.
Often, the invariant is a subset of the set of input space, e,g,.a subarray.
Table 17.2i Top Tips for lnvariants
5,5, 11). (Note that we c;m use 5 twice, since the problem statement said we can use the same entry
more than once.) However, no three entries add up to 22.
Hint: How would you check if a given array entry can be added to two more entries to get the specified
number?
Solution: The brute-force algorithm is to consider all possible triples, e.g.,by three nested for-loops
iterating over all entries. The time complexity is O(n3), where n is the length of the array, and the
space complexity is O(1).
Let A be the input array and f the specified number. We can improve the time complexity to
O(nz)by storing the array entries in a hash table first. Then we iterate over pairs of entries, and for
each A[i] + Aljlwe look for t - (AIil + AUD in the hash table. The space complexity now is O(n).
We can avoid the additional space complexity by first sorting the input. Specifically, sort A and
for each AUl, search for indices j mdk such that Aljl + Alkl = t - A[il. We can do each such search
n O(nlogn) time by iterating over A[l] values and doing binary search tor Afkl.
We can improve the time complexity lo O(n) by starting with A[0] + Aln - 11. If this equals
t-A[il,we'redone. otherwise,if .4[0] +Aln- 1l < f - A[i\,wemovetoA[1]+A[n -1]-thereis
no chance of A[0] pairing with any other entry to get , - Aftl (since A[n - 7] is the largest value in
A). Similarly,if A[0]+Aln- 1] > f - Alil,we move toA[0] + Aln-21. This approach eliminates
an entry in each iteration, and spends O(1) time in each iteratiory yielding an O(n) time bound to
find Atll and A[k] such that A[jl+ Alkl = t - A[i), if such entries exist. The invariant is that if rwo
elements which sum to the desired value exist, they must lie within the subarray currently under
consideration.
Forthegivenexample,aftersortingthearrayis(2,3,5,7,11).ForentryA[0] 
=2,toseeif there
are Aljland A[k] such thatA[0]+A[]+A[k] -- 21,we search for two entries that add up to21.-2 = 79.
The code for this approach is shown below.
def has-three-sum(A, t):
A. sort o
# Finds if the sun of two nunbers in .A equals to t - a
return any(has_tefo_sun(A, t - a) for a in A)
The additional space needed is O(1), and the time complefty is the sum of the time taken to sort,
O(nlogn), and then to run the O(n) algorithm to find a pair in a sorted array that sums to a specified
value, which isO(nz) overall.
Variant So1ve the same problem when the three elements must be distinct. For example, if A =
<5,2,3,4,3) and f = 9, then A[2] + Al2l + Al2l is not acceptable, A[2] + Al2l + Ala]is not acceptable,
but A[1] + Al2l + A[3] and A[1] + A[3] + Alal are acceptable.
Variant Solve the same problem when k, the number of elements to sum, is an additional input.
Variant: Write a prcgram that takes as input an array of integers .4 and an integer T, and retums
a 3-tuple (Afpl,Alql,A[r]) where p,q,r are all distinct, minimizing V - @ld + A[ql + A[r])1, and
265
```
