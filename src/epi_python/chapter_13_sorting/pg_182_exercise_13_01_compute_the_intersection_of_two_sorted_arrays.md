# Exercise 13.1: Compute the intersection of two sorted arrays

**Printed textbook page:** 182. **Reference transcription pages:** 182–182.

> **Unverified OCR transcription:** This section retains the supplied PDF text layer. It is not certified verbatim: code syntax, mathematical symbols, and page boundaries may be corrupted. When two exercises begin on the same page, their excerpts overlap. Do not paste extracted code into a `.py` file without manual verification.

#### Printed page 182 (PDF page 196)

```text
[ [
. The sortO method implements a stable in-place sort for list objects. It retums None-
the calling list itself is updated. It takes two arguments, both optional: key=Nens, an4
reverse=False If key is not None, it is assumed to be a function which takes list elements
and maps them to objects which are comparable-this function defines the sort order. For
example, if a=[1 , 2, 4, 3, 5, 0, 11, 21, 100] then a.sort(key=lambda x: str(x))
maps integers to strings, and a is updated to [0, 1, 100, LL, 2, 2t, 3, 4, 5), i.e., the
entries are sorted according to the lexicographical ordering of their string representation. If
reverse is set to True, the sort is in descending order; otherwise it is in ascending order.
o The sorted function takes an iterable and return a new list containing all items from the
iterable in ascending order. The original list is unchanged. For example,b = sorted(a,
key=lambda x: str(x)) leaves a unchanged, and assigns b to [0, 1, 100, LL, 2, ZL,
3, 4 , 51. The optional arguments key and reverse work identically to sort.
13.1 Coupurs rHE INTERSECTIoN oF Two soRTED ARRAys
A natural implementation for a search engine is to retrieve documents that match the set of words in
a query by maintaini.g a. inverted index. Each page is assigned an integer identifier, its document-
iD. An inverted index is a mapping that takes a word w and retums a sorted array of page-ids which
contain zu-the sort order could be, for example, the page rank in descending order. When a query
contains multiple words, the search engine finds the sorted array for each word and then computes
the intersection of these arrays-these are the pages containing all the words in the query. The most
computationally intensive step of doing this is finding the intersection of the sorted arrays.
Write a program which takes as hput two sorted arrays, and returns a new array containing
elements that are present in both of the input arrays. The input arrays may have duplicate entries,
but the returned array should be free of duplicates. For example, the input is <2,3,3,5,5,6,7,7,8,12>
and (5,5,6,8 ,8,9,70,10), your output should be (5, 6, 8).
Hinf: Solve the problem if the input array lengths diffur by orders of magnitude. What if they are approximately
equal?
Solution: The brute-force algorithm is a "loop join" , i.e., traversing through all the elements of one
array and comparing them to the elements of the other array. Letm and n be the lengths of the two
input arrays
def intersect-two-sorted-arrays (A, B) :
return [a for i, a in enunerate(A) if (i == 0 or a != A[i - 1]) and a in Bl
The brute-force algorithm has O(mn) time complexity.
Since both the arrays are sorted, we can make some optimizations. First, we can iterate through
the first array and use binary search in array to test if the element is present in the second array.
def intersect-two-sorted-arrays (A, B) :
def is-present (k) :
i = bisect. bisect-left (B, k)
return i < Ien(B) and Blil == k
return I
a for i, a in enunerate(A)
if (i == 0 or a != A[i - 1]) and is-present(a)
l
182
```
