# Exercise 15.5: Generate all subsets of size k

**Printed textbook page:** 226. **Reference transcription pages:** 226–226.

> **Unverified OCR transcription:** This section retains the supplied PDF text layer. It is not certified verbatim: code syntax, mathematical symbols, and page boundaries may be corrupted. When two exercises begin on the same page, their excerpts overlap. Do not paste extracted code into a `.py` file without manual verification.

#### Printed page 226 (PDF page 240)

```text
for int-for-subset in range(1 << Ien(S)):
bit-array = int-for-subset
subset = []
while bit-array:
subset. append(int(nath. log2 (bit-array & -(bit-array -
bit-array &= bit-array - 1
power-set, append ( subset)
return power_set
1))))
Since each set takes O(n) time to compute, the time complexiry is O(nZ").In practice, this approach
is very fast. Furthermore, its space complexity is O(n) when we want to just enumerate subsets,
e.g., to print them, rather that to return all the subsets.
Variant: Solve this problem when the input array may have duplicates, i.e., denotes a multi-
set. You should not repeat any multiset. For example, if A = <'1,,2,3,2>, then you should retum
({),tt), <z>,<g>,<1,,2),<L,g>,<2,2>,<2,g>,<1,2,2),<1.,2,g),<2,2,g),<1.,2,2,g>).
15.5 GuNpne'rs ALL suBSETs or slzs k
There are a number of testing applications in which it is required to compute all subsets of a given
size for a specified set.
Write a program which computes all size k subsets of 11,,2,...,?tl, where k and n are Pto-
gram inputs. For example, iI k = 2 and n = 5, then the result is the following:
ll1, 2l, 11., 31, {1, 41, $, 5}, [2, 31, {2, 4}, {2, 51, 13, 41, {3, 5l,, 14, 5}l
Hln f: Think of the right function signature.
Solution: One brute-force approach is to compute all subsets of {1,2,...,fl\, and then restrict the
result to subsets of size k. A convenient aspect of this approach is that we can use Solution 15.4 on
the preceding page to compute all subsets. The time complexity is O(n2"), regardless of k. When
k is much smaller thann, or nearly equal to n, it ends up computing many subsets which cannot
possibly be of the right size.
To gain efficiency, we use a more focused approach. In particular, we can make nice use of case
analysis. There are two possibilities for a subset-it does not contain 1, or it does contain 1. In the
firstcase,weretumallsubsetsofsizekof{2,3,...,n\;inthesecondcase,wecomputeallk-lsized
subsets of 12,3,. . . , n) and add 1 to each of them.
For example, lf n = 4 and k = 2, then we compute all subsets of size 2 from {2,3,41, and all
subsets of size 1 from {2,3,41. We add 1 to each of the latter, and the result is the union of the two
sets of subsets, i.e., l{2,3J, {2,41, {3,4}l u {l'1.,21, U,3}, {1,4}}.
def combinations (n, k) :
def directed-combinations (offset, partial-combination)
if len(Partial-combination) == k:
result . append (list (partial-combination) )
return
# Generate renaining combinations over {offset,
# num-renaining.
num-remaining = k - len(partial-combination)
226
,n-1]ofsize
```
