# Exercise 12.5: Find the nearest repeated entries in an array

**Printed textbook page:** 167. **Reference transcription pages:** 167–167.

> **Unverified OCR transcription:** This section retains the supplied PDF text layer. It is not certified verbatim: code syntax, mathematical symbols, and page boundaries may be corrupted. When two exercises begin on the same page, their excerpts overlap. Do not paste extracted code into a `.py` file without manual verification.

#### Printed page 167 (PDF page 181)

```text
while iter-0 or iter-l:
# Ascend tree in tanden for these two nodes.
if iter-O:
if iter-0 in nodes_on-pat.h-to-root:
return iter_0
node s_on_path_to_root . add ( iter_o )
iter_o = iter_o.parent
if iter-l:
if iter-l in nodes-on-path-to-root:
return iter-1
nodes-on-path-to-root . add ( iter_1 )
iter-1 = iter_l.parent
raise ValueError('node-0 and node_l are not in the same tree')
Note that we are trading space for time. The algorithm for Solution 9.4 on Page 118 used 0(L) space
artdO(h) time, whereas the algorithm presented above uses O(D0 + D1) space and time, where D0
is the distance from the LCA to the first node, and D1 is the distance from the LCA to the second
node. In the worst-case, the nodes are leaves whose LCA is the root, and we end up using O(lr)
space and time, where ft is the height of the tree.
1,2,5 Frup rnr NEAREST REpEATED ENTRTES rN AN ARRAy
People do not like reading text in which a word is used multiple times in a short paragraph. You
are to write a program which helps identify such a problem.
Write a program which takes as input an array and finds the distance between a closest pair of equal
entries. For example, if s = <"All", "wotk", "attd", "no", "play", "makes", "for", "tto", "wotk",
"no"r"tl)n","and", "no"r "results"), then the second and third occurrences of "no" is the closest
Pair.
Hint:Each entry in the array is a candidate.
Solution: The brute-force approach is to iterate over all pairs of entries, check if they are the same,
and if so, if the distance between them is less than the smallest such distance seen so far. The time
complexity is O(nz), where n is the array length.
We can improve upon the brute-force algorithm by noting that when examining an entry, we
do not need to look at every other entry-we only care about entries which are the same. We can
store the set of indices corresponding to a given value using a hash table and iterate over all such
sets. However, there is a better approach-when processirg * entry, all we care about is the closest
previous equal entry. Specifically, as we scan through the array, for each value seen so fat, we storie
in a hash table the latest index at which it appears. When processing the element, we use the hash
table to see the latest index less than the current index holding the same value.
For the given example, when processing the element at index 9, which is "no", the hash table
tells us the most recent previous occurrence af "no" is at index 7, so we update the distance of the
closest pair of equal entries seen so far to 2.
def find-nearest-repetition(paragraph) :
word-to-Iatest-index, nearest-repeated-distance =
for i, word in enunerate(paragraph):
if word in word-to-latest-index:
1,67
i] , float ('inf')
```
