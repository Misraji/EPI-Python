# Exercise 6.13: Find the first occurrence of a substring

**Printed textbook page:** 79. **Reference transcription pages:** 79–81.

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

#### Printed page 80 (PDF page 94)

```text
Given two strings s (the "search string") and f (the "text"), find the first occurrence of s in f
Hltf: Form a signature from a string.
Solution: The brute-force algorithm uses two nested loops, the first iterates through f, the second
tests if s occurs starting at the current index in f. The worst-case complexity is high. If f consists of
n'a's and s is nl2 'a's followed by a'b', it will perform n /2 unsuccessful string comperes, each of
which entails n12 + 7 character compares, so the brute-force algorithm's time complexity is O(n2).
Intuitively, the brute-force algorithm is slow because it advances through f one character at a
time, and potentially does O(m) computation with each advance, where m is the length of s.
There are three linear time string matching algorithms: KMP, Boyer-Moore, and Rabin-Karp. Of
these, Rabin-Karp is by far the simplest to understand and implement.
The Rabin-Karp algorithm is very similar to the brute-force algorithm, but it does not require
the second loop. Instead it uses the concept of a "fingerprint". Specifically,letmbe the length of
s. It computes hash codes of each substring whose length is ru-these are the fingerprints. The key
to efficiency is using an incremental hash function, such as a function with the property that the
hash code of a string is an additive function of each individual character. (Such a hash function
is sometimes referred to as a rolling hash.) For such a function, getting the hash code of a sliding
window of characters is very fast for each shift.
For example, let the strings consist of letters frorn \A,C,G,T). Suppose f is "GACGCCA" and
s is "CGC". Define the code for " N' to be 0, the code for "C" to be 1, etc. Let the hash function
be the decimal number formed by the integer codes for the letters. The hash code of s is 121. The
hash code of the first three characters of t, "GAC", is 201, so s cannot be the first three characters
of f . Continuing, the next substring of f is " ACG" , whose hash code can be computed from 201 by
subtracting 200, then multiplying by 1.O, and finally adding 2. This yields 12, so there no match
yet. We then reach "CGC" whose hash code, 121, is derived in a similar manner. We are not done
yet-there may be a collision. We check explicitly if the substring matches s, which in this case it
does.
For the Rabin-Karp algorithm to run in linear time, we need a good hash function, to reduce the
likelihood of collisions, which entail potentially time consuming string equality checks.
def rabin-karp (t , s) :
if Len(s) > Ien(t):
return -1 # s js not a substring of t
BASE = 26
# Hash codes for the substring of t and s.
t-hash = functools.reduce(lanbda h, c: h * BASE + ord(c), t[:len(s)], 
0)
s-hash = functools.reduce(lanbda h, c: h * BASE + ord(c), s, 0)
power-s = BASE**nax(Ien(s) - 1, 0) # BASE^ls-11.
for i in range(Ien(s), len(t)):
# Checks the trrro substrings are actualTy equal or not
# against hash col-lision.
if t-hash == s-hash and t[i - Ien(s):i] 
== s;
return i - Ien(s) 
# Found a natch.
# Ilses roTTing hash to conpute the hash code
t-hash -= ord(t[i 
- len(s)]) * power-s
t_hash = t-hash * BASE + ord(tlil)
80
to protect
```

#### Printed page 81 (PDF page 95)

```text
# Tries to ,natch s and t[-Ien(s):J.
if t_hash == s-hash and t[-ten(s):] == g
return len(t) - Ien(s)
return -1 # s is not a substring of t.
For a good hash function, the time complexity isO(m + n ), independent of the inputs s and f, where
rz is the length of s and r is the length of f.
81
```
