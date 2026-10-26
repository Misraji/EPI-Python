# Exercise 11.3: Search a cyclically sorted array

**Printed textbook page:** 147. **Reference transcription pages:** 147–147.

> **Unverified OCR transcription:** This section retains the supplied PDF text layer. It is not certified verbatim: code syntax, mathematical symbols, and page boundaries may be corrupted. When two exercises begin on the same page, their excerpts overlap. Do not paste extracted code into a `.py` file without manual verification.

#### Printed page 147 (PDF page 161)

```text
right=mid-1
else: #difference<0
Ieft=mid+1
return -1
The time complexity is the same as that for binary search , i.e., O(logn), where n is the length of A.
Variant: Solve the same problem when A is sorted but may contain duplicates.
11.3 SrancH A cycI,rcAt,ly soRTED ARRAy
An array is said to be cyclically sorted if it is possible to cyclically shift its entries so that it becomes
sorted. For example, the array in Figure 11.2 is cyclically sorted-a cyclic left shift by 4 leads to a
sorted array.
378
478
550
631
103
203
220
234
279
358
A[0] A[1] 
A{21
A[3] AIAJ A[5] A16l AITI
Flgure 11 .2: A cyclically sorted array.
A[8] A[el
Design art O(logn) algorithm for finding the position of the smallest element in a cyclically sorted
array. Assume all elements are distinct. For example, for the array in Figure L7.2, your algorithm
should retum 4.
Hint: Use the divide and conquer principle.
Solution: A brute-force approach is to iterate through the array, comparing the running minimum
with the current entry. The time complexity is O(n),wheren is the length of the array.
The brute-force approach does not take advantage of the special properties of the array, A. For
example, for any m, if Alml > Aln - 1], then the minimum value must be an index in the range
lm + 1',n - 11. Conversely, if A[m) < Aln -'J.1, then no index in the range lm + 7,n - 1] can be the
index of the minimum value. (The minimum value may be at Alml.) Note that it is not possible for
A[m] = A[n - 11, since it is given that all elements are distinct. These two observations are the basis
for a binary search algorithm, described below.
def search-smallest (A) :
left, 
right = 0, len(A) - 1
rhile left < right:
mid = (Ieft + right) // 
z
if A[mid] > Alrightl:
# Ilininun must be in A[niil + l:right 
+ 1].
left=mid+1
else: 
# A[nid] < A[riSht].
# Itininun cannot be in Afnid + l:right 
+ 7] so it must be in AtTeft:nid + 1l
right = mid
# Loop ends when left == rjght.
return left
The time complexity is the same as that of binary search, namely O(logn).
147
```
