# Exercise 24.28: Compute the maximum subarray sum in a circular array

**Printed textbook page:** 390. **Reference transcription pages:** 390–390.

> **Unverified OCR transcription:** This section retains the supplied PDF text layer. It is not certified verbatim: code syntax, mathematical symbols, and page boundaries may be corrupted. When two exercises begin on the same page, their excerpts overlap. Do not paste extracted code into a `.py` file without manual verification.

#### Printed page 390 (PDF page 404)

```text
Given a circular array A, compute its maximum subarray sum in O(n) time, where r is the length
of A. Can you devise an algorithm that takes O(n) time and O(1) space?
Hint:The maximum subarray may or may not wrap around.
Solution: First recall the standard algorithm for the conventional maximum subarray sum problem.
This proceeds by computing the maximum subarray sum S[i] when the subarray ends at l, which
is max(Sff -1.]+ AliT,AUl). Its time complexity is O(n), where n is the length of the array, and space
complexity is O(1).
One approach for the maximum circular subarray is to break the problem into two seParate
instances. The first instance is the noncircular one, and is solved as described above.
The second instance entails looking for the maximum subarray that cycles around. Naively, this
entails finding the maximum subarray that starts at index 0, the maximum subarray ending at index
n - 1,, and adding their sums. However, these two subarrays may overlap, and simply subtracting
out the overlap does not always give the right result (consider the array <\0,-4,5,*4,10)).
Instead, we compute for each I the maximum subarray sum 51 for the subarray that starts at
0 and ends at or before f, and the maximum subarray Ei for the subarray that starts after i and
ends at the last element. Then the maximum subarray sum for a subarray that cycles around is the
maximum over all i of Si + Ei.
def max-subarray-sum-in-circular (A) :
# calculates the non-circular so.lution.
def find-max-subarray O :
maxinun-till = maximum = 0
for a in A:
maximum*ti11 = [ar(a, a + maxinum-till)
maximum = nar(maxirnum, maximum-tiI1)
return maximum
# CalcuTates the solution which is circular.
def find-circular-max-subarray O :
def compute-running-maximum (A) :
partial-sum = At0l
running-maximum = [partial-sum]
for a in A[1:]:
Partial-sum += a
running-maximum. append (nar (running-maximum [ - 1], partial-sum) )
return running-maximum
# Ilaxinun subatray sum starts at index 0 and ends at ot before index i.
maximum-begin = compute-running-maximum(A)
# Ilaxinun subarray sufi starts at index i + 1 and ends at the last
# elenent.
maximum-end = compute-running-maximum(A[:: -1]) [:: -1] [1:] + [0]
# Calculates the maxjraun subarray which is circuTar.
return nar(begin + end
for begin, end in zip(maximum-begin, maximum-end))
return nar(find-max-subarray O, find-circular-max-subarrayO )
The time complexity and space complexity are both O(n)
390
```
