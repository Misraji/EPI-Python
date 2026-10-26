# Chapter 13: Sorting

**Starts at printed page 180.** [Repository overview](../../../README.md)

**Source:** user-supplied EPI Python PDF (2016/2017 edition). **Transcription warning:** PDF text extraction contains OCR errors, especially in code. Consult the original PDF for ambiguous expressions and diagrams.

## Original chapter introduction (unverified PDF text layer)

### Printed page 180

```text
Cnaprrn
Sorting
PROBLEM 1,4 (Meshing). Two monotone sequeflces S,T, of lengths n, m, respectiaely, are stored
intutosystemsofn(p+1),m(p+1)consecutiaememoryloutions,respectiuely: s,s+1,...,s+
n(p + l) - 1 and t, t + 1.,.. ., t + m(p + 1) - 1. . . . lt is desired to find a monotone permutation R
of the sum lS, Tl, and place it at the locations 1 r + 1., . . ., r + (n + m)(p + 1) - 1.
- "Planning And Coding Of Problems Eor An Electronic Computing Instrument,"
H. H. Golosrrxr aNo J. vou Nrur'.raNN, 1948
Sorting-rearranging a collection of items into increasing or decreasing order-is a corunon prob-
lem in computing. Sorting is used to preprocess the collection to make searching faster (as we saw
with binary search through an array), as well as identify items that are similar (e.g., students are
sorted on test scores).
Naive sorting algorithms run in O(nz) ttrne. A number of sorting algorithms run in O(nlogn)
time-heapsort, merge sort, and quicksort are examples. Each has its advantages and disadvan-
tages: for example, heapsort is in-place but not stable; merge sort is stable but not in-place; quicksort
runs O(n2) time in worst-case. (An in-place sort is one which uses 0(L) spacei a stable sort is one
where entries which are equal appear in their original order.)
A well-implemented quicksort is usually the best choice for sorting. We briefly outline altema-
tives that are better in specific circumstances,
For short arrays, e.g., 10 or fewer elements, insertion sort is easier to code and faster than
asymptotically superior sorting algorithms. If every element is known to be at most k places from
its final location, a min-heap can be used to get an O(nlogk) algorithm (Solution 10.3 on Page 137).
If there are a small number of distinct keys, e.g., integers in the range [0..255], counting sort, which
records for each element, the number of elements less than it, works well. This count can be kept in
an array (if the largest number is comparable in value to the size of the set being sorted) or a BSI
where the keys are the numbers and the values are their frequencies. If there are many duplicate
keys we can add the keys to a BST, with linked lists for elements which have the same key; the
sorted result can be derived from an in-order traversal of the BST.
Most sorting algorithms are not stable. Merge sort, carefully implemented, can be made stable.
Another solution is to add the index as an integer rank to the keys to break ties.
Most sorting routines are based on a compare function. However, it is also possible to use
numerical attributes directly, e.9., in radix sort.
The heap data structure is discussed in detail in Chapter 10, Briefly, a max-heap (min-heap)
stores keys drawn from an ordered set. It supports O(logn) inserts and O(1) time lookup for the
maximum (minimum) element; the maximum (minimum) key can be deleted in O(logn) time.
Heaps can be helpful in sorting problems, as illustrated by Problems 1.0.1 on Page 134,10.2 on
Page 135, and 10.3 on Page 136.
180
```

### Printed page 181

```text
Sortingboot camp
It's important to know how to use effectively the sort functionality provided by your language's
library. Let's say we are given a student class that implements a compare method that compares
students by name. Then by default, the array sort library routine will sort by n€une. To sort an array
of students by GPA, we have to explicitly specify the compare function to the sort routine.
class Student (object) :
def --init--(self 
, name, grade_point_average) :
self.name = name
self . grade-point-average = grade_point_average
def --1t--(seIf, other)
return self. name < other . name
students =
Student
Student
Student
Student
l
, 4.0) ,
, 3.0),
, 2.0),
, 3.2)
t
(,A
('c
(,8
('D
# Sort according to __It__ defined jn Student. students renained unchanged
students-sort-by_name = sorted(students)
# Sort students in-pIace by grade_point_average.
students. sort(key=lanbda student : student. grade-point_average)
The time complexity of any reasonable library sort is O(nlogn) for an array with ,4 entries. Most
library sorting functions are based on quicksort, which has O(1) space complexity.
come in two
vors:
.) use sorting to
steps
an
rithm simpler, and (2.) design a custom sorting routine. For the former, it's fine to use a library
sort function, Possibly with a custom comparator. For the latter, use a data structure like a BSf,
heap, or affay indexed by values.
Certain problems become easier to understand, as well as solve, when the input is sorted. The
most natural reason to sort is if the inputs have a natural ordering, and sorting can be used as
a preprocessing step to speed up searching.
For specialized input, e.9., a very small range of values, or a small number of values, it's
possible to sort nO(n) time rather thanO(nlogn)time.
It's often the case that sorting can be implemented in less space than required by a brute-force
approach.
Sometimes it is not obvious what to sort on, e.g., should a collection of intervals be sorted on
slarting points_ql endp-ornts? (Prgblem 13,5 on Page 186)
Table 13.1 : Top Tips for Sorting
Know your sorting libraries
To sort a list in-place, use the sortO method; to sort an iterable, use the function sortedo
181
```
