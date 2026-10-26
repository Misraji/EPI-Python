# Exercise 13.3: Remove first-name duplicates

**Printed textbook page:** 184. **Reference transcription pages:** 184–184.

> **Unverified OCR transcription:** This section retains the supplied PDF text layer. It is not certified verbatim: code syntax, mathematical symbols, and page boundaries may be corrupted. When two exercises begin on the same page, their excerpts overlap. Do not paste extracted code into a `.py` file without manual verification.

#### Printed page 184 (PDF page 198)

```text
We carurot use the above approach with the first array playing the role of the result and still
keep the time complexity O(m + n). The reason is that if an entry in the second array is smaller than
some entry in the first array/ we will have to shift that and all subsequent entries in the first array
to the right by 1. In the worst-case, each entry in the second array is smaller than every entry in the
first array, and the time complexity is O(mn).
We do have spare space at the end of the first array. We take advantage of this by filling the
first array from its end. The last element in the result will be written to index m + n - 1. For
example, if A = (5,73,17, e, e, e, s, -) and B = (3,7,11,19>, then A is updated in the following man-
ner: (5,73,77,-,-,-,19,->,<5,13,17,-,-,17,19,->,<5,13,17,-,13,17,19,->,<5,73,77,7L,13,77,79,-r,
<5,73,7,1.L,73,17,19, -), (5,5,7,17,73,17,19, ->, <3,5,7,77,\3,77,19, ->.
Note that we will never overwrite an entry in the first array that has not already been processed.
The reason is that even if every entry of the second array is larger than each element of the first
array, all elements of the second array will fill up indices m to m + n - l inclusive, which does not
conflict with entries stored in the first array. This idea is implemented in the program below. Note
the resemblance to Solution 6.4 on Page77, where we also filled values from the end.
def merge-two-sorted-arrays (A, m, B, n) :
a, b, write-idx =m - 1, n - 1, n+ n - 1
while a >= 0 and b >= 0:
if A[a] > B[b]:
AIwrite-idx] = AIa]
a-=1
else:
AIwrite-idx] = B[b]
b-=1
write-idx -= 1
while b >= 0:
Alwrite-idxl = Btbl
write-idx, b = write-idx - 1, b - 1
The time complexity is O(m + n). Ituses O(1) additional space
13.3 Rruovr FrRST-NAME DUpLICATES
Design an efficient algorithm for removing all first-name duplicates from an array. For exam-
ple, if the input is ((Ian,Botham),(David,Gower),(Ian,Bell),(Ian,Chappell)), one result could be
((Ian, Bell), (David, Gower)); ((David, Gower), (Ian, Botham)) would also be acceptable.
Hint: Bring equal items close together.
Solution: A brute-force approach is to use a hash table. For the names example, we would need a
hash function and an equals function which use the first name only. We first create the hash table
and then iterate over it to write entries to the result array. The time complexity is O(n), where n is
the number of items. The hash table has a worst-case space complexity of O(n).
We can avoid the additional space complexity if we can reuse the input array for storing the
final result. First we sort the array, which brings equal elements together. Sorting can be done in
O(nlogn) time. The subsequent elimination of duplicates takes O(n) time. Note that sorting an
array requires that its elements are comparable.
class Name
184
```
