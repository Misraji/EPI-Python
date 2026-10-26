# Exercise 15.4: Generate the power set

**Printed textbook page:** 224. **Reference transcription pages:** 224–225.

> **Unverified OCR transcription:** This section retains the supplied PDF text layer. It is not certified verbatim: code syntax, mathematical symbols, and page boundaries may be corrupted. When two exercises begin on the same page, their excerpts overlap. Do not paste extracted code into a `.py` file without manual verification.

#### Printed page 224 (PDF page 238)

```text
satisfies the recurrence C(rz) = 1+nC(n - 1) for n )- L, with C(0) = 1. Expanding this, we see
C(n)=1+n+n(n-1)+n(n-1)(n-2)+...ant=nr.(lfn!+11(n-1)!+1,1(n-Z)l+...+1i1!).Thesum
(1 + 1/1! + 712r. + . . . + T lnl) tends to Euler's number e, so C(n) tends to (e - l)nl, i.e., O(nt). The time
complexity T(r) is O(n xnl), since we do O(n) computation per call outside of the recursive calls.
Now we describe a qualitatively different algorithm for this problem. In Solution 5.11 on
Page 53 we showed how to efficiently compute the permutation that follows a given permutation,
e.g., (2,3,1,4) is followed by (2,3,4,1). We can extend that algorithm to solve the current problem.
The idea is that the n distinct entries in the array can be mapped to 1,2,3,. . ., with 1 corresponding
to the smallest entry. For example, if the array is <7 ,3,5>, we first sort it to obtain, <3,5,7). Using the
approach of Solution 5.11 on Page 53, the next array will be (3,7,5), followed by \5,3,7), <5,7,3>,
<7,3,5>, <7,5,3). This is the approach in the program below.
def permutations (A) :
result = []
while True:
result. append(A. copy O )
A = next-permutation(A)
if not A:
break
return result
The time complexity is O(n x n!), since there are n! permutations and we spend O(n) time to store
each one.
Variant Solve Problem 15.3 on Page 222 when the input affay rrtay have duplicates. You
should not repeat any permutations. For example, if A = (2,2,3,0) then the output should
be (2,2,0,3), <2,2,3,0>, <2,0,2,3), <2,0,3,2>, <2,3,2,0>, <2,3,0,2), <0,2,2,3>, <0,2,3,2>, <0,3,2,2>,
<3, 2, 2, 0>, <3, 2, 0, 2>, <3, 0, 2, 2>.
15.4 GsNpnATs rHE PowER sET
The power set of a set S is the set of all subsets of S, includingboth the empty set 0 and S itself. The
power set of {0, 1,21is graphically illustrated in Figure 15.5.
0
{0, u
t1,2)
{p,r,2l
{0,21
Figure 15.5: The power set of {0, 7,2]ris 10, {0}, {1}, l2l,{0,1,},11,21,{0,2]t, {0, 1,2}}
224
```

#### Printed page 225 (PDF page 239)

```text
Write a function that takes as input a set and retums its power set.
Hint:There are 2r subsets for a given set S of size n. There are 2t k-bit words.
Solution: A brute-force way is to compute all subsets U that do not include a particular element
(which could be any single element). Then we compute all subsets V which do include that element.
Each subset set must appear in U or in V, so the final result is jus tt lUV . The construction is recursive,
and the base case is when the input set is empty, in which case we retum {{}}.
As an example, let S = [0,1,,21. Pick any element, e.g., 0. First, we recursively compute all
subsets of 11.,21. To do this, we select 1. This leaves us with {2}. Now we pick 2, and get to a
basecase. Sothesetof subsetsof [2] is{}unionwith{2},i.e.,{{},{2}}. Thesetof subsetsof {1,2}
thenis{{},t2}} unionwith{{1},11,2}1,i.e.,{{},{2),111,{1,2}}. Thesetofsubsetsof {0,1,2}thenis
Ul,{21,{1,),{1.,2]111union with {{0}, {0,2]1,{0,1},{0,1.,2]r]1,i.e., {{}, l2l,[1],{1,2],{Ol,{O,Zl,{0,U,{0,1.,2]1,
def generate-power_set (input_set) :
# Generate aIl subsets rhose intersectjon with input_setfo],
# input_setIto_be_seTected - IJ is exactTy selected_so_far.
def directed_power_set(to_be_selected, selected_so_far) :
if to_be_selected == Ien(input_set) :
power_set . append (list ( selected_so_far) )
return
directed-power-set(to-be_selected + 1, selected_so_far)
# Generate aII subsets that contajn input_setfto_be_selectedl.
directed-power-set(to_be_selected + 1,
selected_so_far + [input_set Ito_be_selected] I )
Power-set = []
directed-power-set(0, tl)
return power_set
The number of recursive calls, C(n) satisfies the recurrence C(n) = 2C(n - 1), which solves to
C(n) = O(2"). Since we spend O(n) time within a call, the time complexity is O(n2n). The space
complexity is O(n2"), since there are 2ft subsets, and the average subset size is nlz. If we just want
to print the subsets, rather than retuming all of them, we simply perform a print instead of adding
the subset to the result, which reduces the space complexity to O(n)-the time complexity remains
the same.
For a given ordering of the elements of S, there exists a one-to-one correspondence between the
2" bit arrays of length n and the set of all subsets of S-the 1s in the n-length bit array o indicate the
elements of S in the subset correspondingtoa. For example, if S = la,b,c,d!,the bit array (1,0,1,1)
denotes the subset {a,c,dl. This observation can be used to derive a nonrecursive algorithm for
enumerating subsets.
In particular, when n is less than or equal to the width of an integer on the architecture (or
language) we are working on, we can enumerate bit arrays by enumerating integers in [0,2n - 1]
and examining the indices of bits set in these integers. These indices are determined by first isolating
the lowest set bit by computing A = x&-(x - 1), which is described on Page 23, andthen getting the
index by computing logy.
def generate-power-set (S)
power-set = []
225
```
