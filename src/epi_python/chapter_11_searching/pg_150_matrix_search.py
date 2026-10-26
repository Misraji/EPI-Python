"""EPI Python — Exercise 11.6: Search in a 2D Sorted Array

Chapter 11: Searching
Textbook: pages 150–152 (printed page numbers; problem starts on 150,
worked searches and program on 151, end of program and complexity on 152).

PROBLEM (from the textbook)
---------------------------
"Call a 2D array sorted if its rows and its columns are nondecreasing. See
Figure 11.3 for an example of a 2D sorted array."

          C0  C1  C2  C3  C4
    R0    -1   2   4   4   6
    R1     1   5   5   9  21
    R2     3   6   6   9  22
    R3     3   6   8  10  24
    R4     6   8   9  12  25
    R5     8  10  12  13  40
    (Figure 11.3: A 2D sorted array.)

"Design an algorithm that takes a 2D sorted array and a number and checks
whether that number appears in the array. For example, if the input is the
2D sorted array in Figure 11.3, and the number is 7, your algorithm should
return false; if the number is 8, your algorithm should return true."

HINT (from the textbook)
------------------------
"Can you eliminate a row or a column per comparison?"

SOLUTION DEVELOPMENT (following the textbook)
---------------------------------------------
Let the array be A (m rows, n columns) and the number be x.

First idea: binary-search every row separately, O(m log n) time (or
O(n log m) if columns are searched instead). This ignores the fact that
rows AND columns are sorted; it treats each row in isolation.

Looking at corners: if x < A[0][0], x cannot be anywhere, because A[0][0]
is the smallest element. But if x > A[0][0], neither the first row nor the
first column can be ruled out, and searching along both leads to an O(mn)
method -- far worse. The bottom-right corner A[m - 1][n - 1] has the same
problem.

The book's design rule: examine extremal cases. Besides A[0][0] and
A[m - 1][n - 1] there are two other corners. Compare x with the top-right
entry A[0][n - 1]:
  * If x == A[0][n - 1], the value has been found.
  * If x > A[0][n - 1], x is bigger than everything in Row 0, so Row 0 is
    eliminated.
  * If x < A[0][n - 1], x is smaller than everything in Column n - 1, so
    that column is eliminated.
Either way, what remains is a smaller 2D sorted array with one fewer row or
column. (Starting from the other remaining corner, the bottom-left
A[m - 1][0], gives a very similar algorithm.)

Book's worked search for 7 in Figure 11.3 (Figure 11.4(a), not present):
  A[0][4] = 6:  7 > 6,  eliminate Row 0.
  A[1][4] = 21: 7 < 21, eliminate Column 4.
  A[1][3] = 9:  7 < 9,  eliminate Column 3.
  A[1][2] = 5:  7 > 5,  eliminate Row 1.
  A[2][2] = 6:  7 > 6,  eliminate Row 2.
  A[3][2] = 8:  7 < 8,  eliminate Column 2.
  A[3][1] = 6:  7 > 6,  eliminate Row 3.
  A[4][1] = 8:  7 < 8,  eliminate Column 1.
  A[4][0] = 6:  7 > 6,  eliminate Row 4.
  A[5][0] = 8:  7 < 8,  eliminate Column 0.
  No entries remain, so the answer is false.

Book's worked search for 8 (Figure 11.4(b), present): Row 0, then
Column 4, then Column 3, then Row 1, then Row 2 are eliminated; the
comparison with A[3][2] is a match, so the answer is true.

The implementation below, matrix_search, follows this idea.

ADDITIONAL EXAMPLES (added for learning; not printed in this exercise)
---------------------------------------------------------------------
    matrix=[[1, 3, 5], [2, 4, 6]], target=4 -> True
    matrix=[[1, 3, 5], [2, 4, 6]], target=7 -> False
    matrix=[],                     target=2 -> False (empty matrix)
"""


def matrix_search(matrix: list[list[int]], target: int) -> bool:
    """Search a matrix with sorted rows and columns.

    This is the textbook's matrix_search (the only implementation given),
    plus a guard for an empty matrix.

    Type hints: `list[list[int]]` means "a list of rows, each row a list of
    ints"; `-> bool` means True or False is returned. Python does not
    enforce these annotations.
    """

    # An empty list is falsy, so `not matrix` is True for []. The second
    # test catches a matrix whose first row is empty, e.g. [[]]; without it
    # col would start at -1. `or` stops at the first True operand, so
    # matrix[0] is only read when matrix is non-empty. (Guard added in this
    # file.)
    if not matrix or not matrix[0]:
        return False

    # Start from the top-right corner: row 0, last column. Tuple unpacking
    # sets both indices at once.
    row,col=0,len(matrix[0])-1

    # Keep searching while there are unclassified rows and columns, i.e.
    # while (row, col) is still inside the matrix.
    while row < len(matrix) and col >= 0:
        value=matrix[row][col]
        if value == target:
            return True

        # The current entry is the smallest in what is left of its column,
        # and target is smaller still, so the whole column is eliminated.
        # `col-=1` is augmented assignment, short for col = col - 1.
        if value > target:
            col-=1

        # The current entry is the largest in what is left of its row, and
        # target is larger, so the whole row is eliminated.
        else:
            row+=1
    return False


# TEXTBOOK POST-SOLUTION DISCUSSION (page 152)
# --------------------------------------------
# Each iteration removes one row or one column, so at most m + n - 1
# elements are inspected: O(m + n) time. Extra space is O(1).
#
# VARIANTS
# --------
# The book gives no variants for this exercise.


# TEXTBOOK CODE COMPARISON
# ------------------------
# Book: `def matrix_search(A, x):` with
#   `row, col = 0, len(A[0]) - 1  # Start from the top-right corner.`,
#   the comment "Keeps searching while there are unclassified rows and
#   columns.", and if / elif / else branches on `A[row][col] == x`,
#   `A[row][col] < x` (row += 1, "Eliminate this row.") and else
#   (col -= 1, "Eliminate this column.").
# File: parameters renamed `matrix: list[list[int]]` and `target: int`,
#   return hint `-> bool` added; an empty-matrix guard is added (not in the
#   book); the entry is stored in a local `value`; the second test is
#   reversed (`value > target` moves left, else moves down) and written as
#   `if` after a returning `if` instead of `elif`. Behaviour is the same.


# Python executes this block only when this source file is run directly.
# When pytest imports the file, this block is skipped automatically.
# Documentation: https://docs.python.org/3/library/__main__.html
if __name__ == "__main__":
    # Demonstrations check representative input/output behavior: a value
    # that is present, one that is absent, and an empty matrix.
    #
    # `assert` stops the program with an AssertionError if a result is
    # different from the expected value. These are quick smoke checks;
    # pytest provides the more thorough automated verification.
    observed = matrix_search([[1, 3, 5], [2, 4, 6]], 4)
    print("matrix_search:", observed)
    assert observed == True
    observed = matrix_search([[1, 3, 5], [2, 4, 6]], 7)
    print("matrix_search:", observed)
    assert observed == False
    observed = matrix_search([], 2)
    print("matrix_search:", observed)
    assert observed == False
