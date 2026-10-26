# Exercise 18.2: Paint a Boolean matrix

**Printed textbook page:** 278. **Reference transcription pages:** 278–279.

> **Unverified OCR transcription:** This section retains the supplied PDF text layer. It is not certified verbatim: code syntax, mathematical symbols, and page boundaries may be corrupted. When two exercises begin on the same page, their excerpts overlap. Do not paste extracted code into a `.py` file without manual verification.

#### Printed page 278 (PDF page 292)

```text
return False
path . append (cur)
maze Icur. x] [cur. y] = BLACK
if cur == e:
return True
if any(
nap(search-maze-helper, (Coordinate (
cur.x - 1, cur.y), Coordinate(cur.x + 1, cur.y), Coordinate(
cur.x, cur,y - 1), Coordinate(cur.x, cur.y + 1)))):
return True
# cannot find a path, renove the entry added in path.append(cur),
del path[-1]
return FaIse
path = [J
if not search-maze-helper(s) :
return [] # No path between s and e.
return path
The time complexity is the same as that for DFS, namely O(lyl + lEl).
1,8.2 PerNr e BooLseN MATRIx
Let A be a Boolean 2D anay encoding a black-and-white image. The entry A(a,b) can be viewed
as encoding the color at entry (a,b). Call two entries adjacent if one is to the left, right, above or
below the other. Note that the definition implies that an entry can be adjacent to at most four other
entries, and that adjacency is symmetric, i.e., if e0 is adjacent to entry e1, then e1 is adjacent to e0.
Define a path from entry e0 to entry e1 to be a sequence of adjacent entries, starting at e0, ending
at e1, with successive entries being adjacent. Define the region associated with a point (1, fl to be all
points (l',7') such that there exists a path from (i, j) to (i' , j') n which all entries are the same color.
[r particular this implies (1, fl and (l',7') must be the stune color.
(a) 
O) 
(c)
Figure 18.6: The color of all squares associated with the first square marked with a x in (a) have been recolored to
yield the coloring in (b). The same process yields the coloring in (c).
Implement a routine that takes an n x m Boolean anay A together with an entry (r, g) ana flips the
color of the region associated with (x, y). See Figure 18.6 for an examPle of flipping'
278
mt
llll'll
]tL
-
LI
E
-t-'t
l:J rri
..
=I =F E
```

#### Printed page 279 (PDF page 293)

```text
Hint: Solve this conceptually, then think about implementation optimizations.
Solution: As with Solution 18.1 on Page 276, graph search can overcome the complexity of enu-
merative and random search solutions. Specifically, entries can be viewed as vertices, with vertices
corresponding to adjacent entries begin corurected by edges.
For the current problem, we are searching for all vertices whose color is the same as that of (x,y)
that are reachable fuorn(x,y). Breadth-first search is natural when starting with a set of vertices.
Specifically, we can use a queue to store such vertices. The queue is initialized to (x,y). The queue
is popped iteratively. Call the popped point p. First, we record p's initial colo1, and then flip its
color. Next we examine p neighbors. Any neighbor which is the same color as p's initial color is
added to the queue. The computation ends when the queue is empty. Correctness follows from the
fact that any point that is added to the queue is reachable from (r, y) via a path consisting of points
of the same colot, and all points reachable from (r, y) via points of the same color will eventually be
added to the queue.
def flip-color (x , y , A) :
Coordinate = collections,namedtuple('Coordinate,, (,x',,y,))
color = Alxl tyl
q = collections.deque([Coordinate(x, y)])
AIxl[y] = r - Alxllyl # Flips.
rhile q:
x, y = q,poplefto
for d in (0, r), (0, -r), (1, 0), (-1, 0):
next-x, next-y = x + d[0], y + d[1]
if (0 <= next_x < len(A) and 0 <= next_y < Ien(A[next_x])
and A[next-x] [next-y] == color):
# Flips the co7or.
AInext-x][next-y1 = 1 - AInext-x][next-y]
q. append (Coordinate (next_x , next_y) )
The time complexity is the same as that of BFS, i.e., O(mn). The space complexity is a little better
than the worst-case for BFS, since there are at most O(m + n ) vertices that are at the same distance
from a given entry.
We also provide a recursive solution which is in the spirit of DFS. It does not need a queue but
implicitly uses a stack, namely the function call stack.
def flip-color (x , y, A) :
color = Atxl [y]
Alxllyl 
= 1 - A[x]tyl 
# Elips.
for d in (0, 1), (0, -1), (I, 0), (-I, 0):
next-x, next-y = x + d[0], y + d[1]
if (0 <= next_x < len(A) and 0 <= next_y < len(A[next_x])
and AInext-x] [next-y] == color):
flip_coIor(next_x, next_y, A)
The time complexity is the same as that of DFS.
Both the algorithms given above differ slightly from traditional BFS and DFS algorithms. The
reason is that we have a color field already available, and hence do not need the auxiliary color field
traditionally associated with vertices BFS and DFS. Furtherrnore, since we are simply determining
reachability, we only need two colors, whereas BFS and DFS traditionally use three colors to track
state. (The use of an additional color makes it possible, for example, to answer questions about
cycles in directed graphs, but that is not relevant here.)
279
```
