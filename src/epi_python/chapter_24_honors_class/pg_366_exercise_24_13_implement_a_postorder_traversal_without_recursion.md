# Exercise 24.13: Implement a postorder traversal without recursion

**Printed textbook page:** 366. **Reference transcription pages:** 366–367.

> **Unverified OCR transcription:** This section retains the supplied PDF text layer. It is not certified verbatim: code syntax, mathematical symbols, and page boundaries may be corrupted. When two exercises begin on the same page, their excerpts overlap. Do not paste extracted code into a `.py` file without manual verification.

#### Printed page 366 (PDF page 380)

```text
Thebrute-force algorithmentails findingforeach inputtimestamp, themaximuminthe subarray
consisting of elements whose timestamps lie in the window ending at that timestamp. The time
complexity is O(nw), where n is the length of A. The reason is that every window may have up to
zu + 1 elements.
The intuition for improving the time complexity of the brute-force approach stems from noting
that as we advance the window only the boundary changes. Specifically, some older elements fall
out of the windoW and a new element is added. Therefore a queue is a perfect representation for
the window We need the maximum traffic within each window, which suggests using Solution 8.9
on Page 109.
Initialize Q to an empty queue with maximum. Iteratively enqueue (t;,t) in order of increasing
l. For each l, iteratively dequeue Q until the difference of the timestamp at Q's head and fi is
less than or equal to ru. The sequence of maximum values in the queue for each f is the desired
result. For the input in Figure 2a.5@) on the previous page with window size of 3, the output is
((0,1.3), (2,2.5),(3,3.7),(5,3.7),(6,3.7),(8,2.6),(9,2.6),(1.4,1..7)). 
See Figure 24.5b) on the preceding
page for a graphical representation.
class TrafficElenent:
def --init--(self, 
time, volume)
self.time = time
self.volume = volume
# FolTowing operators are needed for Queue[ithltax with naxinun
def --1t--(self , other) :
return self,volune < other,volume
def --eq--(seIf, 
other):
return sel,f.time == other.time and self.volume == other.volume
def calculate-traffic-volumes (A, w) :
sliding-window = Queuel{ithilaxo
maximum-volumes = []
for traffic-info 
in A:
sliding-window . enqueue ( traff ic-info)
rhile traffic-info.time 
- sliding-window.headO.time > w:
sliding-window. dequeue o
maximum-volumes . append (
TrafficEter,rent (traffic-info 
. time , sliding-window ' max O . volume) )
return maximum-volunes
Each element is enqueued once. Each element is dequeued at most once. Since the queue with
maximum data structure has an O(1) amortized time complexity per operation, the overall time
complexity is O(n). The additional space complexity is O(w).
24.13 INrprsl{sNr A posroRDER TRAVERSAL wITHour nncunsIoN $
This problem is concerned with traversing nodes in a binary tree in postorder fashion. See Page 113
for details and examples of these traversals. Generally speaking, a traversal computation is easy to
implement if recursion is allowed.
366
```

#### Printed page 367 (PDF page 381)

```text
Write a program which takes as input a binary tree and performs a postorder traversal of the tree.
Do not use recursion. Nodes do not contain parent references.
Hint: Study the function call stack for the recursive versions.
Solution: The brute-force approach to remove recursion from a function is to mimic the function
call stack with an explicit stack. One of the challenges with this approach is to determine where to
retum to.
Now we address the problem of implementing a postorder traversal without recursion. First
we discuss a roundabout way of doing this. An inverted preorder traversal is the following: visit
root, inverted preorder traverse the right subtree, then inverted preorder traverse the left subtree.
For example, the inverted preorder traversal of the tree in Figure 9.1 on PageTl}visits nodes in the
following order: <A, l, O, P, I, K N, L, M, B, F, G, H, C, E, D).
Intuitively, since the inverted preorder traversal is visit root, traverse right, traverse left, its
reverse is traverse left, traverse right, visit root, i.e., the postorder traversal. Therefore, one way to
comPute the postorder traversal visit sequence without using recursion is to perform an inverted
preorder traversal and instead of outputting nodes, we store them. When the inverted preorder
traversal is complete, we iterate through the nodes in last-in, first-out ordel, which gives the
postorder traversal sequence.
The inverted preorder traversal itself can be performed nonrecursively using the solution to the
first part of this problem, with the order in which the left and right children are pushed swapped.
This algorithm is implemented in the code below.
def postorder-traversal (tree) :
def inverted-preorder_traversal (tree) :
path-stack, result = [tree] , []
rhile path_stack:
curr = path_stack.popo
if not curr:
continue
result . append (curr. data)
path_stack. extend([curr. 1eft, curr.right])
return result
return inverted_preorder_traversal (tree) [: : -1]
The time and space complexity are both O(n), where n is the number of nodes in the tree.
In addition to its being unintuitive, a more technical limitation of the approach given above is
that it requires O(n) additional space. If the result is to be retumed as an array, this is unavoidable.
However, if we are simply required to print the nodes, it is possible to reduce the space complexity
to O(h) where fu is the height of the tree.
We know that a recursive implementation of a postorder traversal takes O(n) and O(h) space, so
we should be able to achieve this complexity by using a stack to mirnic the function call stack. One
challenge is keeping track of where to retum to, since there are two recursive calls. The function
call stack keeps a retum address, but instruction addresses are not accessible from user code. We
can determine where to continue from by inspecting where the last visited node is relative to the
current node. This is explained in more detail below
367
```
