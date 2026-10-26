# Exercise 24.25: Count inversions

**Printed textbook page:** 385. **Reference transcription pages:** 385–385.

> **Unverified OCR transcription:** This section retains the supplied PDF text layer. It is not certified verbatim: code syntax, mathematical symbols, and page boundaries may be corrupted. When two exercises begin on the same page, their excerpts overlap. Do not paste extracted code into a `.py` file without manual verification.

#### Printed page 385 (PDF page 399)

```text
Despite the heuristics helping in some cases, we cannot prove a better bound for the worst-case
time complexity than the original O(n3").
24.25 CouNr rNvrnsrols $
LetAbeanarrayof integers. Callthepairof indices(i,7)invertedif i< jandAfil>A[l]. For
example, if A = <4,1.,2,3>, then the pair of indices (0,3) is inverted. Intuitively, the number of
inverted pairs in an array is a measure of how unsorted it is.
Design an efficient algorithm that takes an array of integers and returns the number of inverted
pairs of indices.
Hint: Let A and B be arrays. How would you count the number of inversions where one element is from A and
the other from B in the array consisting of elements from A and B?
Solution: The brute-force algorithm examines all pairs of indices (1, i), where i < 7. has an O(n2)
complexity, where n is the length of the array.
One way to recognize that the brute-force algorithm is inefficient is to consider how we would
check if an array is sorted. We would not test for every element if all subsequent elements are
Sreater than or equal to it-we just test the next element, since greater than or equal is transitive.
This suggests the use of sorting to speed up counting the number of inverted pairs. In particular,
if we sort the second half of the array, then to see how many inversions exist with an element in the
first half, we could do a binary search for that element in the second half. The elements before its
location in the second half are the ones inverted with respect to it.
Elaborating, suppose we have counted the number of inversions in the left half L and the right
half R of .,{. What are the inversions that remain to be counted? Sorting L and R makes it possible
to efficiently obtain this number. For any (i, j) pafu where I is an index in L and i is an index in R, if
L[r] > R[], then for all j' < 7 we must have L[l] > R[i'].
Forexample,ifA=<3,6,4,2,5,1),thenl=(3,6,4),andR-<2,5,1).Aftersorting,L=\8,4,6),
and R = (\,2,5). The inversion counts for L and R are 1 and2, respectively. l{hen merging to form
their sorted union, since 1 < 3, we know 4,6 are also inverted with respect to 1, so we add ltl - 0 = 3
to the inversion count. Next we process 2. Since 2 < 3, we know 4, 6 are also inverted with respect
to 2, so we add lll - 0 = 3 to the inversion count. Next we process 3. Since 5 > 3,3 does not add
any more inversions. Next we process 4. Since 5 > 4,4 does not add any more inversions. Next we
process 5. Since 5 < 6, we add lll - 2 (which is the index of 6) = 1 to the inversion count. In all we
add3+3+ l. = TtoinversioncountsforLandR(whichwerel and2,respectively)togetthetotal
number of inversions, 10.
def count-inversions (A) :
# Return the nurber of inversions in Afstart:endl.
def count-subarray-inversions(start, 
end) :
# Iterge two sorted subarrays Afstart:nidl and Atnid:endl into
# AIstart:end] and returr the nunber of inversions across AIstart:nid]
# and A[nid:end].
def merge_sort_and_count_inversions_across_subarrays(start, mid, end) :
sorted_A = []
left_start , right_start , inversion_count = start , nrid, 0
385
```
