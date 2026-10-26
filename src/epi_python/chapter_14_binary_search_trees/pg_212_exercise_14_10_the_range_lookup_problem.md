# Exercise 14.10: The range lookup problem

**Printed textbook page:** 212. **Reference transcription pages:** 212–214.

> **Unverified OCR transcription:** This section retains the supplied PDF text layer. It is not certified verbatim: code syntax, mathematical symbols, and page boundaries may be corrupted. When two exercises begin on the same page, their excerpts overlap. Do not paste extracted code into a `.py` file without manual verification.

#### Printed page 212 (PDF page 226)

```text
# possible-anc-or-desc-I .
if ((search-0 is not middle and search-l is not middle)
or search-O is possible-anc-or-desc-1
or search-1 is possible-anc-or-desc-0):
return False
def search-target(source, target) :
rhile source and source is not target:
source = source.left if source.data > target.data else source.right
return source is target
# If we get here, we aTready know one of possible-anc-or-desc-0 or
# possibTe-anc-or-desc-7 has a path to niddle. Check if niddle has a path
# to possible-anc-or-desc-I or to possibJe-anc-or-desc-0.
return search-target (middle, possible-anc-or-desc-1
if search-O is middle else possible-anc-or-desc-0)
\l/hen the middle node does have an ancestor and descendant in the pair, the time complexity is
O(d), where d is the difference between the depths of the ancestor and descendant. The reason is
that the interleaved search will stop when the ancestor reaches the middle node, i.e., after O(d)
iterations. The search from the middle node to the descendant then takes O(d) steps to succeed.
When the middle node does not have an ancestor and descendant in the pair, the tirne complexity
is O(h), which corresponds to a worst-case search in a BST.
14.10 Tnn neNcr LooKUP PRoBLEM
Consider the problem of developing a web-service that takes a geographical location, and retums
the nearest restaurant. The service starts with a set of restaurant locations---each location includes
X and Y-coordinates. A query consists of a location, and should return the nearest restaurant (ties
can be broken arbitrarily).
One approach is to build fwo BSTs on the restaurant locations: 7x sorted on the X coordinates,
and Ty sorted on the Y coordinates. A query on location (p, q) can be performed by finding all the
restaurants whose X coordinate is in the interval lp - D,p + D], and all the restaurants whose Y
coordinate is in the interval Iq - D,q + D], taking the intersection of these two sets, and finding the
restaurant in the intersection which is closest to (p,q). Heuristically, if D is chosen correctly, the
subsets are small and a brute-force search for the closest point is fast. One approach is to start with
a small value for D and keep doubling it until the final intersection is nonempty.
There are other data structures which are more robust, e.g., Quadtrees and k-d trees, btit the
approach outlined above works well in practice.
Write a program that takes as input a BST and an interval and retums the BST keys that lie in the
interval. For example, for the tree in Figure 14.1 on Page198, and interval [16,31], you should
return 17, 19, 23, 29, 31.
Hint: How many edges are traversed when the successor function is repeatedly called m times?
Solution: A brute-force approach would be to perform a traversal (inorder, postordet or preorder)
of the BST and record the keys in the specified interval. The time complexity is that of the traversal,
i.e., O(n), where n is the number of nodes in the tree.
212
```

#### Printed page 213 (PDF page 227)

