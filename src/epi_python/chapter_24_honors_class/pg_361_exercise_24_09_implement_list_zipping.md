# Exercise 24.9: Implement list zipping

**Printed textbook page:** 361. **Reference transcription pages:** 361–361.

> **Unverified OCR transcription:** This section retains the supplied PDF text layer. It is not certified verbatim: code syntax, mathematical symbols, and page boundaries may be corrupted. When two exercises begin on the same page, their excerpts overlap. Do not paste extracted code into a `.py` file without manual verification.

#### Printed page 361 (PDF page 375)

```text
Solution: The challenge in solving this problem is that it requires lookahead. Specifically, the
number of blanks between words in a line cannot be computed till complete set of words in that
line is known.
We solve the problem on a line-by-line basis. First, we compute the words that go into each
line, assuming a single blank between words. After we know the words in a line, we compute the
number of blanks in that line and distribute the blanks evenly. The final line is special-cased.
def justify-text (nords , L) :
curr-1ine-1ength, result, curr_line = 0, tl, tl
for word in words:
if curr_Iine_Iength + len(word) + len(curr_Iine) > L:
# Distribute equaTTy between nords in curr_Ijne,
for i in range(L - curr_1ine_Iength):
curr_lineIi % (Ien(curr_line) - I or 1)] += ' ,
result . append (' ' . join (curr_line) )
curr-line, curr-line-length = tl , 0
curr-line . append (word)
curr-line-length += len(word)
# Use ljust(L) to pad the last ljne with the appropriate number of blanks
return result + [".join(curr_line).Ijust(L)]
Let nbe the sum of the lengths of the strings in A. We spend O(1) time per character in the first pass
as well as the second pass, yielding anO(n) time complexity.
24.9 Inprsl,reNr r,rsr zrrnrNc $
Let L be a singly linked list. Assume its nodes are numbered starting at 0. Define the zip of L to
be the list consisting of the interleaving of the nodes numbered 0,L,2,.. . with the nodes numbered
n - L,n - 2,/t - 3,. . ., where n is the number of nodes in the list. The zipping function is illustrated
tnFigure24.2.
0x 1S00
0x.1240
0x1830
0x2110
0x22 00
(a) List before zipping. The number in hex below each node reprssonts its address in memory.
L
I6
h
lz
ls
la
X
L
/e
la
l1
ls
l2
X
0xi000 
0x2200 
0x1240 
0x2110
(b) List after zipping. Note that nodes are reused-no memory has been allocated.
Flgure24,2z Zipping a list.
0x1830
Implement the zip function,
Hirt: Consider traversing the list in reverse order.
Solution: A brute-force approach is to iteratively identify the head and tail, remove them from the
original list, and append the pair to the result. The time complexity is O(n) + O(n - 2) + O(n - 4) + . . . =
O(nz), where n is the number of nodes. The space complexity is O(1).
361,
```
