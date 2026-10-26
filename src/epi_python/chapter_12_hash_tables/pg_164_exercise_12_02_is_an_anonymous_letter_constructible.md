# Exercise 12.2: Is an anonymous letter constructible?

**Printed textbook page:** 164. **Reference transcription pages:** 164–164.

> **Unverified OCR transcription:** This section retains the supplied PDF text layer. It is not certified verbatim: code syntax, mathematical symbols, and page boundaries may be corrupted. When two exercises begin on the same page, their excerpts overlap. Do not paste extracted code into a `.py` file without manual verification.

#### Printed page 164 (PDF page 178)

```text
The time complexity isO(n), where n is the length of the string. The space complexity isO(c), where
c is the number of distinct characters appearing in the string.
72.2 Is .nN aNoruvMous LETTER coNsrnucrrnlr?
Write a program which takes text for an anonymous letter and text for a rnagazine and determines
if it is possible to write the anonymous letter using the magazine. The anonymous letter can be
written using the magazine if for each character in the anonymous letter, the number of times it
appears in the anonymous letter is no more than the number of times it appears in the magazine.
Hlnf: Count the number of distinct characters appearing in the letter.
Solution: A brute force approach is to count for each character in the character set the number of
times it appears in the letter and in the magazine. If any character occurs more often in the letter
than the magazine we retum false, othenrrise we return true. This approach is potentially slow
because it iterates over all characters, including those that do not occur in the letter or magazine.
It also makes multiple passes over both the letter and the magazine-as many passes as there are
characters in the character set.
A better approach is to make a single pass over the letter, storing the character counts for the
letter in a single hash table-keys are characters, and values are the number of times that character
appears. Next, we make a pass over the magazine. When processing a character c, if c appears in
the hash table, we reduce its count by 1; we remove it from the hash when its count goes to zero. If
the hash becomes empty, we retum true. If we reach the end of the letter and the hash is nonempty,
we retum false--each of the characters remaining in the hash occurs more times in the letter than
the magazine.
def i s-letter-constructible-from-magazine (letter-text , magazine-text) :
# Conpute the frequencies for aII chars in letter-text.
char-frequency-for-letter = collections. Counter (letter-text)
# Checks if characters in magazine-text can cover characters in
# char-frequency- for-7etter.
for c in magazine-text:
if c in char-frequency-for-letter:
char-frequency-for-letterIc] 
-= 1
if char-frequency-for-IetterIc] 
== 6;
del char-frequency-for-letter Ic]
if not char-frequency-for-letter 
:
# All characters .for .letter-text 
are matched.
return True
# Enpty char-frequency-for-letter fleans every char in Ietter-text 
can be
# covered by a character in nagazine-text.
return not char-frequency-for-letter
# Pythonic solution that exploits collections.courter. 
l/ote that the
# subtraction only keeps keys nith positive counts.
def is_Ietter_constructible-from-magazine-pythonic(letter-text, 
magazine-text)
return (not collections.Counter(Ietter-text) 
-
1.64
```
