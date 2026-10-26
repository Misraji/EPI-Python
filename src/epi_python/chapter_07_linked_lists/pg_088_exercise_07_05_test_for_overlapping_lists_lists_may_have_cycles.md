# Exercise 7.5: Test for overlapping lists - lists may have cycles

**Printed textbook page:** 88. **Reference transcription pages:** 88–89.

> **Unverified OCR transcription:** This section retains the supplied PDF text layer. It is not certified verbatim: code syntax, mathematical symbols, and page boundaries may be corrupted. When two exercises begin on the same page, their excerpts overlap. Do not paste extracted code into a `.py` file without manual verification.

#### Printed page 88 (PDF page 102)

```text
LI
I
X
L2
Figure 7.6: Example of overlapping lists.
We can avoid the extra space by using two nested loops, one iterating through the first list, and
the other to search the second for the node being processed in the first list. Howevel the time
complexity isO(nz).
The lists overlap if and only if both have the same tail node: once the lists converge at a node,
they carurot diverge at a later node. Therefore, checking for overlap amounts to finding the tail
nodes for each list.
To find the first overlapping node, we first compute the length of each list. The first overlapping
node is determined by advancing through the longer list by the difference in lengths, and then
advancing through both lists in tandem, stopping at the first conunon node. If we reach the end of
a list without finding a common node, the lists do not overlap.
def overlapping-no-cycIe-lists(L1, 
L2)
def length(L):
length = 0
while L:
length += 1
L = L. next
return length
L1_Ien, L2_Ien = length(L1), length(L2)
if Ll-Ien > L2-Ien:
Ll, LZ = L2, LL # L2 is t}le longer list
# Advances the Tonger ljst 
to get equaT length lists
for - in range(abs(Ll-len - L2-Ien)):
L2 = L2. next
nhile Ll and L2 and Ll is not L2:
Ll, L2 = Ll.next, L2.next
return Ll # None implies there is no overTap between Ll and L2
The time complexity is O(n) and the space complexity is O(1)
7.5 TEsr ron ovERLAppING LISTS-LISTS MAy HAVE cYCLES
Solve Problem 7.4 on the previous page for the case where the lists may each or both have a cycle.
If such a node exists, return a node that appears first when traversing the lists. This node may not
be unique-if one node ends in a cycle, the first cycle node encountered when traversing it may
be different from the first cycle node encountered when traversing the second list, even though the
cycle is the same. In such cases, you may retum either of the two nodes.
For example, Figure 7.7 on the facing page shows an example of lists which overlap and have
cycles. For this example, both A and B are acceptable answers.
88
```

#### Printed page 89 (PDF page 103)

```text
L1,
fa
A
B
Figure 7.7: Overlapping lists.
Hint: Use case analysis. What if both lists have cycles? What if they end in a common cycle? What if one list
has cycle and the other does not?
Solution: This problem is easy to solve using O(rz) time and space complexity, where n is the total
number of nodes, using the hash table approach in Solution 7.4 onPage 87 .
We can improve space complexity by studying different cases. The easiest case is when neither
list is cyclic, which we can determine using SolutionT.3 on Page 86. In this case, we can check
overlap using the technique in Solution 7.4 onPage 87.
If one list is cyclic, and the other is not, they cannot overlap, so we are done.
This leaves us with the case that both lists are cyclic. In this case, if they overlap, the cycles must
be identical.
There are two subcases: the paths to the cycle merge before the cycle, in which case there is a
unique first node that is colrlrnon, or the paths reach the cycle at different nodes on the cycle. For
the first case, we cEIn use the approach of Solution 7 .4 on Page 87 . For the second case, we use the
technique in Solution 7.3 on Page 86.
def overlapping-lists (Ll , L2) :
# Stote the start of cycle if any.
root1, rootz = has_cycIe(L1), has_cycIe(L2)
if not rootl and not root2:
# Both ljsts don't have cycles.
return overlapping_no_cycIe_Iists(L1, L2)
elif (rootl and not root2) or (not rootl and root2)
# One Tist has cycle, one list has no cycle.
return None
# Both lists have cycles.
temp = root2
while True:
temp = temp'next
if temp is rootl or temp is rootZ:
breaL
# L1 and L2 do not end in the sane cycle
if temp is not rootl:
return ilone # CycTes are disjoint.
# Calculates the distance betrveen a and b
def distance (a, b) :
dis = 0
rhile a is not b:
a = a. next
89
```
