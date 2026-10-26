"""EPI Python — Exercise 5.18: Compute the Spiral Ordering of a 2D Array

Chapter 5: Arrays
Textbook: pages 61–64 (printed page numbers; introduced at the bottom of
page 61, problem and first program on page 62, second program on page 63,
variants finishing at the top of page 64).

PROBLEM (from the textbook)
---------------------------
Context: "A 2D array can be written as a sequence in several orders—the
most natural ones being row-by-row or column-by-column. In this problem we
explore the problem of writing the 2D array in spiral order. For example,
the spiral ordering for the 2D array in Figure 5.3(a) on the following
page is <1,2,3,6,9,8,7,4,5>. For Figure 5.3(b) on the next page, the
spiral ordering is <1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10>."

(Figure 5.3: (a) the 3 x 3 array with rows 1 2 3 / 4 5 6 / 7 8 9;
(b) the 4 x 4 array with rows 1 2 3 4 / 5 6 7 8 / 9 10 11 12 /
13 14 15 16. Row ids R0, R1, ... and column ids C0, C1, ... label the
matrix; the value 1 is at entry R0, C0.)

"Write a program which takes an n x n 2D array and returns the spiral
ordering of the array."

HINT (from the textbook)
------------------------
"Use case analysis and divide-and-conquer."

SOLUTION DEVELOPMENT (following the textbook)
---------------------------------------------
Work from the outside toward the centre.

Naive boundary walk: add the whole first row (n elements), then the
remaining n - 1 elements of the last column, then the remaining n - 1 of
the last row, then the remaining n - 2 of the first column. Because the
four pieces have different lengths, the code is hard to get right.

Uniform boundary walk: add the first n - 1 elements of the first row;
then the first n - 1 elements of the last column; then the last n - 1
elements of the last row, in reverse; finally the last n - 1 elements of
the first column, in reverse. What remains is an (n - 2) x (n - 2) array
to be listed in spiral order, so iterate over the layers n x n,
(n - 2) x (n - 2), (n - 4) x (n - 4), .... A matrix of odd dimension
has a corner case at its centre.

Book examples:
  - 3 x 3 (Figure 5.3(a)): add 1,2 (first two of the first row), then 3,6
    (first two of the last column), then 9,8 (last two of the last row),
    then 7,4 (last two of the first column). Left with the 1 x 1 array
    holding 5; after it, everything is processed.
  - 4 x 4 (Figure 5.3(b)): add 1,2,3, then 4,8,12, then 16,15,14, then
    13,9,5. Left with a 2 x 2 matrix, handled the same way in the order
    6,7,11,10.

The book prints this layer-by-layer program (`matrix_in_spiral_order`
with an inner `matrix_layer_in_clockwise(offset)`), then a second,
single-loop program (see the POST-SOLUTION DISCUSSION). NEITHER book
program is present in this file: `matrix_in_spiral_order` here is a
repository implementation using four shrinking boundaries (top, bottom,
left, right); see TEXTBOOK CODE COMPARISON.

ADDITIONAL EXAMPLES (added for learning; not printed in this exercise)
---------------------------------------------------------------------
    []                         -> []
    [[1, 2, 3], [4, 5, 6]]     -> [1, 2, 3, 6, 5, 4]  (rectangular input
                                  is also accepted by this file's code)
The 3 x 3 example in `__main__` is the book's Figure 5.3(a).
"""



# `matrix: list[list[int]]` (a list of rows, each a list of ints) and
# `-> list[int]` are type hints. Python does not enforce them at run time.
# Built-in generics like list[...] need Python 3.9 or newer.
# Documentation: https://docs.python.org/3/library/typing.html
def matrix_in_spiral_order(matrix: list[list[int]]) -> list[int]:
    """Return clockwise perimeter rings from a rectangular matrix.

    Repository implementation (shrinking boundaries). It shares the book's
    function name but is neither of the book's two printed programs. It
    also accepts m x n (non-square) matrices, which the book leaves as a
    variant.
    """

    # An empty list is falsy: nothing to output.
    if not matrix:
        return []

    # any(...) is True if some item of the generator expression is true:
    # here "some row has a different length from row 0".
    # Documentation: https://docs.python.org/3/library/functions.html#any
    if any(len(row) != len(matrix[0]) for row in matrix):
        raise ValueError("All matrix rows must be same length")

    # `result: list[int] = []` is a variable annotation (a type hint on a
    # local variable; not enforced).
    result: list[int] = []

    # The unvisited part of the matrix is rows top..bottom and columns
    # left..right (inclusive). Tuple unpacking sets two names at once.
    top, bottom = 0, len(matrix) - 1
    left, right = 0, len(matrix[0]) - 1
    while top <= bottom and left <= right:

        # Top row, left to right. `row[left:right + 1]` is a slice (a new
        # list with columns left..right); list.extend appends all of its
        # items to `result`.
        # Documentation: https://docs.python.org/3/tutorial/datastructures.html
        result.extend(matrix[top][left:right + 1])
        top += 1

        # Right column, top to bottom.
        for r in range(top, bottom + 1):
            result.append(matrix[r][right])
        right -= 1

        # Bottom row, right to left, if a row is left. reversed() returns
        # an iterator over the slice from its last item to its first, and
        # extend() consumes it.
        # Documentation: https://docs.python.org/3/library/functions.html#reversed
        if top <= bottom:
            result.extend(reversed(matrix[bottom][left:right + 1]))
            bottom -= 1

        # Left column, bottom to top, if a column is left.
        # `range(bottom, top - 1, -1)` counts down from bottom to top
        # (stop is exclusive, step -1).
        if left <= right:
            for r in range(bottom, top - 1, -1):
                result.append(matrix[r][left])
            left += 1
    return result


