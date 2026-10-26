# Exercise 5.15: Compute a random subset

**Printed textbook page:** 57. **Reference transcription pages:** 57–57.

> **Unverified OCR transcription:** This section retains the supplied PDF text layer. It is not certified verbatim: code syntax, mathematical symbols, and page boundaries may be corrupted. When two exercises begin on the same page, their excerpts overlap. Do not paste extracted code into a `.py` file without manual verification.

#### Printed page 57 (PDF page 71)

```text
Hint: lf. the result is stored in A, how would you proceed once A[r - 1] is assigned correctly?
Solution: A brute-force approach might be to iteratively pick random numbers between O and n - 1,,
inclusive. If number repeats, we discard it, and try again. A hash table is a good way to store and
test values that have already been picked.
For example, if n = 4, we might have the sequence 1,,2,1 (repeats), 3, 1 (repeats), 2 (repeat), 0
(done, all numbers from 0 to 3 are present). The corresponding permutation is (1,2,3,0).
It is fairly clear that all permutations are equally likely with this approach. The space complexity
beyond that of the result array is O(n) for the hash table. The time complexity is slightly challenging
to analyze. Early on, it takes very few iterations to get more new values, but it takes a long time
to collect the last few values. Computing the average number of tries to complete the permutation
in this way is known as the Coupon Collector's Problem. It is known that the number of tries on
average (and hence the average time complexity) is O(nlogn).
Clearly, the way to improve time complexity is to avoid repeats. We can do this by restricting
the set we randomly choose the remaining values from. If we apply Solution 5.12 on Page 54 to
<0,t,2,. .. ,n - 1) with k = n, at each iteration the array is partitioned into the partial permutation
and remaining values. Although the subset that is returned is unique (it will be 10,1, . . .,n - 7l), all
n! possible orderings of the elements in the set occur with equal probability. For example ,let n = {.
We begin with (0, 1,2,3>. The first random number is chosen between 0 and 3, inclusive. Suppose
it is 1. We update the array to (1,,0,2,3). The second random number is chosen between 1 and 3,
inclusive. Suppose it is 3. We update the array to (1.,3,0,2). The third random number is chosen
between 2 alrrd 3, inclusive. Suppose it is 3. We update the array to (1,3,2,0). This is the returned
result.
def compute-random-permutation (n) :
permutation = Iist(range(n))
random-sampling (n, permutation)
return permutation
The time complexity is O(n), and, as an added bonus, no storage outside of that needed for the
permutation array itself is needed.
5.15 CoMpurs A RANDoM suBsET
The set {0,'1.,2,... ,n - 1} has ([) = nll((n - k)!/c!) subsets of size k. We seek to design an algorithm
that returns any one of these subsets with equal probability.
Write a program that takes as input a positive integer n and asizek < n, and retums asize-k subset
of 10,L,2,. ..,fl - 1). The subset should be represented as an array. All subsets should be equally
likely and, in addition, all permutations of elements of the array should be equally likely. You may
assume you have a function which takes as input a nonnegative integer I and retums an integer in
the set 10,1,.. .,t - 1l with uniform probability.
Hln f: Simulate Solution,5.12 on Page54, using an appropriate data structure to reduce space.
Solution: Similar to the brute-force algorithm presented in Solution 5.14 on the preceding page, we
could iteratively choose random numbers between 0 and n - 1 until we get k distinct values. This
57
```
