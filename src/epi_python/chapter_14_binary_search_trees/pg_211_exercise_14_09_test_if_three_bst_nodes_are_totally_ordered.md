# Exercise 14.9: Test if three BST nodes are totally ordered

**Printed textbook page:** 211. **Reference transcription pages:** 211–211.

> **Unverified OCR transcription:** This section retains the supplied PDF text layer. It is not certified verbatim: code syntax, mathematical symbols, and page boundaries may be corrupted. When two exercises begin on the same page, their excerpts overlap. Do not paste extracted code into a `.py` file without manual verification.

#### Printed page 211 (PDF page 225)

```text
1,4.9 Trsr rr nrnrr BST NoDEs ARE TorALLy oRDERED
Write a program which takes two nodes in a BST and a third node, the "middle" node, and
determines if one of the two nodes is a proper ancestor and the other a proper descendant of the
middle. (A proper ancestor of a node is an ancestor that is not equal to the node; a proper descendant
is defined similarly.) For example, in Figure 14.1 on Page798, if the middle is Node l,your function
should return true if the two nodes are {A,K} or ll,Ml. It should retum false if the two nodes are
{I, P} or {/, K}. You can assurne that all keys are unique. Nodes do not have pointers to their parents
Hint: For what specific arrangements of the three nodes does the check pass?
Solution: A brute-force approach would be to check if the first node is a proper ancestor of the
middle and the second node is a proper descendant of the middle. If this check retums true, we
retum true. Otherwise, we retum the result of the same check, swapping the roles of the first and
second nodes. For the BST in Figure 14.1 on Page 198, with the two nodes being {L,1} and middle
K, searching for K from L would be unsuccessful, but searching for K from I would succeed. We
would then search for L from K, which would succeed, so we would retum true.
Searching has time complexity O(h),where fu is the height of the tree, since we can use the BST
ProPerty to prune one of the two children at each node. Since we perform a maximum of three
searches, the total time complexity is O(h).
One disadvantage of trying the two input nodes for being the middle's ancestor one-after-
another is that even when the three nodes are very close, e.g., if the two nodes are {A,JI and middle
node is I in Figure 14.1 on Page 198, if we begin the search for the middle from the lower of the two
nodes, e.g., from /, we incur the full O(fi nme complexity.
We can prevent this by performing the searches for the middle from both altematives in an
interleaved fashion. If we encounter the middle from one node, we subsequently search for the
second node from the middle. This way we avoid performing an unsuccessful search on a large
subtree. For the example of lA,Jl and middle I in Figure 14.1 on Page 198, we would search for I
from bothu{ and /, stopping as soon as we get to I from A, thereby avoiding a wasteful search from
/. (We would still have to search for / from I to complete the computation.)
def pair-includes-ancestor-and_descendant_of_m(possible_anc_or_desc_0,
possible_anc_or_desc_1, middle)
search_O, search_1 = possible_anc_or_desc_0, possible_anc_or_desc_1
# Perforn interleaved searching fron possibTe_anc_or_desc_0 and
# possibTe-anc-or-desc-1 for niddle.
while (search_o is not possible_anc_or_desc_1 and search_0 is not middle
and search-1 is not possible_anc_or_desc_O and search_1 is not middle
and (search_0 or search_1)):
if search-O:
search_O = (search_0.Ieft
if search_O. data > middle. data eLse search_0. right)
if search-l:
search-l = (search-l.left
if search_1. data > middle. data else search_1. right)
# If both searches were unsuccessful , or we got fron
# possible-anc-or-desc-0 to possibTe_anc_or_desc_I wjthout seeing niddle,
# or from possibJe-anc-or_desc_7 to possible_anc_or_desc_0 without seeing
# niddle, niddle cannot 7ie between possible_anc_or_desc_0 and
271,
```
