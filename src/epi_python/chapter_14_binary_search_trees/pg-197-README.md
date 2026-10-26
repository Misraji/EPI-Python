# Chapter 14: Binary Search Trees

**Starts at printed page 197.** [Repository overview](../../../README.md)

**Source:** user-supplied EPI Python PDF (2016/2017 edition). **Transcription warning:** PDF text extraction contains OCR errors, especially in code. Consult the original PDF for ambiguous expressions and diagrams.

## Original chapter introduction (unverified PDF text layer)

### Printed page 197

```text
Cnapren
Binary Search Trees
The number of trees which can be formed with n + 1.
gitsen knots a, F,y,... = 1r + 1)'-1.
-"ATheorem on hees,"
A. Cavrrv,1889
BSTs are a workhorse of data structures and can be used to solve almost every data structures
problem reasonably efficiently. They offer the ability to efficiently search for a key as well as find
the min aurrd max elements, look for the successor or predecessor of a search key (which itself need
not be present in the BST), and enumerate the keys in a range in sorted order.
BSTs are similar to arrays in that the stored values (the "keys") are stored in a sorted order.
However, unlike with a sorted array, keys can be added to and deleted from a BST efficiently.
Specifically, a BST is a binary tree as defined in Chapter 9 in which the nodes store keys that are
comparable, e.9,, integers or strings. The keys stored at nodes have to respect the BST property-the
key stored at a node is greater than or equal to the keys stored at the nodes of its left subtree and
less than or equal to the keys stored in the nodes of its right subtree. Figure 14.1 on the following
page shows a BST whose keys are the first 16 prime numbers.
Key lookup, insertion, and deletion take time proportional to the height of the tree, which can
in worst-casebe O(n), if insertions and deletions are naively implemented. However, there are
implementations of insert and delete which guarantee that the tree has height O(logn). These
require storing and updating additional data at the tree nodes. Red-black trees are an example of
height-balanced BSTs and are widely used in data structure libraries.
A common mistake with BSTs is that an object that's present in a BST is not updated. The
consequence is that a lookup for that object returns false, even though it's still in the BST. As a rule,
avoid putting mutable objects in a BST. Otherwise, when a mutable object that's in a BST is to be
updated, always first remove it from the tree, then update it, then add it back.
The BST prototype is as follows:
class BSTNode:
def --init--(self 
, data=None, left=None, right=None):
self.data, self.left, 
self.right 
= data, left, 
right
Binary search trees boot camp
Searching is the single most fundamental application of BSTs. Unlike a hash table, a BST offers the
ability to find the min and max elements, and find the next largest/next smallest element. These
operations, along with lookup, delete and find, take time O(logn) for library implementations of
BSTs. Both BSTs and hash tables use O(n) space-in practice, a BST uses slightly more space.
197
```

### Printed page 198

```text
()
N
i\
il
I
l)
f.
(
II
,14
Flgure 14.1: An example of a BST
The following program demonstrates how to check if a given value is present in a BST. It is a
nice illustration of the power of recursion when operating on BSTs.
def search-bst(tree, key):
return (tree
if not tree or tree.data == key else search-bst(tree.left, key)
if key < tree.data else search-bst(tree.right, key))
Since the program descends tree with in each step, and spends O(1) time per level, the time
complexity is O(h), where h is the height of the tree.
With a BST you can iterate
it is balanced).
ln
of whether
Some problems need a combination of a BST and a hashtable. For example, if you insert
student objects into a BST and entries are ordered by GPA, and then a student's GPA needs to
be updated and all we have is the student's name and new GPA, we cannot find the student by
name without a fulItraversal. However, with an additional hash table, we cEIn directly go to
the corresponding entry in the tree.
Sometimes, it's necessary to augment a BST to make it possible to manipulate more complicated
data, e.g., intervals, and efficiently support more complex queries, e.9., the number of elements
in a range ( on Page 214).
The BST property is a global property-a binary tree may have the property that each node's
key is greater than the key at its left child and smaller than the key at its right child, but it may
not be a BST.
Table 14.1 : Top Tips for Binary Search Trees
Knoza your binary search tree libraries
Some of the problems in this chapter entail writing a BST class; for others, you can use a BST library.
Python does not come with a built-in BST library.
198
```
