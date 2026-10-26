# Exercise 15.8: Generate binary trees

**Printed textbook page:** 229. **Reference transcription pages:** 229–229.

> **Unverified OCR transcription:** This section retains the supplied PDF text layer. It is not certified verbatim: code syntax, mathematical symbols, and page boundaries may be corrupted. When two exercises begin on the same page, their excerpts overlap. Do not paste extracted code into a `.py` file without manual verification.

#### Printed page 229 (PDF page 243)

```text
"02" for "0204457881". We need a more directed approach-specifically, we should enumerate
decompositions that begin with a palindrome.
For the given exampte,"0204451881", we would recursively compute palindromic sequences for
'204451881," (since "0" is a palindrome), and for "M51887" (since "020" is a palindrome). To com-
pute palindromic decompositions for "20M5L88'1", we would recursively compute palindromic
sequences for "04451,881" (since "2" is the only prefix that is a palindrome). To compute palin-
dromic decompositions for '04451,887', we would recursively compute palindromic sequences for
"4451991," (since "0" is the only prefix that is a palindrome). To compute palindromic decomposi-
tions for "4451991" , we would recursively compute palindromic sequences for "451991." (since "4"
is a palindrome) and f.or "51991" (since "44'is a palindrome).
def palindrome-decompositions (input) :
def directed_palindrome_decompositions (offset, partial_partition)
if offset == Ien(input):
result . append (Iist (partial_partition) )
return
for i in range(offset + l, len(input) + 1):
prefix = input Ioffset: i]
if prefix -= prefix [ : : - 1] :
directed_palindrome_decompositions (i,
partial_partition + [prefix])
result = []
directed_palindrome_decompositions (0, [] )
return result
# Pythonic solution uses bottorn-up construction,
def palindrome-decompositions_pythonic (text) :
return ([[text[:i]l 
+ right for i in range(1, len(textl + 1)
if text[:i] == text[:i][::-1]
for right in palindrome_decompositions_pythonic(textIi l)l or
t ilI)
The worst-case time complexity is still O(nx2n), e.g., if the input string consists of n repetitions
of a single character. Howeveq, our program has much better best-case time complexity than the
brute-force approach, e.g., when there are very few palindromic decompositions.
15.8 GuNunerr BTNARy rREES
Write a Program which returns all distinct binary trees with a specified number of nodes. For
example, if the number of nodes is specified to be three, retum the trees in Figure 15.6 on the
following page.
Hint: Can two binary trees whose left subtrees differ in size be the same?
Solution: A brute-force approach to generate all binary trees on rx nodes would be to generate all
binary trees on n - 7 or fewer nodes. Afterwards, form all binary trees with a root and a left child
withn-l orfewernodes,andarightchildwith n-7or fewernodes. Theresultingtreeswould all
229
```
