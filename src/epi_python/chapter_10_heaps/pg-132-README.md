# Chapter 10: Heaps

**Starts at printed page 132.** [Repository overview](../../../README.md)

**Source:** user-supplied EPI Python PDF (2016/2017 edition). **Transcription warning:** PDF text extraction contains OCR errors, especially in code. Consult the original PDF for ambiguous expressions and diagrams.

## Original chapter introduction (unverified PDF text layer)

### Printed page 132

```text
Cnaprnn
Heaps
Using F-heaps we are able to obtain improoed running times
for seoual network optimization algorithms.
- "Fibonacci heaps and their uses,"
M. L. FneoMeN.rNo R. E. TanyaN, 1987
Aheap is a specialized binary tree. Specifically, it is a complete binary tree as defined on Page 113.
The keys must satisfy theheap property-the key at each node is at least as great as the keys stored at
its children. See Figure 10.1(a) for an example of a max-heap. A max-heap can be implemented as
an array; the children of the node at index I are at indices 2i + 1 and 2i + 2. The affay representation
for the max-heap in Figure 10.1(a) is (561,3'1,4,40L,28,156,359,271,,77,3).
A max-heap supports O(Iogn) insertions, O(1) time lookup for the max element, and O(logn)
deletion of the max element. The extract-max operation is defined to delete and retum the maximum
element. See Figure 10.1(b) for an example of deletion of the max element. Searching for arbitrary
keys has O(n) time complexity.
A heap is sometimes referred to as a priority queue because it behaves like a queue, with one
difference: each element has a "ptiority" associated with it, and deletion removes the element with
the highest priority.
The min-heap is a completely symmetric version of the data structure and supports O(1) time
lookups for the minimum element.
(a) A max-heap. Note that the root holds the maximum key,
561.
(b) After the deletion of max ol the heap in (a). Deletion is per-
lormed by replacing the root's key wilh the key at the last leaf
and then recovering the heap property by repeatedly exchang-
ing keys with children.
Figure 10.1 : A max-heap and deletion on that max-heap.
132
```

### Printed page 133

```text
Heaps boot camp
Suppose you were asked to write a program which takes a sequence of strings presented in "stream-
ing" fashion: you cannot back up to read an earlier value. Your program must compute the k longest
strings in the sequence. All that is required is the k longest strings-it is not required to order these
strings.
As we Process the input, we want to track the k longest strings seen so far. Out of these k strings,
the string to be evicted when a longer string is to be added is the shortest one. A min-heap (not
a max-heap!) is the right data structure for this application, since it supports efficient find-min,
remove-min, and insert. In the program below we use a heap with a custom compare function,
wherein strings are ordered by length.
def top-k(k, stream):
# Entries are compared by their Tengths.
min-heap = [(Ien(s), s) for s in itertools.islice(stream, 
k)]
heapq . heapify (min-heap)
for next-string in strean:
# Push next-string 
and pop the shortest strjng in nin_heap.
heapq.heappushpop(min_heap, (1en(next_string), next_string))
return [p[1] for p in heapq.nsmallest(k, min_heap)l
Each string is processed in O(logk) time, which is the time to add and to remove the minimum
element from the heap. Therefore, if there are n strings in the input, the time complexity to process
all of them isO(nlogk).
We could improve best-case time complexity by first comparing the new string's length with
the length of the string at the top of the heap (getting this string takes O(1) time) and skipping the
insert if the new string is too short to be in the set.
sea
w
you care about is
or
you do not
to
support fast lookup, delete, or search operations for arbitrary elements.
A heap is a good choice when you need to compute the k largest or k smallest elements in a
9olleclion. Fqr the fgrmer, qse l min-h91p, for t!1e lattel uge_-a mal heap.
Table 10.1 : Top Tips for Heaps
Know your heap libraies
Heap functionality in Python is provided by the heapq module. The operations and functions we
will use are
o heapq.heapify(L), which transforms the elements in L into a heap in-place,
o heapq.nlargest(k, L) (heapq.nsmallest(k, L))retumstheklargest(smallest)elementsin
L,
o heapq. heappush(h, e), which pushes a new element on the heap,
o heapq.heappop(h), which pops the smallest element from the heap,
o heapq.heappushpop(h, a), which pushes a on the heap and then pops and retums the
smallest element, and
o e = h[0], which retums the smallest element on the heap without popping it.
a
It's very important to remember that heapq only provides min-heap functionality. If you need to
build a max-heap on integers or floats, insert their negative to get the effuct of a max-heap using
133
```
