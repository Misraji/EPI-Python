"""EPI Python — Exercise 14.7: Enumerate Numbers of the Form a + b sqrt(2)

Chapter 14: Binary Search Trees
Textbook: pages 207–210 (printed page numbers; problem starts on 207,
solution on 208).

PROBLEM (from the textbook)
---------------------------
"Numbers of the form a + b sqrt(q), where a and b are nonnegative integers,
and q is an integer which is not the square of another integer, have special
properties, e.g., they are closed under addition and multiplication. Some of
the first few numbers of this form are given in Figure 14.4 on the following
page."

Figure 14.4 (page 208): "Some points of the form a + b sqrt(2). (For
typographical reasons, this figure does not include all numbers of the form
a + b sqrt(2) between 0 and 2 + 2 sqrt(2), e.g., 3 + 0 sqrt(2),
4 + 0 sqrt(2), 0 + 3 sqrt(2), 3 + 1 sqrt(2) lie in the interval but are not
included.)" The points shown are 0.0, 1.0, 1.414, 2.0, 2.414, 2.828, 3.414,
3.828, 4.828.

"Design an algorithm for efficiently computing the k smallest numbers of the
form a + b sqrt(2) for nonnegative integers a and b."

HINT (from the textbook)
------------------------
"Systematically enumerate points."

SOLUTION DEVELOPMENT (following the textbook)
---------------------------------------------
Key fact: sqrt(2) is irrational, so it never equals a/b for integers a, b.
Hence if x + y sqrt(2) = x' + y' sqrt(2) with integers x, y, x', y', then
x = x' and y = y' (otherwise sqrt(2) = (x - x')/(y' - y)).

Brute force: generate every a + b sqrt(2) with integers 0 <= a, b <= k - 1.
That is exactly k^2 numbers and the k smallest must be among them; sort and
return the first k. Time O(k^2 log(k^2)) = O(k^2 log k). It is wasteful to
generate k^2 numbers when only a small fraction matter.

BST approach: the smallest number is 0 + 0 sqrt(2), and the candidates for
the next smallest are 1 + 0 sqrt(2) and 0 + 1 sqrt(2). So keep a collection
of numbers, initially {0 + 0 sqrt(2)}, and k times extract its smallest
element a + b sqrt(2) and insert (a + 1) + b sqrt(2) and a + (b + 1) sqrt(2).
The collection needs extract-minimum and insert, and must not hold
duplicates when the same number is inserted twice. A BST does all this
efficiently. Trace from the book:
- start with 0 + 0 sqrt(2); extract it, insert 1 + 0 sqrt(2) and
  0 + 1 sqrt(2);
- extract 1 + 0 sqrt(2), insert 2 + 0 sqrt(2) and 1 + 1 sqrt(2); the BST
  now holds 0 + 1 sqrt(2) = 1.414, 2 + 0 sqrt(2) = 2, 1 + 1 sqrt(2) = 2.414;
- extract 0 + 1 sqrt(2), insert 1 + 1 sqrt(2) and 0 + 2 sqrt(2); the first
  is already present, so the BST becomes 2 + 0 sqrt(2) = 2,
  1 + 1 sqrt(2) = 2.414, 0 + 2 sqrt(2) = 2.828.
(Though not visible in this small example, inserted values can be smaller
than values already present, so a real ordered structure is needed.) The
book implements this with an `ABSqrt2` class (fields a, b and val, ordered
and compared by val) and a `bintrees.RBTree`.

O(n) approach: simple to implement but less obvious. The (n+1)-th value is
1 or sqrt(2) added to some earlier value. Scanning all earlier results for
the smallest such sum exceeding the n-th value would cost O(n) per element.
Instead, store results in an array A and track just two indices: i, the
smallest index with A[i] + 1 > A[n - 1], and j, the smallest index with
A[j] + sqrt(2) > A[n - 1]. The next entry is the smaller of A[i] + 1 and
A[j] + sqrt(2); afterwards increment i if it was A[i] + 1, increment j if it
was A[j] + sqrt(2), and increment both if the two are equal.

Worked trace from the book (A = <0>, i = j = 0):
1. A[0] + 1 = 1 < A[0] + sqrt(2) = 1.414: push 1, increment i.
   A = <0,1>, i = 1, j = 0.
2. A[1] + 1 = 2 > A[0] + sqrt(2) = 1.414: push 1.414, increment j.
   A = <0,1,1.414>, i = 1, j = 1.
3. A[1] + 1 = 2 < A[1] + sqrt(2) = 2.414: push 2, increment i.
   A = <0,1,1.414,2>, i = 2, j = 1.
4. A[2] + 1 = 2.414 = A[1] + sqrt(2) = 2.414: push 2.414, increment both.
   A = <0,1,1.414,2,2.414>, i = 3, j = 2.
5. A[3] + 1 = 3 > A[2] + sqrt(2) = 2.828: push 2.828, increment j.
   i = 3, j = 3. (The printed list here reads <0,1,1.414,2,2.828>, leaving
   out the 2.414 pushed in step 4.)
6. A[3] + 1 = 3 < A[3] + sqrt(2) = 3.414: push 3, increment i.
   A = <0,1,1.414,2,2.828,3> as printed, i = 4, j = 3.

This file implements the O(n) two-index method, using plain floats instead
of ABSqrt2 objects. The BST (bintrees) listing is not present.

ADDITIONAL EXAMPLES (added for learning; not printed in this exercise)
---------------------------------------------------------------------
    k=5 -> [0.0, 1.0, 1.414..., 2.0, 2.414...]
"""

