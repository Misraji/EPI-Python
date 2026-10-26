# Exercise 24.14: Compute fair bonuses

**Printed textbook page:** 368. **Reference transcription pages:** 368–369.

> **Unverified OCR transcription:** This section retains the supplied PDF text layer. It is not certified verbatim: code syntax, mathematical symbols, and page boundaries may be corrupted. When two exercises begin on the same page, their excerpts overlap. Do not paste extracted code into a `.py` file without manual verification.

#### Printed page 368 (PDF page 382)

```text
We maintain a stack of nodes which evolves exactly as the sequence of nodes that the recursive
algorithm makes calls from.
To determine when a nonleaf at the top of the stack is ready for visiting, we need to know if we
are moving back up the tree, and if so, which side of this nonleaf we are retuming from. If we are
coming back up from the left, we do not want to push the left child again, but do want to push the
right child, since we still need to mimic the second recursive call. If we are coming up from the
right child both children have been visited, so we want to pop the stack and visit the nonleaf node.
# We use stack and previous node pointer to simul.ate postorder traversal
def postorder-traversal (tree) :
if not tree: # Enpty tree.
return []
path-stack, prev, postorder-sequence = [tree], None, []
while path-stack:
curr = path-stack[-1]
if not prev or prev.Ieft is curr or prev.right is curr:
# We cane down to curr fron prev.
if curr. left: 
# Traverse 7eft.
path-stack. append (curr . left)
elif curr. right 1 # Traverse right .
path-stack. append (curr . right)
else: 
# Leaf node, rrisit current node.
postorder-sequence. append(curr. data)
path-stack.pop o
elif curr.left 
is prev:
# Done with Left, now traverse right,
if curr. right:
path-stack. append (curr. ri ght)
else: 
# No right child, so vjsit curr.
postorder-sequence. append(curr. data)
path-stack .pop o
else :
# Finished traversing Teft and right, so visit curr
postorder-sequence . append (curr. data)
path-stack.pop o
prev = curr
retufn postorder-sequence
The time complexity is O(n), since we perform a constant amount of work per node (a push and a
pop). The space complexity is O(h), since the stack corresponds to a path starting at the root.
24.74 Covrpurs FArR BoNUSEs I
You manage a team of developers. You have to give concert tickets as a bonus to the develoPers.
For each developer, you know how many lines of code he wrote the previous week, and you want
to reward more productive developers. 
1
The developers sit in a row. Each developer, save for the first and last, has fwo neighbors, You
must give each developer one or more tickets h such a way that if a developer has written more
1In practice, lines-of-code is a very poor productivity metric.
368
```

#### Printed page 369 (PDF page 383)

```text
lines of code than a neighbor, then he receives more tickets than his neighbor. (If two neighboring
developers have written an equal number of lines of code, they do not have to receive the same
number of tickets.)
For example, if Andy, Bob, Charlie, and David sit in a row from Ieft to right, and they wrote
300,400, 200, and 500 lines of code, respectively, the previous week, then Andy and Charlie should
receive one ticket each, and Bob and David should receive two tickets, for a total of six tickets. If
instead they wrote 300,400,400, and 400 lines of code, respectively, then Andy, Charlie, and David
should receive a single ticket and Bob should receive two tickets for a total of five tickets.
Your task is to develop an algorithm that computes the minimum number of tickets you need
to buy to satisfy the constraint.
Write a program for computing the minimum number of tickets to distribute to the developers,
while ensuring that if a developer has written more lines of code than a neighboq, then he receives
more tickets than his neighbor.
Hlnf; Consider iteratively improving an assignment that may not satisfy the constraint.
Solution: A brute-force approach is to start by grving each developer a ticket. Next we perform
the following iteration. We check if all developers are satisfied. If they are all satisfied, we are
done. Otherwise, if some developer is not satisfied, i.e., he has written more lines of code than a
neighbor, but does not have more tickets than that neighbol, we give him one more ticket than his
neighbor. This approach uses the minimum number of tickets initially, and every additional ticket
that is given is necessary. The time complexity is O(kn2), where k is the maximum number of tickets
given to any single developer, and n is the number of developers.
The key insight to a better algorithm is the observation that the least productive developer
never needs to be given more than a single ticket. We can propagate this observation by processing
developers in increasing order of productivity. Subsequently, when we process a developer if his
neighbors have been processed, he must be at least as productive as them. If a developer is more
productive than a neighbor, he must be given at a minimum one more ticket than that neighbor.
If a developer is only as productive as his neighbors, we only need give him the same number of
tickets, as per the problem specification.
For the given example, our algorithm starts by trving 1 ticket to David. Andy is next in order
of productivity, so we give him 1 ticket, since he has only one neighbor, who is more productive
than him. Next we process Bob. He is more productive than Andy, so we give him 1 + 1 = 2 tickets.
Then comes Charlie. He is a neighbor of Charlie and David, and is more productive than both, so
we give him max(2,1) + 1 = 3 tickets, for a total of 7 tickets.
This approach yields the correct result because once a developer is processed, we only process
developers who are at least as productive in the future, meaning that once his bonus is assigned, it
will never need updating in the future. Furthermore, any bonus that we assign is forced upon us
by the problem constraints.
A min-heap is a suitable data structure for processing the developers, and is used in the following
Program.
def calculate-bonus (productivity) :
# Stores (productivity, index)-pair in nin_heap where ordered by
# productivity.
EmployeeData = collections. namedtuple('EmployeeData', ('productivity',
369
```
