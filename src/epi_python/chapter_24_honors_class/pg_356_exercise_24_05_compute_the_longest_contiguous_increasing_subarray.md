# Exercise 24.5: Compute the longest contiguous increasing subarray

**Printed textbook page:** 356. **Reference transcription pages:** 356–356.

> **Unverified OCR transcription:** This section retains the supplied PDF text layer. It is not certified verbatim: code syntax, mathematical symbols, and page boundaries may be corrupted. When two exercises begin on the same page, their excerpts overlap. Do not paste extracted code into a `.py` file without manual verification.

#### Printed page 356 (PDF page 370)

```text
The algorithm performs a traversal of the array, with a constant amor-mt of computation per entry,
a nested conditional, followed by another traversal of the array, with a constant amount of com-
putation per entry. Hence, the time complexity is O(n) + O(1) + O(n) = O(n). The additional space
complexity is O(1), corresponding to the local variables.
Varianh Let A be as above. Compute an array B where B[i] is the product of all elements in A except
AU]. You cannot use division. Your time complexity should be O(n), and you can only use 0(L)
additional space.
Varianfi Let A be as above. Compute the maximum over the product of all triples of distinct
elements of A.
24.5 Coupurr rHE LoNGEST coNTIGUous INCREASING susenRAv I
An array is increasing if each element is less than its succeeding element except for the last element.
Implement an algorithm that takes as input an atay A of n elements, and retums the beginning and
endingindicesof alongestincreasingsubarrayof A. Forexample, lf A= (2,1,1,3,5,13,7,19,17,23>,
the longest increasing subarray is (3,5, 13), and you should return (2,4).
Hint:lf A[il>Ali+ 1],insteadof checking Ali+71 <A[i+ 2],gofurtheroutinthearray.
Solution: The brute-force algorithm is to test every subarray: two nested loops iterate through
the starting and ending index of the subarray, an inner loop to test if the subarray is increasing,
and some logic to track the longest subarray. The time complexity is O(n3), e.g., for the array
<0,7,2,3,... ,ft - 1). The time complexity can easily be irnproved to O(nz) by caching whether the
subarray Ali, jlis increasing when examining Aft,l + 1].
Looking more carefully at the example, the longest subarray ending at 3 is A12,21, because
3 < 11. Conversely, since 13 > 5, the longest subarray ending at 13 is the longest subarray ending at
5 (which is A[2,3]) together with 13, i.e., Al2,4l. In general, the longest increasing subarray ending
at index f + 1 inclusive is
(1.) the single entry A[7 + 7], if Ali+ 1l < Aljl, or
(2.) the longest increasing subarray ending at index f together with A[l + ].1, if Alj + 1l > Alil.
This fact can be used directly to improve the brute-force algorithm to one whose time complexity
is O(n).
The additional space complexity is O(1), since all we need is the length of the longest subarray
ending at 7 when processing I + 1. Two additional variables can be used to hold the length and
ending index of the longest increasing subarray seen so far.
We can heuristically improve upon the O(n) algorithm by observing that iI Ali - 1l * Ali|G.e.,
we are starting to look for a new subarray starting at l) and the longest contiguous subarray seen uP
to index I has length L, we can move on to index I + L and work backwards towards l. Specifically,
if forany j,i< j<i+Lwehave AU-ll*A[j),wecanskiptheearlierindices. Forexample,after
processing 13, we work our way back from the entry at index 4 + 3 = 7, i.e., 13's index plus the
length of the longest increasing subarray seen so far (3). Since A[7] = 17 < A167 = 19, we do not
need to examine prior entries-no increasing array ending at AlTl can be longer than the current
best.
356
```
