# Exercise 18.5: Clone a graph

**Printed textbook page:** 282. **Reference transcription pages:** 282–282.

> **Unverified OCR transcription:** This section retains the supplied PDF text layer. It is not certified verbatim: code syntax, mathematical symbols, and page boundaries may be corrupted. When two exercises begin on the same page, their excerpts overlap. Do not paste extracted code into a `.py` file without manual verification.

#### Printed page 282 (PDF page 296)

```text
def is-deadlocked(G):
def has-cycIe (cur) :
# Visiting a gtay vertex neans a cycle
if cur. color == GraphVertex. gray:
return True
cur.color = GraphVertex.gray # llarks current vertex as a gtay one
# Traverse the neighbor vertices.
if any(nert.color != GraphVertex.black and has-cycle(nert)
for nert in cur. edges) :
return True
cur,color = GraphVertex.black # ltarks current vertex as black'
return FaIse
return any(vertex.color == GraphVertex.white and has-cycle(vertex)
for vertex in G)
The time complexity of DFS is O(lyl + lEl): we iterate over all vertices, and spend a const.rnt amount
of time per edge. The space complexity is O(lVl), which is the maximum stack depth-if we 8o
deeper than lVl calls, some vertex must repeat, implying a cycle in the graph, which leads to early
termination.
Varianh Solve the same problem for an undirected graPh.
Varianh Write a program that takes as input an undirected graph, which you can assume to be
connected, and checks if the graph remains connected if any one edge is removed.
18.5 Crorlr A GRAPH
Consider a vertex type for a directed graph in which there are two fields: an integer label and a list
of references to other vertices. Design an algorithm that takes a reference to a vertex u, arrd creates
a copy of the graph on the vertices reachable from z. Retum the copy of u.
Hlnfr Maintain a map from vertices in the original graph to their counterparts in the clone.
Solution: We traverse the graph starting fromu. Each time we encounter a vertex or an edge that is
not yet in the clone, we add it to the clone. We recognize new vertices by maintaining a hash table
mapping vertices in the original graph to their counterparts in the new graPh, Any standard graPh
traversal algorithm works-the code below uses breadth first search'
class Graphvertex:
def --init--(self 
, labe1)
seIf.label = Iabel
self.edges = []
def clone-graph(G)
if not G:
return None
q = collections.deque([G])
vertex-map = {G: Graphvertex(G.label)}
while q:
v = e.poplefto
282
```
