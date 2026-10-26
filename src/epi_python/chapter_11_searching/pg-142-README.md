# Chapter 11: Searching

**Starts at printed page 142.** [Repository overview](../../../README.md)

**Source:** user-supplied EPI Python PDF (2016/2017 edition). **Transcription warning:** PDF text extraction contains OCR errors, especially in code. Consult the original PDF for ambiguous expressions and diagrams.

## Original chapter introduction (unverified PDF text layer)

### Printed page 142

```text
Cnaprnn
Searchirg
- 
"The Anatomy of A l-arge-Scale Hypertextwl Web Search Engine,"
S. M. BnrN eNo L. Pacs, 1998
Search algorithms can be classified in a number of ways. Is the underlying collection static or
dlmamic, i.e., inserts and deletes are interleaved with searching? Is it worth spending the com-
putational cost to preprocess the data so as to speed up subsequent queries? Are there statistical
properties of the data that can be exploited? Should we operate directly on the data or transform
ir?
In this chapter, our focus is on static data stored in sorted order in an array. Data structures
appropriate for dynamic updates are the subject of Chapters 10,12, and 14,
The first collection of problems in this chapter are related to binary search. The second collection
pertains to general search.
142
```

### Printed page 143

```text
Binary search
Given an arbitrary collection of n keys, the only way to determine if a search key is present is by
examining each element. This has O(n) time complexity. Fundamentally, binary search is a natural
elimination-based strategy for searching a sorted array. The idea is to eliminate half the keys from
consideration by keeping the keys in sorted order. If the search key is not equal to the middle
element of the array, one of the two sets of keys to the left and to the right of the middle element
can be eliminated from further consideration.
Questions based on binary search are ideal from the interviewers perspective: it is a basic
technique that every reasonable candidate is supposed to know and it can be implemented in a
few lines of code. On the other hand, binary search is much trickier to implement correctly than it
aPPears-you should implement it as well as write comer case tests to ensure you understand it
properly.
Many published implementations are incorrect in subtle and not-so-subtle ways-a study re-
ported that it is correctly implemented in only five out of twenty textbooks. Jon Bentley, in his book
"Programming Pearls" reported that he assigned binary search in a course for professional program-
mers and found that 90% failed to code it correctly despite having ample time. (Bentley's students
would have been gratified to know that his own published implementation of binary search, in
a column titled "Writing Correct Programs", contained a bug that remained undetected for over
twenty years.)
Binary search can be written in many ways-recursive, iterative, diffurent idioms for condi-
tionals, etc. Here is an iterative implementation adapted from Bentley's book, which includes his
brg.
def bsearch (t , A) :
L,U=0,Ien(A)-1
while L <= U:
!l = (L + U) // 
2
if A[]ll < t:
L=l{+ 
1
elif e[u] == t:
return lt
else:
U=l{-1
return -1
Theerrorisintheassignmentlt= (L +U) / zrnLtne4,whichcanpotentiallyleadtooverflow
This overflow can be avoided by using M = L + (U - L) / Z.
The time complexity of binary search is given by T(n) = T(nl2) + c, where c is a constant. This
solves toT(n) = O(logn), which is far superior to the O(n) approach needed when the keys are
unsorted. A disadvantage of binary search is that it requires a sorted array and sorting .u:r array
takes O(n log n ) time. However, if there are m€rny searches to perform, the time taken to sort is not
an issue.
Many variants of searching a sorted array require a little more thinking and create opportunities
for missing comer cases.
143
```

### Printed page 144

```text
Searchingboot camp
When objects are comparable, they can be sorted and searched for using library search functions.
Typically, the language knows how to compare built-in types, e.9., integers, strings, library classes
for date, URLs, SQL timestamps, etc. However, user-defined types used in sorted collections
must explicitly implement comparison, and ensure this comparison has basic properties such as
transitivity. (If the comparison is implemented incorrectly, you may find a lookup into a sorted
collection fails, even when the item is present.)
Suppose we are given as input an array of students, sorted by descending GPA, with ties broken
on name. In the program below, we show how to use the library binary search routine to perform
fast searches in this array. In particulal we pass binary search a custom comparator which compares
students on GPA (higher GPA comes first), with ties broken on name.
Student = collections.namedtuple('student', ('name', 'grade-point-average'))
def comp-gpa (student) :
return (-student.grade-point-average, student.name)
def search-student (students , target , comp-gpa) :
i = bisect.bisect-left([comp-gpa(s) for s in students], comp-gpa(target))
return 0 <= i < len(students) and students[i] == target
Assuming the i-th element in the sequence can be accessed in O(1) time, the time complexity of the
program is O(logn).
Binary
rs an
1S
to more than just
aftays, e.g., it can be used to search an interval of real numbers or integers.
If your solution uses sorting, and the computation performed after sorting is faster than sorting,
e.g., O(n) or O(logn),look for solutions that do not perform a complete sort'
Consider time/space tradeoffs, such as
Table 11 .1 : Top Tips for Searching
Know your searching libraries
The bisect module provides binary search functions for sorted list. Specifically, assuming a is a
sorted list.
o To find the first element that is not less than a targeted value, use bi sect . bi sect-Ieft (a , x) .
This call retums the index of the first entry that is greater than or equal to the targeted value.
If all elements in the list are less than x, the retumed value is len(a).
o Tofindthefirstelementthatisgreaterthanatargetedvalue,usebisect.bisect-right(a,x).
This call retums the index of the first entry that is greater than the targeted value. If all elements
in the list are less than or equal to x, the retumed value is len(a).
In an interview, if it is allowed, use the above functions, instead of implementing your own binary
search.
144
```
