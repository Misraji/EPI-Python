# Exercise 24.19: Find the line through the most points

**Printed textbook page:** 375. **Reference transcription pages:** 375–375.

> **Unverified OCR transcription:** This section retains the supplied PDF text layer. It is not certified verbatim: code syntax, mathematical symbols, and page boundaries may be corrupted. When two exercises begin on the same page, their excerpts overlap. Do not paste extracted code into a `.py` file without manual verification.

#### Printed page 375 (PDF page 389)

```text
By the above argument, after the entire input is processed, C[l] mod 3 will be 1 at exactly those
bit-positions where the input that appears once has a 1.
def find-element-appears_once (A)
counts=[0]*32
for x in A:
for i in range(32):
countsli]+=x61
x)>=1
def handle-negative (n) :
return n if n < 2**31 else n - 2**32
# Any resuTt greater than ot equal to 2**3L nust correspond to an negative
# value.
return handle_negative(suD(l << i for i, c in enunerate(counts) if c :x 3))
The time complexity is O(n) and space complexity is O(1).
Variant: Solve the same problem when one entry appears twice and the rest appear three times
24.79 FrNo rur LrNE THRoucH THE Mosr norwrs $
You are given a set of points in the plane. Each point has integer coordinates. Design an algorithm
for computing a line that contains the maximum number of points in the set.
Hint: A line can be uniquely represented by two numbers.
Solution: This problem may seem daunting at first-there are literally infinitely many lines. The
only lines we care about are those that pass through points in the set, and, more specifically,lines
that pass through at least two points in the set.
A brute-force approach then is to compute all such lines, and for each such line, count exactly
how many points from the set lie on it. We can use a hash table to represent the set of lines. The
set of points corresponding to a line could itself be stored using a hash table. If there are n points
in the set, there are n(n - 1)12 pairs of points. Naively, we would compute the set of lines defined
by pairs of points, and then iterate over all points, checking for each line if that point belongs
to that line. The time complexity is dominated by the iteration over points and lines, which is
O(nxn(n-l)12)=O(n3).
A better approach is to add the pair of points to the set of points on the line they define
immediately. for each pair we have to do a lookup, an insert into the hash table if the defined
line is not already present, and two inserts into the corresponding set of points. The hash table
operations arc O(L) time, leading to an O(nz) tirrre complexity for this part of the computation. The
sPace comPlexity is also O(n2). This is a consequence of the time complexity. At a first glance, it
seems like the sPace complexity might be higheq, since there are O(nz) pairs of lines, and each can
have up to O(n) points. However, there is an inverse relationship between the number of lines and
the number of points per line.
We finish by finding the line with the maximum number of points with a simple iteration through
the hash table searching for the line with the most points in its corresponding set. There are at most
n(n - 7) l2lines, so the iteration takes O(nz) time, yielding an overall time bound of O(nz).
375
```
