# Exercise 6.6: Reverse all the words in a sentence

**Printed textbook page:** 73. **Reference transcription pages:** 73–73.

> **Unverified OCR transcription:** This section retains the supplied PDF text layer. It is not certified verbatim: code syntax, mathematical symbols, and page boundaries may be corrupted. When two exercises begin on the same page, their excerpts overlap. Do not paste extracted code into a `.py` file without manual verification.

#### Printed page 73 (PDF page 87)

```text
alphanumeric characters. We retum false as soon as there is a mismatch. If the indices cross, we
have verified palindromicity.
def is-palindrome (s) :
# i noves forward, and j noves backward.
i,j=0,Ien(s)-1
rhile i < j:
# i and j both skip non-alphanuneric characters
rhile not s[i].isalnumo and i < j:
i+=1
while not s[j].isalnumo and i < j:
j -=1
if slil. lowerO != s[j]. lowerO:
return FaIse
i, j = i + I, j - 1
return True
we spend o(1) per character, so the time complexity is o(n), wheren is the length of s
6.6 Rrvrnsr ALL THE woRDs IN A sENTENCE
Given a string containing a set of words separated by whitespace, we would like to transform it to
a string in which the words appear in the reverse order. For example, "Alice likes Bob" transforms
to "Bob likes Alice". We do not need to keep the original string.
Implement a function for reversing the words in a string s.
Hint: lt' s difficult to solve this with one pass.
Solution: The code for computing the position for each character in the final result in a single pass
is intricate.
Howevet for the special case where each word is a single character, the desired result is simply
the reverse of s.
For the general case, reversing s gets the words to their correct relative positions. However, for
words that are longer than one characteq, their letters appear in reverse order. This situation can be
corrected by reversing the individual words.
For example, "ralr. is costly" reversed yields "yltsoc si mar". We obtain the final result by
reversing each word to obtain "costly is ram".
# Assume s is a string encoded as bytearray
def reverse-words (s) :
# First, reverse the rhole string,
s. reverse ()
def reverse-range (s , start , end) :
while start < end:
slstartl, sIend] = slendl, slstartl
start , end = start + l, end - I
start = 0
rbile True:
end = s. find(b'
if end < 0:
break
start )
73
```
