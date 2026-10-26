# Exercise 20.3: Plagiarism detector

**Printed textbook page:** 304. **Reference transcription pages:** 304–304.

> **Unverified OCR transcription:** This section retains the supplied PDF text layer. It is not certified verbatim: code syntax, mathematical symbols, and page boundaries may be corrupted. When two exercises begin on the same page, their excerpts overlap. Do not paste extracted code into a `.py` file without manual verification.

#### Printed page 304 (PDF page 318)

```text
Most stemming systems are based on simple rewrite rules, e.g., remove suffixes of the form "es",
"s" , and "atior." . Suffix removal does not always work. For example, wolves should be stemmed
to wolf. To cover this case, we may have a rule that replaces the suffix "yes" with"f".
Most rules amount to matching a set of suffixes and applying the corresponding transformation
to the string. One way of efficiently performing this is to build a finite state machine based on all
the rules.
A more sophisticated system might have exceptions to the broad rules based on the stem
matching some pattems. The Porter stemmer, developed by Martin Porter, is considered to be one
of the most authoritative stemming algorithms in the English language. It defines several rules
based on pattems of vowels and consonants.
Other approaches include the use of stochastic methods to learn rewrite rules and n-gram based
approaches where we look at the surrounding words to determine the correct stemming for a word.
20.3 Precrnnrsu DETECToR
Design an efficient algorithm that takes as input a set of text files and retums pairs of files which
have substantial commonality.
Hint : Design a hash function which can incrementally hash Sli, i + k - 1] for i = 0, 1, 2, . . . .
Solution: We will treat each file as a string. We take a pair of files as having substantial commonality
if they have a substring of length k in common, where k is a measure of commonality. (Later, we
will have a deeper discussion as to the validity of this model.)
Let li be the length of the string corresponding to the fth file. For each such string we can
compute li - k + t hash codes, one for each klength substring.
We insert these hash codes in a hash table G, recording which file each code corresponds to,
and the offuet the corresponding substring appears at. A collision indicates that the two length-
k substrings are potentially the same.
Since we are computing hash code for each k length substring, it is important for efficiency to
have a hash function which can be updated incrementally when we delete one character and add
another. Solution 6.13 on Page 80 describes such a hash function.
In addition, it is important to have many slots in G, so that collisions of unequal strings is rare.
A total of ),]slr1l1 - k + 1) strings are added to the hash table. If k is small relative to the string length
and G has significantly fewer slots than the total number of characters in the strings, then we are
certain to have collisions.
If it is not essential to refurn an exact ;rnswer, we can save storage by only considering a subset
of substrings, e.g., those whose hash codes have 0s in the last b bits. This means that on average
we consider $ of the total set of substrings (assuming the hash function does a reasonable job of
spreading keys).
The solution presented above can lead to many false positives, For example, if each file corre-
sponds to an HTML page, all pages with a common embedded script of length k or longer will show
up as having substantial overlap. We can account for this through preprocessing, e.9., parsing the
documents and removing headers. (This may require multiple passes with some manual inspection
driving the process.) This solution will also not work if, for example, the files are similar in that they
are the exact same program, but with ids renamed. (It is however, resilient to code blocks being
304
```
