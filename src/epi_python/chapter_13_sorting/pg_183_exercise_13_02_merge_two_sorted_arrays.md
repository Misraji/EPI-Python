# Exercise 13.2: Merge two sorted arrays

**Printed textbook page:** 183. **Reference transcription pages:** 183–183.

> **Unverified OCR transcription:** This section retains the supplied PDF text layer. It is not certified verbatim: code syntax, mathematical symbols, and page boundaries may be corrupted. When two exercises begin on the same page, their excerpts overlap. Do not paste extracted code into a `.py` file without manual verification.

#### Printed page 183 (PDF page 197)

```text
The tirne complexity is O(mlogn), where z is the length of the array being iterated over. We can
further improve our run time by choosing the shorter array for the outer loop since if n is much
smaller thanm, then n log(m) is much smaller than ru log(n).
This is the best solution if one set is much smaller than the other. Howevel, it is not the best when
the array lengths are sirnilar because we are not exploiting the fact that both arrays are sorted. We
can achieve linear runtime by simultaneously advancing through the two input arrays in increasing
order. At each iteration, if the array elements differ, the smaller one can be eliminated. If they are
equal, we add that value to the intersection and advance both. (We handte duplicates by comparing
the current element with the previous one.) For example, if the arrays dte- A = (2,3,3,5,7,111 and
3 = (3,3,7,15,31>, then we know by inspecting the first element of each that 2 cannot belong to the
intersection, so we advance to the second element of A. Now we have a corunon element,3, which
we add to the result, and then we advance in both arrays. Now we are at 3 in both arrays, but we
know 3 has already been added to the result since the previous element in A is also 3. We advance
in both again without adding to the intersection. Comparing 5 to7,we can eliminate 5 and advance
to the fourth element in A, which is 7, and equal to the element that B's iterator holds, so it is added
to the result. We then eliminate 11, and since no elements remain in A, we retum (3,7).
de:f intersect-two-sorted-arrays (A, B) :
i, j, intersection-A-B = 0, 0, []
rhile i < Ien(A) and j < len(B):
if Atil == Btjl:
if i == 0 or A[i] != Ali - 1l:
intersection_A_B . append (A Ii ] )
i, i = i + 1, j + 1
elif Atil < B[j]:
i+=1
else: #Atil>Btjl.
j+=t
return intersection_A_B
Since we spend O(1) time per input array element, the time complexity for the entire algorithm is
O(m + n).
13.2 Mrncs rwo soRTED ARRAYS
Suppose you are given two sorted arrays of integers. If one array has enough empty entries at its
end, it can be used to store the combined entries of the two arays in sorted order. For example,
consider (5,13,17, v, e, s, u, -) and (3,7,1\,19), where - denotes an empty entry. Then the combined
sorted entries canbe stored in the first array as <3,5,7,77,73,17,19,-).
Write a Program which takes as input two sorted arrays of integers, and updates the first to the
combined entries of the two arrays in sorted order. Assume the first array has enough empty entries
at its end to hold the result.
Hint: Avoid repeatedly moving entries.
Solution: The challenge in this problem lies in writing the result back into the first array-if we
had a third array to store the result it, we could solve by iterating through the two input arrays in
tandem, writing the smaller of the entries into the result. The time complexity isO(m+ n),wherem
and n arc the number of entries initially in the first and second arrays.
183
```
