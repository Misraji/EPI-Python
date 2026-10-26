# Exercise 16.7: The bedbathandbeyond.com problem

**Printed textbook page:** 249. **Reference transcription pages:** 249–250.

> **Unverified OCR transcription:** This section retains the supplied PDF text layer. It is not certified verbatim: code syntax, mathematical symbols, and page boundaries may be corrupted. When two exercises begin on the same page, their excerpts overlap. Do not paste extracted code into a `.py` file without manual verification.

#### Printed page 249 (PDF page 263)

```text
as well as Washington, D.C., cast their vote for the same candidate. Write a program to determine
if a tie is possible in a presidential election with two candidates.
Table 16.2: Electoral college votes.
Electors
State:..:.,., I 
.'Eleetonc
State
Alabama
Alaska
Arizona
Arkansas
Califomia
Colorado
Connecticut
Delaware
Florida
Georgia
Hawaii
Idaho
Illinois
Indiana
Iowa
Kansas
Kentucky
Louisiana
Maine
Maryland
Massachusetts
Michigan
Minnesota
Mississippi
Missouri
Montana
Nebraska
Nevada
New Hampshire
New |ersey
New Mexico
New York
North Carolina
North Dakota
8
4
10
11
L6
10
6
10
3
5
6
4
L4
5
29
15
3
9
3
11
6
55
9
7
J
29
16
4
4
20
11
6
6
8
State.r : 
i,' Electoils.'
Ohio 
18
Oklahoma 
7
Oregon 
7
Pennsylvania 
20
Rhode Island 
4
South Carolina 
9
South Dakota 
3
Tennessee 
11
Texas 
38
Utah 
6
Vermont 
3
Virginia 
13
Washington 
12
West Virginia 
5
Wisconsin 
10
Wyoming 
3
Washington, D.C. 
3
1.6.7 THE BEDBATHANDBEyoND.coM pRoBLEM
Suppose you are designing a search engine. L:r addition to getting keywords from a page/s con-
tent, you would like to get keywords from Uniform Resource Locators (URLs). For example,
bedbathandbeyond.com yields the keywords "bed, bath, beyond,bat, hand": the first two coming
from the decomposition "bed bath beyond" and the latter two coming from the decomposition "bed
bat hand beyond".
Given a dictionary, i.e., a set of strings, and a narne, design an efficient algorithm that checks
whether the name is the concatenation of a sequence of dictionary words. If such a concatenation
exists, return it. A dictionary word may appear more than once in the sequence. For exarrrple, "a",
" man", " a", " p)lan", " a", " canal" is a valid sequence for "amanaplanacanal".
Hint: Solve the generalized problem, i.e., determine for each prefix of the name whether it is the concatenation
of dictionary words.
Solution: The natural approach is to use recursion, i.e., find dictionary words that begin the
name, and solve the problem recursively on the remainder of the name. Implemented naively, this
aPProach has very high time complexity on some input cases, e.g., if the name is N repetitions of
"AB" followedby "C" and the dictionary words are "N', "8", and "AB" the time complexity is
exponential in N. For example, for the string " AB.NBC' , then we recurse on the substring " ABC'
twice (once from the sequence " N','B' and once from "AB").
The solution is straightforr.rrard--<ache intermediate results. The cache keys are prefixes of the
string. The corresponding value is a Boolean denoting whether the prefix can be decomposed into
a sequence of valid words.
It's easy to determine if a string is a valid word-we simply store the dictionary in a hash table.
A prefix of the given string can be decomposed into a sequence of dictionary words exactly if it
is a dictionary word, or there exists a shorter prefix which can be decomposed into a sequence of
dictionary words and the difference of the shorter prefix and the current prefix is a dictionary word.
249
```

#### Printed page 250 (PDF page 264)

```text
For example, for "amanaplanacanal";
(1.) the prefrx"a" has a valid decomposition (since "a" is a dictionary word),
(2.) the prefix "am" has a valid decomposition (since "atrr" is a dictionary word),
(3.) the prefix "ama" has a valid decomposition (since "a" has a valid decomposition, and "am"
is a dictionary word), and
(4.) "aman" has a valid decomposition (since "am" has a valid decomposifion and "an" is a
dictionary word).
Skipping ahead,
5. "amanapl" does not have a valid decomposition (since none of "1", "p1", apl", etc. are dictio-
nary words), and
6. "amanapla" does not have a valid decomposition (since the only dictionary word ending the
string is "a" ar.d "amanapl" does not have a valid decomposition).
The algorithm tells us if we can break a given string into dictionary words, but does not yield the
words themselves. We can obtain the words with a little more book-keeping. Specifically, if a prefix
has a valid decomposition, we record the length of the last dictionary word in the decomposition.
def decompose-into-dictionary-words(domain, dictionary) :
# When the aTgorithnr finis&es, last--Iength[i] t= -I indjcates domain[:i +
# 7l has a vaTid deconposition, and the Tength of the last string in the
# decomposition is Iast-lengthfiJ.
last-length = t-rl " Ien(domain)
for i in range(Ien(domain)):
# If donain[:i + 1] is a dictionary word, set last-Iength[i] to the
# Tength of that word,
if domain[:i + 1] in dictionary:
last-lengthlil=i+1
# If Tast-Tength[i] = -7 Took for j < i such that dornain[: j + 7] has a
# vaTid decomposition and donain[j + l:i + 1] is a dictionary word. If
# so, record the length of that word in last-length[i].
if last-lengthIi] 
== -1:
for j in range(i):
if last-lenSthtjl 
!= -1 and domain[j + 1:i + l] in dictionary:
last_lengthtil=i-j
break
decompositions = []
if last-length[-1] 
!= -1:
# donain can be assemb.Ied by dictionary words.
idx=Ien(domain)-1
rhile idx >= 0:
decompositions.append(domainIidx + 1 - Iast-lengthIidx]:idx 
+ 1l)
idx -= Iast-lengthIidx]
decornpositions = decompositions [: : -1]
return decompositions
Letnbe thelengthof theinputstrings. Foreachk <nwe checkforeachi < kwhetherthe
substring s[j + 1,,k|is a dictionary word, and each such check requires O(k - j) time. This implies
the time complexity is O(n3). We can improve the time complexity as follows. Let W be the length
of the longest dictionary word. We can restrict f to range fromk - W tok- l withoutlosing any
decompositions, so the time complexity improves to O(n2W).
250
```
