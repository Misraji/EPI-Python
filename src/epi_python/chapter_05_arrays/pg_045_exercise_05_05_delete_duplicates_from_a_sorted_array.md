# Exercise 5.5: Delete duplicates from a sorted array

**Printed textbook page:** 45. **Reference transcription pages:** 45–45.

> **Unverified OCR transcription:** This section retains the supplied PDF text layer. It is not certified verbatim: code syntax, mathematical symbols, and page boundaries may be corrupted. When two exercises begin on the same page, their excerpts overlap. Do not paste extracted code into a `.py` file without manual verification.

#### Printed page 45 (PDF page 59)

```text
Write a program which takes an array of n integers, where A[i] denotes the maximum you can
advance from index l, and retums whether it is possible to advance to the last index starting from
the beginning of the array.
Hint: Analyze each location, starting from the beginning.
Solution: It is natural to try advancing as far as possible in each step. This approach does not
always work, because it potentially skips indices containing large entries. For example, if A =
<2,4,1,1,0,2,3), then it advances to index 2, which contains a 1, which leads to index 3, after which
it cannot progress. Howevel, advancing to index 1, which contains a 4lets us proceed to index 5,
from which we can advance to index 5.
The above example suggests iterating through all entries in A. As we iterate through the array,
we track the furthest index we know we can advance to. The furthest we can advance from index i
is i + Alil. If, for some I before the end of the array, I is the furthest index that we have demonstrated
that we can advance to, we cannot reach the last index. Otherwise, we reach the end.
For example, if A = <3,3,7,0,2,0,1),we iteratively compute the furthest we can advance to as
0,3,4,4,4,6,6,7, which reaches the last index, 6. lf A = (3,2,0,0,2,0,7>, we iteratively update the
furthest we can advance to as 0,3,3,3,3, after which we cannot advance, so it is not possible to
reach the last index.
The code below implements this algorithm. Note that it is robust with respect to negative entries,
since we track the maximum of how far we proved we can advance to and i + Ali).
def can-reach-end(A):
furthest-reach-so-far, last-index = 0, len(A) - 1
i=0
rhile i <= furthest-reach-so-far and furthest_reach_so_far < last_index
furthest-reach-so-far = nar(furthest-reach-so_far, AIi] + i)
i+=1
return furthest-reach_so_far >= last_index
The time complexity is O(n), and the additional space complexity (beyond what is used for A) is
three integer variables, i.e., O(7).
Variant: Write a program to compute the minimum number of steps needed to advance to the last
location.
5.5 Dsrsrr DUpLTcATEs FRoM A soRTED ARRAy
This problem is concemed with deleting repeated elements from a sorted array. For example, for
the array <2,3,5,5,7,1.1.,L1.,77,73>, then after deletion, the array is (2,3,5,7,77,73,0,0,0). After
deleting repeated elements, there are 6 valid entries. There are no requirements as to the values
stored beyond the last valid element.
Write a program which takes as input a sorted array and updates it so that all duplicates have been
removed and the remaining elements have been shifted left to fill the emptied indices. Return the
number of valid elements. Many languages have library functions for performing this operation-
you cannot use these functions.
Hint:There is an O(n) time and O(1) space solution.
45
```
