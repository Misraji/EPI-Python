# Exercise 24.17: Find the kth largest element - large n, small k

**Printed textbook page:** 373. **Reference transcription pages:** 373–373.

> **Unverified OCR transcription:** This section retains the supplied PDF text layer. It is not certified verbatim: code syntax, mathematical symbols, and page boundaries may be corrupted. When two exercises begin on the same page, their excerpts overlap. Do not paste extracted code into a `.py` file without manual verification.

#### Printed page 373 (PDF page 387)

```text
A-x = float('inf') 
if x >= Ien(A) else e[x]
B-k-x-l = float('-inf') 
if k - x <= 0 else B[k - x - 1]
B-k-x = float('inf') 
if k - x >= len(B) else B[k - x]
if e_x < B_k_x_l:
b=x+1
elif A-x-1 > B-k_x:
t=x-l
else:
# B[k - x - 1] <= A[x] and A[x - 1] < B[k - x]
return nar(A_x_1, B_k_x_l)
A-b-1 = float('-inf') 
if b <= 0 else Atb - 1l
B-k-b-l = float('-inf') 
if k - b - 1 < 0 else Btk - b - 1l
return nax(A_b_l, B_k_b_l)
since in each iteration we halve the length of lb,t) the time complexity is O(logk).
24.77 Frun rur krrr lancnsr ELEMENT-LARGE /1, sMALL k e
The goal of this Problem is to design an algorithm for computing the kth largest element in a
sequence of elements that is presented one element at a time. The length of the sequence is not
known in advance, and could be very large.
Design an algorithm for computing the kth largest element in a sequence of elements.
Hfut; Track the k largest elements, but don't update the collection immediately after each new element is read.
Solution: The natural approach is to use a min-heap containing the k largest elements seen thus far,
just as in Solution 10.4 on Page 138. IA/hen the last element in the sequence is read, the desired value
is the element at the root of the min-heap. This approach has time complexity O(nlogk),where n is
the total number of elements in the sequence.
We know of a very fast algorithm for finding the kth largest element in an array of fixed size
(Solution 11.8 on Page 153). We cannot directly apply that here without allocating O(n) space.
However, we can break our input into fixed size arrays and run Solution 11.8 on Page 153 over
those arrays to eliminate all but the k largest elements from each array. These elements are added
over to the next array.
def find_kth_largest_unknown_length(stream, k) :
candidates = []
for x in stream:
candidates. append(x)
iflen(candidates) 
>=2* k- 
1:
# Reorders elernents about nedian with Targer elements appearing
# before the nedian.
find-kth-largest (k, candidates)
# Resize to keep just tle k Targest ele.r,ents seen so far.
de1 candidates [k: ]
# Finds the k- th -Iargest eiernent in candidates.
find-kth-Iargest (k, candidates)
return candidatestk - 1l
373
```
