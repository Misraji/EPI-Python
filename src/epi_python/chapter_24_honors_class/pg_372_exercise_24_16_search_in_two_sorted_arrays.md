# Exercise 24.16: Search in two sorted arrays

**Printed textbook page:** 372. **Reference transcription pages:** 372–372.

> **Unverified OCR transcription:** This section retains the supplied PDF text layer. It is not certified verbatim: code syntax, mathematical symbols, and page boundaries may be corrupted. When two exercises begin on the same page, their excerpts overlap. Do not paste extracted code into a `.py` file without manual verification.

#### Printed page 372 (PDF page 386)

```text
right = mid - 1 # Search the Left part if out-of-bound
return -1 # Nothing matched k.
The run time of the first loop is O(logn), since we double the tested index with each iteration. The
second loop is conventional binary search, i.e.,O(Logn), so the total time complexity is O(logn).
24.16 SrancH rN rwo soRTED ennavs $
You are given two sorted arrays and a positive integer k. Design an algorithm for computing the kth
smallest element in an array consisting of the elements of the initial two arrays arranged in sorted
order. Array elements may be duplicated within and across the input arrays.
Hint: The first k elements of the first array together with the first k elements of the second array are initial
candidates. Iteratively eliminates a constant fraction of the candidates.
Solution: You could merge the two arrays into a third sorted array and then look for the answer-the
merge would take O(m + n) time, where m and n are the lengths of the input arrays.
You can optimize somewhat by building the merged array on the first k elements, which would
be an O(k) operation-this is faster than forming the combined array when k is small, but when k is
comparable to m and n, the time complexity isO(m + n).
What we really need is some form of binary search that takes advantage of the sortedness of
A and B. Intuitively, if we focus on finding the indices in A and B that correspond to the first k
elements, we stand a good chance of using binary search. Specifically, suppose the first k elements
of the unionof A and B consist of the firstx elements of A and the firstk-relements of B. We'll
now see how to use binary search to determine r.
Let's maintain an interval [b, f] that contains r. The iteration continues as long asb < t. We will
contract this interval by half in each iteration. At each iteration consider the midpoint, x = b + l,* ).
IfAlxl<B[(k-r)-1],thenA[r]mustbeinthefirstk-lelementsoftheunion,soweupdatebto
r+ l andcontinue. Similarly, if Alx- 1l > B[k-r],then Alx-Tlcannotbeinthefirstkelements,
sowecanupdate ttox- L. Otherwise,wemusthaveB[(k-r) - 1] SAlxlandA[r- 1] < Blk- xl,
in which case the result is the larger of A[x - 1] and BI(k - x) - 11, since the first t elements of A and
the first k - x elements of B when sorted end in Alx - 11 or B[(k - r) - 1].
If the iteration ends without returning, it mustbe that b = f. Clearly, x = b = t. We simply return
the larger of Alx - lland Bl(k- x) - 11. (If A[x- 1] = Bl(k-x) - 1l,we arbitrarily retumeither.)
The initial values for b and f need to be chosen carefully. Naively setting b = 0,t = k does not
work, since this choice may lead to array indices in the search lying outside the range of valid
indices. The indexing constraints for A and B can be resolved by initializing b to max(0,k - n) and t
to min(la,k).
def find-kth-in-two-sorted-arrays (A, B, k) :
# Lower bound of elernents we wi77 choose in A
b=nar(0,k-Ien(B))
# Ilpper bound of efements we wi77 choose in I
t = rin(Ien(A), k)
while b < t:
x = b + (r. - b) // 2
A-x-l = float('-inf') 
if x <= 0 else A[x - 1]
372
```
