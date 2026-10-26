# Chapter 18: Graphs

**Starts at printed page 273.** [Repository overview](../../../README.md)

**Source:** user-supplied EPI Python PDF (2016/2017 edition). **Transcription warning:** PDF text extraction contains OCR errors, especially in code. Consult the original PDF for ambiguous expressions and diagrams.

## Original chapter introduction (unverified PDF text layer)

### Printed page 273

```text
Crr,q.preR.
Graphs
Concerning these bridges, it was asked whethu anyone could arrange a route in
such a way that he would cross each bridge once and only once.
- "The solution of a problem relating to the geometry of position,"
L.Eul:x,174l
Informally, a graph is a set of vertices and coru:rected by edges. Formally, a directed graph is a set
V of aertices and a set E cVxV ofedges. Givenanedge e = (u,a),thevertexz is its source,anda
is its slnk. Graphs are often decorated, e.g.,by adding lengths to edges, weights to vertices, a start
vertex, etc. A directed graph can be depicted pictorially as in Figure 18.1.
A path in a directed graph ftom u to vertex u is a sequence of vertices (uo,at, . . . ,rJn_t) where
uo = tt, an-i. = o, and each (o;,o;a1) is an edge. The sequence may consist of a single vertex. The
length of the path (uo,ur,.. .,an-t) is n * 1. Intuitively, the length of a path is the number of edges
ittraverses. If thereexistsapathfrom LttoTJ, aissaid tobereachablefromu. For example,the
sequence (a,c,e,d,h) is a path in the graph represented in Figure 18.1.
5
Flgure 18.1 : A directed graph with weights on edges.
A directed acyclic graph (DAG) is a directed graph in which there are no cycles, i.e., paths which
contain one or more edges and which begin and end at the same vertex. See Figure 18.2 on the
next page for an example of a directed acyclic graph. Vertices in a DAG which have no incoming
edges are referred to as sources; vertices which have no outgoing edges are referred to as sinks. A
topological ordering of the vertices in a DAG is an ordering of the vertices in which each edge is from
a vertex earlier in the ordering to a vertex later in the ordering. Solution 18.8 on Page 286 uses the
notion of topological ordering.
7
2
7
4
5
12
4
273
```

### Printed page 274

```text
[
Figure 18.2: A directed acyclic graph. Vertices a,g,m ate sources and vertices l,f,h,n are sinks. The ordering
(a,b,c,e,d, g,h,k,i, j, f ,l,m,n) is a topological ordering of the vertices.
An undirected graph is also a tuple (V, E); however, E is a set of unordered pairs of vertices,
Graphically, this is captured by drawing arrowless connections between vertices, as in Figure 18.3.
Flgure 18.3: An undirected graph
If G is an undirected graph, vertices u and o are said tobe connected if G contains a path from
utoo;otherwise, uando aresaid tobedisconnected. Agraphissaidtobeconnectedif everypair
of vertices in the graph is connected. A connected component is a maximal set of vertices C such
that each pair of vertices in C is connected in G. Every vertex belongs to exactly one connected
component.
For example, the graph in Figure 18.3 is connected, and it has a single connected component. If
edge (h, i) is removed, it remains connected. If additionally (f , i) is removed, it becomes disconnected
and there are two connected components,
A directed graph is called weakly connected if replacing all of its directed edges with undirected
edges produces an undirected graph that is corurected. It is connected if it contains a directed path
from u to u or a directed path from a to u for every pair of vertices u alrrd a. It is strongly connected
if it contains a directed path from u to o ar.-'rd a directed path from o to u for every pair of vertices z
and a.
Graphs naturally arise when modeling geometric problems, such as determining connected
cities. However, they are more general, and can be used to model many kinds of relationships.
A graph can be implemented in two ways-using adjacency lists or an adjacency matrix. In the
adjacency list representation, each vertex o, has a list of vertices to which it has an edge. The
adjacency matrix representation uses a lVl x IVI Boolean-valued matrix indexed by vertices, with
274
```

### Printed page 275

```text
a 1 indicating the presence of an edge. The time and space complexities of a graph algorithm are
usually expressed as a function of the number of vertices and edges.
A free (sometimes called a free tree) is a special sort of graph-it is an undirected graph that is
connected but has no cycles. (Many equivalent definitions exist, e.g., a graph is a free tree if and
only if there exists a unique path between every pair of vertices.) There are a number of variants
on the basic idea of a tree. A rooted tree is one where a designated vertex is called the root, which
leads to a parent-child relationship on the nodes. An ordered tree is a rooted tree in which each
vertex has an ordering on its children. Binary trees, which are the subject of Chapter 9, diffur from
ordered trees since a node may have only one child in a binary tree, but that node may be a left or
a right child, whereas in an ordered tree no analogous notion exists for a node with a single child.
Specifically, in a binary tree, there is position as well as order associated with the children of nodes.
As an example, the graph in Figure 18.4 is a tree. Note that its edge set is a subset of the edge
set of the undirected graph in Figure 18.3 on the facing page. Given a graph G = (V,E),if the graph
G' = (V,E') where E' c E, is a tree, then G' is referred to as a spanning tree of G.
Flgure 18.4: A tree.
Graphsboot camp
Graphs are ideal for modeling and analyzing relationships between pairs of objects. For example,
suPPose you were given a list of the outcomes of matches between pairs of teams, with each outcome
being a win or loss. A nafural question is as follows: given teams A and B, is there a sequence of
teams starting with A and ending with B such that each team in the sequence has beaten the next
team in the sequence?
A slick way of solving this problem is to model the problem using a graph. Teams are vertices,
and an edge from one team to another indicates that the team corresponding to the source vertex
has beaten the team corresponding to the destination vertex. Now we can apply graph reachability
to perform the check. Both DFS and BFS are reasonable approaches-the program below uses DFS.
llatchResult = collections.nanedtuple('llatchResu1t,, (,winning_team,,
'Iosing_team') )
def can-team-a-beat_team_b(matches, team_a, team_b) :
def build-graphO:
graph = collections . defaultdict (set)
for match in matches:
graphImatch. winning_team] . add(natch, losing_team)
return graph
def is-reachable_dfs(graph, curr, dest, visited=set())
if curr == dest:
275
```
