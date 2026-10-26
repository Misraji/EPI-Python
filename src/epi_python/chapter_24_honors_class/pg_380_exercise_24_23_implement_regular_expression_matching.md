# Exercise 24.23: Implement regular expression matching

**Printed textbook page:** 380. **Reference transcription pages:** 380–382.

> **Unverified OCR transcription:** This section retains the supplied PDF text layer. It is not certified verbatim: code syntax, mathematical symbols, and page boundaries may be corrupted. When two exercises begin on the same page, their excerpts overlap. Do not paste extracted code into a `.py` file without manual verification.

#### Printed page 380 (PDF page 394)

```text
0x I 000
0xlr) l0
li;r I 8.1G
0x2 5 90
0x i2 l0
0x-l 120
$x 2 f,)'l0
0x,l.1i;ij
0i 1 t.18
0x I70{'
(a) Two BSTs.
Sxi 4(,(,
i)x i /0ft
f.inll l{J
0::10 l0
0x1$00
0x.:i l2 0
0x2 'l!,0
li x.r0 ! 0
Figwe 24.7
memory.
(b) Merged BST conesponding to the two BSTs in (a).
Example of merging two BSTs. The number in hex adiacent to each node represents its address in
can take these two lists and form a new list on the same nodes which is the union of the keys in
sorted order (Solution 7.1 on Page 84). This new list can be viewed as a tree holding the union of
the keys of the odginal trees. The time complexity is O(n), and space complexity is O(h), where fu is
the maximum of the heights of the two initial trees.
The problem with this approach is that while it meets the time and space constraints, it retums
a tree that is completely unbalanced. However, we can convert this tree to a height-balanced one
using Solution24.20 on Page 377, completing the desired construction.
def merge-two-bsts(A, B):
A, B = bst-to-doubly-list(A), 
bst-to-doubly-Iist(B)
A-1ength, B-length = count-length(A), count-length(B)
return build-bst-from-sorted-doubly-Iist(
merge-two-sorted-lists(A, B), A-length + B-length)
The time complexity of each stage is O(n), and since we recycle storage, the additional sPace
complexity is dominated by the time to convert a BST to a list, which isO(h).
24.23 INrprrMsNt REGULAR ExpRESSIoN MATcHING I
A regular expression is a sequence of characters that forms a search pattern. For this problem we
define a simple subset of a fult regular expression language. We describe regular expressions by
examples, rather than a formal syntax and semantics.
A regular expression is a string made up of the following characters: alphanumeric, . (dot),
* (star), ^, and $. Examples of regular expressions ate al aW, aW.9, aW.9*, dW,*9*, ^a, aW$, and
^aW.9*$. Not all strings are valid regular expressions. For example, if ^ appears, it must be the first
11
77
5
23
3
7
13
2
79
380
```

#### Printed page 381 (PDF page 395)

