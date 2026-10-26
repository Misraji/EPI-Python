# Exercise 18.4: Deadlock detection

**Printed textbook page:** 281. **Reference transcription pages:** 281–281.

> **Unverified OCR transcription:** This section retains the supplied PDF text layer. It is not certified verbatim: code syntax, mathematical symbols, and page boundaries may be corrupted. When two exercises begin on the same page, their excerpts overlap. Do not paste extracted code into a `.py` file without manual verification.

#### Printed page 281 (PDF page 295)

```text
def fill-surrounded-regions (board) :
n, m = 1en(board), len(board[0])
q = collections.deque([
(i, j) for k in range(n) for i, j in ((k, 0), (k, m - 1))
I + t(i, j) for k in range(m) for i, j in ((0, k), (n - 1, k))l)
rhile q:
x, y = q.poplefto
if 0 <= x < n and 0 <= y < n and board[x]tyl ==,W,:
board Ix] tYl = 'r'
q.extend([(x - L, y), (x + 1, y), (x, y - t), (x, y + 1)])
board[:] = [t'B'if 
c != 'T'else 'I'l'for c in row] for row in boardl
The time and space complexity are the same as those for BFS, namely O(mn),where m andr? are the
number of rows and columns in A.
1.8.4 Dseorocx DErECrroN
High performance database systems use multiple processes and resource locking. These systems
may not provide mechanisms to avoid or prevent deadlock a situation in which two or more
competing actions are each waiting for the other to finish, which precludes all these actions from
progressing. Such systems must support a mechanism to detect deadlocks, as well as an algorithm
for recovering from them.
One deadlock detection algorithm makes use of a "wait-for" graph to track which other processes
a Process is currently blocking on. In a wait-for graph, processes are represented as nodes, and an
edge from Process P to Q implies Q is holding a resource that P needs and thus P is waiting for Q
to release its lock on that resource. A cycle in this graph implies the possibility of a deadlock. This
motivates the following problem.
Write a program that takes as input a directed graph and checks if the graph contains a cycle.
Hint:Focus on "back" edges.
Solution: We can check for the existence of a cycle in G by running DFS on G. Recall DFS maintains
a color for each vertex. Initially, all vertices are white. When a vertex is first discovered, it is colored
gray. When DFS finishes processing a vertex, that vertex is colored black.
As soon as we discover an edge from a gray vertex back to a gray vertex, a cycle exists in G and
we can stop. Conversely, if there exists a cycle, once we first reach vertex in the cycle (call it o), we
will visit its predecessor in the cycle (call it a) before finishing processing o, i.e., we will find an edge
from a gray to a gray vertex. h summary, a cycle exists if and only if DFS discovers an edge from
a gtay vertex to a gray vertex. Since the graph may not be strongly connected, we must examine
each vertex, and run DFS from it if it has not already been explored.
class Graphvertex
white, gray, black = range(3)
def --init--(self):
self.color = Graphvertex.white
self.edges = []
287
```
