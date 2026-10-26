# Exercise 6.9: Convert from Roman to decimal

**Printed textbook page:** 76. **Reference transcription pages:** 76–76.

> **Unverified OCR transcription:** This section retains the supplied PDF text layer. It is not certified verbatim: code syntax, mathematical symbols, and page boundaries may be corrupted. When two exercises begin on the same page, their excerpts overlap. Do not paste extracted code into a `.py` file without manual verification.

#### Printed page 76 (PDF page 90)

```text
s = '1'
for - in range(I, n):
s = next-number(s)
return s
# Pythonic solutjon uses the power of itertools.groupbyO.
def Iook-and-say-pythonic (n) :
s = '1'
for - in range(n - 1):
s = ". join(
str(Ien(list(group))) + key for key, group in itertools.groupby(s))
return s
The precise time complexity is a function of the lengths of the terms, which is extremely hard to
arralyze. Each successive number can have at most twice as many digits as the previous number-
this happens when all digits are different. This means the maximum length number has length no
more than 2'. Since there are ,7 iterations and the work in each iteration is proportional to the length
of the number computed in the iteration, a simple bound on the time complexity is O(nZ').
6.9 CoNvrnt pnor'r Rouert ro DECIMAL
The Roman numeral representation of positive integers uses the symbols I,V,X,L,C,D,M. Each
symbolrepresentsavalue,withibeingl,Vbeing5,Xbeingl0,Lbeing50,Cbeingl00,Dbeing
500, and M being 1000.
In this problem we give simplified rules for representing numbers in this system. Specifically,
define a string over the Roman number symbols to be a valid Roman number string if symbols
appear in nonincreasing order, with the following exceptions allowed:
o I can immediately precede V and X.
o X can immediately precede L and C.
o C can immediately precede D and M.
Back-to-back exceptions are not allowed, e.g.,lXC is invalid, as is CDM.
A valid complex Roman number string represents the integer which is the sum of the symbols
that do not correspond to exceptionsi for the exceptions, add the difference of the larger symbol
and the smaller symbol.
For example, the strings "XXXXXIIIIIIII", "LVIII" and "LIX" are valid Roman number strings
representing 59. The shortest valid complex Roman number string corresponding to the integer 59
is "LIX".
Write a program which takes as input a valid Roman number string s and retums the integer it
corresponds to.
Hint: Startby solving the problem assuming no exception cases.
Solution: The brute-force approach is to scan s from left to right, adding the value for the corre-
sponding symbol unless the symbol subsequent to the one being considered has a higher value, in
which case the pair is one of the six exception cases and the value of the pair is added.
A slightly easier-to-code solution is to start from the right, and if the symbol after the current
one is greater than it, we subtract the current symbol. The code below performs the right-to-left
76
```
