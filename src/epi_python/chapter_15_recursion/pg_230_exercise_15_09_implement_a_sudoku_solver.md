# Exercise 15.9: Implement a Sudoku solver

**Printed textbook page:** 230. **Reference transcription pages:** 230–231.

> **Unverified OCR transcription:** This section retains the supplied PDF text layer. It is not certified verbatim: code syntax, mathematical symbols, and page boundaries may be corrupted. When two exercises begin on the same page, their excerpts overlap. Do not paste extracted code into a `.py` file without manual verification.

#### Printed page 230 (PDF page 244)

```text
Flgure 15.6: The five binary trees on three nodes.
be distinct, since no two would have the same left and right child. However, some will have fewer
than n - 1 nodes, and some will have more.
The key to efficiency is to direct the search. If the left child has k nodes, we should only use right
children with n - 1, - k nodes, to get binary trees with n nodes that have that left child. Specifically,
we get all binary trees on n nodes by getting all left subtrees on I nodes, and right subtrees on n - 1- i
nodes, for I between 0 and n - 1.
Looking carefully at Figure 15.6, you will see the first two trees correspond to the trees on three
nodes which have a left subtree of size 0 and a right subtree of size 2. The third tree is the only tree
on three nodes which has a left subtree of size 1 and a right subtree of size 1. The last two trees
correspond to the trees on three nodes which have a left subtree of size 2 and a right subtree of size
0. The set of two trees on two nodes is itself computed recursively: there is a single binary tree on
one node, and it may be on either side of the root.
def generate-aII-binary-trees (num-nodes) :
if num-nodes == 0: # Enpty tree, add as a l{one
return INone]
result = []
for num-left-tree-nodes in range(num-nodes) :
num-right-tree-nodes = num-nodes - 1 - num-left-tree-nodes
left-subtree s = generate-alI-binary-tree s (num-left-tree-node s)
right-subtrees = generate-aI1-binary-trees (num-right-tree-nodes)
# Generates aII conbjnations of Ieft-subtrees and right-subtrees
result += [
BinaryTreeNode (0, Ieft , right)
for left in left-subtrees for right in right-subtrees
l
return result
ThenumberofcallsC(n)totherecursivefunctionsatisfiestherecurrenceC(n) =Li=rC(n-i)C(i-7).
The quantity C(n) is called the nth Catalan number. It is known to be equal t" ffi..Comparing
Solution L5.6 on Page 227 to this solution, you will see considerable similarity-the Catalan numbers
appear in numerous types of combinatorial problems.
15.9 IIvrpr-eNrnNr e Supoxu soLvER
Implement a Sudoku solver. See Problem 5.17 on Page 60 for a definition of Sudoku.
Hint: Apply the constraints to speed up a brute-force algorithm.
Solution: A brute-force approach would be to try every possible assignment to emPty entries,
and then check if that assignment leads to a valid solution using Solution 5.17 on Page 60. This
230
```

#### Printed page 231 (PDF page 245)

```text
is wasteful, since if setting a value early on leads to a constraint violation, there is no point in
continuing. Therefore, we should apply the backtracking principle.
Specifically, we traverse the 2D array entries one at a time. If the entry is empty, we try each
value for the entry and see if the updated 2D array is still valid; if it is, we recurse, If all the
entries have been filled, the search is successful. The naive approach to testing validity is calling
Solution 5.17 on Page 60. However, we can reduce runtime considerably by making use of the fact
that we are adding a value to an array that already satisfies the constraints. This means that we
need to check just the row, column, and subgrid of the added entry.
For example/ suppose webegin with the lower-left entry for the configuration in Figure 5.2(a) on
Page 60. Adding a 1 to entry does not violate any row, column, or subgrid constraint, so we move
on to the next entry in that row. We cannot put a 1, since that would now violate a row constraint;
however, a 2 is acceptable.
def solve-sudoku(partial-assignment) :
def solve-partial-sudoku(i, j) :
if i == Ien(partial_assignment):
i=0 
#Startsarow.
j*=t
if j == len(partial_assignmentlil):
return True # Entire natrix has been fi77ed without confTict
# Skips nonenpty entries.
if partial-assignmenttil tjl != EHPTY-ENTRY
return solve_partial_sudoku(i * 1, j)
def valid-to-add(i, j, val):
# Check row constraints.
if any(val == partial_assignment tkl tjl
for k in range(Ien(partial_assignment)))
return False
# Check colunn constraints,
if val in partial-assignmentIi]
return FaIse
# Check region constraints.
re gion-si ze = int (nath. sqrt (len (partial_as si gnment ) ) )
I=i//region-size
l=j 
// region_size
return not any(
val == partial_assignmentIregion_size * I + a][region_size * J
+bl
for a, b in itertools.product(range(region_size), repeat=2))
for vaI in range(1, len(partial_assignment) + 1):
# It's substantial-l.y quicker to check if entry va7 with any of the
# constraints if we add jt at (i,j) 
adding it, rather than adding jt and
# then checking a77 constraints. Tie teason js that we know we are
# starting with a vaTid configuration, and the only entry which can
# cause a probTen is entry val at (i,jl.
if valid-to-add (i , j , va1) :
partial-assignmentIi][j] = va1
231,
```
