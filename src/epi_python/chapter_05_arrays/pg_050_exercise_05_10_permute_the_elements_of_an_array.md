# Exercise 5.10: Permute the elements of an array

**Printed textbook page:** 50. **Reference transcription pages:** 50–51.

> **Unverified OCR transcription:** This section retains the supplied PDF text layer. It is not certified verbatim: code syntax, mathematical symbols, and page boundaries may be corrupted. When two exercises begin on the same page, their excerpts overlap. Do not paste extracted code into a `.py` file without manual verification.

#### Printed page 50 (PDF page 64)

```text
is-prine = [False, FaIse] + [True] " (n - 1)
forpinrange(2,n+1):
if is-prine [p] :
primes. append (p)
# Sieve p's nu-ltiples.
for i in range(p, n + 1, p):
is-PrimeIi] = False
return primes
We justified the sifting approach over the trial-division algorithm on heuristic grounds. The
time to sift out the multiples of p is proportional to nlp, so the overall time complexity is O(nl2 +
n13 + n15 + n17 + nl11 +... ). Although not obvious, this sum asymptotically tends to nloglogn,
yielding anO(n loglogn) time bound. The space complexity is dominated by the storage for P, i.e.,
o(n).
The bor-rnd we gave for the trial-division approach, namely O(n3l2;, is based on an O( 1fi) bound
for each individual test. Since most numbers are not prime, the actual time complexity of trial-
division is actually lower on average, since the test frequently early-returns false. It is known that
the time complexify of the trial-division approach is O@3lz l(logn)z), so sieving is in fact superior
to trial-division.
We can improve runtime by sieving p's multiples from p2 instead of p, since all numbers of the
formkp, where k < phave already been sieved out. The storage can be reduced by ignoring even
numbers. The code below reflects these optimizations.
# Given n, return all prines up to and including n.
def generate-primes (n) :
if n < 2:
return []
size=(n-3)//2+t
primes = [2] # Stores the prizes fron 7 to n.
# is-prineliJ represents (2i + 3) is prine or not.
# InitialTy set each to true. Then use sieving to elininate nonprines.
is-prime=[true]tsize
for i in range(size):
if is-prime Ii] :
P=i+2+3
prines . append (p)
# Sieving fron p^2, where p^2 = (4i^2 + 12i + 9). The index in is-prirne
# is (2i^2 + 6i + 3) because is*prinefi] represents 2i + 3.
#
# Note that we need to use Tong for j because p^2 night overfTow.
for j in range(2 * i**2 + 6 * i + 3, size, p):
is-PrimeIj] = FaIse
return primes
The asymptotic time and space complexity are the same as that for the basic sieving approach.
5.10 PrnNrurs rHE ELEMENTS oF AN ARRAv
A permutation is a rearrangement of members of a sequence into a new sequence. For example,
there are 24 permutations of (a,b,c,d); some of these are (b,a,d,c),(d,a,b,c), and (a,d,b,cl.
50
```

#### Printed page 51 (PDF page 65)

```text
A permutation can be specified by an array P, where P[] represents the location of the element
at i in the permutation. For example, the aray (2,0,1,3) represents the permutation that maps the
element at location 0 to location 2, the element at location 1 to location 0, the element at location 2
to location 1, and keep the element at location 3 unchanged. A permutation can be applied to an
array to reorder the array. For example, the permutation (2,0, 1,3) applied to A = (a,b,c,d) yields
the array \b,c,a,d).
Given an arrayA of n elements and a permutation P, apply P to A.
Hint: Any permutation can be viewed as a set of cyclic permutations. For an element in a cycle, how would
you identify if it has been permuted?
Solution: It is simple to apply a permutation-array to a given array if additional storage is available
to write the resulting array. We allocate a new array B of the same length, set B[P[i]l = A[i] for each
l, and then copy B to A. The time complexity is O(n), and the additional space complexity is O(n).
A key insight to improving space complexity is to decompose permutations into simpler struc-
tures which can be processed incrementally. For example, consider the permutation (3,2,1,0). To
apply it to an array / = (a,b,c,6), we move the element at index 0 (a) to index 3 and the element
already at index 3 (5) to index 0. Continuing, we move the element at index 1 (b) to index 2 and
the element already at index 2 (c) to index 1. Now all elements have been moved according to the
permutation, and the result is (6,c,b,a).
This example generalizes: every permutation can be represented by a collection of independent
permutations, each of which is cyclic, that is, it moves all elements by a fixed offret, wrapping
around.
This is significant, because a single cyclic permutation can be performed one element at a time,
i.e., with constant additional storage. Consequently, if the permutation is described as a set of
cyclic permutations, it can easily be applied using a constant amount of additional storage by
applying each cyclic permutation one-at-a-time. Therefore, we want to identify the disjoint cycles
that constitute the permutation.
To find and apply the cycle that includes entry I we just keep going forward (from I to PU]) till
we get back to l. After we are done with that cycle, we need to find another cycle that has not yet
been applied. It is trivial to do this by storing a Boolean for each array element.
One way to perform this without explicitly using additional O(n) storage is to use the sign bit
in the entries in the permutation-array. Specifically, we subtract n from P[] after applying it. This
means that if an entry in P[r] is negative, we have performed the corresponding move.
For example, to apply <3,7,2,0>, we begin with the first entry, 3. We move A[0] to A[3], first
saving the original A[3]. We update the permutation to <-1.,1,2,0>. We move.4[3] to A[0]. Since
P[0] is negative we know we are done with the cycle starting at 0. We also update the permutation
to (-1,1.,2,-41. Now we examine P[1]. Since it is not negative, it means the cycle it belongs to
cannot have been applied. We continue as before.
def apply-pernutation (perm , A) :
for i in range(Ien(A)):
# Check if the element at index i has not been noved by checking if
# pern[i] is nonnegative.
nert = i
rhile pern[nert] >= 0:
51
```
