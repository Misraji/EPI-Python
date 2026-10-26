"""EPI Python — Exercise 5.19: Rotate a 2D Array

Chapter 5: Arrays
Textbook: pages 64–65 (printed page numbers; problem, figure, hint and
brute force on page 64; in-place program, RotatedMatrix class and variant
on page 65).

PROBLEM (from the textbook)
---------------------------
Context: "Image rotation is a fundamental operation in computer graphics.
Figure 5.4 illustrates the rotation operation on a 2D array representing
a bit-map of an image. Specifically, the image is rotated by 90 degrees
clockwise."
(Figure 5.4: (a) the initial 4 x 4 array with rows 1 2 3 4 / 5 6 7 8 /
9 10 11 12 / 13 14 15 16; (b) the array rotated 90 degrees clockwise,
with rows 13 9 5 1 / 14 10 6 2 / 15 11 7 3 / 16 12 8 4.)

"Write a function that takes as input an n x n 2D array, and rotates the
array by 90 degrees clockwise."

HINT (from the textbook)
------------------------
"Focus on the boundary elements."

SOLUTION DEVELOPMENT (following the textbook)
---------------------------------------------
A little experimentation shows that the ith column of the rotated matrix
is the ith row of the original matrix. For example, the first row of
Figure 5.4(a), <13,14,15,16>, becomes the first column of the rotated
version. [Book text as printed; in Figure 5.4(a), <13,14,15,16> is the
LAST row, and it is the first column of 5.4(b) read top to bottom.]

Brute force: allocate a new n x n array, write the rotation into it
(rows of the original become columns of the new array), then copy the new
array back over the original, since the problem asks for the original to
be updated. Time and additional space are both O(n^2).

Since a new array is not explicitly required, ask whether the rotation
can be done in place with O(1) extra storage:
  - The rotation can be done layer by layer; different layers are
    independent of each other.
  - Within a layer, elements can be exchanged in groups of four. In the
    4 x 4 example: send 1 to 4's location, 4 to 16's, 16 to 13's and 13
    to 1's; then 2 to 8's location, 8 to 15's, 15 to 9's and 9 to 2's;
    and so on.
The program works from the outermost layer inward, performing these
four-way exchanges within each layer. It is implemented here as
`rotate_matrix`.

The book also prints a class `RotatedMatrix` (see POST-SOLUTION
DISCUSSION); it is not implemented in this file.

ADDITIONAL EXAMPLES (added for learning; not printed in this exercise)
---------------------------------------------------------------------
    [[1, 2], [3, 4]] -> [[3, 1], [4, 2]]
"""



# `matrix: list[list[int]]` (a list of rows of ints) and the return
# annotation are type hints; Python does not enforce them at run time.
# Built-in generics like list[...] need Python 3.9 or newer.
# Documentation: https://docs.python.org/3/library/typing.html
def rotate_matrix(matrix: list[list[int]]) -> list[list[int]]:
    """Rotate a square image matrix 90 degrees clockwise, in place.

    This is the textbook's `rotate_matrix(square_matrix)` program, written
    with explicit layer bounds instead of the book's `~` indexing. The
    same list object is modified and returned.
    """
    n = len(matrix)

    # any(...) is True if some row's length differs from n, i.e. the
    # matrix is not square. This check is not in the book.
    # Documentation: https://docs.python.org/3/library/functions.html#any
    if any(len(row) != n for row in matrix):
        raise ValueError("Rotation requires an n x n square matrix")

    # `n // 2` (floor division) is the number of layers that need moving;
    # for odd n the centre element stays where it is.
    for layer in range(n // 2):

        # lo/hi are the first and last row (and column) index of this
        # layer, set by tuple unpacking.
        lo, hi = layer, n - 1 - layer

        # Each j handles one group of four cells, one on each side of the
        # layer. hi - lo groups cover the whole layer (the corners are
        # included once, at j = 0).
        for j in range(hi - lo):

            # Four-way exchange using one temporary: save the top cell,
            # then move left -> top, bottom -> left, right -> bottom, and
            # finally the saved top -> right. In clockwise rotation each
            # element moves one side clockwise (e.g. 1 goes to 4's spot).
            top = matrix[lo][lo + j]
            matrix[lo][lo + j] = matrix[hi - j][lo]
            matrix[hi - j][lo] = matrix[hi][hi - j]
            matrix[hi][hi - j] = matrix[lo + j][hi]
            matrix[lo + j][hi] = top
    return matrix


# TEXTBOOK POST-SOLUTION DISCUSSION (page 65)
# ------------------------------------------
# The in-place program has time complexity O(n^2) and additional space
# complexity O(1).
#
# The book then notes that the EFFECT of a rotation can be obtained with
# O(1) space and O(1) time, with some limitations: return an object r
# that wraps (composes) the original matrix A. Reading the element at
# indices i and j of r becomes a read of A at index [n - 1 - j][i];
# writes are translated the same way. Creating r takes constant time
# (it only stores a reference to A), and reads and writes cost the same as
# before. The approach breaks down when other clients use the original
# A, because writes through r change A. Even if A itself is never written,
# if methods called on the stored objects change their state, the system
# becomes corrupted. Copy-on-write can be used to solve these issues.
# The book prints this idea as `class RotatedMatrix` with methods
# `__init__(self, square_matrix)`, `read_entry(self, i, j)` and
# `write_entry(self, i, j, v)`, both using `[~j][i]` indexing (book
# comment: "Note that A[~i] for i in [0, len(A) - 1] is A[-(i + 1)].").
#
# VARIANTS
# --------
# Variant (stated in the book; no solution given): Implement an algorithm
# to reflect A, assumed to be an n x n 2D array, about the horizontal axis
# of symmetry. Repeat the same for reflections about the vertical axis,
# the diagonal from top-left to bottom-right, and the diagonal from
# top-right to bottom-left.


# TEXTBOOK CODE COMPARISON
# ------------------------
# - Book: `def rotate_matrix(square_matrix)` with
#   `matrix_size = len(square_matrix) - 1`, loops
#   `for i in range(len(square_matrix) // 2): for j in range(i,
#   matrix_size - i):` and ONE simultaneous tuple assignment of four
#   cells using the `~` operator (`~i` == `-(i + 1)`, i.e. counting from
#   the end; book comment: "Perform a 4-way exchange. Note that A[~i] for
#   i in [0, len(A) - 1] is A[-(i + 1)]."). Book returns None.
# - File: parameter `matrix`, type hints, square-shape ValueError check,
#   explicit `lo`/`hi` bounds with j running 0..hi-lo-1 (offset form),
#   positive indices instead of `~`, a temporary variable `top` and four
#   sequential assignments instead of one tuple assignment, and
#   `return matrix`.
# - MISSING FROM THE FILE: the book's `class RotatedMatrix` (constant-time
#   rotated view) is not implemented.


# Python executes this block only when this source file is run directly.
# When pytest imports the file, this block is skipped automatically.
# Documentation: https://docs.python.org/3/library/__main__.html
if __name__ == "__main__":

    # Added 2 x 2 example: rotating [[1, 2], [3, 4]] clockwise gives
    # [[3, 1], [4, 2]].
    m = [[1, 2], [3, 4]]

    # print() with several arguments separates them with a space.
    print("rotated matrix:", rotate_matrix(m))

    # `assert` stops the program with an AssertionError if the condition
    # is false. Checking `m` itself (not the return value) shows that the
    # rotation happened in place. pytest provides the more thorough
    # automated verification.
    assert m == [[3, 1], [4, 2]]