```text
The brute-force approach does not exploit the BST property-it would work unchanged for an
arbitrary binary tree.
We can use the BST property to prune the traversal as follows:
o If the root of the tree holds a key that is less than the left endpoint of the interval, the left
subtree cannot contain any node whose key lies in the interval.
o If the root of the tree holds a key that is greater than the right endpoint of the interval, the
right subtree cannot contain any node whose key lies in the interval.
o Otherwise, the root of the tree holds a key that lies within the interval, and it is possible for
both the left and right subtrees to contain nodes whose keys lie in the interval.
For example, for the tree in Figure 14.1 on Page 198, and interval 11.6,427, we begin the traversal
at A, which contains 19. Since 19 lies n 176,421, we explore both of A's children, namely B and I.
Continuing with B, we see B's key 7 is less than 16, so no nodes in B's left subtree can lie in the
interval 1L6,421. Similarly, when we get to l, since 43 > 42, we need not explore I's right subtree.
Interval = collections.namedtuple('Interval', 
('Ieft','right,))
def range-lookup-in-bst (tree , interval) :
def range-lookup-in-bst-helper (tree)
if tree is None:
return
if interval, left <= tree. data <= interval. right
# tree.data J.ies in the intervaT.
range-I ookup-in-bst-helper (tree . left )
result . append (tree . data)
range-lookup_in_bst_helper (tree . ri ght)
elif interval. left > tree. data:
range_Iookup_in_bst_helper (tree . ri ght)
else: # intervaT.right > tree.data
range-lookup_in_bst_helper (tree . left )
result = []
range-lookup-in-bst-helper (tree)
return result
The time complexity is tricky to analyze. It makes sense to reason about time complexity
in terms of the number of keys m that lie in the specified interval. We partition the nodes into
two categories-those that the program recurses on and those that it does not. For our working
example, the program recurses on A,B,F,G,H,I,],K,L,M,N. Not all of these have keys in the
specified interval, but no nodes outside of this set can have keys in the interval. Looking more
carefully at the nodes we recurse on, we see these nodes can be partitioned into three subsets-
nodes on the search path to L6, nodes on the search path to 42, and the rest. All nodes in the third
subset must lie in the result, but some of the nodes in the first two subsets may or may not lie in
the result. The traversal spends O(h) $ne visiting the first two subsets, md O(m) time traversing
the third subset-each edge is visited twice, once downwards, once upwards. Therefore the total
time complexity is O(m + fu), which is much better tharrO(n) brute-force approach when the tree is
balanced, and very few keys lie in the specified range.
213
```

#### Printed page 214 (PDF page 228)

```text
AugmentedBSTs
Thus far we have considered BSTs in which each node stores a key, a left child, a right child, and,
possibly, the parent. Adding fields to the nodes can speed up certain queries. As an example,
consider the following problem.
Suppose you needed a data structure that supports efficient insertion, deletion, lookup of integer
keys, as well as range queries, i.e., determining the number of keys that lie in an interval.
We could use a BST, which has efficient insertion, deletion and lookup. To find the number of
keys that lie in the interval lll,Vl,we could search for the first node with a key greater than or equal
to U, and then call the successor operation ( 9.10 on Page 123) until we reach a node whose key is
greater than V (or we run out of nodes). This has O(h + m) time complexity, where h is the height of
the tree and m is the number of nodes with keys within the interval. When m islarge, this become
slow
We can do much better by augmenting the BST. Specifically, we add a size field to each node,
which is the number of nodes in the BST rooted at that node.
For simplicity, suppose we want to find the number of entries that are less than a specified value.
As an example, say we want to count the mrmber of keys less than 40 in the BST in Figure 14.1 on
Page 198, and that each node has a size field. Since the root A's key, 19, is less than 40, the BST
property tells us that all keys in A's left subtree are less than 40. Therefore we cEu:I add 7 (which
we get from the left child's size field) and 1 (for A itself) to the running count, and recurse with A's
right child.
Generalizing, let's say we want to count all entries less than o. We initialize count to 0. Since
there can be duplicate keys in the tree, we search for the first occurrence of u in an inorder traversal
using Solution1.4.2 on Page 201. (If a is not present, we stop when we have determined this.) Each
time we take a left child, we leave count unchanged; each time we take a right child, we add one
plus the size of the corresponding left child. If u is present, when we reach the first occurrence of o,
we add the size of o's left child, The same approach can be used to find the number of entries that
are greater than o, less than or equal to o, and greater than or equal to u.
For example, to count the number of less than 40 in the BST in Figure 14.1 on Page 198 we would
search for 40. Since A's key, 19 is less than 40, we update count to 7 + L = 8 and continue from
L Since I's key, 43 is greater than 40, we move to I's left child, /. Since /'s key, 23 is less than 40,
update count to 8 + l. = 9, and continue from K. Since K's key,37 is less than 40, we update count
to 9 + 2 + L = 12, and continue from N. Since N's key, 41, is greater than 40, we move to N's left
child, which is empty. No other keys can be less than 40, so we retum count, i.e.,12. Note how we
avoided exploring A and K's left subtrees.
The time bound for these computations is O(h), since the search always descends the tree. When
m islarge, e.g., comparable to the total number of nodes in the tree, this approach is much faster
than repeated calling successor.
To compute the number of nodes with keys in the intervallL,Ul, first compute the number of
nodes with keys less than L and the number of nodes with keys greater than U, and subtract that
from the total number of nodes (which is the size stored at the root).
The size field can be updated on insert and delete without changing the O(h) time complexity
of both. Essentially, the only nodes whose size field change are those on the search path to the
added/deleted node. Some conditional checks are needed for each such node, but these add
constant time per node, leavingtheO(h) time complexity unchanged.
21.4
```
