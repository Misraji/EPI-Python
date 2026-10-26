# Exercise 5.11: Compute the next permutation

**Printed textbook page:** 52. **Reference transcription pages:** 52–53.

> **Unverified OCR transcription:** This section retains the supplied PDF text layer. It is not certified verbatim: code syntax, mathematical symbols, and page boundaries may be corrupted. When two exercises begin on the same page, their excerpts overlap. Do not paste extracted code into a `.py` file without manual verification.

#### Printed page 52 (PDF page 66)

```text
]
AIi], AIpermInert]l = AIpernlnert]l, 
AIil
temp = permInert]
# Subtracts 7en(pern) fron an entry in pern to nake jt negative,
# which indicates the corresponding move has been performed.
Perm[nert] -= len(Perm)
nert = temp
# Restore pern.
perm[:] = [a + len(perm) for a in perm]
The program above will apply the permutation in O(n) time. The space complexity isO(7), assuming
we ctrn temporarily modify the sign bit from entries in the permutation array.
If we cannot use the sign bit, we cerr allocate an array of n Booleans indicating whether the
element at index I has been processed. Altematively, we can avoid using O(n) additional storage by
going from left-to-right and applying the cycle only if the current position is the leftmost position
in the cycle.
def apply-permutation(perm, A) :
def cyclic-permutation (start , perm , A) :
i, temp = start, Alstart]
wbile True:
next_i = perm[i]
next-temp = AInext-i]
lInext-il 
= temp
i, temP = next-i , next-tem,
if i == start:
break
for i in range(len(A)):
# Iraverses the cycTe to see if i is
5 = perm[i1
while j != i:
if j < i:
break
i = pernIjl
else :
cyclic-permutation(i, 
perm, A)
the minimum elernent
Testing whether the current position is the leftmost position entails traversing the cycle once more,
which increases the run time to O(nz).
Variant Given Nr affay A of integers representing a permutation, update A to represent the inverse
pennutation using only constant additional storage.
5.11 Colrpurr rHE NEXT pERMUTATToN
There exist exactly n! permutations of r elements. These can be totally ordered using the dictionary
ordering-define permutation p to appear before permutation q if n the first place where p and
q differ in their array representations, starting from index 0, the corresponding entry for p is less
than that for 4. For example, <2,0,1> < <2,1,0>. Note that the permutation (0, 1,2) is the smallest
permutation under dictionary ordering, ar.d <2,1,0) is the largest permutation under dictionary
ordering.
52
```

#### Printed page 53 (PDF page 67)

```text
Write a program that takes as input a permutation, and returns the next permutation under dictio-
nary ordering. If the permutation is the last permutation, return the empty array. For example, if
the input is (1,0,3,2) your function should retum <1.,2,0,3>. If the input is (3,2,1,0), return O.
Hint: Study concrete examples.
Solution: A brute-force approach might be to find all permutations whose length equals that of
the input array, sort them according to the dictionary order, then find the successor of the input
permutation in that ordering. Apart from the enormous space and time complexity this entails,
simply computing all permutations of length n is a nontrivial problem; see Problem 15.3 on Page222
for details.
The key insight is that we want to increase the permutation by as little as possible. The loose
analogy is how a car's odometer increments; the difference is that we cannot change values, only
reorder them. We will use the permutation (6,2,7,5,4,3,0> to develop this approach.
Specifically, we start from the right, and look at the longest decreasing suffix, which is (5,4,3,0)
for our example. We cannot get the next permutation just by modifying this suffix, since it is already
the maximum it can be.
Instead we look at the entry e that appears just before the longest decreasing suffix, which is 1
in this case. (If there's no such element, i.e., the longest decreasing suffix is the entire permutation,
the permutation must be (n - L,n - 2,.. . ,2,1,0), for which there is no next permutation.)
Observe that e must be less than some entries in the suffix (since the entry immediately after e is
greater than e). Intuitively, we should swap e with the smallest entry s in the suffix which is larger
than e so as to minimize the change to the prefix (which is defined to be the part of the sequence
that appears before the suffix).
For our example, e is 1 and s is 3. Swapping s and e results in <6,2,3,5,4,1,,0>.
We are not done yet-the new prefix is the smallest possible for all permutations greater than
the initial permutation, but the new suffix may not be the smallest. We can get the smallest suffix
by sorting the entries in the suffix from smallest to largest. For our working example, this yields
the suffix <0,1.,4,5>.
As an optimization, it is not necessary to call a full blown sorting algorithm on suffix. Since the
suffix was initially decreasing, and aJter replacing s by e it remains decreasing, reversing the suffix
has the effect of sorting it from smallest to largest.
The general algorithm for computing the next permutation is as follows:
(1.) Find k such thatplk) < plk + Ll and entries after index k appear in decreasing order.
(2.) Find the smallest p[] such that p[] > p[k] (such an / must exist since pfkl < pfk + 1)).
(3.) Swap p[] and p[k] (note that the sequence after position k remains in decreasing order).
(4.) Reverse the sequence after position k.
def next-permutation(perm) 
:
# Find the first 
entry from the right that is sraal-ler than
# inmediateTy after it.
inversion-point = len(perm) - 2
rhile (inversion-point >= 0
and permIinversion-point] >= permIinversion_point +
inversion-point -= I
if inversion-point == -1:
return [] 
# pern is the J.ast perrnutation.
the entry
53
1l )
```
