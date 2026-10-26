# Exercise 13.8: Partitioning and sorting an array with many repeated entries

**Printed textbook page:** 191. **Reference transcription pages:** 191–192.

> **Unverified OCR transcription:** This section retains the supplied PDF text layer. It is not certified verbatim: code syntax, mathematical symbols, and page boundaries may be corrupted. When two exercises begin on the same page, their excerpts overlap. Do not paste extracted code into a `.py` file without manual verification.

#### Printed page 191 (PDF page 205)

```text
return seIf. Ieft. is-closed and not other. left. is-closed
def union-of-intervals (intervals) 
:
# Enpty input.
if not intervals:
return []
# Sort interva.ls according to left 
endpoints of intervaTs.
intervals, sorto
result = [intervals[0]l
for i in intervals:
if intervals and (i.1eft.va1 < result[-1].right.val or
(i.left.vaI 
== result[-1].right.val and
(i. left.is-closed or resuLt[-1]. right. is_closed)))
if (i.right.val > result[-1],right.va1 or
(i.right,val == result[-1].right.val and i.right.is_closed)) :
result [-1] . right = i. right
else:
result. append(i)
return result
The time complexity is dominated by the sort step, i.e.,O(nlogn).
13.8 Panrrrrowrrtc AND soRTrNG AN ARRAy wrrH MANy REpEATED ENTRTES
Suppose you need to reorder the elements of a very large array so that equal elements appear
together. For example, if the array is (b,a,c,b,d,a,b,d) then (a,a,b,b,b,c,d,dl is an acceptable
reordering/ as is (d, d, c, a, a, b, b, b).
If the entries are integers, this reordering can be achieved by sorting the array. If the number
of distinct integers is very small relative to the size of the array, an efficient approach to sorting
the array is to count the number of occurrences of each distinct integer and write the appropriate
number of each integer, in sorted order, to the array. When array entries are obiects, with multiple
fields, only one of which is to be used as a key, the problem is harder to solve.
You are given an array of student objects. Each student has an integer-valued age field that is to be
treated as a key. Rearrange the elements of the array so that students of equal age appear together.
The order in which diffurent ages appear is not important. How would your solution change if ages
have to appear in sorted order?
Hint: Count the number of students for each age.
Solution: The brute-force approach is to sort the array, comparing on age. If the array length is r,
the time complexity is O(nlogn) and space complexity is O(1). The inefficiency in this approach
stems from the fact that it does more than is required-the specification simply asks for students of
equal age to be adjacent.
We use the approach described in the introduction to the problem. Howeve{, we cannot apply
it directly, since we need to write objects, not integers-two sfudents may have the same age but
still be different.
For example, consider the array ((Greg,14), (John,12), (Andy,11), (jim,13), (Phil,12), (Bob,13),
(Chip,13), (Tim,14)). We can iterate through the array and record the number of students of each
191
```

#### Printed page 192 (PDF page 206)

```text
age in a hash. Specifically, keys are ages, and values are the corresponding counts. For the given
example, on completion of the iteration, the hash is (14,2),(12,2),(11,,1),(13,3). This tells us that
we need to write two students of age 1.4, two students of age 12, one student of age 11 and three
students of age 13. We can write these students in any ordel as long as we keep students of equal
age adjacent.
If we had a new array to write to, we can write the two students of age 14 starting at index 0,
thetwostudentsofage12startingatindex0+2=2,theonestudentofagellatindex2+2=4,
and the three students of age 13 starting at index 4 + 1 = 5. We would iterate through the original
array, and write each entry into the new array according to these offsets. For example, after the first
four iterations, the new array would be ((Greg, 14), -, $ohn, 12), -, (Andy,11),(Jirn,13), -, -).
The time complexity of this approach is O(n), but it entails O(n) additional space for the result
array. We can avoid having to allocate a new array by performing the updates in-place. The idea is
to maintain a subarray for each of the different types of elements. Each subarray marks out entries
which have not yet been assigned elements of that type. We swap elements across these subarrays
to move them to their correct position.
In the program below, we use two hash tables to track the subarrays. One is the starting offset
of the subarray, the other its size. As soon as the subarray becomes empty, we remove it.
Person = collections.namedtuple('Person', ('age','name'))
def group-by-age (people) :
age_to-count = collections.Counter([person.age for person in people])
age-to-offset, offset = {}, 
0
for age , count in age-to-count , items () :
age-to-offsetIage] = offset
offset += count
rhile age-to-offset:
from-age = nert(iter(age-to-offset))
from-idx = age_to-offset Ifrom-age]
to-age = people Ifron-idx] . age
to-idx = age-to-offset Ipeople Ifrom-idx] . agel
people Ifrorn-idx] , people Ito-idx] - people Ito-idx] , people Ifrom-idx]
# Use age-to-count to see when we are finished with a particuTar age
age-to-countIto-age] -= 1
if age-to-count I to-age ] :
age-to-offsetIto-age] = to-idx + I
else:
del age_to-offset Ito-age]
The time complexity isO(n), since the first pass entails n hash table inserts, and the second pass
spends O(1) time to move one element to its proper location. The additional space complexity is
dictated by the hash table, i.e., O(m), where rz is the number of distinct ages.
If the entries are additionally required to appear sorted by age, we can use a BST-based map
(Chapter 14) to map ages to counts, since the BST-based map keeps ages in sorted order. For
our example, the age-count pairs would appear in the order (1,1,,1),(12,2),(13,3),(1,4,2). The time
complexity becomes O(n + mlogm), since BST insertion takes time O(logm). Such a sort is often
referred to as a counting sort.
192
```
