# Exercise 6.12: Implement run-length encoding

**Printed textbook page:** 79. **Reference transcription pages:** 79–79.

> **Unverified OCR transcription:** This section retains the supplied PDF text layer. It is not certified verbatim: code syntax, mathematical symbols, and page boundaries may be corrupted. When two exercises begin on the same page, their excerpts overlap. Do not paste extracted code into a `.py` file without manual verification.

#### Printed page 79 (PDF page 93)

```text
Letnbethelengthofs. EachofthethreeiterationstakesO(n)time,implyingano(n)timecomplexity.
6.12 IMprsN,rrNr RUN-LENGTH ENCoDTNG
Run-length encoding (RLE) compression offers a fast way to do efficient on-the-fly compression
and decompression of strings. The idea is simple-encode successive repeated characters by the
rePetition count and the character. For example, the RLE of "aaaabcccaa" is "4a1b3c2a". The
decoding of "3e4f2e" refurns "eeeffffee".
Implement run-length encoding and decoding functions. Assume the string to be encoded consists
of letters of the alphabet, with no digits, and the string to be decoded is a valid encoding.
Hint:This is similar to converting between binary and string representations.
Solution: First we consider the decoding function. Every encoded string is a repetition of a string of
digits followed by a single character. The string of digits is the decimal representation of a positive
integer. To generate the decoded string, we need to convert this sequence of digits into its integer
equivalent and then write the character that many times. We do this for each character,
The encoding function requires an integer (the repetition count) to string conversion.
def decoding (s) :
count, result = 0, tl
for c in s:
if c. isdigit O :
count = count * 10 + int(c)
else: # c is a Letter of alphabet.
result.append(c * count) # Appends count copies of c to result
count = 0
return " . join(result)
def encoding(s):
result, count = [] , 1
for i in range(l, len(s) + 1):
if i == Ien(s) or slil != sli - 1l:
# Found new character so write the count of previous chatacter
result.append(str(count) + sIi - 1])
count = 1
else: # stil == s[i - 7J.
count += 1
return " . join(result)
The time complexity is O(n), where n is the length of the string
6.13 FrNp rns FrRST occuRRENCE oF A suBSTRTNG
A good string search algorithm is fundamental to the performance of many applications. Several
clever algorithms have been proposed for string search, each with its own trade-offt. As a result,
there is no single perfect answer. If someone asks you this question in an interview, the best way
to approach this problem would be to work through one good algorithm in detail and discuss at a
high level other algorithms.
79
```
