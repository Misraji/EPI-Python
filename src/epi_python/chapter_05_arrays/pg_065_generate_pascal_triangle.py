"""EPI Python — Exercise 5.20: Compute Rows in Pascal's Triangle

Chapter 5: Arrays
Textbook: pages 65–66 (printed page numbers; introduced at the bottom of
page 65; figure, problem, solution, program, complexity and variant on
page 66).

PROBLEM (from the textbook)
---------------------------
Context: "Figure 5.5 on the following page shows the first five rows of a
graphic that is known as Pascal's triangle. Each row contains one more
entry than the previous one. Except for entries in the last row, each
entry is adjacent to one or two numbers in the row below it. The first row
holds 1. Each entry holds the sum of the numbers in the adjacent entries
above it."
(Figure 5.5 shows the rows 1 / 1 1 / 1 2 1 / 1 3 3 1 / 1 4 6 4 1,
centred like a pyramid.)

"Write a program which takes as input a nonnegative integer n and returns
the first n rows of Pascal's triangle."

HINT (from the textbook)
------------------------
"Write the given fact as an equation."

SOLUTION DEVELOPMENT (following the textbook)
---------------------------------------------
Brute force: lay the arrays out in memory the way they appear in the
figure (centred). The hard part is then working out which indices to loop
over and read from.

Better: keep every row left-aligned, so each row's first entry is at
index 0. Then the rule is simple: the jth entry of the ith row is 1 when
j = 0 or j = i; otherwise it is the sum of the (j - 1)th and jth entries
of row i - 1.

Book example:
  R0 = <1>
  R1 = <1,1>
  R2 = <1, R1[0] + R1[1] = 2, 1>
  R3 = <1, R2[0] + R2[1] = 3, R2[1] + R2[2] = 3, 1>

The book prints one program, `generate_pascal_triangle(n)`, implemented
here with the same name.

ADDITIONAL EXAMPLES (added for learning; not printed in this exercise)
---------------------------------------------------------------------
    n = 0 -> []
    n = 1 -> [[1]]
    n = 3 -> [[1], [1, 1], [1, 2, 1]]
    n = 5 -> the five rows of Figure 5.5.
"""



# `n: int` and `-> list[list[int]]` (a list of rows, each a list of ints)
# are type hints. Python does not enforce them at run time. Built-in
# generics like list[...] need Python 3.9 or newer.
# Documentation: https://docs.python.org/3/library/typing.html
def generate_pascal_triangle(n: int) -> list[list[int]]:
    """Construct the first n rows of Pascal's triangle.

    This is the textbook's `generate_pascal_triangle(n)` program, building
    each row as it goes instead of preallocating all rows.
    """
    triangle = []
    for row_index in range(n):

        # `[1] * k` makes a list of k ones. Row i has i + 1 entries, and
        # both ends (j = 0 and j = i) stay 1.
        row = [1] * (row_index + 1)

        # Interior entries j = 1 .. i - 1 (range's stop is excluded). For
        # rows 0 and 1 this range is empty.
        for column in range(1, row_index):

            # Book comment: "Sets this entry to the sum of the two above
            # adjacent entries." `triangle[-1]` is the previous row: a
            # negative index counts from the end of the list.
            row[column] = triangle[-1][column - 1] + triangle[-1][column]

        # list.append adds the finished row at the end of `triangle`.
        # Documentation: https://docs.python.org/3/tutorial/datastructures.html
        triangle.append(row)
    return triangle


# TEXTBOOK POST-SOLUTION DISCUSSION (page 66)
# ------------------------------------------
# Each entry costs O(1) time, so the total time is
# O(1 + 2 + ... + n) = O(n(n + 1)/2) = O(n^2). The space complexity is
# likewise O(n^2).
#
# It is a known fact that the ith entry of the nth row of Pascal's
# triangle is the binomial coefficient C(n, i) ("n choose i"). That does
# not make the problem trivial, because computing C(n, i) is itself
# tricky. (In fact, Pascal's triangle can be used to compute C(n, i).)
#
# VARIANTS
# --------
# Variant (stated in the book; no solution given): Compute the nth row of
# Pascal's triangle using O(n) space.


# TEXTBOOK CODE COMPARISON
# ------------------------
# - Name and parameter match the book (`generate_pascal_triangle(n)`);
#   type hints added.
# - Book preallocates every row with a list comprehension,
#   `result = [[1] * (i + 1) for i in range(n)]`, then fills interior
#   entries with `result[i][j] = result[i - 1][j - 1] + result[i - 1][j]`
#   for `i in range(n)`, `j in range(1, i)`. File builds `triangle` row by
#   row: creates `row = [1] * (row_index + 1)`, fills it from
#   `triangle[-1]` (the previous row), then appends it. Variable names
#   differ (`result`/`i`/`j` vs `triangle`/`row_index`/`column`). Same
#   output.


# Python executes this block only when this source file is run directly.
# When pytest imports the file, this block is skipped automatically.
# Documentation: https://docs.python.org/3/library/__main__.html
if __name__ == "__main__":
    # Run a few self-contained examples before exploring the pytest suite.
    #
    # n = 0, 1 and 3 are added boundary/small cases; n = 5 reproduces the
    # five rows of the book's Figure 5.5. print() with several arguments
    # separates them with a space. `assert` stops the program with an
    # AssertionError if a result differs from the expected value; pytest
    # provides the more thorough automated verification.
    observed = generate_pascal_triangle(0)
    print("generate_pascal_triangle:", observed)
    assert observed == []
    observed = generate_pascal_triangle(1)
    print("generate_pascal_triangle:", observed)
    assert observed == [[1]]
    observed = generate_pascal_triangle(3)
    print("generate_pascal_triangle:", observed)
    assert observed == [[1], [1, 1], [1, 2, 1]]
    observed = generate_pascal_triangle(5)
    print("generate_pascal_triangle:", observed)
    assert observed == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
