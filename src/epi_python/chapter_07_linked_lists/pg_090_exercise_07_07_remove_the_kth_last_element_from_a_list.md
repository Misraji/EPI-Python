# Exercise 7.7: Remove the kth last element from a list

**Printed textbook page:** 90. **Reference transcription pages:** 90–90.

> **Unverified OCR transcription:** This section retains the supplied PDF text layer. It is not certified verbatim: code syntax, mathematical symbols, and page boundaries may be corrupted. When two exercises begin on the same page, their excerpts overlap. Do not paste extracted code into a `.py` file without manual verification.

#### Printed page 90 (PDF page 104)

```text
dis += 1
return dis
# Ll and L2 end in the sane cycle, Jocate the overTapping node if they
# first 
overTap before cyc-Ie starts.
steml-length, stem2-length = distance(L1, rootl), 
distance(L2, root2)
if steml-length > stem2-Iength:
L2, LL = Ll, L2
rootl, root2 = root2, rootl
for - in range(abs(steml.-Iength - stemz-length)):
L2 = L2, next
while Ll is not L2 and Ll is not rootl and L2 is not rootz:
Ll , L2 = Ll. next , L2 . next
# If Ll == L2 before reaching toot1, it neans the overTap first occurs
# before the cycle starts; otherrise, the first overlapping node is not
# unique, we can return any node on the cycle,
return L1 if L1 is L2 else rootl
The algorithm has time complexity O(n + m), where n a d m are the lengths of the input lists, and
space complexity O(1).
7.6 Dnrprr A NoDE FRoM A sINGLy LINKED LIST
Given a node in a singly linked list, deleting it in O(1) time appears impossible because its prede-
cessor's next field has to be updated. Surprisingly, it can be done with one small caveat-the node
to delete cannot be the last one in the list and it is easy to copy the value part of a node.
Write a program which deletes a node in a singly linked list. The input node is guaranteed not to
be the tail node.
Hint: lnstead of deleting the node, can you delete its successor and still achieve the desired configuration?
Solution: Given the pointer to a node, it is impossible to delete it from the list without modifying
its predecessor's next pointer and the only way to get to the predecessor is to traverse the list from
head, which requires O(n) 6nq where n is the number of nodes in the list'
Civen a node, it is easy to delete its successor, since this just requires updating the next pointer
of the current node. If we copy the value part of the next node to the current node, and then delete
the next node, we have effectively deleted the current node. The time complexity is O(1).
# Issunes node-to-delete is not tai7.
def deletion-from-Iist (node-to-delete) :
node-to-deIete. data = node-to-delete. next. data
node-to-delete . next = node-to-deIete. next . next
7.7 Rruovn rns krH LAsr ELEMENT FRoM A LIST
Without knowing the length of a linked list, it is not trivial to delete the kth last element in a singly
linked list.
Given a singly linked list and an integer k, write a program to remove the kth last element from the
list. Your algorithm cannot use more than a few words of storage, regardless of the length of the
list. In particulaq, you cannot assume that it is possible to record the length of the list.
90
```
