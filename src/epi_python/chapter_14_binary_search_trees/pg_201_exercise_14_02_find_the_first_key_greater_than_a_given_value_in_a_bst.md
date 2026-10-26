# Exercise 14.2: Find the first key greater than a given value in a BST

**Printed textbook page:** 201. **Reference transcription pages:** 201–201.

> **Unverified OCR transcription:** This section retains the supplied PDF text layer. It is not certified verbatim: code syntax, mathematical symbols, and page boundaries may be corrupted. When two exercises begin on the same page, their excerpts overlap. Do not paste extracted code into a `.py` file without manual verification.

#### Printed page 201 (PDF page 215)

```text
stored at the root), their time complexity is still O(n).
We can search for violations of the BST property in a BFS manner, thereby reducing the time
complexity when the property is violated at a node whose depth is small.
Specifically, we use a queue, where each queue entry contains a node, as well as an upper and
a lower bound on the keys stored at the subtree rooted at that node. The queue is initialized to the
root, with lower bound -oo and upper bound oo, We iteratively check the constraint on each node.
If it violates the constraint we stop-the BST property has been violated. Otherwise, we add its
children along with the corresponding constraint.
For the example in Figure 14.1 on Page 198, we initialize the queue with (A, [-m, m]). Each
time we pop a node, we first check the constraint. We pop the first entry, (A, [-*, -]), and add
its children, with the corresponding constraints, i.e., (B,l-*,19]) and (1,119,m]). Next we pop
(B,I-*,191), and add its children, i.e., (C,l-*,71) and (D, [7,19]). Continuing through the nodes,
we check that all nodes satisfy their constraints, and thus verify the tree is a BST.
If the BST property is violated in a subtree consisting of nodes within a particular depth, the
violation will be discovered without visiting any nodes at a greater depth. This is because each
time we enqueue an entry, the lower and upper bounds on the node's key are the tightest possible.
def is-binary-tree-bst (tree) :
QueueEntry = collections . namedtupJ.e ('QueueEntry' , ('node ' , 'Iower' ,
'upper ' ) )
bfs-queue = collections . deque (
IQueueEntry(tree, float('-inf 
'), float('inf 
'))])
rhile bfs-queue:
front = bfs_queue. popleft ()
if front . node:
if not front. lower <= front. node . data <= front . upper:
return False
bfs-queue += [
QueueEntry(front.node.left, front.lower, front.node.data),
QueueEntry(front.node.right, front.node.data, front.upper)
l
return True
The time complexity isO(n), and the additional space complexity is O(n).
14.2 FINo THE FIRST KEY GREATER THAN A GIVEN VALUE TN a BST
Write a pro$am that takes as input a BST and a value, and retums the first key that would appear
in an inorder traversal which is greater than the input value. For example, when applied to the BST
in Figure 14.1 on Page 198 you should retum 29 for input 23.
Hint: Pertorm binary search, keeping some additional state.
Solution: We can find the desired node in O(n) tnte, where n is the number of nodes in the BS! by
doing an inorder walk. This approach does not use the BST property.
A better approach is to use the BST search idiom. We store the best candidate for the result and
update that candidate as we iteratively descend the tree, eliminating subtrees by comparing the
keys stored at nodes with the input value. Specifically, if the current subtree's root holds a value
less than or equal to the input value, we search the right subtree. If the current subtree's root stores
201,
```
