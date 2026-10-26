# Chapter 5: Arrays

**Starts at printed page 37.** [Repository overview](../../../README.md)

**Source:** user-supplied EPI Python PDF (2016/2017 edition). **Transcription warning:** PDF text extraction contains OCR errors, especially in code. Consult the original PDF for ambiguous expressions and diagrams.

## Original chapter introduction (unverified PDF text layer)

### Printed page 37

```text
Cnaprrn
Arrays
The machine can alter the scanned symbol and its behauior
is in part determined by that symbol, but the symbols on
the tape elsewhere do not affect the behauior of the machine.
- 
" lntelligmt Machinery,"
A. M. TunrNc, 1948
The simplest data structure is the array, which is a contiguous block of memory. It is usually
used to represent sequences. Given an array A, Ali) denotes the (l + 1)th object stored in the
array. Retrieving and updating A[i] takes O(1) time. Insertion into a full array can be handled by
resizing, i.e., allocating a new array with additional memory and copying over the entries from the
original array. This increases the worst-case time of insertion, but if the new array has, for example,
a constant factor larger than the original array, the average tirne for insertion is constant since
resizing is infrequent. Deleting an element from an array entails moving all successive elements
one over to the left to fill the vacated space. For example, if the array is <2,3,5,7,9,LL,'1,3,17), then
deleting the element at index 4 results in the array <2,3,5,7,'!.'!.,13,17,0). (We do not care about the
last value.) The time complexity to delete the element at index I from an array of length n is O(n - i).
The same is true for inserting a new element (as opposed to updating an existing entry).
Array boot camp
The following problem gives good insight into working with arrays: Your input is an array of
integers, and you have to reorder its entries so that the even entries appear first. This is easy if you
use O(n) space, where n is the length of the array. Howeveq, you are required to solve it without
allocating additional storage.
\A/hen working with arrays you should take advantage of the fact that you can operate efficiently
on both ends. For this problem, we can partition the array into three subarrays: Even, Unclassified,
and Odd, appearing in that order. Initially Even and Odd are empty, and Unclassified is the entire
array. We iterate through Unclassified, moving its elements to the boundaries of the Even and Odd
subarrays via swaps, thereby expanding Even and Odd, and shrinking Unclassified.
def even-odd (A) :
next-even, next-odd = 0, len(A) - I
rhile next-even < next_odd:
if A[next-even] % 2 == 0:
next_even += 1
else :
AInext-even], Alnext_oddl = 4;n"rt_oddl
next_odd -= I
37
A I next-even ]
```

### Printed page 38

```text
The additional space complexity is clearly O(l)-a couple of variables that hold indices, and a
temporary variable for performing the swap. We do a constant amount of processing per entry, so
the time complexity isO(n).
Array problems often have simple brute.force solutions that use O(n) space, but there are subtler
solutions that use the array itself to reduce space complexity to O(1).
Filling an array from the front is slow, so see if it's possible to write values from the back
Instead of deleting an entry (which requires moving all entries to its left), consider overwriting
it.
When dealing with integers encoded by an array consider processing the digits from the back
of the array. Altemately, reverse the array so the least-significant digit is the first entry.
Be comfortable with writing code that operates on subarrays
It's incredibly easy to make off-by-l errors when operating on arrays-reading past the last
element of an array is a comrnon error which has catastrophic consequences.
Don't worry about preserving the integrity of the array (sortedness, keeping equal entries
together, etc.) until it is time to retum.
An array can serve as a good data structure when you know the distribution of the elements in
advance. For example, a Boolean array of length W is a good choice for representing a subset
of {0,'1.,. .. ,W - 1}. (When using a Boolean array to represent a subset of {'J.,2,3,.. . ,fl|, allocate
anarray of sizen+1to simplifyindexing.) 
.
\A/hen operating on 2D arrays, use parallel logic for rows and for columns
Sometimes it's easier to simulate the specification, than to analytically solve for the result. For
example, rather than writing a formula for the l-th entry in the spiral order for an n x n matrix,
just compute the output from the beginning.
Table 5.1 : Top Tips for Arrays
Know yow affay libraries
Arrays in Python are provided by the list type. (The tuple type is very similar to the list type,
withtheconstraintthatitisimmutable.) Thekeypropertyof alististhatitisdynamically-resized,
i.e., there's no bound as to how many values can be added to it. In the same way, values can be
deleted and inserted at arbitrary locations.
o Know the symtax for instantiating a list, e.8., [3, 5, 7, tt], [1] + [0] * 10,
Iist(range(100)). (List comprehension, described later, is also a powerful tool for in-
stantiating arrays.)
o Thebasicoperationsarelen(A),A.append(42),A.remove(2),andA.insert(3, 
28).
o Knowhowtoinstantiate a2D aruay, e.9., [[1 , 2, 4f , [3, 5, 7, 97, [13]1.
38
```
