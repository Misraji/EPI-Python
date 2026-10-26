# Exercise 6.3: Compute the spreadsheet column encoding

**Printed textbook page:** 70. **Reference transcription pages:** 70–70.

> **Unverified OCR transcription:** This section retains the supplied PDF text layer. It is not certified verbatim: code syntax, mathematical symbols, and page boundaries may be corrupted. When two exercises begin on the same page, their excerpts overlap. Do not paste extracted code into a `.py` file without manual verification.

#### Printed page 70 (PDF page 84)

```text
denote by'N. We continue with 23/13 = 1. Since l mod 13 = 1 and 1/13 = 0, the final digit is 1,
and the overall result is "1A7". The design of the algorithm nicely illustrates the use of reduction.
Since the conversion algorithm is naturally expressed in terms of smaller similar subproblems,
it is natural to implement it using recursion.
def convert-base (num-as-string , b1 , b2) :
def construct-fron-base (num-as-int , base) :
return (' ' if num-as-int == 0 else
construct-from-base(num-as-int // base, base) +
string.hexdigits Inum-as-int % base] .upperO)
is-negative = num-as-string[0]
num-as-int = functools. reduce (
lanbda x, c: x * b1 + string.hexdigits.index(c.lowerO),
num-as-stringIis-negative :], 0)
return ('-'if 
is-negative else ") + ('0'if 
num-as-int == 0 else
construct-from-base (num-as-int, b2) )
The time complexity is O(n(7 + logo,bl)), where n is the length of s. The reasoning is as follows.
First, we perform n multiply-and-adds to get.t from s. Then we perform Logorx multiply and adds
to get the result. The value r is upper-bounded by b!, andlog6,(b\) = nlogo,b1.
6.3 Corrpurn rHE spREADSHEET coLUMN ENcoDING
Spreadsheets often use an alphabetical encoding of the successive columns. Specifically, columns
areidentifiedby"N',"8","C",,,,,"X","Y","2","AN',"A8",.,.,"22","AAN',"4A8",.,..
Implement a function that converts a spreadsheet column id to the corresponding integeq, with" N'
corresponding to 1. For example, you should retum 4 for "D" ,27 for " AN' ,702 for "ZZ" , elc. How
would you test your code?
Hint: Therc are 26 characters in ["A", "2"1, and each can be mapped to an integer.
Solution: A brute-force approach could be to enumerate the column ids, stopping when the id
equals the input. The logic for getting the successot of "2", " AZ" , etc. is slightly involved. The
bigger issue is the time-complexity-it takes 266 steps to get to "ZZZZZZ'.In general, the time
complexity is 0(26"), where rz is the length of the string.
We can do better by taking larger jumps. Specifically, this problem is basically the problem of
converting a string representing abase-26 number to the corresponding integer, excePt that "N'
corresponds to 1 not 0. We can use the string to integer conversion approach given in Solution 6.1
on Page 68.
For example to convert "ZZ",we initialize result to 0. We add26, multiply by 26, then add 26
again, i.e., the id is 262 + 26 = 702.
Goodtestcasesarearoundboundaries, e.$,,"N',"8","Y","2",".|UY',"AB","2Y","22",ar:.d
some random strings, e.g., "M" , "82" , "CCC".
def ss-decode-col-id(co1) :
return functool s . reduce (
Ianbda result, c: result * 26 + ord(c) - ord('A') + 1, col, 0)
The time complexity is O(n)
70
```
