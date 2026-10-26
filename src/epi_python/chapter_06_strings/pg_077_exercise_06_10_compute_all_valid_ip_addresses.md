# Exercise 6.10: Compute all valid IP addresses

**Printed textbook page:** 77. **Reference transcription pages:** 77–77.

> **Unverified OCR transcription:** This section retains the supplied PDF text layer. It is not certified verbatim: code syntax, mathematical symbols, and page boundaries may be corrupted. When two exercises begin on the same page, their excerpts overlap. Do not paste extracted code into a `.py` file without manual verification.

#### Printed page 77 (PDF page 91)

```text
iteration. It does not check that when a smaller symbol appears to the left of a larger one that it is
one of the six allowed exceptions, so it will, for example, return 99 for "1C".
def roman-to-integer (s)
T = {'I': 
l, 'V': 
5
X': 10, 'L': 50, 'C': 100, 'D': 500, 'Il': 1000]
return functools. reduce(
lanbda val, i: val + (-Ttstill if Tlstill < rIsli + 1]l else Ttstill),
reversed(range(1en(s) - 1)), Ttst-tll)
Each character of s is processed in O(1) time, yielding m O(n) overall time complexity, where n is
the length of s.
Variant: Write a program that takes as input a string of Roman number symbols and checks whether
that string is valid.
Varianh Write a program that takes as input a positive integer r? and rehrms a shortest valid simple
Roman number string representing,4.
6.1,0 CoupurE ALL vALrD IP aoonrssrs
A decimal string is a string consisting of digits between 0 and 9. Lrtemet Protocol (IP) addresses can
be written as four decimal strings separated by periods, e.g.,192J68.1201. A careless programmer
mangles a string representing an IP address in such away that all the periods vanish.
Write a Program that determines where to add periods to a decimat string so that the resulting
string is a valid IP address. There may be more than one valid IP address corresponding to a string,
in which case you should print all possibilities.
For example, if the mangled string is "1921.6811." then two corresponding IP addresses are
192.168.1.1 and19.21,6.81.1. (There are seven other possible IP addresses for this string.)
Hint: Use nested loops.
Solution: There are three periods in a valid IP address, so we can enumerate all possible placements
of these periods, and check whether all four corresponding substrings are between 0 and 255. We
can reduce the number of placements considered by spacing the periods 1 to 3 characters apart. We
can also prune by stopping as soon as a substring is not valid.
For example, if the string is "\921687'1.", we could put the first period aftet "1" , "19" , and "l9Z" .
If the first part is "1" , the second part could be "9" , "92" , and "92l" . Of these, "921" is illegal so we
do not continue with it.
def get-valid-ip-address (s) :
def is-valid-part(s):
# '00', '000', '01', etc. are not va7id, but '0' is valid
return len(s) == 1 or (s[0] l='0'and 
int(s) <= 255)
result, parts = [] , [None] * 4
for i in range(l, nin(4, len(s))):
Parts [0] = s [: i]
if is-valid-part(parts [0]) :
for j in range(1, nin(Ien(s) - i, 4))
parts[1] = sli:i + jl
if is-valid_part(parts [1] ) :
77
```
