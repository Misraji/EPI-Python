# Exercise 16.12: Find the longest nondecreasing subsequence

**Printed textbook page:** 257. **Reference transcription pages:** 257–258.

> **Unverified OCR transcription:** This section retains the supplied PDF text layer. It is not certified verbatim: code syntax, mathematical symbols, and page boundaries may be corrupted. When two exercises begin on the same page, their excerpts overlap. Do not paste extracted code into a `.py` file without manual verification.

#### Printed page 257 (PDF page 271)

```text
1,6.72 FrNo firs LoNGEST NoNDECREAsTNG suBSEeuENCE
The problem of finding the longest nondecreasing subsequence in a sequence of integers has
implications to many disciplines, including string matching and analyzing card games. As a
concrete instance, the length of a longest nondecreasing subsequence for the array in Figure 16.15
is 4. There are multiple longest nondecreasing subsequenc€s, €.g.2 <o,4,70,14) and (0,2,6,9). Note
that elements of non-decreasing subsequence are not required to immediately follow each other in
the original sequence.
A[0] ,4[U A[2] A[3] Al4l A[5] A[6] AlTl At8] 
Atel
Figure 16.15: An array whose longest nondecreasing subsequences are of length 4.
Write a Program that takes as input an array of numbers and retums the length of a longest
nondecreasing subsequence in the array.
Hfufr Express the longest nondecreasing subsequence ending at an entry in terms of the longest nondecreasing
subsequence appearing in the subarray consisting of preceding elements.
Solution: A brute-force approach would be to enumerate all possible subsequences, testing each
one for being nondecreasing. Since there are 2n subsequences of an array of length n, the time
complexity would be huge. Some heuristic pruning can be applied, but the program grows very
cumbersome.
If we have processed the initial set of entries of the input array, intuitively this should help
us when processing the next entry. For the given example, if we know the lengths of the longest
nondecreasing subsequences that end at lndices O,l, . . .,5 and we want to know the longest nonde-
creasing subsequence that ends at Index 6, we simply look for the longest subsequence ending at an
entry in.4[0,5] whose value is less than or equal to A[61. For Index 6 in the example in Figure 16.15,
there are two such longest subsequences, namely the ones ending at Index 2 and Index 4, both of
which yield nondecreasing subsequences of length 3 ending at A[61.
Generalizing, define t[i] to be the length of the longest nondecreasing subsequence of A that
ends at and includes Index i. As an example, for the array in Figure 16.1s, Ll6) = 3. The longest
nondecreasing subsequence that ends at Index I is of length 1 (if Alil is smaller than all preceding
entries) or has some element, say at Lrdex i, as its penultimate entry, in which case the subsequence
restricted to A[0, j] must be the longest subsequence ending at Index i. Based on this, L[] is either
1 (if A[il is less than all previous entries), or 1 + max{Llj]li < i and A[7] < Ati)\.
We can use this relationship to compute L, recursively or iteratively. If we want the sequence as
well, for each l, in addition to storing the length of the nondecreasing sequence ending at l, we store
the index of the last element of the subsequence that we extended to get the value assigned to L[l].
Applying this algorithm to the example in Figure 16.15, we compute L as follows:
(1.) LI0l = 1 (since there are no entries before Entry 0)
(2.) Ltll = 1 +max(L[O]) = 2 (sinceA[0] < A[1])
(3.) Ll2) = l. + max(L[0]) = 2 (since A[0] s Al2) and A[1] > A[2))
(4.) Lt3l = 1 + max(L\0l,Ll11,Ll2l) = 3 (since A[0],A[1] and Al2l s,4t3l)
(5.) tt4l = l. + max(L[O]) = 2 (since A[0] < Al4), AI1),A[2] and Algl > Al4l)
257
0
8
4
72
2
10
5
74
1
9
```

#### Printed page 258 (PDF page 272)

```text
(6.) Ltsl = 1+ max(L[0],1[1],1[2],Ll4l) = 3 (since Al0l,Al1.),AI21,Al4l <,4[5]andA[3] > A[5])
(7.) Ll61= 1 + max(L[0],L121,L141) = 3 (since Al0l, A121, Al4l < ,4[6] and Al1.l, A131, A[5] > A[6])
(S.) LtTl = 1 + max(L[0],L[1],t[2],Ll3l,Ll47,L[5],t[6]) = 4 (since Al0),Al11Al2l, Al3), Al4l, A151,
A16l < Al71)
(9.) LI8l = 1 + max(L[O]) = 2 (since A[0] < A[8] md Al1lAl27, A[3], Al4l, Al5l, A16), Al71> A[8])
(10.) Ltgl = 1+max(Llol,Ull,Llzl,Ll4l,Ll6l,L[8]) = a(sinceA[0],411'1,Al2l,Al47,A16l,A[8] sA[9]
and A[3], Al5l, Al71> A[9])
Therefore the maximum length of a longest nondecreasing subsequence is 4. There are multiple
longest nondecreasing sequences of length 4, e.g., (0,8,12,14>, <0,2,6,9), <0,4,6,9>.
Here is an iterative implementation of the algorithm.
def tongest-nondecreasing-subsequence-Iength(A) 
:
# max_Tength[i] hoTds the Tength of the Iongest nondecreasing subsequence
# of A[:i + 1].
max-length = [f] " len(A)
for i in range(l, len(A)):
max-Iength[i] = nar(1 + nax(
[max-lengthtj] for j in range(i)
if Atil >= Atjll, default=O), max-lengthliJ)
return nax (max-length)
The time complexity is O(nz) (each LUI takes O(n ) time to compute), and the space complexity is
O(te) (to store L).
Varianft Write a program that takes as input an array of numbers and retums a longest nondecreas-
ing subsequence in the array.
Variant Define a sequence of numbers (ao,at,...,an-t) tobe alternating if ai 1 aial forevenl and
ai) aial forodd L Givenanarrayof numbersA of length n,firrdalongestsubsequence (lo,.. .,ir-)
such that <Alio|,Alii,... ,Ali,r-i) is alternating.
Variant Define a sequence of numbers (ao, at, . . . , an-t) tobe weakly alternating tI no three consecutive
terms in the sequence are increasing or decreasing. Given an array of numbers A of length n, hnd
alongestsubsequence(10,...,i*-t| suchthat <Aliol,Alii,...,Alir-i) isweaklyaltemating.
Varianh Define a sequence of numbers (ao,nt,...,an-t) tobe conaex if ai < ry*, for l' < I <
n - 2. Given an array of numbers A of length n, find a longest subsequence (i0,...,ir-t) such that
<Aliol, Alii, . . ., Alir-i) is convex.
VariankDefineasequenceof numbers (ao,At,...,an-t)tobebitonicif thereexistsksuchthatai 1a;a1,
for0 < I < kand a;) ai4,fork < i <n- 1. Givenanarrayof numbersA of length n,find alongest
subsequence (lo,.. .,i*) such that \A[id,Alii,... ,Alir-i) is bitonic.
Varianh Define a sequence of points in the plane tobe ascending if each point is above and to the
right of the previous point. How would you find a maximum ascending subset of a set of points in
the plane?
Variant: Compute the longest nondecreasing subsequence nO(n logn ) time'
258
```