# Python standard library: mathematical functions on floats.
# Module documentation: https://docs.python.org/3/library/math.html
# sqrt API: https://docs.python.org/3/library/math.html#math.sqrt
from math import sqrt


# Type hints: an int k in, a list of floats out. Python does not enforce
# annotations at run time.
def generate_first_k_a_b_sqrt2(k: int) -> list[float]:
    """Generate the first k distinct increasing values of a + b*sqrt(2).

    This is the textbook's second, O(k) implementation (two indices i, j).
    """

    # Added input checks (not in the book): reject negative k with a
    # ValueError; k == 0 (falsy) gives an empty list.
    if k < 0:
        raise ValueError('k must be nonnegative')
    if not k:
        return []

    # A starts as <0 + 0 sqrt(2)>; both indices point at it.
    values=[0.0]
    i=j=0

    # range(1, k) runs k - 1 times; `_` is the conventional name for a loop
    # variable that is not used.
    for _ in range(1,k):
        increment_one=values[i]+1.0

        # math.sqrt(x) returns the square root of x as a float. sqrt(2) is
        # irrational, so the float is only an approximation
        # (1.4142135623730951).
        # Documentation: https://docs.python.org/3/library/math.html#math.sqrt
        increment_sqrt=values[j]+sqrt(2)

        # The next value is the smaller candidate; built-in min() returns the
        # smaller of its arguments.
        candidate=min(increment_one,increment_sqrt)
        values.append(candidate)

        # Floating-point roundoff may make mathematically identical candidates
        # differ in the last few bits. Advance both streams on near-equality.
        # 1e-12 is scientific notation for 0.000000000001. Using two separate
        # `if` statements (not if/elif) lets BOTH indices advance when the
        # candidates are (nearly) equal, as the book requires.
        epsilon = 1e-12
        if increment_one <= increment_sqrt + epsilon:
            i += 1
        if increment_sqrt <= increment_one + epsilon:
            j += 1
    return values


# TEXTBOOK POST-SOLUTION DISCUSSION (pages 209–210)
# -------------------------------------------------
# BST version: each iteration does one deletion and two insertions; there are
# k iterations, so time O(k log k). Space O(k), since there are no more than
# 2k insertions.
#
# Two-index version: each additional element takes O(1) time, so computing
# the first n values of the form a + b sqrt(2) takes O(n) time.
#
# VARIANTS
# --------
# The textbook gives no variants for this exercise.


# TEXTBOOK CODE COMPARISON
# ------------------------
# - Book defines `class ABSqrt2` with `__init__(self, a, b)` storing a, b and
#   `val = a + b * math.sqrt(2)`, plus `__lt__` and `__eq__` comparing
#   `val`. The file has no ABSqrt2 class; it stores plain float values.
# - Book's first `generate_first_k_a_b_sqrt2(k)` uses the third-party
#   `bintrees.RBTree` (comments "Initial for 0 + 0 * sqrt(2)." and "Adds the
#   next two numbers derived from next_smallest."): NOT present in this file.
# - Book's second `generate_first_k_a_b_sqrt2(k)` (comment "Will store the
#   first k numbers of the form a + b sqrt(2).") builds `cand` as a list of
#   ABSqrt2 objects, appends `min(cand_i_plus_1, cand_j_plus_sqrt2)`,
#   advances i / j when `cand_i_plus_1.val == cand[-1].val` /
#   `cand_j_plus_sqrt2.val == cand[-1].val` (exact equality), and returns
#   `[a.val for a in cand]`. File: same two-index logic on floats
#   (`values`, `increment_one`, `increment_sqrt`, `candidate`), uses
#   `from math import sqrt`, adds checks for negative and zero k, and
#   compares with an `epsilon = 1e-12` tolerance instead of exact equality.
#   Type hints added.


# Python executes this block only when this source file is run directly.
# When pytest imports the file, this block is skipped automatically.
# Documentation: https://docs.python.org/3/library/__main__.html
if __name__ == '__main__':

    # An added example: the first five values 0, 1, sqrt(2), 2, 1 + sqrt(2).
    result=generate_first_k_a_b_sqrt2(5)
    print('First five a + b*sqrt(2) values:',result)

    # `assert` stops the program with an AssertionError if the condition is
    # false. Here it checks that the output is in ascending order (equal to
    # its sorted copy) and has five entries. Full tests are in tests/.
    assert result==sorted(result) and len(result)==5
