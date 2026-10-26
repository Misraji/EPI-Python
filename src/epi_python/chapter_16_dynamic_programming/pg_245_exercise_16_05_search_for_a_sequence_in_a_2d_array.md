# Exercise 16.5: Search for a sequence in a 2D array

**Printed textbook page:** 245. **Reference transcription pages:** 245–245.

> **Unverified OCR transcription:** This section retains the supplied PDF text layer. It is not certified verbatim: code syntax, mathematical symbols, and page boundaries may be corrupted. When two exercises begin on the same page, their excerpts overlap. Do not paste extracted code into a `.py` file without manual verification.

#### Printed page 245 (PDF page 259)

```text
def compute-x_choose_y(*, y)
if y in (0, x):
return I
if x-choose-y[x][y] == O:
without-y = compute-x-choose-y(x - f, y)
with-y = compute-x-choose-y(x - 1, y - 1)
x-choose-ylxltyl = without-y + with-y
return x_choose_y txl tyl
x-choose-y = [[0] o (k + 1) for _ in range(n + 1)l
return compute_x_choose_y(n, k)
The number of subproblems is O(nk) and once ('o1) ana (-l) are known, (X) "u" be computed in
O(1) time, yielding an O(nk) time complexity, The space complexity is also O(nk); it can easily be
reduced to O(k).
16.5 Srencn FoR A sEeuENCE rN A 2D anney
Suppose you are given a 2D array of integers (the "grid"), and a 1D array of integers (the "pattern").
We say the pattern occurs in the grid if it is possible to start from some entry in the grid and traverse
adjacent entries in the order specified by the pattem till all entries in the pattern have been visited.
The entries adjacent to an entry are the ones directly above, below, to the left, and to the right,
assuming they exist. For example, the entries adjacent to (3,4) are (3,3), (3,5), (2,4) and (4,4). It is
acceptable to visit an entry in the grid more than once.
As an example, if the grid is
and the pattern is (1,3,4,6), then the pattem occurs in the grid--consider the entries
((0,0), (1,0), (1, 1),(2,1)). However, <7,2,3,4) does not occur in the grid.
Write a Program that takes as arguments a 2D array and a lD array, and checks whether the 1D
array occurs in the 2D array.
Hint: Staft with length 1 prefixes of the 1D array, then move on to length 2,3,.. . prefixes.
Solution: A brute-force approach might be to enumerate all 1D subarrays of the 2D subarray. This
has very high time complexity, since there are many possible subarrays. Its inefficiency stems from
not using the target 1D subarray to guide the search.
Let the 2D aray be A, and the 1D array be S. Here is a guided way to search for matches. Let's
say we have a suffix of S to match, and a starting point to match from. If the suffix is empty, we
are done. Otherwise, for the suffix to occur from the starting point, the first entry of the suffix must
equal the entry at the starting point, and the remainder of the suffix must occur starting at a point
adjacent to the starting point.
For example, when searching for (1,,3,4,6) starting at (0,0), since we match 1 with A[0][0], we
would continue searching for (3,4,6) from (0,1) (which fails immediately, since At0]tU * 3) and
from (1,0), Since A[0][1] = 3, we would continue searching for (4,6) from (0,1)'s neighbors, i.e.,
from (0,0) (which fails immediately), then from (1,1) (which eventually leads to success).
J
5
7
2
4
6
245
```
