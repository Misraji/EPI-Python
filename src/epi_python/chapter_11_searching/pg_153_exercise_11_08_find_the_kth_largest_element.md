# Exercise 11.8: Find the kth largest element

**Printed textbook page:** 153. **Reference transcription pages:** 153–154.

> **Unverified OCR transcription:** This section retains the supplied PDF text layer. It is not certified verbatim: code syntax, mathematical symbols, and page boundaries may be corrupted. When two exercises begin on the same page, their excerpts overlap. Do not paste extracted code into a `.py` file without manual verification.

#### Printed page 153 (PDF page 167)

```text
def find-min-max(A):
def min-max (a , b) :
return Hinl{ax(a, b) if a < b else ilin}Iax(b, a)
if len(A) <= t:
return llinllax(A[0], At0l)
global-min-max = min-max(A[0], Atll)
# Process two e.lefients at a time.
for i in range(z, len(A) - L, 2):
local_min_max = min_nax(Alil, AIi + 1])
global-min-max = llinl{ax(
nin(global-min-max, smallest, Iocal_min_max. smallest),
nar (gIobal_min_max . largest , local_min_max . largest) )
# If there is odd nunber of eTenents in the array, [re stj]I 
need to
# conpare the last element ,rjth the existing answer.
if Ien(A) % 2:
global-min-max = llinl{ax(
nin(g1oba1-min-max. smallest, AI-11),
nar(global-min_max. largest , At -11))
return gIobaI-min-max
The time complexity isO(n) and the space complexity is O(1).
Variank What is the least number of comparisons required to find the min and the max in the
worst-case?
11.8 FtNo rsu krH rancrsr ELEMENT
M*y algorithms require as a subroutine the computation of the kth largest element of an array. The
first largest element is simply the largest element. The nth largest element is the smallest element,
where n is the length of the array,
For example, if the input array I = (3,2,L,5,4>, then A[3] is the first largest element in A, A[0]
is the third largest element in A, and A[2] is the fifth largest element in A.
Design an algorithm for computing the kth largest element in an array.
Hint:Use divide and conquer in conjunction with randomization.
Solution: The brute-force approach is to sort the input array A in descending order and retum the
element at index k - 1. The time complexity is O(nlogn), where n is the length of A.
Sorting is wasteful, since it does more than what is required. For example, if we want the first
largest element, we can compute that with a single iteration, which is O(n).
For general k, we can store a candidate set of k elements in a min-heap, in a fashion analogous to
Solution 10.4 on Page 138, which will yield aO(nlogk) time complexity and O(k) space complexity.
This approach is faster than sorting but is not in-place. Additionally, it does more than what's
required-it computes the k largest elements in sorted orde1, but all that's asked for is the kth largest
element.
Conceptually, to focus on the kth largest element in-place without completely sorting the array
we can select an element at random (the "pivot"), and partition the remaining entries into those
153
```

#### Printed page 154 (PDF page 168)

```text
greater than the pivot and those less than the pivot. (Since the problem states all elements are
distinct, there cannot be any other elements equal to the pivot.) If there are exactly k - 1 elements
greater than the pivot, the pivot mustbe the kth largest element. If there are more than k- 1 elements
greater than the pivot, we can discard elements less than or equal to the pivot-the k-largest element
must be greater than the pivot. If there are less than k - 1 elements greater than the pivot, we can
discard elements greater than or equal to the pivot.
Intuitively, this is a good approach because on average we reduce by half the number of entries
to be considered.
Implemented naively, this approach requires O(n) additional memory. Howeve(, we can avoid
the additional storage by using the array itself to record the partitioning.
# The nunbering starts fron one, i.e., 
if A = [i, 1, -1, 2]
# find-kth-Iargest (1, A) returns i, find-kth-Iargest(2, 
A) returns 2,
# find-kth-Iargest(3, 
A) returns 1, and find-kth-largest(4, 
d) returns -1'
def find-kth-largest (k, e) :
def find-kth (comp) :
# Partition A[7eft:right 
+ 1] around pivot-idx, returns the new index of
# the pivot, new-pivot-idx, after partition. 
After partitioning,
# A[7eft:new-pivot-idx] 
contains e.lements that are greater tlan the
# pivot, and A[new-pivot-idx + 1:right + 7] contains elerents that are
# -Iess than the pivot.
#
# Note: ".less than" is defined by the conp object.
#
# Returns the ner index of the pivot element after partition.
def partition-around-pivot (left , right , pivot-idx) 
:
pivot-value = 6[pivot-idx]
new-pivot-idx = left
Alpivot-idxl , Alrightl = AlriShtl, 
eIpivot-idxl
for i in range(left, right):
if comp(Alil, pivot-value) :
llll;,lil]l;:'::';"*' 
= Arnew-pivot-idxr' Aril
AIright], 
Alnew-pivot-idxl = AInew-pivot-idx], AIright]
return new-pivot-idx
left, right = 0, Ien(A) - I
rhile left <= right:
# Generates a randon integer in [left, right].
pivot-idx = random. randint (left , right)
new-pivot-idx - partition-around-pivot(left, right, pivot-idx)
if new-pivot-idx == k - 1:
return AInew-pivot-idx]
elif new-pivot-idx > k - 1:
right - new-pivot-idx - 1
else: # new-pivot-idx < k - 1.
Ieft=new-pivot-idx+1
return find-kth (operator. gt)
Since we expect to reduce the number of elements to process by roughly hali the average time
complexity T(n) satisfies I(n) = O(n) + T(nlz). This solves to T(n) = O(n).The space complexity is
O(1). The worst-case time complexity is O(nz), which occurs when the randomly selected pivot is
154
```
