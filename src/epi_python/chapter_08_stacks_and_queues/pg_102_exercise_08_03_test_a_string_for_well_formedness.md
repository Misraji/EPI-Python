# Exercise 8.3: Test a string for well-formedness

**Printed textbook page:** 102. **Reference transcription pages:** 102–102.

> **Unverified OCR transcription:** This section retains the supplied PDF text layer. It is not certified verbatim: code syntax, mathematical symbols, and page boundaries may be corrupted. When two exercises begin on the same page, their excerpts overlap. Do not paste extracted code into a `.py` file without manual verification.

#### Printed page 102 (PDF page 116)

```text
8.3 Tnsr l sTRING ovrn "{,},(,),[,]" ron wELL-FoRMEDNESS
A string over the characters " l,l ,O,l,l" is said to be well-formed if the different types of brackets
match in the correct order.
For example, "(UXQ)" is well-formed, as is "[0t]{00}]". However, "{)", "0", and "[0[]{00" are
not well-formed,
Write a program that tests if a string made up of the characters '(', ')' ,'I' ,'l' /'l' and")' is well-formed,
Hirlr \Alhich left parenthesis does a right parenthesis match with?
Solution: Let's begin with well-formed strings consisting solely of left and right parentheses/ e.g./
"0(0)". If such a string is well-formed, each right parenthesis must match the closest left parenthesis
to its left. Therefore, starting from the left, every time we see a left parenthesis, we store it. Each
time we see a right parenthesis, we match it with a stored left parenthesis. Since there are not
brackets or braces, we c€u1 simply keep a count of the number of unmatched left parentheses.
For the general case, we do the same, except that we need to explicitly store the unmatched left
characters, i.e., left parenthesis, left brackets, and left braces. We cannot use three counters, because
that will not tell us the last unmatched one. A stack is a perfect option for this application: we use
it to record the unmatched left characters, with the most recent one at the top.
If we encounter a right character and the stack is empty or the top of the stack is a different
type of left character, the right character is not matched, implying the string is not matched. For
example, if the input string is "(011)", when we encounter the first ']', the character at the top of
the stack is '(', so the shing is not matched. Conversely, if the input string is "(0U)", when we
encounter the first ']', the character at the top of the stack is '[', so we continue on. If all characters
have been processed and the stack is nonempty, there are unmatched left characters so the string is
not matched.
def is-welI-formed (s) :
left-chars, lookup = [], {'(': 
')', '{': '}', '[':
for c in s:
if c in lookup:
Ieft-chars. append(c)
elif not left-chars or lookupIleft-chars.popO]
# unnatched right char or rnismatched chars.
return False
return not Ieft-chars
t']
!= c
The time complexity is O(n) since for each character we perform O(1) operations.
8,4 Nonlaauzu PATHNAMES
A file or directory can be specified via a string called the pathname. This string may specify an
absolute path, starting from the root, e.g., /usr/bin/gcc, or a path relative to the current working
directory, e.g., scripts,/awkscripts.
The same directory may be specified by multiple directory paths. For example,
/usr/llb/. ./bin/gcc and scripts// ./../scripts/awkscripts/././ specify equivalent abso-
lute and relative pathnames.
102
```
