# Exercise 16.3: Count the number of ways to traverse a 2D array

**Printed textbook page:** 242. **Reference transcription pages:** 242–243.

> **Unverified OCR transcription:** This section retains the supplied PDF text layer. It is not certified verbatim: code syntax, mathematical symbols, and page boundaries may be corrupted. When two exercises begin on the same page, their excerpts overlap. Do not paste extracted code into a `.py` file without manual verification.

#### Printed page 242 (PDF page 256)

```text
is " gtaa" and s2 is " atc" , then "gattac a" arrd " gtataac" can be formed by interleaving s1 and sz but
" gatacta" cannot. Design an algorithm that takes as input strings s1, s2 irnd f, and determines if f is
an interleaving of s1 and s2.
16.3 CouNr rHE NUMBER oF wAys ro TRAVERsE e 2D lnuv
In this problem you are to count the number of ways of starting at the top-left comer of a2D array
and getting to the bottom-right comer. All moves must either go right or down. For example, we
show three ways in a 5 x 5 2D array in Figure 16.5. (As we will see, there are a total of 70 possible
ways for this example.)
Figure 16.5: Paths through a2D array.
Write a program that counts how many ways you can go from the top-left to the bottom-right in a
2D array.
Hint:Il I > 0 and f > 0, you can get to (1,7) from (i -1, j) or (i,i -l).
Solution: A brute-force approach is to enumerate all possible paths. This can be done using
recursion. Howeve{, there is a combinatorial explosion in the number of paths, which leads to huge
time complexity.
The problem statement asks for the number of paths, so we focus our attention on that. A
key observation is that because paths must advance down or right, the number of ways to get to
the bottom-right entry is the number of ways to get to the entry immediately above it, plus the
number of ways to get to the entry immediately to its left. Let's treat the origin (0,0) as the top-left
entry. Generalizing, the number of ways to get to (i, j) is the number of ways to get to (i - 7, j)
plus the number of ways to get to (i, j- 1). (If i = 0 or 7 = 0, there is only one way to get to
(i, fl from the origin.) This is the basis for a recursive algorithm to count the number of paths.
Implemented naively, the algorithm has exponential time complexity-it repeatedly recurses on
the same locations. The solution is to cache results. For example, the number of ways to get to (1, i)
for the configuration in Figure L6.5 is cached in a matrix as shown in Figure 16.6 on the facing page.
def number-of-ways (n, m) :
def compute-number-of-ways-to-xy(x, 
y)
ifx==Y==0:
return 1
if number-of-waYsIx][Y] == O:
vrays-top = 0 if x == 0 else compute-number-of-lrays-to-xy(x - 1, y)
ways-left = 0 if y == 0 else compute-number-of-ways-to-xy(x, y - 1)
number-of-waysIx][y] = ways-top + ways-left
242
```

#### Printed page 243 (PDF page 257)

```text
return number-of-ways Ix] [y]
number-of-ways = [[0] " m for _ in range(n)l
return conpute_number_of_ways_to_xy(n - 1, m - 1)
The time complexity is O(nm), and the space complexity is O(nm), where r is the number of rows
and m is the number of columns.
1
1
1
1
1
1111
3
5
2
3
4
5
45
Figure 16.6: The number of ways to get from (0,0) to (i, j) tor 0 < i, j < 4.
A more analytical way of solving this problem is to use the fact that each path from (0,0) to
(n-"1.,m - 1) is-a sequence of m* t horizontal steps and n - l verticalsteps. There are ("il;\ =
(#i1= ffisuchpaths.
Varianh Solve the same problem using O(min(n,m)) space.
Variant Solve the same problem in the prcsence of obstacles, specified by a Boolean 2D array, where
the presence of a true value represents an obstacle.
Variant: A fisherman is in a rectangular sea. The value of the fish at point (i, j) inthe sea is specified
by an n x m 2D array A. Write a program that computes the maximum value of fish a fisherman
can catch on a path from the upper leftmost point to the lower rightmost point. The fisherman can
only move down or right, as illustrated in Figure 16.7.
\J
@
Figure 16.7: Alternate paths for a fisherman
fisherman.
Ditferent types of fish have different values, which are known to the
Variant: Solve the same problem when the fisherman can begin and end at any point. He must still
move down or right. (Note that the value at (i, j) may be negative.)
variant A decimal number is a sequence of digits, i.e., a sequence over {0,L,2, . . . ,9l.The sequence
has to be of length 1 or more, and the first element in the sequence cannot be 0. Call a decimal
e
\J
\J
&
oes
243
```
