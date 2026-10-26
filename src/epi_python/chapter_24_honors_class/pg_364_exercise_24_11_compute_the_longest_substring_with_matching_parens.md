# Exercise 24.11: Compute the longest substring with matching parens

**Printed textbook page:** 364. **Reference transcription pages:** 364–364.

> **Unverified OCR transcription:** This section retains the supplied PDF text layer. It is not certified verbatim: code syntax, mathematical symbols, and page boundaries may be corrupted. When two exercises begin on the same page, their excerpts overlap. Do not paste extracted code into a `.py` file without manual verification.

#### Printed page 364 (PDF page 378)

```text
new-Iist-head = it.next
while it. next :
it. next , it = it. next . next , it . next
return new-list-head
The time complexity isO(n). The space comPlexiry is O(1).
24.71, Coururt rHE LoNGEsr suBSTRING wITH MATCHING PARENS €I
Problem 8.3 on Page 102 defines matched strings of parens, brackets, and braces. This problem
is restricted to strings of parens. Specifically, this problem is concerned with a long substrings of
matched parens. As an example, if s is "((0)0(0(", then "(0)0" is a longest substring of matched
Parens.
Write a program that takes as input a string made up of the characters '(' and')', and returns the
size of a maximum length substring in which the parens are matched.
Hint: Startwith a brute-force algorithm and then refine it by considering cases in which you can advance more
quickly.
Solution: One approach would be to run the algorithm in Solution 8.3 on Page 102 on all substrings.
The time complexity is O(nz),where n is the length of the string-there are (;) = ry 
substrings,
and the matching algorithm runs in time O(n),
Note that if a prefix of a string fails the matched test because of an unmatched right parens, no
extension of that prefix can be matched. Therefore, a faster approach is for each I to find the longest
substring starting at the lth character that is matched. This leads to anO(nz) algorithm.
Finally, if a substring ends in an unmatched right parens, but all of that substring's prefixes
ending in right parens are matched, then no nonempty suffix of the prefix can be the prefix of a
matched string, since any such suffix has fewer left parens. Therefore, as soon as a prefix has an
r.rnmatched right parens, we can continue with the next character after that prefix. We store the left
parentheses' indices in a stack. At the same time, when we process a right Parens for the given
prefix, if it matched, we use the index at the top of the stack to update the longest matched string
seen for this prefix.
For the given example, "((0)0((X", *e push left parentheses and pop on right parentheses.
Before the first pop, the stack is <0,'J,,2>, where the first array element is the bottom of the stack. The
corresponding matched substring length is 3 - 1 = 2. Before the second pop, the stack is (0,1). The
corresponding matched substring length is 4 - 0 = 4. Before the third pop, the stack is (0,5). The
corresponding matched substring length is 6 - 0 = 6. Before the last pop, the stack is (0,7,8). The
corresponding matched substring length is9 - 7 = 2.
def longest-matching-parentheses (s) :
max-length, end, left-parentheses-indices = 0, -1,
for i, c in enunerate(s):
if c == '(':
Ieft-parenthe ses-indices . append (i)
elif not left-parentheses-indices :
end=i
else:
left-parentheses-indices . pop o
364
tl
```
