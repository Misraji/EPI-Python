# Exercise 10.3: Sort an almost-sorted array

**Printed textbook page:** 136. **Reference transcription pages:** 136–136.

> **Unverified OCR transcription:** This section retains the supplied PDF text layer. It is not certified verbatim: code syntax, mathematical symbols, and page boundaries may be corrupted. When two exercises begin on the same page, their excerpts overlap. Do not paste extracted code into a `.py` file without manual verification.

#### Printed page 136 (PDF page 150)

```text
Hint: Can you cast this in terms of combining k sorted arrays?
Solution: The brute-force approach is to sort the array, without taking advantage of the k-increasing-
decreasing property. Sorting algorithms run in time O(n log n), where n is the length of the array.
If k is significantly smaller than n we can do better. For example , if k = 2, the input array consists
of two subarrays, one increasing, the other decreasing. Reversing the second subarray yields two
sorted arrays, and the result is their merge. It is fairly easy to merge two sorted arrays in O(n ) time.
Generalizing, we could first reverse the order of each of the decreasing subarrays. For the
example in Figure 10.2 on the precedingpage, we would decompose A into four sorted arrays-
<57,73\,493), <221,,294), <339,41,8,452), and <190,442). Now we can use the techniques in Solu-
tion 10.1 on Page 134 to merge these.
def sort-k-increasing-decreasing-array(A) :
# Deconposes A jnto a set of sorted atrays.
sorted-subarrays = []
INCREASING, DECREASING = range(2)
subarray-type = INCREASING
start-idx = 0
for i in range(I, len(A) + 1):
if (i == Ien(A) or # A is ended. Adds the Tast subarray.
(Ati - 1l < Atil and subarray-type == DECREASING) or
(AIi - rl >= Atil and subarray-type == INCREASING)):
sorted-subarrays.append(AIstart-idx:i] if subarray-type ==
INCREASING else AIi - 1:start-idx - 1:-1])
start-idx = i
subarray-type = (DECREASING
if subarray-type =- INCREASING else INCREASING)
return merge-sorted-arrays (sorted-subarrays)
# Pythonic solutjon, uses a stateful object to trace the rnonotonic subarrays
def sort-k-increasing-decreasing-array-pythonic (A) :
class ilonotonic:
def --init-_(self):
self .-Iast = float('-inf 
')
def --c aI l-- ( sel f , curr ) :
res=curr<self.-Iast
self.-last 
= curr
return res
return merge-sorted-arrays ([
list(group) [:: -1 if is-decreasing else 1]
for is-decreasing , group in itertools. groupby(A, I'lonotonic O)
l)
]ust as in Solution 10.1 on Page 134, the time complexity is O(n logk) time.
10.3 Sonr aN ALMosr-soRTED ARRAY
Often data is almost-sorted-for example, a server receives timestamped stock quotes and earlier
quotes may arrive slightly after later quotes because of differences in server loads and network
routes. In this problem we address efficient ways to sort such data.
136
```
