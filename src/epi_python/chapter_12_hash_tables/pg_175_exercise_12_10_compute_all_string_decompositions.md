# Exercise 12.10: Compute all string decompositions

**Printed textbook page:** 175. **Reference transcription pages:** 175–175.

> **Unverified OCR transcription:** This section retains the supplied PDF text layer. It is not certified verbatim: code syntax, mathematical symbols, and page boundaries may be corrupted. When two exercises begin on the same page, their excerpts overlap. Do not paste extracted code into a `.py` file without manual verification.

#### Printed page 175 (PDF page 189)

```text
# Finds the upper bound of the largest rarge containing a
upper-bound=a+1
while upper-bound in unprocessed_entries:
unprocessed-entrie s . remove (upper_bound)
upper-bound += I
max-interval-size = uar(max_interval_size,
upper-bound - lower_bound - 1)
return max-interval-size
The time complexity of this approach is O(n), where n is the array length, since we add and remove
array elements in the hash table no more than once.
12.70 Cor"rrurn ALL srRrNG DEcoMposlTroNs
This problem is concemed with taking a string (the "sentence" string) and a set of strings (the
"wotds"), and finding the substrings of the sentence which are the concatenation of all the words
(in atty order). For example, if the sentence string is "amanaplanacanal" and the set of words
is l"carr","upl","Nra"l, "aplal:.acaurr" is a substring of the sentence that is the concatenation of all
words.
Write a program which takes as input a string (the "sentence") and an array of shings (the "words"),
and retums the starting indices of substrings of the sentence string which are the concatenation
of all the strings in the words array. Each string must appear exactly once, and their ordering is
immaterial. Assume all strings in the words array have equal length. It is possible for the words
array to contain duplicates.
Hirf: Exploit the fact that the words have the same length.
Solution: Let's begin by considering the problem of checking whether a string is the concatenation
strings in words. We can solve this problem recursively-we find a string from words that is a
prefix of the given string, and recurse with the remaining words and the remaining suffix.
I,Vhen all strings in words have equal length, say n, only one distinct string in words can be a
prefix of the given string. So we can directly check the first n characters of the string to see if they
are in words. If not, the string cannot be the concatenation of words. If it is, we remove that string
from words and continue with the remainder of the string and the remaining words.
To find substrings in the sentence string that are the concatenation of the strings in words, we
cuu:r use the above process for each index in the sentence as the starting index.
def find-all_substrings (s, words) :
def match-aI1-words-in_dict (start) :
curr-string-to-freq = collections . Counter o
for i in range(start, start + len(words) o unit_size, unit_size):
curr-word = s[i:i + unit_size]
it = word_to_freqIcurr_word]
if it == 6;
return False
curr-string-to_freqIcurr_word] += I
if curr_string_to_freqIcurr_word] > it:
# curr_word occurs too nany tires for a rnatch to be possible
175
```
