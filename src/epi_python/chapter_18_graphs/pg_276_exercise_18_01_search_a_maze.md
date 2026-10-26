# Exercise 18.1: Search a maze

**Printed textbook page:** 276. **Reference transcription pages:** 276–277.

> **Unverified OCR transcription:** This section retains the supplied PDF text layer. It is not certified verbatim: code syntax, mathematical symbols, and page boundaries may be corrupted. When two exercises begin on the same page, their excerpts overlap. Do not paste extracted code into a `.py` file without manual verification.

#### Printed page 276 (PDF page 290)

```text
return True
elif curr in visited or curr not in graph:
return False
visited. add(curr)
return any(is-reachable-dfs(graph, team, dest) for team in graphIcurr])
return is-reachable-dfs(build-graphO, team-a, team-b)
The time complexity and space complexity are both O(E), where E is the number of outcomes.
to use a graph when the
e.8.,
segments between cities.
More generally, consider using a graph when you need to analyze any binary relationship,
between objects, such as interlinked webpages, followers in a social graph, etc. In such cases,
quite often the problem can be reduced to a well-known graph problem.
Some graph problems entail analyzing structure, e.g., looking for cycles or connected compo-
nents. DFS works particularly well for these applications.
Some graph problems are related to optimization, e.g., find the shortest path from one vertex to
another. BFS, Diikstra's shortest path algorithm, and minimum spanning tree are examples
of graph algorithms appropriate for optimization protlems.
Table 18.1: Top Tips for Graphs
Graph search
Computing vertices which are reachable from other vertices is a fundamental operation which
can be performed in one of two idiomatic ways, namely depth-first search (DFS) and breadth-first
search (BFS). Both have linear time complexity-O(lyl + lEl) to be precise. In the worst-case there is
a path from the initial vertex covering all vertices without any repeats, and the DFS edges selected
correspond to this path, so the space complexity of DFS is O(lyl) (this space is implicitly allocated
on the function call stack). The space complexity of BFS is also O(IVD, since in a worst-case there
is an edge from the initial vertex to all remaining vertices, implying that they will all be in the BFS
queue simultaneously at some point.
DFS and BFS differ from each other in terms of the additional information they provide, e.g.,
BFS can be used to compute distances from the start vertex and DFS can be used to check for the
presence of cycles. Key notions in DFS include the concept of discoaery time au-ld finishing time for
vertices.
18.1 SEancH A MAZE
It is natural to apply graph models and algorithms to spatial problems. Consider a black and white
digitized image of a maze-white pixels represent open €ueas and black spaces are walls. There are
two special white pixels: one is designated the entrance and the other is the exit. The goal in this
problem is to find a way of getting from the entrance to the exit, as illustrated in Figure 18.5 on the
next page.
Given a2D array of black and white entries representing amaze with designated entrance and exit
points, find a path from the entrance to the exit, if one exists.
276
```

#### Printed page 277 (PDF page 291)

```text
E
s
-'l
rr E
L
J
r J
L -1
s J
(a) A maze. 
(b) A path lrom entrance to exit. 
(c) A shortest path from entrance to exit.
Figure 18.5: An instance of the maze search problem, with two solutions, where S and E denote the entrance and exit,
respectively.
Hirzf: Model the maze as a graph.
Solution: A brute-force approach would be to enumerate every possible path from entry to exit.
However, we know from Solution 16.3 on Page 242 that the number of paths is astronomical. Of
course, pruning helps, since we can stop as soon as a path hits a black pixel, but the worse-case
behavior of enumerative approaches is still very bad.
Another approach is to perform a random walk moving from a white pixel to a random adjacent
white pixel. Given enough time this will find a path, if one exists. However, it repeats visits, which
retards the progress. The random walk does suggest the right way-we should keep track of pixels
that we have already visited. This is exactly what DFS and BFS do to ensure progress.
This suggests modeling the maze as a graph. Each vertex corresponds to a white pixel. We will
index the vertices based on the coordinates of the corresponding pixel, i.e., vertex 
",,i 
corresponds
to the white entry at (i, il lr:.the 2D array. Edges model adjacent white pixels.
Now, run a DFS starting from the vertex corresponding to the entrance. If at some point,
we discover the exit vertex in the DFS, then there exists a path from the entrance to the exit.
If we implement recursive DFS then the path would consist of all the vertices in the call stack
corresponding to previous recursive calls to the DFS routine.
This problem can also be solved using BFS from the entrance vertex on the same graph model.
The BFS tree has the property that the computed path will be a shortest path from the entrance.
However BFS is more difficult to implement than DFS since in DFS, the compiler implicitly handles
the DFS stack, whereas in BFS, the queue has to be explicitly coded. Since the problem did not call
for a shortest path, it is better to use DFS.
WHITE, BLACK = range(2)
Coordinate = collections. namedtuple ('Coordinate' , ('
'v') )
def search-maze (maze , s , e) :
# Perforn DFS to find a feasible path.
def search_maze-helper (cur) :
# Checks cur is within naze and is a rvhite pixe7.
if not (0 <= cur.x < Ien(maze) and 0 <= cur.y < len(maze[cur.x])
and maze [cur. x] [cur. y] == I{HITE) :
fl E
r J
r J
r J
s
277
```
