# Exercise 10.5: Compute the median of online data

**Printed textbook page:** 139. **Reference transcription pages:** 139–139.

> **Unverified OCR transcription:** This section retains the supplied PDF text layer. It is not certified verbatim: code syntax, mathematical symbols, and page boundaries may be corrupted. When two exercises begin on the same page, their excerpts overlap. Do not paste extracted code into a `.py` file without manual verification.

#### Printed page 139 (PDF page 153)

```text
length of the sequence is not known in advance. Your algorithm cannot use more than O(k)
additional storage. What are the worst-case inputs for your algorithm?
10.5 Colrpurs rHE MEDTAN oF oNLTNE DATA
You want to compute the running median of a sequence of numbers. The sequence is presented to
you in a streaming fashion-you carmot back up to read an earlier value, and you need to output
the median after reading in each new element. For example, if the input is 1.,0,3,5,2,0,1 the output
is L, 0.5,'1.., 2, 2, 1,.5, L.
Design an algorithm for computing the running median of a sequence.
Hint: Avoid looking at all values each time you read a new value.
Solution: The brute-force approach is to store all the elements seen so far in an array and compute
the median using, for example Solution 11..8 on Page 153 for finding the kth smallest enhy in an
array. This has time complexity O(nz) for computing the running median for the first n elements.
The shortcoming of the brute-force approach is that it is not incremental, i.e., it does not take
advantage of the previous computation. Note that the median of a collection divides the collection
into two equal parts. When a new element is added to the collection, the parts can change by at
most one element, and the element to be moved is the largest of the smaller half or the smallest of
the larger half.
We can use two heaps, a max-heap for the smaller half and a min-heap for the larger half. We
will keep these heaps balanced in size. The max-heap has the property that we can efficiently extract
the largest element in the smaller part; the min-heap is similar.
For example, let the input values be 1,,0,3,5,2,0,1. Let L and H be the contents of the min-heap
and the max-heap, respectively. Here is how they progress:
(1.) Read in 1: L = lll,H = [], median is 1.
(2.) Read in 0: L = ll),H = [0], median is (1 + O)12 = 0.5.
(3.) Read in 3: L = l1,3l,H = [0], median is 1.
(4.) Read in 5: L = l3,5l,H = f1,01, median is (3 + 1)12 = 2.
(5.) Read n2 L = f2,3,5f,H = f1,0f, median is 2.
(6.) Read in 0: L = 12,3,51,H = [1,0,0], median is (2 + 1)12 = 1.5.
(7.) Read in L: L = 11.,2,3,5),H = 11,,0,01, median is 1.
def online-median(sequence) :
# nin_heap stores the Targer half seen so far.
min-heap = []
# nax_heap stores the snaller half seen so far
# vaTues in nax-heap are negative
max-heap - []
result = []
for x in sequence:
heapq. heappush (max-heap , -heapq . heappushpop (min_heap , x) )
# Ensure nin-heap and max_heap have equa-l nunber of elenents jf an eyen
# number of elements is read,' otherrise , nin_heap must &ave one more
# eTenent than max_heap.
if len(max-heap) > len(rnin_heap) :
heapq. heappush(min-heap, -heapq. heappop(max_heap))
result.append(0.5 * (nin_heap[0] + (-max_heap[0]))
139
```
