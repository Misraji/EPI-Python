# Chapter 16: Dynamic Programming

**Starts at printed page 234.** [Repository overview](../../../README.md)

**Source:** user-supplied EPI Python PDF (2016/2017 edition). **Transcription warning:** PDF text extraction contains OCR errors, especially in code. Consult the original PDF for ambiguous expressions and diagrams.

## Original chapter introduction (unverified PDF text layer)

### Printed page 234

```text
CHaprsn
Dynamic Programming
The important fact to obsense is thnt we hnoe attempted to solae a maximization
problem inoolving a particular oalue of x and a particular oalue of N by first
solaing the ganerul problem inooluing an arbitrary oalue of x anil an arbitrary
oalue of N.
- 
" Dynamic P ro gramming,"
R. E. Brrrr"rlN, 1957
DP is a general technique for solving optimization, search, and counting problems that can be
decomposed into subproblems. You should consider using DP whenever you have to make choices
to arrive at the solution, specifically, when the solution relates to subproblems.
Like divide-and-conquet DP solves the problem by combining the solutions of multiple smaller
problems, but what makes DP different is that the same subproblem may reoccur. Therefore, a
key to making DP efficient is caching the results of intermediate computations. Problems whose
solutions use DP are a popular choice for hard interview questions.
To illustrate the idea underlying DR consider the problem of computing Fibonacci numbers.
The first two Fibonacci numbers are 0 and 1. Successive numbers are the sums of the two previous
numbers. The first few Fibonacci numbers ate 0,1,L,2,3,5,8,13,2L,.... The Fibonacci numbers
arise in many diverse applications-biology, data structure analysis, and parallel computing are
some examples.
Mathematically,thenthFibonaccinumberF(rz)isgivenbytheequationF(r) =F(n-7)+F(n-2),
with F(0) = 0 and F(1) = L. A function to compute F(z) that recursively invokes itself has a time
complexity that is exponential in n. This is because the recursive function computes some F(l)s
repeatedly. Figure 16.1 on the next page graphically illustrates how the function is repeatedly
called with the same arguments.
Caching intermediate results makes the time complexity for computing the nth Fibonacci number
linear in n, albeit at the expense of O(rz) storage.
def fibonacci (n, cache={}) :
if n <= l:
return n
elif n not in cache:
cacheIn] = fibonacci(n - 1) + fibonacci(n - 2)
return cache In]
Minimizing cache space is a recurring theme in DP. Now we show a proglam that computes
F(n) in O(n) time and O(1) space. Conceptually, in contrast to the above program/ this program
iteratively fills in the cache in a bottom-up fashion, which allows it to reuse cache storage to reduce
the space complexity of the cache.
def fibonacci (n)
234
```

### Printed page 235

```text
F(5), 1
F(4),2
F(3),11
F(r),7
F(0),5
F(3).3
F(2),4
r(1),s
F(1),e
F(2),8
F(0), 10
F(1),13
F(2),12
F(0),14
F(1),15
Figure 16.1 : Tree of recursive calls when naively computing the Sth Fibonacci number, F(5). Each node is a call: F(x)
indicates a call with argument r, and the italicized numbers on the right are the sequence in which calls take place. The
children of a node are the subcalls made by that call. Note how there are 2 calls to F(3), and 3 calls to each of F(2),
r(1), and F(0).
ifn<=1
retErn n
f-minus-Z, f-minus-l = 0, 1
for - in range(l, n):
f = f-minus-2 + f-minus-l
f-minus_2 , f-minus-l = f_minus_l, f
return f-ninus_1
The key to solving a DP problem efficiently is finding a way to break the problem into subprob-
lems such that
o the original problem can be solved relatively easily once solutions to the subproblems are
available, and
. these subproblem solutions are cached.
Usually, but not always, the subproblems are easy to identify.
Here is a more sophisticated application of DP. Consider the following problem: find the
maximum sum over all subarrays of a given array of integer. As a concrete example, the maximum
subarray for the array in Figure 15.2 starts at index 0 and ends at index 3.
904
40
523
t2
-J55
-385
-124
481
-31
1tol
A[1] Al2l A[3] Al4l A[s] A16l AlTl 
A[8]
Flgure 16.2: An array with a maximum subarray sum of 1479.
The brute-force algorithm, which computes each subarray sum, has O(n3) time complexity-
there are $ 
subarrays, and each subarray sum takes O(n) time to compute. The brute-force
algorithm can be improved to O(nz), at the cost of O(n) additional storage, by first computing
s[k] = I A[0,k) for all k. The sum for A[], i] is then sti] - st, - 1.1, where s[-1] is taken to be 0.
Hereisanaturaldivide-and-conqueralgorithm. Takem = lf .ltobethemiddleindexof A. Solve
the problem for the subarrays L = Al},m) arrd R = Alm + 1.,n - 1]. In addition to the answers for
each, we also retum the maximum subarray sum / for a subarray ending at the last entry in L, and
the maximum subarray sum r for a subarray starting at the first entry of R. The maximum subarray
235
```
