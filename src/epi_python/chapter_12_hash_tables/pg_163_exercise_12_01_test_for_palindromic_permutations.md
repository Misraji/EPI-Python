# Exercise 12.1: Test for palindromic permutations

**Printed textbook page:** 163. **Reference transcription pages:** 163–163.

> **Unverified OCR transcription:** This section retains the supplied PDF text layer. It is not certified verbatim: code syntax, mathematical symbols, and page boundaries may be corrupted. When two exercises begin on the same page, their excerpts overlap. Do not paste extracted code into a `.py` file without manual verification.

#### Printed page 163 (PDF page 177)

```text
# subtract (keeping onTy positiye counts), coTTections.Counter({'a'
c-d
# intersection: 
nin(c[x], dtxl), 
coTTections.Counter({'a': l, 'b':
c&d
# union: nax(c[x], dtxl), 
coTTections.Counter({'a': 3, 'b': 2})
cld
2])
1])
Themostimportantoperationsforsetares.add(42),s.remove(4z),s.discard(123),x 
in s,
aswellas s <= t (is s asubsetof t), and s - t (elements in s that arenotin t).
The basic operations on the three key-value collections are similar to those on set. One difference
is with iterators-iteration over a key-value collection yields the keys. To iterate over the key-value
pairs, iterate over itensO; to iterate over values/ use valuesO. (The keysO method refurns an
iterator to the keys.)
Not every type is "hashable", i.e., can be added to a set or used as a key in a dict. Lr particulaq,
mutable containers are not hashable-this is to prevent a client from modifyi.g ao object after
adding it to the containeq, since the lookup will then fail to find it if the slot that the modified object
hashes to is different.
Note that the built-in ha sh O function can greatly simplify the implementation of a hash function
for a user-defined class, i.e., implementing _-hash(selO_.
12.1 Tssr ron pALrNDRoMrc pERMUTATToNS
A palindrome is a string that reads the same forvrrards and backwards, e.g., "level", "rotator", and
"foobaraboof".
Write a program to test whether the letters forming a string can be permuted to form a palindrome.
For example, "edified" can be permuted to form "deified".
Hint: Find a simple characterization of strings that can be permuted to form a palindrome.
Solution: A brute-force approach is to compute all permutations of the string, and test each one for
palindromicity. This has a very high time complexity. Examining the approach in more detail, one
thing to note is that if a string begins with say 'a', then we only need consider permutations that
end with 'a'. This observation can be used to prune the permutation-based algorithm. Howevel,
a more powerful conclusion is that all characters must occur in pairs for a string to be permutable
into a palindrome, with one exception, if the string is of odd length. For example, for the string
"edified" , which is of odd length (7) there are two 'e', two 'd's, two 'i's, and one 'f'-this is enough
to guarantee that "edified" can be permuted into a palindrome.
More formally, if the string is of even length, a necessary and sufficient condition for it to be a
palindrome is that each character in the string appears an even number of times. If the length is
odd, all but one character should appear an even number of times. Both these cases are covered by
testing that at most one character appears an odd number of times, which can be checked using a
hash table mapping characters to frequencies.
def can-form-palindrome (s) :
# A string can be permuted to forn a paTindrone if 
and onTy if the number
# of chars whose frequencies is odd is at most 1.
return sun(v X 2 for v in collections.Counter(s).valuesO) 
<= 1
1,63
```
