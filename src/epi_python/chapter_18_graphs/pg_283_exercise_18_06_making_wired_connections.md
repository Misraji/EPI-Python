# Exercise 18.6: Making wired connections

**Printed textbook page:** 283. **Reference transcription pages:** 283–283.

> **Unverified OCR transcription:** This section retains the supplied PDF text layer. It is not certified verbatim: code syntax, mathematical symbols, and page boundaries may be corrupted. When two exercises begin on the same page, their excerpts overlap. Do not paste extracted code into a `.py` file without manual verification.

#### Printed page 283 (PDF page 297)

```text
for e in v.edges:
# Try to copy vettex e.
if e not in vertex-nap:
vertex-map Ie] = Graphvertex (e. label)
q. append (e)
# Copy edge v->e.
vertex_map Iv] . edges. append(vertex_map Ie])
return vertex_map IG]
The space complexity is O(lyl + lEl), which is the space taken by the result. Excluding the space for
the result, the space complexity is O(lyl)-this comes from the hash table, as well as the BFS queue.
1,8.6 MaxrNc wrRED coNNEcrroNS
Consider a collection of electrical pins on a printed circuit board (PCB). For each pair of pins, there
may or may not be a wire joining them. This is shown in Figure 18.8, where vertices correspond
to pins, and edges indicate the presence of a wire between pins. (The significance of the colors is
explained later.)
Flgure 18.8: A set of pins and wires between them
Design an algorithm that takes a set of pins and a set of wires connecting pairs of pins, and
determines if it is possible to place some pins on the left half of a PCB, and the remainder on the
right half, such that each wire is between left and right halves. Retum such a division, if one exists.
For example, the light vertices and dark vertices in Figure 18.8 are such division.
Hint: Model as a graph and think about the implication of an odd length cycle.
Solution: A brute-force approach might be to try all partitions of the pins into two sets. Howeve{,
the number of such partitions is very high.
A better approach is to use corurectivity information to guide the partitioning. Assume the pins
are numbered from 0 to p - 1. Create an undirected graph G whose vertices are the pins. Add an
edge between pairs of vertices if the corresponding pins are connected by a wire. For simplicity,
assume G is connected; if not, the corurected components can be ao-.talyzed independently.
Run BFS on G beginning with any vertex os. Assign uo arbitrarily to lie on the left half. All
vertices at an odd distance from os are assigned to the right half.
lA/hen performing BFS on an undirected graph, all newly discovered edges will either be from
vertices which are at a distance d from zrs to undiscovered vertices (which will then be at a distance
d + 1 from us) or from vertices which are at a distance d to vertices which are also at a distance d.
First, assume we never encounter an edge from a distance k vertex to a distance t vertex. In this
case, each wire is from a distance k vertex to a distance k + 1. vertex, so all wires are between the left
and right halves.
283
```
