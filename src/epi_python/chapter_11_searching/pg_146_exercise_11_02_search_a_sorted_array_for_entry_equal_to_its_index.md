# Exercise 11.2: Search a sorted array for entry equal to its index

**Printed textbook page:** 146. **Reference transcription pages:** 146–146.

> **Unverified OCR transcription:** This section retains the supplied PDF text layer. It is not certified verbatim: code syntax, mathematical symbols, and page boundaries may be corrupted. When two exercises begin on the same page, their excerpts overlap. Do not paste extracted code into a `.py` file without manual verification.

#### Printed page 146 (PDF page 160)

```text
The complexitybound is stillO(log n)-this isbecause each iteration reduces the size of the candidate
set by half.
Varianh Design an efficient algorithm that takes a sorted array and a key, and finds the index of
the first occurrence of an element greater than that key. For example, when applied to the array in
Figure 11.1 on the preceding page your algorithm should return 9 if the key is 285; if it is -13, your
algorithm should return 1..
Varianh Let A be an unsorted array of n integers, with A[0] > A[1] and Aln - 2) < A[n - 11. Call an
index I a local minimum if AU] is less than or equal to its neighbors. How would you efficiently find
a local minirnum, if one exists?
Varianfi Write a program which takes a sorted anay A of integers, and an integer k, and refurns
the interval enclosing k, i.e., the pair of integers L and U such that L is the first occurrence of k in
A and U is the last occurrence of k in A. If k does not appear in A, return [-1, -1]. For example if
1= (7,2,2,4,4,4,7,11,'1.1.,13) and k = 77, you should retum [7,8].
Variant Write a progr.rm which tests if p is a prefix of a string in an array of sorted strings.
1,1,,2 Srancu A soRTED ARRAv FoR ENTRv EeUAL To ITS INDEX
Design an efficient algorithm that takes a sorted array of distinct integers, and retums an index I
such that the element at index I equals i. For example, when the input is <-2,0,2,3,6,7,91your
algorithm should return 2 or 3.
Hinf; Reduce this problem to ordinary binary search.
Solution: A brute-force approach is to iterate through the array, testing whether the lth entry equals
l. The time complexity is O(n), where n is the length of the array.
The brute-force approach does not take advantage of the fact that the array (call it A) is sorted
and consists of distinct elements. In particular, note that the difference between an entry and its
index increases by at least 1 as we iterate through A. Observe that if Aljl > /, then no entry after j
can satisfy the given criterion. This is because each element in the array is at least 1 greater than the
previous element. For the siune reason , if A[jl < j , no entry before i can satisfy the given criterion.
The above observations can be directly used to create a binary search type algorithm for finding
an I such that A[i] = l. A slightly simpler approach is to search the secondary affay B whose fth
entry is Ali) - i for 0, which is just ordinary binary search. We do not need to actually create the
secondary array, we can simply use A[i] - i wherever Bft] is referenced.
For the given example, the secondary array B is (-2, -1,,0,0,2,2,3). Binary search for 0 retums
the desired result, i.e., either of index 2 or 3.
def search-entry-equal-to-its-index(A) 
:
left, right = 0, len(A) - 1
while left <= right:
mid = (left + right) // 
2
difference = Almidl - mid
# Afnid] == nid if and only if difference == 0
if difference == 0:
return mid
elif difference > 0:
146
```
