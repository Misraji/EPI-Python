# Exercise 24.8: Justify text

**Printed textbook page:** 360. **Reference transcription pages:** 360–360.

> **Unverified OCR transcription:** This section retains the supplied PDF text layer. It is not certified verbatim: code syntax, mathematical symbols, and page boundaries may be corrupted. When two exercises begin on the same page, their excerpts overlap. Do not paste extracted code into a `.py` file without manual verification.

#### Printed page 360 (PDF page 374)

```text
def rook-attack(A):
m, n:Ien(A), 
Ien(A[0])
has_first-row-zero = any(not At0ltil 
for j in range(n))
has-first_colunn-zero = any(not Atiltol 
for i in range(m))
for i in range(l, m):
for j in range(l, n):
if not ltil tj I :
Atil iol = Atol tjl = o
for i in range(l, m):
if not Alil tol:
for j in !ange(l, n)
atiltjl 
= 0
for j in range(l, n):
if not etOl tjl:
for i in range(l, m)
Atiltjl 
= 0
if has-first-row-zero
for j in range(n)
etol tjl = o
if has-first-column-zero
for i in range(m):
Atiltol = 0
The time complexity is O(nm) since we perform O(1) computation per entry. The space complexity
is O(1).
24.8 Jusrrrv rErr O
This problem is concerned with justifying text. It abstracts a problem arising in typesetting. The
input is specified as a sequence of words, and the target line length. After justification, each
individual line must begin with a word, and each subsequent word must be separated from prior
words with at least one blank. If a line contains more than one word, it should not end in a blank.
The sequences of blanks within each line should be as close to equal in length as possible, with the
longer blank sequences, if any, appearing at the initial part of the line. As an exception/ the very
last line should use single blanks as separators, with additional blanks appearing at its end.
For example ,if. A = ("The", "ql)ick", "btown", "fox" , "jumped", "over", "the" , "lazy", "dogs.")
and the line length L is 1,1,, then the retumed result should be "The---quick" , "brown---fox" ,
"jumped-over" , "the- ---Lazy" , "dogs . ------" . The symbol - denotes a blank.
Write a program which takes as input an array A of strings and a positive integer L, and computes
the justification of the text specified by A.
Hlnfr Solve it on a line-by-line basis, assuming a single blank between pairs of words. Then figure out how to
distribute excess blanks.
360
```
