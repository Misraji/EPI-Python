# Exercise 16.8: Find the minimum weight path in a triangle

**Printed textbook page:** 251. **Reference transcription pages:** 251–251.

> **Unverified OCR transcription:** This section retains the supplied PDF text layer. It is not certified verbatim: code syntax, mathematical symbols, and page boundaries may be corrupted. When two exercises begin on the same page, their excerpts overlap. Do not paste extracted code into a `.py` file without manual verification.

#### Printed page 251 (PDF page 265)

```text
If we want all possible decompositions, we can store all possible values of f that gives us a correct
break with each position. Note that the number of possible decompositions can be exponential here.
This is illustrated by the string "itsitsitsits. . . ".
Variant: Palindromic decompositions were described in Problem 15.7 on Page228. Observe every
string s has at least one palindromic decomposition, which is the trivial one consisting of the
individual characters. For example, if s is "O2OM51881" then "0", "2", "0", "4", "4", "5", "1", "8",
tt8" | 't1" is such a trivial decomposition. The minimum decomposition of s is "020" , "44" , "5" ,
"1881.". How would you compute a palindromic decomposition of a string s that uses a minimum
number of substrings?
16.8 FrNp rnr MTNIMUM wErcHT pATH rN A TRTANcLE
A sequence of integer arrays in which the nth array consists of n entries naturally corresponds to a
triangle of numbers. See Figure 16.10 for an example.
FIgure 16.10: A number triangle.
Define a path in the triangle to be a sequence of entries in the triangle in which adjacent entries
in the sequence correspond to entries that are adjacent in the triangle. The path must start at the
top, descend the triangle continuously, and end with an entry on the bottom row. The weight of a
path is the sum of the entries.
Write a program that takes as input a triangle of numbers and retums the weight of a minimum
weight path. For example, the minimum weight path for the number triangle in Figure 16.10 is
shown in bold face, and its weight is 15.
Hint:l//hat property does the prefix of a minimum weight path have?
Solution: A brute-force approach is to enumerate all possible paths. Although these paths are quite
easy to enumerate, there are 2'-1 such paths in a number triangle with n rows.
A far better way is to consider entries in the lth row For any such entry, if you look at the
minimum weight path ending at it, the part of the path that ends at the previous row must also be a
minimum weight path. This gives us a DP solution. We iteratively compute the minimum weight
of a path ending at each entry in Row i. Since #ter we complete processing Row l, we do not need
the results for Row i -'1, to process Row i * 1, we ciul reuse storage.
def minimum-path-wei ght (triangle )
min-weight-to-curr_row = [0]
for row in triangle:
2
4
4
8
5
6
4
2
6
2
1
5
2
J
4
251
```
