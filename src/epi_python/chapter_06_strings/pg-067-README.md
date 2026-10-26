# Chapter 6: Strings

**Starts at printed page 67.** [Repository overview](../../../README.md)

**Source:** user-supplied EPI Python PDF (2016/2017 edition). **Transcription warning:** PDF text extraction contains OCR errors, especially in code. Consult the original PDF for ambiguous expressions and diagrams.

## Original chapter introduction (unverified PDF text layer)

### Printed page 67

```text
CrIeprnn
Strings
Stuingpattern matching is an important problem that occurs in
,?tany areas of science and information processing. ln comput-
ing, it occurs naturally as part of ilata processing, text editing,
term rewriting, kxical analysis, and information retrieoal.
- 
" Algorithms Eor Einding Patterns in Strings,"
A. V. Ano, 1990
Strings are ubiquitous in programming today-scripting, web development, and bioinformatics all
make extensive use of strings.
A string can be viewed as a special kind of array, narnely one made out of characters. We
treat strings separately from arrays because certain operations which ere corunonly applied to
strings-for example, comparison, joining, splitting, searching for substrings, replacing one string
by another, parsing, etc.-do not make sense for general arrays.
You should know how strings are represented in memory, and understand basic operations on
strings such as comparison, copying/ joining, splitting, matchin& etc. Advanced string processing
algorithms often use hash tables (Chapter 12) and dynamic programming (Page 234). In this chapter
we present problems on strings which can be solved using basic techniques.
Stingsboot camp
A palindromic string is one which reads the same when it is reversed. The program below checks
whether a string is palindromic. Rather than creating a new string for the reverse of the input
string, it traverses the input string forwards and backwards, thereby saving space. Notice how it
uniformly handles even and odd length strings.
def is-palindromic (s) :
# Note that s[-jJ for i in [0,len(s) - 1] is st-(i + t)l
return all(slil 
== s[-i] for i in range(Ien(s) // 2))
The time complexity is O(n) and the space complexity is O(1), where rz is the length of the string.
Know your sting libraries
The k"y operators and functions on strings are s[3], len(s), s + t, s[2:4] (arrd
all the other variants of slicing for lists described on Page 39), s in t, s.stripO,
s.startswith(prefix), s.endswith(suffix), 'Euclid,Axiom 5,Parallel Lines'.split(','),
3 * '01', ','.join(('Gauss', 'Prince of Hathematicians', '1777-1855')), s.tolowerO,
and'Name {name}, Rank {rank}' .format(name='Archimedes', rank=3).
It's important to remember that strings are immutable-operations like s = s[1:] or s +=
' 123' imply creating a new array of characters that is then assigned back to s. This implies that
concatenating a single character n times to a string in a for loop has O(nz) trrrre complexity. (Some
67
```