# TEXTBOOK POST-SOLUTION DISCUSSION (pages 63–64)
# ----------------------------------------------
# The layer-by-layer program runs in O(n^2) time.
#
# That solution uses four nearly identical iterations. The book then gives
# a solution with a single iteration. Start at R0,C0 and visit
# R0,C0, R0,C1, ..., R0,C(n-2) (moving right); then R0,C(n-1), R1,C(n-1),
# ..., R(n-2),C(n-1) (moving down); then R(n-1),C(n-1), R(n-1),C(n-2), ...,
# R(n-1),C1 (moving left); then R(n-1),C0, R(n-2),C0, ..., R1,C0 (moving
# up). Mark each processed element by setting it to 0, which is assumed
# not to occur in the array (any value not in the array would do). After
# R1,C0, the same process starts again from R1,C1, and so on until every
# element is processed. Conceptually, the array is processed in "shells"
# from the outside moving to the centre. (In the program, the direction
# turns whenever the next cell is outside the matrix or already zeroed.)
#
# The single-loop program has time complexity O(n^2) and space complexity
# O(1). (Note that it overwrites the input matrix with zeros.)
#
# VARIANTS
# --------
# Variant 1 (stated in the book; no solution given): Given a dimension d,
# write a program to generate a d x d 2D array which in spiral order is
# <1,2,3,...,d^2>. For example, if d = 3, the result should be
#     A = [1 2 3]
#         [8 9 4]
#         [7 6 5].
#
# Variant 2 (stated in the book; no solution given): Given a sequence of
# integers P, compute a 2D array A whose spiral order is P. (Assume the
# size of P is n^2 for some integer n.)
#
# Variant 3 (stated in the book; no solution given): Write a program to
# enumerate the first n pairs of integers (a, b) in spiral order, starting
# from (0,0) followed by (1,0). For example, if n = 10, your output should
# be (0,0), (1,0), (1,-1), (0,-1), (-1,-1), (-1,0), (-1,1), (0,1), (1,1),
# (2,1).
#
# Variant 4 (stated in the book; no solution given): Compute the spiral
# order for an m x n 2D array A.
#
# Variant 5 (stated in the book; no solution given): Compute the last
# element in spiral order for an m x n 2D array A in O(1) time.
#
# Variant 6 (stated in the book; no solution given): Compute the kth
# element in spiral order for an m x n 2D array A in O(1) time.


# TEXTBOOK CODE COMPARISON
# ------------------------
# - Book program 1: `def matrix_in_spiral_order(square_matrix)` with a
#   nested `matrix_layer_in_clockwise(offset)` that handles the odd centre
#   (`if offset == len(square_matrix) - offset - 1`) and adds each side by
#   slicing, using `list(zip(*square_matrix))` to read columns and
#   negative-step slices for the reversed sides; the outer loop runs
#   `for offset in range((len(square_matrix) + 1) // 2)`.
# - Book program 2: also `def matrix_in_spiral_order(square_matrix)`,
#   using `SHIFT = ((0, 1), (1, 0), (0, -1), (-1, 0))`, a `direction`
#   index turned with `(direction + 1) & 3`, and zeroing visited cells.
# - MISSING FROM THE FILE: neither book program is implemented. The file's
#   single function reuses the name `matrix_in_spiral_order` (parameter
#   `matrix`, type hints) but uses a different algorithm: four boundary
#   indices (top/bottom/left/right) shrunk after each side, with
#   `extend`/`append`/`reversed`. It also adds an empty-input return, a
#   ragged-row ValueError, and supports rectangular matrices; it does not
#   modify the input (book program 2 does).


# Python executes this block only when this source file is run directly.
# When pytest imports the file, this block is skipped automatically.
# Documentation: https://docs.python.org/3/library/__main__.html
if __name__ == "__main__":

    # The book's Figure 5.3(a) example; its spiral order is
    # <1,2,3,6,9,8,7,4,5>.
    m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    # print() with several arguments separates them with a space.
    print("spiral order:", matrix_in_spiral_order(m))

    # `assert` stops the program with an AssertionError if the result
    # differs from the expected list. pytest provides the more thorough
    # automated verification.
    assert matrix_in_spiral_order(m) == [1, 2, 3, 6, 9, 8, 7, 4, 5]
