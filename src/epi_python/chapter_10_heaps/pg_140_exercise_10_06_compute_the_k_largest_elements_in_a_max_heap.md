# Exercise 10.6: Compute the k largest elements in a max-heap

**Printed textbook page:** 140. **Reference transcription pages:** 140–141.

> **Unverified OCR transcription:** This section retains the supplied PDF text layer. It is not certified verbatim: code syntax, mathematical symbols, and page boundaries may be corrupted. When two exercises begin on the same page, their excerpts overlap. Do not paste extracted code into a `.py` file without manual verification.

#### Printed page 140 (PDF page 154)

```text
if len(ruin-heap) == Ien(max-heap) else min-heap[0])
return result
The time complexity per entry is O(logn), corresponding to insertion and extraction from a heap
10.6 CoMpurs rHE k LARGEST ELEMENTs IN A MAX-HEAp
A heap contains limited information about the ordering of elements, so unlike a sorted array or a
balanced BSI naive algorithms for computing the k largest elements have a time complexity that
depends linearly on the number of elements in the collection.
Given a max-heap, represented as an array A, design an algorithm that computes the k
largest elements stored in the max-heap. You cannot modify the heap. For example, if
the heap is the one shown in Figure 10.1(a) on Page 132, then the array representation is
<561.,31.4,401.,28,756,359,271.,11,3), the four largest elements are 561,,31,4,401, and 359.
Solution: The brute-force algorithm is to perform k extract-max operations. The time complexity is
O(klogn),where n is the number of elements in the heap. Note that this algorithm entails modifying
the heap.
Another approach is to use an algorithm for finding the kth smallest element in an array, such
as the one described in Solution 11.8 on Page 153. That has time complexity almost certain O(n),
and it too modifies the heap.
The following algorithm is based on the insight that the heap has partial order information,
specifically, a parent node always stores value greater than or equal to the values stored at its
children. Therefore, the root, which is stored in A[0], must be one of the k largest elements-in fact,
it is the largest element. The second largest element must be the larger of the root's children, which
are A[1] and A[2]-this is the index we continue processing from.
The ideal data structure for tracking the index to process next is a data structure which support
fast insertions, and fast extract-max, i.e., in a max-heap. So our algorithm is to create a max-heap
of candidates, initialized to hold the index 0, which serves as a reference to A[0]. The indices in
the max-heap are ordered according to corresponding value in A. We then iteratively perform k
extract-max operations from the max-heap. Each extraction of an index I is followed by inserting
the indices of l's left child, 2i + 1, and right child, 2i + 2, to the max-heap, assuming these children
exist.
def k-largest-in-binary-heap(A, k)
if k <= 0:
return []
# stotes the (-value, index)-pair in candidate-nax-heap. This heap is
# ordered by value field. 
Uses the negative of value to get the effect of
# a nax heap.
candidate-max-heap = []
# The Targest element in A js at index 0.
candidate-max-heap. append((-AI0l, 0))
result = []
for - in range(k):
candidate-idx = candidate-max-heap t0l t ll
result. append(-heapq. heappop (candidate-nax-heap) [0] )
left-child-idx 
= 2 t candidate-idx + 1
if left-child-idx 
< Ien(A):
140
```

#### Printed page 141 (PDF page 155)

```text
heapq.heappush(candidate_max_heap, (-AIteft_chiId_idx],
right-child-idx = 2 * candidate-idx * r'"tt-tnild-idx))
if right_child_idx < ten(A):
heapq. heappush(candidate_rnax_heap, (-AIright_chitd_idx],
ri sht-chi Id-i dx ) )
return result
The total number of insertion and extract-max operations is O(k), yielding an O(klogk) time com-
plexity, and an O(k) additional space complexity. This algorithm does not modify the original
heap.
141
```
