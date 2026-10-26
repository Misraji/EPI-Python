# Exercise 5.12: Sample offline data

**Printed textbook page:** 54. **Reference transcription pages:** 54–54.

> **Unverified OCR transcription:** This section retains the supplied PDF text layer. It is not certified verbatim: code syntax, mathematical symbols, and page boundaries may be corrupted. When two exercises begin on the same page, their excerpts overlap. Do not paste extracted code into a `.py` file without manual verification.

#### Printed page 54 (PDF page 68)

```text
# Swap the sfiallest entry after index inversion-point that is greater than
# permIinversion-pointJ. Since entries in pern are decreasing after
# inversion-point , if we search in reverse order, the first 
entry that is
# greater than pern[inversion-point] is the entry to srap with.
for i in reversed(range(inversion-point + 1, Ien(perm))):
if permIi] > permtinversion-pointl :
permlinversion-pointl, permIi] = permIi], permIinversion-point]
break
# Entries in pern nust appear in decreasing order after inversion-point,
# so we sinply reverse these entries to get tfie srnallest dictionary order
permIinversion-point + 1:] = reversed(permIinversion-point + 1:])
return perm
Each step is an iteration through an array, so the time complexity is O(n). All that we use are a few
local variables, so the additional space complexity is O(1).
Varianh Compute the kth permutation under dictionary ordering, starting from the identity per-
mutation (which is the first permutation in dictionary ordering).
Varianh Given a permutation p, retum the permutation corresponding to the pratioils permutation
of p under dictionary ordering.
5.72 SeNrprs oFFLTNE DArA
This problem is motivated by the need for a company to select a random subset of its customers to
roll out a new feature to. For example, a social networking company may want to see the effect of
a new UI on page visit duration without taking the chance of alienating all its users if the rollout is
unsuccessful.
Implement an algorithm that takes as input an array of distinct elements and a size, and returns
a subset of the given size of the array elements. All subsets should be equally likely. Retum the
result in input array itself.
Hint: How would you construct a random subset of size k + 1 given a random subset of size k?
Solution: Let the input array be A, its length n, artd the specified size k. A naive approach is to
iterate through the input array, selecting entries with probability k/n. Although the average number
of selected entries is k, we may select more or less than k entries in this way.
Another approach is to enumerate all subsets of size k and then select one at random from
these. Since there are ([) subsets of size k, the time and space complexity are huge. Furthermore,
enumerating all subsets of size k is nontrivial (Problem 15.5 on Page 226).
The key to efficiently building a random subset of size exactly k is to first build one of sizek - 1.
and then adding one more element, selected randomly from the rest. The problem is trivial when
k = 1. We make one call to the random number generator, take the retumed value mod n (callit r),
and swap A[0] with A[r]. The entry A[0] now holds the result.
For k > 1, we begin by choosing one element at random as above and we now repeat the same
process with the n - 1 element subarray All.,n - 11. Eventually, the random subset occupies the
slots A[0, k - 1] and the remaining elements are in the last n - k slots.
54
```
