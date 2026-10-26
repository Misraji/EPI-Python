# Exercise 15.6: Generate strings of matched parens

**Printed textbook page:** 227. **Reference transcription pages:** 227–227.

> **Unverified OCR transcription:** This section retains the supplied PDF text layer. It is not certified verbatim: code syntax, mathematical symbols, and page boundaries may be corrupted. When two exercises begin on the same page, their excerpts overlap. Do not paste extracted code into a `.py` file without manual verification.

#### Printed page 227 (PDF page 241)

```text
i = offset
rhile i <= n and num-remaining (= n - i + 1:
directed_combinations(i + 1, partial_combination + til)
i+= 
1
result = []
directed-combinations (1 , Il )
return result
The time comPlexity is O(n(i\; the reasoning is analogous to that for the recursive solution enu-
merating the powerset (Page 225).
75.6 GrNrnets srRrNGs oF MATCHED pARENs
Strings in which parens are matched are defined by the following three rules:
o The empty string, "" , is a string in which parens are matched.
o The addition of a leading left parens and a trailing right parens to a string in which parens
are matched results in a string in which parens are matched. For example, since "(0)0" is a
string with matched parens, so is "((0)0)".
o The concatenation of two strings in which parens are matched is itself a string in which
Parens are matched. For example, since "(0)0" Ntd "0" are strings with matched parens, so
is "(0X)0".
For example, the set of strings containing two pairs of matched parens is t(0) 00), a.rd the set
of strings with three pairs of matched parens is {((0)), (00), (0)0,0(0),000}.
Write a program that takes as input a number and retums all the strings with that number of
matched pairs of parens.
Hlzf: Think about what the prefix of a string of matched parens must look like.
Solution: A brute-force approach would be to enumerate all strings on 2k parentheses. To test
if the parens in a string are matched, we use Solution 8.3 on Page 102, specialized to one type of
parentheses. There are 2x possible strings, which is a lower bound on the time complexity. Even if
we restrict the enumeration to strings with an equal number of left and right parens, there are (f;)
strings to consider.
We can greatly improve upon the time complexity by enumerating in a more directed fashion.
For example, some strings can never be completed to a string with k pairs of matched parens, e.g.,
if a string begins with ). Therefore, one way to be more directed is to build strings incrementally.
We will ensure that as each additional character is added, the resulting string has the potential to
be completed to a string with ft pairs of matched parens.
Suppose we have a string whose length is less than 2k, and we know that string can be completed
to a string with k pairs of matched parens. How can we extend that string with an additional
character so that the resulting string can still be completed to a string with k pairs of matched
parens?
There are two possibilities: we add a left parens, or we add a right parens.
o If we add a left parens, and still want to complete the string to a string with k pairs of matched
parens, it must be that the number of left parens we need is greater than 0.
227
```
