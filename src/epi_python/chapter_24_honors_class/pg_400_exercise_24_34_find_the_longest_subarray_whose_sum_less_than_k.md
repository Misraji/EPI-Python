# Exercise 24.34: Find the longest subarray whose sum less than k

**Printed textbook page:** 400. **Reference transcription pages:** 400–401.

> **Unverified OCR transcription:** This section retains the supplied PDF text layer. It is not certified verbatim: code syntax, mathematical symbols, and page boundaries may be corrupted. When two exercises begin on the same page, their excerpts overlap. Do not paste extracted code into a `.py` file without manual verification.

#### Printed page 400 (PDF page 414)

```text
def search-frequent-items (k, stream) :
table = collections . Counter o
n = 0 # Count the nunber of strings
for buf in stream:
tableIbuf] += I
n+= 1
# Detecting k jtems in table, at ]east one of thern nust have exactTy
# one in it. 
We rj]l 
discard those k items by one for each.
if len(tabIe) == k'
for it in table:
table Iit] 
-= 1
table = +table # renove a7l zero values
# Resets tabTe for the folTowing counting
for it in table:
tablelitl 
= 0
# Resets the stream and read it again.
# Counts the occurrence of each candidate word
for buf in stream:
if buf in table:
table Ibuf] += 1
# Selects the word which occurs > n / k times.
return [it for it, value in table.itemso if value > n / k]
The code may appear to take O(nD nrne since the inner loop may take k steps (decrementing
count for all k entries) and the outer loop is called n tirnes. However each word in the sequence can
be erased only once, so the total time spent erasin g is O(n) and the rest of the steps inside the outer
loop run in O(1) time.
The first step yields a set S of not more than k words; set S is a superset of the words that occur
greater than f times. To get the exact set, we need to make another Pass over the sequence and
count the number of times each word in S actually occurs. We retum the words in S which occur
more than f times.
24.34 FrNn rHr LoNGEST suBARRAy wHosE suna < k $
Here we consider finding the longest subarray subject to a constraint on the subarray sum. For
example, for the array in Figure 24,11 on the next page, the longest subarray whose subarray sum
is no more than 184 is A[3,61.
437
-15
639
342
-14
5b5
-924
635
167
-70
Atol A[1] Al2l Al3) A141 A[s] A16l Aln 
A[8]
Figure 24.11: An array for the longest subarray whose sum < k problem.
400
A[e]
```

#### Printed page 401 (PDF page 415)

```text
Design an algorithm that takes as input an array A of n numbers and a key k, and retums the length
of a longest subarray of A for which the subarray sum is less than or equal to k.
Hint: When can you be sure that an index i cannot be the starting point of a subarray with the desired property,
without looking past i?
Solution: The brute-force solution entails computing L!r=,apr1,i.e., the sum of the element n Ali, jl,
forall0 < i < i Sn- 1, where n isthe lengthof A. LetPbe theprefixsumarrayfor A,i.e.,
Plil = L:k=oA[k]; P can be computed in a single iteration over z4 n O(n) time. Note that the sum
of the elements in the subarray Ali, jl is PIjl - Pli - 1l (for convenience, take p[-1] = 0). The time
complexity of the brute-force solutionis O(nz), and the additional space complexity is O(n) (the size
of P).
The trick to improving the time complexity to O(n) comes from the following observation.
Suppose u < o and Plul > P[u]. Then z will never be the ending point of a solution. The reason is
that for any w < u, Alw,al is longer than Altt,z] and if Afw,u) satisfies the sum constraint, so must
Alw,ul. This motivates the definition of the array Q: set QUI = min(p[l], el, + 1l) for i < n - 1., and,
Qln - 11= Pln - 1).
Let a < b be indices of elements in A. Define Mr,6 to be the minimum possible sum of a subarray
begiruring ataandextendingtoborbeyond. NotethatMe,6 = Qlbl,andMo,6= elbl-pla-1l,when
a > 0' If Mn,6 > k,no subarray starting at a that includes b can satisfy the sum constraint, so we can
incrementa. IfMn,6<k,thenweareassuredthereexistsasubarrayoflengthb-a+lsatisfying
the sum constraint, so we compare the length of the longest subarray satisfying the sum constraint
identified so far to b - a + 1 and conditionally update it. Consequently, we can increment b.
Suppose we initialize a and b to 0 and iteratively perform the increments to a and b described
above until b = n. Then we will discover the length of a maximum length subarray that satisfies the
sum constraint. We justify this claim after presenting an implementation of these ideas below.
de:f find-Iongest-subarray_less_equal_k(A, k) :
# BuiTds the prefix sur accordjng to A.
prefix_sum = list(itertools. 
accunulate(A))
# EarTy returns if the sun of .A is snaller than or equal to k
if prefix-sum[-1] <= k:
return len(A)
# Builds min_prefix_sun.
min-prefix-sum = Iist(
reversed (
functools.reduce(Ianbda s, v: s + [nin(v, st-1])1,
reversed(prefix_sum[: -1]), Iprefix_sumt-1]l)))
a=b=max_Iength=0
rhile a < len(A) and b < Ien(A):
min_curr_sus = (min_prefix_sum[b] - prefix_sumIa - 1]
if a > 0 else min_prefix_sum[b])
if min-curr-sum <= k:
curr*Iength=b-a+1
if curr_length > max_Iength:
max_length = curr_length
b+= 1
else: # nin_curr_sunr > k.
401
```
