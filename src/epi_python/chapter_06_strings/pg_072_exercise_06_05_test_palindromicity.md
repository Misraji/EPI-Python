# Exercise 6.5: Test palindromicity

**Printed textbook page:** 72. **Reference transcription pages:** 72–72.

> **Unverified OCR transcription:** This section retains the supplied PDF text layer. It is not certified verbatim: code syntax, mathematical symbols, and page boundaries may be corrupted. When two exercises begin on the same page, their excerpts overlap. Do not paste extracted code into a `.py` file without manual verification.

#### Printed page 72 (PDF page 86)

```text
write-idx, a-count = 0, 0
for i in range(size):
if s[i] != 'b':
sIwrite-idx] = stil
write-idx += 1
if 
s [i] == 'a' :
a-count += 1
# Backward iteration: replace 'a's with
cur-idx=write-idx-1
write-idx += a-count - I
final-size = write-idx + 1
while cur-idx >= 0:
if 
s [cur-idx] =- 'a' :
sIwrite-idx - 1:write-idx + 1] =
write-idx -= 2
else:
sIwrite-idx] 
= sIcur-idx]
nrite-idx -= 1
cur-idx -= 1
return final-size
'dd's starting from the end
'dd'
The forward and backward iterations each take O(n) tirne, so the total time complexity is O(n). No
additional space is allocated.
Variant You have an array C of characters. The characters may be letters, digits, blanks, and
punctuation. The telex-encoding of the array C is an array T of characters in which letters, digits,
and blanks appear as before, but punctuation marks are spelled out. For exalnple, telex-encoding
entails replacing the character "." by the string "DOT", the character "," by "COMMA", the
character "?" by "QUESTION MARK", and the character "!" by "EXCLAMATION MARK".
Design an algorithm to perform telex-encoding with O(1) space.
Variant: Write a program which merges two sorted arrays of integers, A and B. Specifically, the
final result should be a sorted array of length tn + n, where n and m are t}r.e lengths of A arrd B,
respectively. Use O(1) additional storage-assume the result is stored in A, which has sufficient
space. These arrays are C-style arrays, i.e., contiguous preallocated blocks of memory.
6.5 Tusr peuupRoMrcrrY
For the purpose of this problem, define a palindromic string to be a string which when all the
nonalphanumeric are removed it reads the same front to back ignoring case. For example, "A man,
a plan, a canal/ Panama." and "Able was I, ere I saw Elba!" are palindromic, but "Ray a Ray" is not.
Implement a function which takes as input a string s and retums true if s is a palindromic string.
Hint:Use two indices.
Solution: The naive approach is to create a reversed version of s, and compare it with s, skipping
nonalphanumeric characters. This requires additional space proportional to the length of s.
We do not need to create the reverse-rather, we can get the effect of the reverse of s by traversing
s from right to left, Specifically, we use two indices to traverse the string, one forwards, the other
backwards, skipping nonalphanumeric characters, performing case-insensitive comparison on the
72
```
