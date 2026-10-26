# Exercise 12.4: Compute the LCA, optimizing for close ancestors

**Printed textbook page:** 166. **Reference transcription pages:** 166–166.

> **Unverified OCR transcription:** This section retains the supplied PDF text layer. It is not certified verbatim: code syntax, mathematical symbols, and page boundaries may be corrupted. When two exercises begin on the same page, their excerpts overlap. Do not paste extracted code into a `.py` file without manual verification.

#### Printed page 166 (PDF page 180)

```text
self .-isbn-price-table = collections.0rderedDicto
self.-capacity = 6xp3.i1,
def lookup (se1f , isbn) :
i:f isbn not in self.-isbn-price-table:
return -1
price = self .-isbn-price-table.pop(isbn)
self. -isbn-price-table Iisbn] - price
return price
def insert (self , isbn , price) :
# lle add the value for key only if key is not present - we don't update
# existing va-lues.
if isbn in seIf.-isbn-price-table:
price = self .-isbn-price-table.pop(isbn)
elif self .-capacity <= Ien(self .-isbn-price-table) 
:
self . -i sbn-price-tabIe . popitem(Iast=False)
self . -isbn-price-tab1eIisbn] = price
def erase (self, isbn) :
return self.-isbn-price-table.pop(isbn, None) is not None
The time complexity for each lookup is O(1) for the hash table lookup and O(1) for updating the
queue, i.e., O(1) overall.
12.4 CoNapurs rHE LCA, opTIMIzING FoR closE ANCEsroRs
Problem 9.4 on Page 118 is concerned with computing the LCA in a binary tree with parent pointers
in time proportional to the height of the tree. The algorithm presented in Solution 9.4 on Page 118
entails traversing all the way to the root even if the nodes whose LCA is being computed are very
close to their LCA.
Design an algorithm for computing the LCA of two nodes in a binary tree. The algorithm's time
complexity should depend only on the distance from the nodes to the LCA.
Hirf; Focus on the extreme case described in the problem introduction.
Solution: The brute-force approach is to traverse upwards from the one node to the root, recording
the nodes on the search path, and then traversing upwards from the other node, stopping as soon
as we see a node on the path from the first node. The problem with this approach is that if the two
nodes are far from the root, we end up haversing all the way to the root, even if the LCA is the
parent of the two nodes, i.e., they are siblings. This is illustrated in by L and N in Figure 9.1 on
Page772.
Intuitively, the brute-force approach is suboptimal because it potentially processes nodes well
above the LCA. We can avoid this by altemating moving upwards from the two nodes and storing
the nodes visited as we move up in a hash table. Each time we visit a node we check to see if it has
been visited before.
def lca(node-O, node-1):
iter-o, 
iter-l 
= node-o, node-l
nodes-on-path-to-root = seto
1.66
```