```text
character, if $ appears, it must be the last characte4, and star must follow an alphanumeric character
or dot. Beyond the base cases-a single alphanumeric character, dot, a single alphanumeric char-
acter followed by a star, dot followed by star-regular expressions are concatenations of shorter
regular expressions.
Now we describe what it means for a regular expression to match a string. Lrtuitively, an
alphanumeric character matches itself, dot matches any single charactel, and star matches zero or
more occurrences of the preceding character.
In the absence of ^ and $, there is no concept of an "anchor". ln particular, if the string contains
any substring matched by the regular expression, the regular expression matches the string itself.
The following examples illustrate the concept of a regular expression matching a string. More
than one substring may be matched. If a match exists, we underline a matched substring.
o aW9 matches any string containing aW9 as a substring. For example , aWg,glYgbcw, abSaW!,
and cc?aW9raW9z arc all matched by aW9, but aW8, bcd8, and xy are not.
o a.9. matches any string containing a substring of length 4 whose first and third characters are
a and 9, respectively. For example, ab9w, acgbcW ab8a999, and cc2aWgr are all matched by
a.9., but az9, a989a, and bac9 are not.
o aW*9 matches any string containing a substring beginning with a, ending with 9, with zero
or more ws in between. For example,& N9, aww9b9cw, au9aww9, ab8awWW9w9aa,
aurrd cc2a9raW9zWW9ac are all matched by aW*9, but aWWU9,baxg, and aXWgWa are not.
o a.*9 matches any string containing a substring beginning with a ending with 9, with zero
or more characters between. For example, & il9, aZW9b9cw, -ja9, b8awuw9w, and
cc2a9raU9z are all matched by a.*9,but 9UWaW8,b9aaaX, and XUq8 are not.
o aW9*.b3 matches any string containing a substring beginning with aW, followed by zero or
more 9s, followed by a single character, followed by b3. For example, ceaW999zb34b3az,
ceaW9b34, and pqaWzb38q are matched by aW9*.b3, but ceaW98zb34 and pqaW988b38q are
not.
If the regular expression begins with ^, that indicates the match must begin at the start of the string.
If the regular expression ends with $, the match must end at the end of the string.
o ^aW.9 matches strings which begin with a substring consisting of a, followed by W, followed
by ar,y character, followed by 9. For example, aW99zer, aWW9, and aWPgGA are all matched
by ^aW.9,but baWx9, aW9, and aWcc9O are not.
o aW.9$ matches strings whose last character is 9, third last character is W and fourth last char-
acter is a. (The second last character can be anything.) For example, aWW9, at{WgabcaWzg,
baaWX9, and abcaWP9, are all matched by aW.9$, but a14/W99, aW, and aWcc9O are not.
o ^aW9$ is matched by aW9 and nothing else.
Design an algorithm that takes a regular expression and a string, and checks if the regular expression
matches the string.
Hln f: Regular expressions are defined recursively.
Solution: The key insight is that regular expressions are defined recursively, both in terms of their
syntax (what strings are valid regular expressions), as well as their semantics (when does a regular
expression match a string). This suggests the use of recursion to do matching.
First, some notation: sk denotes the kth suffix of string s, i.e., the string resulting from deleting
the first k characters from s. For example, if s = aWaW9W9, then s0 = aWaW9W9, and s2 = aW9W9.
381
```

#### Printed page 382 (PDF page 396)

```text
Let r be a regular expression and s a string. If r starts with ^, then for r to match s, the remainder
of r must match a prefix of s. If r ends with a $, then for r to match s, some suffix of s must be
matched by r without the trailing $. If r does not begin with ^, or end with $, r matches s if it
matches some substring of s.
A function that checks whether a regular expression matches a string at its beginning has to
check the following cases:
(1.) Length-0 regular expressions.
(2.) A regular expression starting with ^ or ending with $.
(3.) A regular expression starting with a * match, e.9., a*wXY or .*Wa.
(4.) A regular expression starting with an alphanumeric character or dot.
Case (1.) is trivial, we just retum true. Case (2.) entails a single call to the match function for a
regular expression beginning with ^, and some checking logic for a regular expression ending with
g. Case (3.) is handled by a traversal down the string checking that the prefix of the string thus far
matches the alphanumeric character or dot until some suffix is matched by the remainder of the
regular expression. Each suffix check is a call to the match function. Case (4.) involves examining
a character, possibly followed by a call to the match function.
As an example, consider the regular expression ab.c*d. To check if it matches s =
caeabbedeabacccde, we iterate over the string. Since s[0] = c, we cannot match the regular ex-
pression at the start of s. Next we try sl. Since s[1] = a, we recursively continue checking with
sl and b.c*d. However s[2] * b, so we retum false from this call. Continuing, s2 is immediately
eliminated. With s3, since s[3] = a, we continue recursively checking with sa and b.c*d. Since
s[4] = 6, we continue checking with .c*d. Since dot matches any single character, it matches s[5],
so we continue checking with c*d. Since s[6] = e, the only prefix of s6 which matches c*d is the
empty one. However, when we continue checking with d, since s[6] * d, we retum false for this
call. Skipping some unsuccessful checks, we get to se. Similar to before, we continue to s12, and c*d.
The string begiruring at offret 12 matches c* with prefixes of length 0,L,2,3. After the first three, we
do not match with the remaining d. However, after the prefix ccc, the following string does end in
d, so we retum true.
def is-match(regex, s) :
def is-match-here (regex , s) :
if not regex:
# Case (1.): Enpty regex matches all strings
return True
if regex == '$' :
# Case (2.): Reach the end of regex, and ]ast char is '$
return not s
if len(regex) >= 2 and regex[1] == '*':
# Case (3.): A '*' match.
# Iterate through s, checking '"' condition, if '*' condition holds,
# perforns the renaining checks.
i= 
1
rhile i <= len(s) and resextOl in ('.', sti - 1l):
if is-natch-here(regex[2:], sli:l) 
:
return True
i+=1
382
```
