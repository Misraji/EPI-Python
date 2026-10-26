# Chapter 7: Linked Lists

**Starts at printed page 82.** [Repository overview](../../../README.md)

**Source:** user-supplied EPI Python PDF (2016/2017 edition). **Transcription warning:** PDF text extraction contains OCR errors, especially in code. Consult the original PDF for ambiguous expressions and diagrams.

## Original chapter introduction (unverified PDF text layer)

### Printed page 82

```text
Cuaprsn
Linked Lists
The S-expressions arcformed according to the t'ollowing recursioe rules.
L. The atomic symbols pypz, etc., are S-exprcssions.
2. Anull expression A is also admitted.
3. lf e is an S-expression so is (e).
4. lf e1 and ez are S-expressions so is (ey e2).
- "Recursbe Eunctions Of Symbolic Expressions,"
]. McCanrrrv, 1959
A list implements an ordered collection of values, which may include repetitions. Sepcifically, a
singly linked list is a data structure that contains a sequence of nodes such that each node contains
an object and a reference to the next node in the list. The first node is referred to as the head and the
last node is referred to as the tail; the tail's next field is null. The structure of a singly linked list is
given in Figure 7.1. There are many variants of linked lists, e.g, tn a doubly linked list, each node has
a link to its predecessor; similarly, a sentinel node or a self-loop can be used instead of null to mark
the end of the list. The structure of a doubly linked list is given in Figure 7.2.
A list is similar to an array in that it contains objects in a linear order. The key differences are that
inserting and deleting elements in a list has time complexity O(1). On the other hand, obtaining the
kth element in a list is expensive, having O(n) time complexity. Lists are usually building blocks of
more complex data structures. However, as we will see in this chapter, they can be the subject of
tricky problems in their own right.
2
X
J
5
J
L
EE
0x 1200
Figure 7.1 : Example of a singly linked list. The number in hex below a node indicates the memory address of that node.
Figure7.2:, Example of a doubly linked list.
For all problems in this chapter, unless otherwise stated, each node has two entries-a data field,
and a next field, which points to the next node in the list, with the next field of the last node being
null. Its prototype is as follows:
class ListNode:
def --init--(self 
, data=0, next-node=None)
self.data = data
self.next = next-node
0x 1 154
0x2 200
0x 1000
0x2 1 1E
2 X
-
5
J
L
X
2
TEE
82
```

### Printed page 83

```text
Linked lists boot camp
There are two types of list-related problems-those where you have to implement your own list,
and those where you have to exploit the standard list library. We will review both these aspects
here, starting with implementation, then moving on to list libraries.
Implementing a basic list APl-search, insert, delete-for singly linked lists is an excellent way
to become comfortable with lists.
Search for a key:
def search-list (L, key) :
while L and L.data != key
L = L. next
# If key was not present in the List, L wi77 have become nu77
return L
Insert a new node after a specified node:
# Insert new_node after node.
def insert-after(node, 
new-node)
new-node.nert = node.nert
node. nelt = new-node
Delete a node:
# DeTete the node past this one. i{ssume node is not a taiT
def delete-after(node) :
node. next = node . next . n€xt
Insert and delete are local operations and have O(1) time complexity. Search requires traversing the
entire list, e.g,1f the key is at the last node or is absent, so its time complexity is O(n), where n is
the number of nodes.
List
a
that uses
space/
a
that uses the existing list nodes to reduce space complexity to O(1).
Very often, a problem on lists is conceptually simple, and is more about cleanly coding what's
specified, rather than designi.g an algorithm.
Consider using a dummy head (sometimes referred to as a sentinel) to avoid having to check
for empty lists. This simplifies code, and makes bugs less likely.
It's easy to forget to update next (and previous for double linked list) for the head and tail.
Algorithms operating on singly linked lists often benefit from using two iterators, one ahead of
the otheq, or one advancing- quicker than the other.
Table 7.1 : Top Tips for Linked Lists
Knout your linked list libraries
We now review the standard linked list library with the reminder that many interview problems
that are directly concerned with lists require you to write your own list class.
Under the hood, the Python list type is typically implemented as a dynamically resized array,
and the key methods on it are described on Page 38. This chapter is concemed specifically with
83
```
