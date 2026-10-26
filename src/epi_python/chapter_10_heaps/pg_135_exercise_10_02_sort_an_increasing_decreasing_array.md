# Exercise 10.2: Sort an increasing-decreasing array

**Printed textbook page:** 135. **Reference transcription pages:** 135–135.

> **Unverified OCR transcription:** This section retains the supplied PDF text layer. It is not certified verbatim: code syntax, mathematical symbols, and page boundaries may be corrupted. When two exercises begin on the same page, their excerpts overlap. Do not paste extracted code into a `.py` file without manual verification.

#### Printed page 135 (PDF page 149)

```text
min-heap = []
# BuiTds a list of iterators for each array in sorted-arrays
sorted_arrays-iters = [iter(x) 
for x in sorted_arrays]
# Puts first elenent fron each iterator in nin_heap.
for i, it in enuuerate(sorted_arrays_iters):
first-element = nert(it, l{one)
if first-element is not None:
heapq.heappush(min-heap, (first_element, i))
result = []
while min-heap:
smallest-entry , smallest-array-i = heapq. heappop (min_heap)
smallest-array_iter = sorted_arrays_iters Ismal1est_array_i]
result . append ( smallest-entry)
next-element = nert(smal1est_array_iter, None)
if next-element is not None:
heapq. heappush(min-heap, (next_eIement, smallest_array_i))
return result
# Pythonic so-Iutjon, uses the heapq.nerge() nethod rshich tal<es nuTtiple inputs
def merge-sorted-arrays_pythonic (sorted_arrays) :
return list(heapq. merge (*sorted_arrays))
Let k be the number of input sequences. Then there ane no more than k elements in the min-heap.
Both extract-min and insert take O(logk) time. Hence, we can do the merge nO(nlogk) time. The
sPace comPlexity is O(k) beyond the space needed to write the final result. Lr particular, if the data
comes from files and is written to a file, instead of arrays, we would need only O(k) additional
storage.
Altematively, we could recursively merge the k files, two at a time using the merge step from
merge sort. We would go from k to klz then kl4, etc. files. There would be logk stages, and each
has time complexity O(n), so the time complexity is the same as that of the heap-based approach,
i.e., O(nlogk). The space complexity of any reasonable implementation of merge sort would end
up being O(n), which is considerably worse than the heap based approach when k << n.
10.2 Sonr aN TNCREASTNG-DECREASTNG ARRAy
An array is said to be k-increasing-decreasing if elements repeatedly increase up to a certain index
after which they decrease, then again increase, a total of k times. This is illustrated in Figure 10.2.
5/
L31
493
294
221
339
4r.8
452
442
190
,4[0] A[1] Al2l At3l Al4l A[s] A161 A[7] A[8] Alel
Flgure 1 0.2: A  -increasing-decreasing array.
Design an efficient algorithm for sorting a k-increasing-decreasing array.
135
```
