"""EPI Python — Exercise 17.8: Compute the Largest Rectangle Under the Skyline

Chapter 17: Greedy Algorithms and Invariants
Textbook: pages 270–272 (printed page numbers; problem and hint on 270,
Figure 17.5 and solution development on 271, program, complexity and
variant on 272).

PROBLEM (from the textbook)
---------------------------
You are given a sequence of adjacent buildings. Each has unit width and an
integer height. These buildings form the skyline of a city. An architect
wants to know the area of a largest rectangle contained in this skyline.
See Figure 17.5 on the next page for an example.

Let A be an array representing the heights of adjacent buildings of unit
width. Design an algorithm to compute the area of the largest rectangle
contained in this skyline.

Figure 17.5 (book): thirteen unit-width buildings A..M at x = 0..12 with
heights A=1, B=4, C=2, D=5, E=6, F=3, G=2, H=6, I=6, J=4, K=2, L=1, M=3.
The shaded largest rectangle under the skyline has area 2 x (11 - 1) = 20.
The tallest rectangle is from 7 to 9 and the widest from 0 to 1, but
neither is the largest rectangle.

HINT (from the textbook)
------------------------
How would you efficiently find the largest rectangle which includes the
ith building, and has height A[i]?

SOLUTION DEVELOPMENT (following the textbook)
---------------------------------------------
1. Brute force: for every pair (i, j) take min(A[i..j]) * (j - i + 1).
   O(n^3). Iterating over i and then j >= i while tracking the running
   minimum height improves this to O(n^2), but this line of attack cannot
   reasonably be pushed below O(n^2).

2. A different brute force: for each building i, find how far left and
   right one can go without dropping below A[i]. This is the largest
   rectangle "supported" by building i, which acts like a "pillar" of that
   rectangle. In Figure 17.5 the largest rectangle supported by G spans 1
   to 11, and the one supported by F spans 3 to 6. One forward and one
   backward scan per i gives O(n^2) overall.

3. Refinement (left-to-right sweep). When processing building i we do not
   yet know how far right its rectangle goes, but we DO know that earlier
   buildings TALLER than A[i] cannot extend past i: building i "blocks"
   them. Example: reaching F, the rectangles supported by B, D and E (all
   taller than F) cannot extend past 5.
   - B need not be considered at F: C had already blocked it.
   - C need not be kept separately from G: they have equal heights and C
     is not yet blocked, so they support the same largest rectangle.
   So we only track buildings not yet blocked, and we may replace an
   existing building of equal height with the current one. Call these the
   active pillars. Iterating from 0 to 12, the active pillar sets are:
   {A}, {A,B}, {A,C}, {A,C,D}, {A,C,D,E}, {A,C,F}, {A,G}, {A,G,H},
   {A,G,I}, {A,G,J}, {A,K}, {L}, and {L,M}.

4. When a building leaves the active set we know where its rectangle ENDS
   on the right: e.g. at C, B's rectangle ends at 2; at F, the rectangles
   of D and E end at 5. Its LEFT end is just after the closest active
   pillar with lower height. Example at F: active pillars {A, C, D, E}; E
   and D are removed because both are taller than F. E's rectangle has
   height 6 and starts after D, at 4: area 6 x (5 - 4) = 6. D's rectangle
   has height 5 and starts after C, at 3: area 5 x (5 - 3) = 10.

5. Data structure: insertions and deletions in the active set happen in
   last-in first-out order, so use a STACK with the rightmost active
   building on top. The left boundary of a popped building is then simply
   the building below it on the stack. Example: at F the stack is
   A, C, D, E (E on top); E is blocked, its rectangle ends where F begins
   (5) and begins where D ends (4).

6. Finishing: at the end the stack is not empty (it holds at least the
   last building). Process those entries the same way, except that their
   rectangles end at n, the number of buildings. In the example the stack
   holds L and M at the end, and both rectangles end at 13.

The book's program is calculate_largest_rectangle(heights). This file's
largest_rectangle_under_skyline implements the same stack algorithm (see
TEXTBOOK CODE COMPARISON below for small differences).

ADDITIONAL EXAMPLES (added for learning; not printed in this exercise)
---------------------------------------------------------------------
    []                  -> 0  (no buildings)
    [1]                 -> 1
    [2, 1, 5, 6, 2, 3]  -> 10 (heights 5 and 6 give 5 x 2)
    [2, 2, 2]           -> 6  (equal heights: 2 x 3)
"""


