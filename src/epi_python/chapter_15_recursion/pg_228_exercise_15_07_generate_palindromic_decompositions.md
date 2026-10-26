# Exercise 15.7: Generate palindromic decompositions

**Printed textbook page:** 228. **Reference transcription pages:** 228–228.

> **Unverified OCR transcription:** This section retains the supplied PDF text layer. It is not certified verbatim: code syntax, mathematical symbols, and page boundaries may be corrupted. When two exercises begin on the same page, their excerpts overlap. Do not paste extracted code into a `.py` file without manual verification.

#### Printed page 228 (PDF page 242)

```text
[ ]
. If we add a right parens, and still want to complete the string to a string with k pairs of
matched parens, it must be that the number of left parens we need is less than the number of
right parens (i.e., there are unmatched left parens in the string).
As a concrete example, if k = 2,we would go through the following sequence of strings: "","(",
"((", "(0" , "(0)", "0", "0(", "00".of these, "(0)" and "00" are complete, and we would add them
to the result.
def generate-balanced-parentheses (num-pairs) :
def directed-generate-balanced-parentheses 
(num-Ieft-parens-needed,
num-ri ght-parens-needed,
valid-prefix,
result=[]):
if num-left-parens-needed > 0: # Able to insert'('.
directed-generate-balanced-parentheses 
(num-Ieft-parens-needed - 1,
num-ri ght-parens-needed,
valid-prefix + ' (')
if num-left-parens-needed < num-right-parens-needed :
# Able to jnsert ')'.
directed-generate-balanc ed-parenthe se s (num-I eft-parens-needed,
num-right-parens-needed - 1,
valid-prefix + ') ')
if not num-right-parens-needed :
result . append (valid-prefix)
return result
return directed-generate-balanced-parentheses 
(num-pairs , nun-pairs , ' ')
The number C(k) of strings with k pairs of matched parens grows very rapidly with k. Specifically,
it can be shown that C(k + 1) = Xl=o (l t <t + 1), which solves to (2k)l I((kl(k + 1)!).
15.7 GnNrnern pALrNDRoMrc DECoMposITIoNs
A string is said to be palindromic if it reads the same backwards and forwards. A decomposition of
a string is a set of strings whose concatenation is the string. For example, " 611116" is palindromic,
and "6'1,7" , "'11" , "6" is one decomposition for it.
Compute all palindromic decompositions of a given string. For example, if the string is
"020U51881.", then the decomposition "020", "44" , "5", "188L" is palindromic, as is "020', u44u,
"5" , "7" , "88" , "1', However, '02044, "5", "188L" is not a palindromic decomposition.
Hint: Focrts on the first palindromic string in a palindromic decomposition.
Solution: We can brute-force compute all palindromic decompositions by first computing all
decompositions, and then checking which ones are palindromic. To compute all decomPositions,
we use prefixes of length 1,2. . . for the first string in the decomposition, and recursively compute
the decomposition of the corresponding suffix. The number of such decompositions is 2n-1 ,where
n is the length of the string. (One way to understand this is from the fact that every l?-bit vector
corresponds to a unique decomposition-the 1s in the bit vector denote the starting point of a
substring.)
Clearly, the brute-force approach is inefficient because it continues with decompositions that
cannot possibly be palindromic, e.g., it will recursively compute decompositions that begin with
228
```
