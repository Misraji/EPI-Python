# Exercise 16.11: The pretty printing problem

**Printed textbook page:** 254. **Reference transcription pages:** 254–256.

> **Unverified OCR transcription:** This section retains the supplied PDF text layer. It is not certified verbatim: code syntax, mathematical symbols, and page boundaries may be corrupted. When two exercises begin on the same page, their excerpts overlap. Do not paste extracted code into a `.py` file without manual verification.

#### Printed page 254 (PDF page 268)

```text
. two single stair advances followed by a double stair advance,
o a single stair advance followed by a double stair advance followed by a single stair advance,
o a double stair advance followed by two single stairs advances, and
o two double stair advances.
Hint: How many ways are there in which you can take the last step?
Solution: A brute-force enumerative solution does not make sense, since there are €u:l exponential
number of possibilities to consider.
Since the first advance can be one step, two steps,. . ., k steps, and all of these lead to different
ways to get to the top, we can write the following equation for the number of steps F(n,k):
F(n,k) =\r{n - i,t)
k
For the working example, F(4,2) = F(4- 2,2) + F(4- 1,2).Recursing, F(4-2,2) = F(4 - 2- 2,2) +
F(4 - 2 - 1,2). Both F(0,2) and F(1,2) are base-cases, with a value of 1, so F(4 - 2,2) = 2. Continuing
withF(4 -1,2),F(4-1.,2)=F(4-7-2,2)+F(4-1,-1,,2). Thefirsttermisabase-case,withavalue
of 1. The second term has already been computed-its value is 2. Therefore, F(4 - 1,2) = 3, and
F(4,2)=3+2.
In the program below, we cache values of F(i,k),0 < i < n to improve time complexity.
def number-of-ways-to-top(top, maximum-step)
def compute-nunber-of-ways-to-h (h) :
if h <= 1:
return 1
if number-of-ways-to-hthl == O'
number-of-ways-to-h[h] = sum(
compute-number-of-ways-to-h(h - i)
for i in range(l, nin(maximum-step, h) + 1))
return number-of-ways-to-h IhJ
number-of-ways-to-h = [0] o (top + 1)
return compute-nunber-of-ways-to-h (top)
We take O(k) time to fill in each entry, so the total time complexity is O(kn). The space complexity
is O(n).
1,6.11 Tnn pnrrrv PRINTING PRoBLEM
Consider the problem of laying out text using a fixed width font. Each line can hold no more than
a fixed number of characters. Words on a line are to be separated by exactly one blank. Therefore,
we may be left with whitespace at the end of a line (since the next word will not fit in the remaining
space). This whitespace is visually unappealing.
Define the messiness of the end-of-line whitespace as follows. The messiness of a single line
ending with b blank characters is b2. tfhe total messiness of a sequence of lines is the sum of the
messinesses of all the lines. A sequence of words can be split across lines in different ways with
different messiness, as illustrated in Figure 16.12 on the next page.
254
```

#### Printed page 255 (PDF page 269)

