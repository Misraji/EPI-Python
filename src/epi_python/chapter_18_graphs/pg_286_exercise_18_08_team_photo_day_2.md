# Exercise 18.8: Team photo day - 2

**Printed textbook page:** 286. **Reference transcription pages:** 286–288.

> **Unverified OCR transcription:** This section retains the supplied PDF text layer. It is not certified verbatim: code syntax, mathematical symbols, and page boundaries may be corrupted. When two exercises begin on the same page, their excerpts overlap. Do not paste extracted code into a `.py` file without manual verification.

#### Printed page 286 (PDF page 300)

```text
Given a positive integer fl, how would you compute a shortest addition chain exponentiation
program to evaluate rn?
Ailo ance d gr aph algorithms
Up to this point we looked at basic search and combinatorial properties of graphs. The algorithms
we considered were all linear time complexity and relatively straightforward-the major challenge
was in modeling the problem appropriately.
There are four classes of complex graph problems that can be solved efficiently, i.e., in polynomial
time. Most other problems on graphs are either variants of these or, very likely, not solvable by
polynomial tirne algorithms. These four classes are:
o Shortest path-given a graph, directed or undirected, with costs on the edges, find the minimum
cost path from a given vertex to all vertices. Variants include computing the shortest paths
for all pairs of vertices, and the case where costs are all nonnegative.
o Minimum spanning tree-$venan undirected graph G = (V,E), assumed to be connected, with
weights on each edge, find a subset E' of the edges with minimum total weight such that the
subgraph 5,' = (V,E') is connected.
o Matching-given an undirected graph, find a maximum collection of edges subject to the
constraint that every vertex is incident to at most one edge. The matching problem for
bipartite graphs is especially corunon and the algorithm for this problem is much simpler
than for the general case. A corunon variant is the maximum weighted matching problem in
which edges have weights and a maximum weight edge set is sought, subject to the matching
constraint.
o Maximumflow-gqvena directed graph with a capacity for each edge, find the maximum flow
from a given source to a given sink, where a flow is a function mapping edges to numbers
satisfying conservation (flow into a vertex equals the flow out of it) and the edge capacities.
The minimum cost circulation problem generalizes the maximum flow problem by adding
lower bounds on edge capacities, and for each edge, a cost Per unit flow.
These four problem classes have polynomial time algorithms and can be solved efficiently in
practice for very large graphs. Algorithms for these problems tend to be specialized, and the natural
approach does not always work best. For example, it is natural to apply divide-and-conquer to
compute the MST as follows. Partition the vertex set into two subsets, comPute MSTs for the
subsets independently, and then join these two MSTs with an edge of minimum weight between
them. Figure 18.9 on the facing page shows how this algorithm can lead to suboptimal results.
In this chapter we restrict our attention to shortest-path problems.
18.8 Tnl.u puoro pev-2
How would you generalize yout solution to Problem 13.9 on Page 193, to determine the largest
number of teams that can be photographed simultaneously subject to the same constraints?
Hint: Form a DAG in which paths correspond to valid placements.
Solution: Let G be the DAG with vertices corresponding to the teams as follows and edges from
vertex X to Y iff Team X can be placed behind Team Y.
Every sequence of teams where a team can be placed behind its predecessor corresponds to
a path in G. To find the longest such sequence, we simply need to find the longest path in the
286
```

#### Printed page 287 (PDF page 301)

```text
e
J
4
J
J
4
6
1
6
5
(a) A weighted undirected graph
(b) An MST built by divide-and-conquer
Irom the MSTs on la,b,cl and ld,e,fl.
The edge (D,e) is the lightest edge con-
necting the tYvo MSTS.
(c) An optimum MST.
Figure 18.9: Divide-and-conquer applied to the MST problem is suboptimum-the MST in (b) has weight 1.8, but the
MST in (c) has weight 14.
DAG G. We can do this, for example, by topologically ordering the vertices in G; the longest path
terminating at vertex a is the maximum of the longest paths terminating at u's fan-ins concatenated
with u itself.
class Graphvertex:
def --init--(self):
self.edges = []
self.max-distance = 0
def find-largest-nutnber-teams (G) :
def build-topological_ordering O :
def dfs (cur) :
cur.max-distance = 1
for next in cur.edges:
if not next.max-distance
dfs (next)
vertex-order . append ( cur)
vertex_order = []
:for g in G:
if not g.max-distance
dfs (g)
return vertex-order
def find-longest-path(vertex-order) 
:
max-distance = 0
while vertex-order:
u = vertex_order.popo
max-distance = nar(max_distance, u.max_distance)
for v in u.edges:
v.nax_distance = nar(v.max_distance, u.max_distance + 1)
return max-distance
return find-longest-path (bui 1d-topologi caI_ordering O )
The topological ordering computation is O(lyl + lEl) and dominates the computation time. Clearly
lVl is the number of teams. The number of edges E depends on the heights, but can be as high as
O(Vl\,e.g., when there is a path of length lyl - 1.
287
```

#### Printed page 288 (PDF page 302)

```text
Varianh LetT = {To,Tt,. . . ,Tn-tl be a set of tasks. Each task runs on a single generic server. Task
T; has a duration ri, arrrd a set P; (possibly empty) of tasks that must be completed before T; can be
started. The set is feasible if there does not exist a sequence of tasks (To,Tu . . . ,Tn-1, T6) starting and
ending at the same task such that for each consecutive pair of tasks, the first task must be completed
before the second task can begrn.
Given an instance of the task scheduling problem, compute the least amount of time in which
all the tasks can be performed, assuming an unlimited number of servers. Explicitly check that the
system is feasible.
288
```
