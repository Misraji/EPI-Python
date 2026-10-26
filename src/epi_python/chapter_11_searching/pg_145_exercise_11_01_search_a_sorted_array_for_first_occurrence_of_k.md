# Exercise 11.1: Search a sorted array for first occurrence of k

**Printed textbook page:** 145. **Reference transcription pages:** 145–145.

> **Unverified OCR transcription:** This section retains the supplied PDF text layer. It is not certified verbatim: code syntax, mathematical symbols, and page boundaries may be corrupted. When two exercises begin on the same page, their excerpts overlap. Do not paste extracted code into a `.py` file without manual verification.

#### Printed page 145 (PDF page 159)

```text
11.1 SrucH A soRTED ARRAy FoR FrRsr occuRnnrucn or k
Binary search commonly asks for the index of any element of a sorted array that is equal to a
specified element. The following problem has a slight twist on this.
-14
-10
2
108
108
243
285
285
285
401.
A[0] A[1]
Al2l A[3] Al4l ,{[s] A16l Aln 
A[8]
Figure 11.1 : A sorted array with repeated elements.
Alel
Write a method that takes a sorted array and a key and retums the index of the first occurrence of
that key in the array. Retum -1 if the key does not appear in the array. For example, when applied
to the array in Figure 11.1 your algorithm should return 3 if the given key is 108; if it is 285, your
algorithm should retum 6.
Hint: What happens when every entry equals k? Don't stop when you first see k.
Solution: A naive approach is to use binary search to find the index of any element equal to the key,
k. (If k is not present, we simply retum -1.) After finding such an element, we traverse backwards
from it to find the first occurrence of that element. The binary search takes time O(logn), where n is
the number of entries in the array. Traversingbackwards takes O(rz) time in the worst-case--consider
the case where entries are equal to k.
The firndamental idea of binary search is to maintain a set of candidate solutions. For the current
problem, if we see the element at index i equals k, although we do not know whether I is the first
element equal to k, we do know that no subsequent elements can be the first one. Therefore we
remove all elements with index i + 1 or more from the candidates.
Let's apply the above logic to the given example, with k = 108. We start with all indices as
candidates, i.e., with [0,9]. The midpoint index, 4 contains k. Therefore we can now update the
candidate set to [0,3], and record 4 as an occurnence of k. The next midpoint is 1, and this index
contains -10. We update the candidate set to [2,3]. The value at the midpoint2is2, so we update
the candidate set to [3,3]. Since the value at this midpoint is 108, we update the first seen occurrence
of k to 3. Now the interval is 13,2), which is empty, terminating the search-the result is 3.
def search-first-of-k (A , k) :
Ieft, right, result = 0, Ien(A) - 1, -1
# A[left:right 
+ 1] is the candidate set.
while left <= right:
mid = (teft + right) // 
2
if A[mid] > k:
right=mid-1
elif Almidl == k:
result = mid
right = mid - 1 # Nothing to the right of nid can be solutjon
else: #A[nid]<k.
left=mid+1
return result
1.45
```
