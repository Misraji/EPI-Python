# Exercise 5.19: Rotate a 2D array

**Printed textbook page:** 64. **Reference transcription pages:** 64–64.

> **Unverified OCR transcription:** This section retains the supplied PDF text layer. It is not certified verbatim: code syntax, mathematical symbols, and page boundaries may be corrupted. When two exercises begin on the same page, their excerpts overlap. Do not paste extracted code into a `.py` file without manual verification.

#### Printed page 64 (PDF page 78)

```text
<1,2,3, . . . ,d2>. For example , if d = 3, the result should be
Variant: Given a sequence of integers P, compute a 2D array A whose spiral order is P. (Assume
the size of P is n2 for some integer n.)
Variant: Write a program to enumerate the hrst n pairs of integers (a,b) tn spiral order,
starting from (0,0) followed by (1,0). For example, if n = 10, your output should be
(0, 0), (1,0), (1, -1), (0, -1), (-1, -1), (-1,0), (-1,1), (0, 1), (1, 1), (2,1).
Variant: Compute the spiral order for ar.mxn2D array A.
VarianL Compute the last element in spiral order for an m x n 2D aruay A in O(1) time.
Variant Compute the kth element in spiral order for an m x n 2D array A in O(1) time.
5.19 Rorerr e 2D annev
Image rotation is a fundamental operation in computer graphics. Figure 5.4 illustrates the rotation
operation on a 2D array representing a bit-map of an image. Specifically, the image is rotated by
90 degrees clockwise.
^li il
1234
5678
9101112
13 't4 15 16
13951
L41062
15t't73
161284
(a) lnitial 4x42D array. 
(b) Anay rotated by 90 degrees clockwise.
Figure 5.41 Example of 2D array rotation.
Write a function that takes as input an n x n 2D array, and rotates the array by 90 degrees clockwise.
Hint: Focus on the boundary elements.
Solution: With a little experimentation, it is easy to see that lth column of the rotated matrix is the
Ith row of the original matrix. For example, the first row, (13,1"4,15,L6) of the initial array in 5.4
becomes the first column in the rotated version. Therefore, a brute-force approach is to allocate a
new rx x n 2D array, write the rotation to it (writing rows of the original matrix into the columns of
the new matrix), and then copying the new array back to the original one. The last step is needed
since the problem says to update the original array. The time and additional space complexity are
bothO(n2).
64
```
