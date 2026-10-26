# Exercise 14.1: Test if a binary tree satisfies the BST property

**Printed textbook page:** 199. **Reference transcription pages:** 199–200.

> **Unverified OCR transcription:** This section retains the supplied PDF text layer. It is not certified verbatim: code syntax, mathematical symbols, and page boundaries may be corrupted. When two exercises begin on the same page, their excerpts overlap. Do not paste extracted code into a `.py` file without manual verification.

#### Printed page 199 (PDF page 213)

```text
The sortedcont.ainers module the best-in-class module for sorted sets and sorted dictionaries-
it is performant, has a clean API that is well documented, with a responsive community. The
underlying data structure is a sorted list of sorted lists. Its asymptotic time complexity for inserts
and deletes is O(l|i)) since these operations entail insertion into a list of length roughly 1k, ruther
than the O(log n)) of balanced BSTs. In practice, this is not an issue, since CPUs are highly optimized
for block data movements.
In the interests of pedagogy, we have elected to use the bintrees module which implements
sorted sets and sorted dictionaries using balanced BSTs. Howeveq, any reasonable interviewer
should accept sortedcontainers wherever we use bintrees.
Below, we describe the functionalities added by bintrees.
o insert(e) inserts new element e in the BST.
o discard(e) removes e in the BST if present.
o min-itemO/max-itemO yield the smallest and largest key-value pair in the BST.
o min-keyO/max-keyO yield the smallest and largest key in the BST.
o pop--rninO/pop:naxO remove the retum the smallest and largest key-value pair in the BST.
It's particularly important to note that these operations take O(logn), since they are backed by the
underlying tree.
The following program illustrates the use of bintrees.
t = bintrees.RBTree([(5,
(6,
'AIfa ') , (2 , 'Bravo') , (7 , 'Char1ie') , (3 , 'Delta ') ,
'Echo') I )
print(t[2]) 
#'Bravo'
print(t.min-itenO, t.max-itemO) # (2, 'Bravo'), (7, 'CharTie')
# {2: 'Bravo', 3: 'Delta', 5: 'A7fa', 6
t . insert (9 , 'Golf ' )
print (t)
'Echo', 7: 'Charlie', 9: 'GoIf']
print(t.min-keyO, t.max-keyO) # 2, 9
t. discard(3)
print(t) 
# {2: 'Bravo', 5: 'A7fa', 6: 'Echo', 7: 'Charlie', 9: 'Golf'}
#a=(2:'Bravo')
a = t.pop_mino
print(t) 
# {5: 'AIfa', 6: 'Echo', 7: 'CharTie', 9: 'colf'}
*b=(9,'colf')
b = t.pop-nax()
print (t) # {5: 'Alfa' , 6: 'Echo' , 7: 'CharTie'}
14.1 Tnsr lr A BTNARy IREE sATrsFrEs rnn BST pRopERry
Write a Program that takes as input a binary tree and checks if the tree satisfies the BST property.
Hint: ls it correct to check for each node that its key is greater than or equal to the key at its left child and less
than or equal to the key at its right child?
199
```

#### Printed page 200 (PDF page 214)

```text
Solution: A direct approach, based on the definition of a BST, is to begin with the root, and compute
the maximum key stored in the root's left subtree, and the minimum key in the root's right subtree.
We check that the key at the root is greater than or equal to the maximum from the left subtree and
less than or equal to the minimum from the right subtree. If both these checks pass, we recursively
check the root's left and right subtrees. If either check fails, we retum false.
Computing the minimum key in a binary tree is straightforward: we take the minimum of the
key stored at its root, the minimum key of the left subtree, and the minimum key of the right subtree.
The maximum key is computed similarly. Note that the minimum can be in either subtree, since a
general binary tree may not satisfy the BST property.
The problem with this approach is that it will repeatedly traverse subtrees. In the worst-case,
when the tree is a BST and each node's left child is empty, the complexrty is O(nz), where n is the
number of nodes. The complexity can be improved to O(n) by caching the largest and smallest keys
at each node; this requires O(n) additional storage for the cache.
We now present two approaches which have O(n) time complexity.
The first approach is to check constraints on the values for each subtree. The initial constraint
comes from the root. Every node in its left (right) subtree must have a key less than or equal (greater
than or equal) to the key at the root. This idea generalizes: if all nodes in a tree must have keys
in the range [/, uf , and the key at the root is zu (which itself must be between [, u], otherwise the
requirement is violated at the root itself), then all keys in the left subtree must be in the range [, ar],
and all keys stored in the right subtree must be in the range [ru, a].
As a concrete example, when applied to the BST in Figure 14.1 on Page198, the initial range is
[-*, *]. For the recursive call on the subtree rooted at B, the constraint is [-oo,19]; the 19 is the
upper bound required by A on its left subtree. For the recursive call starting at the subtree rooted at
F, the constraint is [7,19]. For the recursive call starting at the subtree rooted at K, the constraint is
123,431. The binary tree in Figure 9.1 on Page 112 is identified as notbeing a BST when the recursive
call reaches C-the constraint is [-oo,6], but the key at F is 277, so the tree cannot satisfy the BST
property.
def is-binary-tree-bst(tree, low-range=float('-inf'), high-range=float('inf'))
if not tree:
return True
elif not low-range <= tree.data <= high-range:
return False
return (is-binary-tree-bst (tree. left , low-range , tree. data)
and is-binary-tree-bst(tree.right, tree.data, high-range))
The time complexity is O(n), and the additional space complexity is O(ft), where h is the height of
the tree.
Alternatively, we can use the fact that an inorder traversal visits keys in sorted order. Further-
more, if an inorder traversal of a binary tree visits keys in sorted order, then that binary tree must
be a BST. (This follows directly from the definition of a BST and the definition of an inorder walk.)
Thus we can check the BST property by performing an inorder traversal, recording the key stored
at the last visited node. Each time a new node is visited, its key is compared with the key of the
previously visited node. If at any step in the walk, the key at the previously visited node is greater
than the node currently being visited, we have a violation of the BST property.
All these approaches explore the left subtree first. Therefore, even if the BST property does not
hold at a node which is close to the root (e.g., the key stored at the right child is less than the key
200
```
