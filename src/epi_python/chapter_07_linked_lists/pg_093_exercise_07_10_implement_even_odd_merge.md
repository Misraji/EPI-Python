# Exercise 7.10: Implement even-odd merge

**Printed textbook page:** 93. **Reference transcription pages:** 93–93.

> **Unverified OCR transcription:** This section retains the supplied PDF text layer. It is not certified verbatim: code syntax, mathematical symbols, and page boundaries may be corrupted. When two exercises begin on the same page, their excerpts overlap. Do not paste extracted code into a `.py` file without manual verification.

#### Printed page 93 (PDF page 107)

```text
return L
# Computes the length of L and the taiT
tail,n=L,1
tlhile tail. next:
n+= 1
tail = tail.next
k%=n
ifk==0:
return L
tail.next = L # llakes a cycle by connecting the tail to the head
steps-to_new-head, new_taiI = n - k, tail
rhile steps-to_new_head :
steps-to-new_head -= I
new-tail = new-tail.next
new-head = new-taiI. next
new-tailnext = None
return new_head
The time complexity is O(n), and the space complexity is O(1)
7.10 IvrprnurNr EvEN-oDD MERGE
Consider a singly linked list whose nodes are numbered starting at 0. Define the even-odd merge of
the list to be the list consisting of the even-numbered nodes followed by the odd-numbered nodes.
The even-odd merge is illustrated in Figure 7.10.
0x 1000
0x 1240
0xl 8 30
0x2 1I0
0x2 200
(a) The initial list is L. The number in hex below a node indicates the memory address of that node.
L
l6
l1
lz
ls
la
X
L
ls
I2
la
11
l3
X
Sx1000 
0x1830 
0x220S 
0x1240
(b) The even-odd merge of L-note that no new nodes have been allocated.
Flgure 7.10: Even-odd merge example.
0x2 I 10
Write a program that computes the even-odd merge.
Hint: Use temporary additional storage.
Solution: The brute-force algorithm is to allocate new nodes and compute two new lists, one for
the even and one for the odd nodes. The result is the first list concatenated with the second list.
The time and space complexity are both O(n).
However, we can avoid the extra space by reusing the existing list nodes. We do this by iterating
through the list, and appending even elements to one list and odd elements to another list. We use
an indicator variable to tell us which list to append to. Finally we append the odd list to the even
list.
93
```
