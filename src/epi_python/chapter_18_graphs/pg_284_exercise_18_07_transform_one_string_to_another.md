# Exercise 18.7: Transform one string to another

**Printed textbook page:** 284. **Reference transcription pages:** 284–285.

> **Unverified OCR transcription:** This section retains the supplied PDF text layer. It is not certified verbatim: code syntax, mathematical symbols, and page boundaries may be corrupted. When two exercises begin on the same page, their excerpts overlap. Do not paste extracted code into a `.py` file without manual verification.

#### Printed page 284 (PDF page 298)

```text
-rtr.I 
If any edge is from a distance k vertex to a distance k vertex, we stop-the pins cannot be
partitioned into left and right halves as desired. The reason is as follows. Let u and o be such
vertices. Consider the first corunon ancestor a in the BFS tree of u and a (such an ancestor must
exist since the search started at "0). 
The paths ?u arrd p, in the BFS tree from a to u and o are of
equal length; therefore, the cycle formed by going from a to u via pr, then through the edge (u, o),
and then back to a froma viap, has an odd length. A cycle in which the vertices can be partitioned
into two sets must have an even number of edges-it has to go back and forth between the sets and
terminate at the starting vertex, and each back and forth adds two edges. Therefore, the vertices in
an odd length cycle cannot be partitioned into two sets such that all edges are between the sets.
class Graphvertex:
def --init--(se1f):
self.d = -1
self.edges = []
def i s-any-placement-feasible (G) :
def bfs (s) :
s.d = 0
q = collections. deque([s])
while q:
for t in q [0] . edges :
if t.d == -1: # Unvisited vertex,
t.d = q[0].d + 1
q . append (t )
elif t.6 == q [0] . d:
return False
del qtol
return True
return all(bfs(v) for v in G if v.d -- -1)
The complexity is the same as for BFS, i.e., O(p + zu) time complexity, where zu is the number of
wires, and O(p) space complexity.
Graphs that can be partitioned as described above are known as bipartite graphs. Another
term for such graphs is 2-colorable (since the vertices can be assigned one of two colors without
neighboring vertices having the same color).
18.7 TnaNsronu oNE srRrNG To ANoTHER
Lets and f be strings and D a dictionary, i.e., a set of strings. Define stoproduce t if there exists a
sequenceof stringsfromthedictionaryP = (s0,s1, ...,sn-r) suchthatthefirststringiss,thelaststring
is f, and adjacent strings have the same length and differ in exactly one character. The sequence
P is called a production sequence. For example, if the dictionary is {bat, cot, dog, dag, dot, cat}, then
(cat, cot, dot, dog) is production sequence.
Givena dictionary D and two stringss and f,writea programtodetermineif s produces f. Assume
that all characters are lowercase alphabets. If s does produce t, output the length of a shortest
production sequence; otherwise, output -1.
2U
```

#### Printed page 285 (PDF page 299)

```text
Hint: Treat strings as vertices in an undirected graph, with an edge between u and u if and only if the
corresponding strings differ in one character.
Solution: A brute-force approach may be to explore all strings that differ in one character from the
starting string, then two characters from the starting string, etc. The problem with this approach is
that it may explore lots of strings that are outside the dictionary.
A better approach is to be more focused on dictionary words. hr particulal, it's natural to model
this problem using graphs. The vertices correspond to strings from the dictionary and the edge
(u,t;) indicates that the strings corresponding to u and zt differ in exactly one character. Note that
the relation "differs in one character" is syrnmetric, so the graph is undirected.
For the given example, the vertices would be {bat, cot, dog, dag, dot, cat}, and the edges would
be {(bat cat), (cot, dot), (cot, cat), (dog, dag), (dog, dot)}.
A production sequence is simply a path in G, so what we need is a shortest path from s to f in G.
Shortest paths in an undirected graph are naturally computed using BFS.
# Uses 8FS to find the least steps of transformation.
def transform_string(D, s, t):
StringWithDistance = collections.namedtuple(
'StringwithDistance', ('candidate_string','distance,))
q = collections.deque([StringWithDistance(s, 0)])
D.remove(s) # Ifarks s as visited by erasing it in D.
rhile q:
f = q.poptefto
# Returns if we find a match.
if f.candidate-string == t:
return f,distance # Nunber of steps reaches t
# Tries all possibie transfornations of f.candidate_string.
for i in range(Len(f. candidate_string)) 
:
for c in string.ascii_lowercase: 
# Iterates through ,a, - ,2,.
cand = f.candidate_string[:i] 
+ c + f.candidate_stringli 
+ 1:l
if cand in D:
D. remove (cand)
q. append(Stringl{ithDistance(cand, f.distance + 1))
return -1 # Cannot find a possible transformations.
The number of vertices is d, the number of words in the dictionary. The number of edges is, in the
worst-case, O(dz). The time complexity is that of BFS, namely O(d+ dz) = O(dz).If the string length n
is less than d then the maximum number of edges out of a vertex is O(n), implying anO(nd) bound.
Variant An addition chain exponentiation program for computhg ," is a finite sequence
(x, xi' , xi' , . . . , xn) where each element after the first is either the square of some previous element
or the product of any two previous elements. For example, the term 115 can be computed by the
following two addition chain exponentiation programs.
P7 = \x,xz - (x)',rn =1f12,x8 =1xa)2,x12 =x8x4,x14 =x12f ,x15 =xlax)
P2 = (x,f = (*)',r' = x2x,x5 = x3f ,x70 = 1x5)2,x1s = xl}xs)
It is not obvious, but the second program, P2, is the shortest addition chain exponentiation program
for computing r1s.
285
```