# Type hints: `heights: list[int]` and `-> int` document the expected types;
# Python does not enforce annotations at run time.
def largest_rectangle_under_skyline(heights: list[int]) -> int:
    """Largest axis-aligned rectangle below an integer-height histogram.

    The textbook's stack-of-active-pillars program (book name:
    calculate_largest_rectangle).
    """

    # stack: indices of the active pillars, heights increasing from bottom
    # to top. A Python list works as a stack: append() pushes onto the end
    # and pop() removes and returns the last item, both O(1).
    stack=[]
    best=0

    # `heights + [0]` builds a NEW list with a sentinel building of height 0
    # at index n (the caller's list is not changed). As in the book, this
    # zero-height building blocks every remaining pillar at the end, so the
    # final stack is emptied by the same loop instead of separate code.
    extended=heights+[0]

    # enumerate(iterable) yields (index, item) pairs, so the loop gets both
    # the building's position and its height without manual counting.
    for index,height in enumerate(extended):

        # `while stack and ...`: an empty list is falsy, so the loop stops
        # when the stack is empty (and never evaluates stack[-1] then).
        # stack[-1] is the top of the stack (negative index = from the end).
        # Every pillar strictly taller than the current building is blocked:
        # its rectangle ends just before `index`.
        while stack and extended[stack[-1]]>height:
            popped=stack.pop()

            # Conditional expression `A if cond else B`. If the stack is now
            # empty, nothing lower lies to the left, so the rectangle starts
            # at 0 and its width is `index`. Otherwise it starts right after
            # the new top (the closest lower pillar).
            width=index if not stack else index-stack[-1]-1

            # Built-in max(a, b) returns the larger argument.
            best=max(best,extended[popped]*width)

        # The current building becomes the rightmost active pillar.
        stack.append(index)
    return best


# TEXTBOOK POST-SOLUTION DISCUSSION (page 272)
# --------------------------------------------
# Time complexity is O(n). While advancing, the work for each building is
# proportional to the pushes and pops it causes. A single building can cause
# several pops, but overall there are at most n pushes and at most n pops,
# because each index is pushed once and so can be popped at most once.
# Processing whatever remains on the stack at the end is also O(n): at most
# n entries, O(1) each. Hence O(n) overall.
#
# Space complexity is O(n), the largest size the stack can reach, e.g.
# when the buildings appear in ascending order of height.
#
# VARIANTS
# --------
# Variant (stated in the book; no solution given): Find the largest square
# under the skyline.


# TEXTBOOK CODE COMPARISON
# ------------------------
# - Name: book `def calculate_largest_rectangle(heights):`; file
#   `def largest_rectangle_under_skyline(heights: list[int]) -> int:`
#   (renamed, type hints added; parameter name unchanged).
# - Variables: book `pillar_indices, max_rectangle_area = [], 0` and loop
#   `for i, h in enumerate(heights + [0])`; file uses `stack`, `best`, a
#   named list `extended = heights + [0]`, and `index, height`. The book's
#   comment "By appending [0] to heights, we can uniformly handle the
#   computation for rectangle area here." is paraphrased in the file's
#   comment rather than kept verbatim.
# - Pop condition differs: the book pops while the top height is `>= h`
#   (equal-height pillars are replaced, matching the text's "replace
#   existing buildings whose height equals that of the current building");
#   the file pops only while `> height`, so equal-height pillars stay on the
#   stack. Both give the same maximum area.
# - The book reads heights from the original `heights` list; the file reads
#   from `extended`. The book stores the popped height in `height`; the file
#   stores the popped index in `popped`.


# Python executes this block only when this source file is run directly.
# When pytest imports the file, this block is skipped automatically.
# Documentation: https://docs.python.org/3/library/__main__.html
if __name__ == "__main__":

    # Executable demonstration cases (added; the book's Figure 17.5 skyline
    # is not used); pytest has the full set. They show empty input, one
    # building, a mixed skyline and equal heights.
    #
    # `assert` raises AssertionError if its condition is False; these are
    # quick smoke checks.
    result=largest_rectangle_under_skyline([])
    print('largest_rectangle_under_skyline', result)
    assert result == 0
    result=largest_rectangle_under_skyline([1])
    print('largest_rectangle_under_skyline', result)
    assert result == 1
    result=largest_rectangle_under_skyline([2, 1, 5, 6, 2, 3])
    print('largest_rectangle_under_skyline', result)
    assert result == 10
    result=largest_rectangle_under_skyline([2, 2, 2])
    print('largest_rectangle_under_skyline', result)
    assert result == 6
