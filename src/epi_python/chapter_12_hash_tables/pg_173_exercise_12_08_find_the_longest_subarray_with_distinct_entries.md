# Exercise 12.8: Find the longest subarray with distinct entries

**Printed textbook page:** 173. **Reference transcription pages:** 173–173.

> **Unverified OCR transcription:** This section retains the supplied PDF text layer. It is not certified verbatim: code syntax, mathematical symbols, and page boundaries may be corrupted. When two exercises begin on the same page, their excerpts overlap. Do not paste extracted code into a `.py` file without manual verification.

#### Printed page 173 (PDF page 187)

```text
12.8 FrNp rnr LoNGEST suBARRAy wrrH DrsrrNCT ENTRTES
Write a program that takes an array and returns the length of a longest subarray with the property
thatallitselementsaredistinct. Forexample,if thearrayis (f,s,f,e,t,w,e,n,w,e) thenalongest
subarray all of whose elements are distinct is (s, f ,e,t,w).
Hint: What should you do if the subarray from indices I to f satisfies the property, but the subarray from I to
i+ldoesnot?
Solution: We begin with a brute-force approach. For each subarray, we test if all its elements are
distinct using a hash table. The time complexity isO(n3),where n is the array length since there are
O(nz) subarrays, and their average length is O(n).
We can improve on the brute-force algorithm by noting that if a subarray contains duplicates,
every array containing that subarray will also contain duplicates. Therefore, for any given starting
index, we can compute the longest subarray starting at that index containing no duplicates in time
O(rz), since we can incrementally add elements to the hash table of elements from the starting index.
This leads to an O(n2) algorithm. As soon as we get a duplicate, we cannot find a longerbeginning
at the same initial index that is duplicate-free.
We can improve the time complexity by reusing previous computation as we iterate through the
array. Suppose we know the longest duplicate-free subarray ending at a given index. The longest
duplicate-free subarray ending at the next index is either the previous subarray appended with the
element at the next index, if that element does not appear in the longest duplicate-free subarray
at the current index. Otherwise it is the subarray beginning at the most recent occurrence of the
element at the next index to the next index. To perform this case analysis as we iterate, all we need
is a hash table storing the most recent occurrence of each element, and the longest duplicate-free
subarray ending at the current element.
For the given example, (f,s,f,e,t,u),e,n,u),e), when we process the element at index 2, the
longest duplicate-free subarray ending at index 1 is from 0 to 1. The hash table tells us that the
element at index 2, namely f , appears in that subarray, so we update the longest subarray ending at
index 2 to being from index '1, to 2. Indices 3-5 introduce fresh elements. Index 6 holds a repeated
value, e, which appears within the longest subarray ending at index 5; specifically, it appears at
index 3. Therefore, the longest subarray ending at index 6 to start at index 4.
def longest-subarray-with-distinct-entries 
(A) :
# Records the rost tecent occurrences of each entry.
most_recent_occurrence = {}
longest-dup-free-subarray-start_idx = result = 0
for i, a in enunerate(A):
# Defer updating dup_idx until ue see a dupTicate.
if a in most_recent_occurrence:
dup_idx = most_recent_occurrence Ia]
# Atil appeared before. Did it appear jn the longest current
# subartay?
if dup_idx >= longest_dup_free_subarray_start_idx :
result = nar(result, i - longest_dup_free_subarray_start_idx)
Iongest_dup_free_subarray_start_idx = dup_idx + 1
most-recent-occurrenceIa] = i
return [ar(result, len(A) - longest_dup_free_subarray_start_idx)
173
```
