# Exercise 20.2: Design a solution to the stemming problem

**Printed textbook page:** 303. **Reference transcription pages:** 303–303.

> **Unverified OCR transcription:** This section retains the supplied PDF text layer. It is not certified verbatim: code syntax, mathematical symbols, and page boundaries may be corrupted. When two exercises begin on the same page, their excerpts overlap. Do not paste extracted code into a `.py` file without manual verification.

#### Printed page 303 (PDF page 317)

```text
distance may not be the right distance function when perfomring spelling correction-it does not
take into account the commonly misspelled words or the proximity of letters on a keyboard.
How would you build a spelling correction system?
Hint: Start with an appropriate notion of distance between words.
Solution: The basic idea behind most spelling correction systems is that the misspelled word's
Levenshtein distance from the intended word tends to be very small (one or two edits). Hence,
if we keep a hash table for all the words in the dictionary and look for all the words that have a
Levenshtein distance of 2 from the text, it is likely that the intended word will be found in this set.
If the alphabet has z characters and the search text has n characters, we need to perform O(n2m2)
hash table lookups. More precisely, for a word of length n, we car- pick any two characters and
change them to any other character in the alphabet. The total number of ways of selecting any two
characters is n(n - 1) 12, arrd each character can be changed to one of (m - 1) other chars. Therefore,
the number of lookups is n(n - 1)(m - 1)212.
The intersection of the set of all strings at a distance of two or less from a word and the set of
dictionary words may be large. It is important to provide a ranked list of suggestions to the users,
with the most likely candidates are at the beginning of the list. There are several ways to achieve
this:
. Typing errors model--often spelling mistakes are a result of typing errors. Typi"g errors can
be modeled based on keyboard layouts.
o Phonetic modeling-a big class of spelling errors happen when the person spelling it knows
how the words sounds but does not know the exact spelling. In such cases, it helps to map
the text to phonemes and then find all the words that map to the same phonetic sequence.
o History of refinements-often users themselves provide a great amount of data about the most
likely misspellings by first entering a misspelled word and then correcting it. This historic
data is often immensely valuable for spelling correction.
r Stemming-often the size of a dictionary can be reduced by keeping only the stemmed version
of each word. (This entails stemming the query text.)
20,2 DssrcN A soLUTroN To rHE sTEMMTNG pRoBLEM
luVhen a user submits the query "computation" to a search engine, it is quite possible he might
be interested in documents containing the words "computers", "compute", arrd "computing" also.
If you have several keywords in a query it becomes difficult to search for all combinations of all
variants of the words in the query.
Stemming is the process of reducing all variants of a given word to one conunon root,
both in the query string and in the documents. An example of stemming would be mapping
lcomputers,computer,computel to compute. It is almost impossible to succinctly capture all possible
variants of all words in the English language but a few simple rules can get us most cases.
Design a stemming algorithm that is fast and effective.
Hint: The examples are suggestive of general rules.
Solution: Stemming is a large topic. Here we mention some basic ideas related to stemming-this
is in no way a comprehensive discussion on stemming approaches.
303
```
