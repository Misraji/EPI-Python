# Exercise 6.11: Write a string sinusoidally

**Printed textbook page:** 78. **Reference transcription pages:** 78–78.

> **Unverified OCR transcription:** This section retains the supplied PDF text layer. It is not certified verbatim: code syntax, mathematical symbols, and page boundaries may be corrupted. When two exercises begin on the same page, their excerpts overlap. Do not paste extracted code into a `.py` file without manual verification.

#### Printed page 78 (PDF page 92)

```text
for k in range(l, nin(len(s) - i - j, a)):
parts[2], parts[3] = sli + j:i + j + kl, sli + j + k:l
if is-va1id-part(parts [2]) and is-valid-part(parts [3])
result. append(' .' . join(parts))
return result
The total number of IP addresses is a constant (232), implying an O(1) time complexity for the above
algorithm.
Varianft Solve the analogous problem when the number of periods is a parameter k and the string
length is unbounded.
6.11. Wnmr A srRrNG sINUSoIDALLY
We illustrate what it means to write a shing in sinusoidal fashionby means of an example. The string
e-I
"Hello-World!" written in sinusoidal fashion is H 
I 
o 
I{ 
r 
d
1o!
(Here - denotes ablank.)
Define the snakestring of s to be the left-right top-to-bottom sequence in which characters appear
when s is written in sinusoidal fashion. For example, the snakestring string for "Hello-World!" is
"e-lHloWrdlo!".
Write a program which takes as input a string s and retums the snakestring of s'
Hint: Try concrete examples, and look for periodicity.
Solution: The brute-force approach is to populate a 3 x n 2D array of characters, initialized to null
entries. We then write the string in sinusoidal manner in this array. Finally, we read out the non-null
characters in row-major manner.
However, observe that the result begins with the characters s[1],s[5],s19),..., followed by
s[0],s[2],s[4],..., and then s[3],s[7],s[11],.... Therefore, we can create the snakestring directly,
with three iterations through s.
def snake-string (s) :
result = []
# outputs the first row , i.€. , s tll , stil , s[9] ,
for i in range(l, len(s), 4):
result. append(sliJ)
# outputs the second row, i.e., s[0], s[2], s[4],
for i in range(0, len(s), 2):
result.append(sIiJ)
# ?utputs the third row, i.e., s[3], s[7], s[11],
for i in range(3, Ien(s), 4):
result. append(s IiJ )
return " . join(result)
# Python so-l.ution uses slicing with right steps
def snake-string-pythonic (s) :
return s[1::4] + s[::2] + s[3::4]
78
```