```text
I have inserted a large number of---
new examples from the papers for the
I{athematical Tripos during the last-
twenty years, which should be useful
to Cambridge students.----
f have inserted a large nunber------
of new exarnples from the papers-----
for the llathematical Tripos during--
the last twenty years, which shoutd-
be useful to Cambridge students.----
(a) Messiness =32 +G +L2 +02 +1,42 =206. 
(b) Messiness =62 +52 +22 +L2 +42 =82.
Figure 16.12; Two layouts for the same sequence of words; the line length L is 36.
Given text, i.e., a string of words separated by single blanks, decompose the text into lines such that
no word is split across lines and the messiness of the decomposition is minimized. Each line can
hold no more than a specified number of characters.
Hizf: Focus on the last word and the last line.
Solution: A greedy approach is to fit as many words as possible in each line. However, some
experimentation shows this is suboptimal. See Figure 16.13 for an example. In essence, the greedy
algorithm does not spread words uniformly across the lines, which is the key requirement of the
problem. Adding a new word may necessitate moving earlier words.
0
a
d
1
2
b
34
01234
Linel 
a 
b
Line 2 
c 
il
(a) Greedyplacement: Linel hasamessinessof 02,and (b) Optimum placement: Line t has a messiness of 22,
Line 2 has a messiness of 42. 
and Line 2 has a messiness of 22.
Flgure 16.13: Assuming the text is "a b c d" and the line length is 5, placing words greedily results in a total messiness
of 16, as seen in (a), whereas the optimum placement has a total messiness of 8, as seen in @).
Suppose we w€rnt to find the optimum placement for the lth word. As we have just seen, we
cannot trivially extend the optimum placement for the first i - L words to an optimum placement
for the ith word. Put another way, the placement that results by removing the fth word from an
optimum placement for the first I words is not always an optimum placement for the first i - 1
words. However, what we can say is that if in the optimum placement for the lth word the last line
consists of words j, j + 1,. . ., i, then in this placement, the first i - 1 words must be placed optimally.
In an optimum placement of the first i words, the last line consists of some subset of words
ending in the lth word. Furthermore, since the first i words are assumed to be optimally placed,
the placement of words on the lines prior to the last one must be optimum. Therefore, we can write
a recursive formula for the minimum messiness, M(l), when placing the first I words. Specifically,
M(l), equals mniai f (j,i) + M(j - 1), where f (j,i) is the messiness of a single line consisting of words
i to I inclusive.
We give an example of this approach in Figure 16.14 on the next page. The optimum placement
of "aaabbb c d ee" is shown in Figure 16.1,a@) on the following page. The optimum placement of
"aaabbb c d ee ff" is shown in Figure 16.14(b) on the next page.
To determine the optimum placement for "aaa bbb c d ee ff ggg gggg" , we consider two cases-
the final line is "ff ggggggg", a71d the final line is "ggggggg".(No more cases are possible, since we
Line 1
Line 2
255
```

#### Printed page 256 (PDF page 270)

```text
cannot fit "ee ff gg1gggg" on a single line.)
If the final line is "ff ggggggg", then the "aaa bb c d ee" must be placed as in Figure 16.14(a). If
the final line is "ggggggg",ther."aaabbb c d ee ff" mustbe placed as in Figure 16.14(b). These two
cases are shown in Figure 16.14(c) and Figure 16.14(d), respectively. Comparing the two, we see
Figure 16.1a(c) has the lower messiness and is therefore optimum.
a
c
b
e
0
a
c
4
b
5
b
678910012345678910
aa
d
e
(a) Optimum placement tor "aaa bbb c d ee".
112 
3 4 5 6 7 8 910
aaabbb
(b) Optimum placement tor "aaa bbb c d ee lf".
't 23 
4 5 6 7 8 910
0
a
c
e
8
e
qb
d
I
c
ob
ft8
e
ob
o6
ob
8
oooo
6bob
(c) Optimum placement for "aaa bbb c d ee fl ggggggg" (d) Optimum placement for "aaa bbb c d ee tf ggggggg"
when the final line is "ggggggg". 
when the final line is "ff ggggggg".
Figure 16.14: Solving the pretty printing problem for text "aaa bb c d ee tf ggggggg" and line length L1
The recursive computation has exponential complexity, because it visits identical subproblems
repeatedly. The solution is to cache the values for M.
def minimum-messiness (words , line-length) :
num-remaining-blanks = li.ne-length - Ien(words[0])
# nin-nessiness[jJ is the njnimum rnessiness when placing words[0:i + 1].
min-messines5 = ([num-remaining-blanks**2] + [float('inf')] 
o
(len(words) - 1))
for i in range(1, len(words)):
num-remaining-blanks = line-Iength - len(wordsIi])
min-messiness[i] = min-nessiness[i - 1] + num-remaining-blanks**2
# Try adding wordsti - 11, wordsti - 21, ...
for j in reversed(range(i)):
num-remaining-blanks -= len(wordsIj]) + 1
if num-remaining-blanks < 0:
# Not enough space to add nore words.
break
first-j-messiness = 0 if j - 1 < 0 else min-messiness[j - 1]
current-line-messiness = num-remaining-blanks**2
min-messiness Ii] = nin(min-messiness Ii],
first-j-messiness + current-Iine-messiness)
return min-messiness [ - 1]
Let L be the line length. Then there can certainly be no more than L words on a line, so the amount
of time spent processing each word is O(L). Therefore, if there are n words, the time comPlexiry is
O(nL). The space complexity is O(n) for the cache.
Variant: Solve the same problem when the messiness is the sum of the messinesses of all but the
last line.
Variant: Suppose the messiness of a line ending with b blank characters is defined to be b. Can you
solve the messiness minimization problem nO(n) time and O(1) space?
256
```
