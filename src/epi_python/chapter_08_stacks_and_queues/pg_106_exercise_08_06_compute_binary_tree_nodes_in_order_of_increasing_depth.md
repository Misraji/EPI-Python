# Exercise 8.6: Compute binary tree nodes in order of increasing depth

**Printed textbook page:** 106. **Reference transcription pages:** 106–106.

> **Unverified OCR transcription:** This section retains the supplied PDF text layer. It is not certified verbatim: code syntax, mathematical symbols, and page boundaries may be corrupted. When two exercises begin on the same page, their excerpts overlap. Do not paste extracted code into a `.py` file without manual verification.

#### Printed page 106 (PDF page 120)

```text
Know your queue libraries
Some of the problems require you to implement your own queue class; for others, use the
collections . deque class.
o q. append(e) pushes an element onto the queue. Not much can go wrong with a call to push.
. q[0] willretrieve,butnotremove,theelementatthefrontof thequeue. Similarly,q[-1] will
retrieve, but not remove, the element at the back of the queue.
o q. popleft O will remove and return the element at the front of the queue.
Dequeing or accessing the head/tail of an empty collection results in an IndexError exception being
raised.
8.6 CoNrpurs BTNARv rREE NoDES IN oRDER oF INCREASING DEprH
Binary trees are formally defined in Chapter 9. In particular, each node in a binary tree has a depth,
which is its distance from the root.
Given a binary tree, return an array consisting of the keys at the same level. Keys should appear
in the order of the corresponding nodes' depths, breaking ties from left to right. For example, you
should retum <<31,4>, <6,6), <271,,561,2,271>, <28,0,3,1.,28>, <17,40'1.,257>, (641)) for the binary tree
in Figure 9.1 on Page112.
Hint: First think about solving this problem with a pair of queues.
Solution: A brute force approach might be to write the nodes into an array while simultaneously
computing their depth. We can use preorder traversal to compute this array-by traversing a node's
left child first we c€u:r ensure that nodes at the same depth are sorted from left to right. Now we
can sort this array using a stable sorting algorithm with node depth being the sort key. The time
complexity is dominated by the time taken to sort, i.e., O(nlogn), and the space complexity is O(n),
which is the space to store the node depths.
Intuitively, since nodes are already presented in a somewhat ordered fashion in the tree, it
should be possible to avoid a full-blow sort, thereby reducing time complexity. Furthermore, by
processing nodes in order of depth, we do not need to label every node with its depth.
In the following, we use a queue of nodes to store nodes at depth I and a queue of nodes at
depth I + 1. After all nodes at depth I are processed, we are done with that queue, and can start
processing the queue with nodes at depth I + 1, putting the depth I + 2 nodes in a new queue.
def binary-tree-depth-order (tree) :
result = []
if not tree:
return result
curr-depth-nodes = [tree]
vhile curr-depth-nodes:
result. append([curr. data for curr in curr-depth-nodes])
curr-depth-nodes = [
child
for curr in curr-depth-nodes for child in (curr.Ieft, 
curr.right)
if child
l
return result
106
```
