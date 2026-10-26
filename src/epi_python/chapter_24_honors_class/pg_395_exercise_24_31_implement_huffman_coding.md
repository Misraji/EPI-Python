# Exercise 24.31: Implement Huffman coding

**Printed textbook page:** 395. **Reference transcription pages:** 395–397.

> **Unverified OCR transcription:** This section retains the supplied PDF text layer. It is not certified verbatim: code syntax, mathematical symbols, and page boundaries may be corrupted. When two exercises begin on the same page, their excerpts overlap. Do not paste extracted code into a `.py` file without manual verification.

#### Printed page 395 (PDF page 409)

```text
table = [x + y if y else 0 for x, y in zip(tabIe, row)]
nax_rect_area = nax(max_rect_area, calculate_largest_rectangle (tabIe))
return max_rect_area
The largest square 2D subarray containing only 1s can be computed similarly, with a minor
variant on the algorithm in Solution 17.8 on Page271.
Varianfi Solve the largest square 2D subarray problem using O(rz) time.
24.31, IuprrurNr HumuaN coDrNG S
One way to comPress text is by building a code book which maps each character to a bit string,
referred to as its code word. Compression consists of concatenating the bit strings for each char-
acter to form a bit string for the entire text. (The codebook, i.e., the mapping from characters to
corresponding bit strings is stored separately, e.g., in a preamble.)
When decompressing the string, we read bits until we find a string that is in the code book and
then repeat this process until the entire text is decoded. For the compression to be reversible, it
is sufficient that the code words have the property that no code word is a prefix of another. For
example, 011 is a prefix of 0110 but not a prefix of 1100.
Since our objective is to compress the text, we would like to assign the shorter bit strings to
more common characters and the longer bit strings to less common characters. We will restrict our
attention to individual characters. (We may achieve better compression if we examine corunon
sequences of characters, but this increases the time complexity.)
The intuitive notion of commonness is formaluedby the frequency of a character which is a
number between zero and one. The sum of the frequencies of all the characters is 1. The average
code length is defined to be the sum of the product of the length of each character's code word with
that character's frequency. Table 24.7 on the following page shows the frequencies of letters of the
English alphabet.
Table 24.1: English characters and theirfrequencies, expressed as percentages, in everyday documents.
Character
a
b
c
d
e
f
oD
h
i
Frequency
8.17
t.49
2.78
4.25
12.70
2.23
2.02
5.09
6.97
Frequency
6.33
9.06
2.76
0.98
2.36
0.15
1.97
0.07
Charact€r i ,Ffeqgency
j 
0.15
0.77
4.03
2.41
5.75
7.51
1.93
0.10
5.99
S
t
u
v
x
v
z
k
I
m
n
o
P
q
r
Given a set of characters with corresponding frequencies, find a code book that has the smallest
average code length.
Hirfr Reduce the problem fromn characters to one on z - 1 characters.
395
```

#### Printed page 396 (PDF page 410)

```text
Solution: The trivial solution is to use fixed length bit strings for each character. To be precise, if
there are n distinct characters, we can use fiog nl bits per character. If all characters are equally
likely, this is optimum, but when there is large variation in frequencies, we can do much better.
A natural heuristic is to split the set of characters into two subsets, which have approximately
equal aggregate frequencies, solve the problem for each subset, and then add a 0 to the codes from
the first set and a 1 to the codes from the second set to differentiate the codes from the two subsets.
This approach does not always result in the optimum coding, e.g., when the characters are A,B,C,D
with frequencies {0.4,0.35,0.2,0.05}, it forms the code words 00, 10, 1'1,,01, whereas the optimum
coding is 0, 10, 110, 111. It also requires being able to partition the characters into two subsets whose
aggregate frequencies are close, which is computationally challenging.
Another strategy is to assign 0 to the character with highest frequency, solve the same problem
on the remaining characters, and then prefix those codes with a 1. This approach fares very poorly
when characters have the same frequency, e.g., if A,B,C,D all have frequency 0.25, the resulting
coding is 0, 10, 100, 111, whereas 00,01, 10, 11 is the optimum coding. Intuitively, this strategy fails
because it does not take into account the relative frequencies.
Huffrnan coding yields an optimum solution to this problem. (There may be other optimum
codes as well.) It is based on the idea that you should focus on the least frequent characters, rather
than the most frequent ones. Specifically, combine the two least frequent characters into a new
character, recursively solve the problem on the resulting n - 1 characters; then create codes for the
two combined characters from the code for their combined character by adding a 0 for one and a 1
for the other.
More precisely, Huffman coding proceeds in three steps:
(1.) Sort characters in increasing order of frequencies and create a binary tree node for each
character. Denote the set just created by S.
(2,) Create a new node u whose children are the two nodes with smallest frequencies and assign
a's frequency to be the sum of the frequencies of its children.
(3.) Remove the children from S and add u to S. Repeat from Step (2.) till S consists of a single
node, which is the root.
Mark all the left edges with 0 and the right edges with 1. The path from the root to a leaf node
yields the bit string encoding the corresponding character.
Apptying this algorithm to the frequencies for English characters presented in Table 24.1 yields
the Huffman tree in Figure 24.9 on the next page. The path from root to leaf yields that character's
Huffman code, which is listed in Table 24.2 on the facing page. For example, the codes for t,e, and
z are 000,100, and 001001000, respectively.
The codebook is explicitly given in Table 24.2on the next page. The average code length for this
coding is 4'205' In contrast, the trivial codhg takes flog26.l = 5 bits for each character'
In the implementation below, we use a min-heap of candidate nodes to represent S.
CharwithFrequency = collections.nanedtuple('CharWithFrequency', ('c','freq'))
def huffman-encoding (symbols) :
class BinaryTree:
def --init--(self, 
aggregate-freq, s, left=None, right=None)
self.aggregate-freq = aggregate-freq
self.s = s
396
```

#### Printed page 397 (PDF page 411)

```text
Flgure 24.9: A Hutfman tree for the English characters, assuming the frequencies given in Table p4.1 on the lacing
page.
Table 24,22 Hutfman codes for English characters, assuming the frequencies given in Table 24J onthe facing page.
a
b
c
d
e
t
8
h
i
1110
11.0000
01001
11111
100
00101
110011
0110
1011
)
k
I
m
n
o
p
q
f
001001011
0010011
11110
0011 1
1010
1101
110001
001001001
0101
s
t
u
v
w
x
v
z
01"
000
01000
001000
00110
001001010
110010
001001000
se1f.left, self.right = left, right
def --1t--(self , other) I
return self,aggregate-freq <= other.aggregate_freq
# InitialTy assigns each synboT jnto candjdates.
candidates - [BinaryTree(s.freq, s) for s in synbols]
heapq . heapify ( candidates)
# Keeps conbining tro nodes untjl there js one node left,
rhile len(candidates) > I:
Ieft , right = heapq, heappop (candidates) , heapq. heappop (candidates)
heapq . heappush ( candidates,
BinaryTree (left . aggregate_freq + right , aggregate_freq ,
None, 1eft, right))
def assign-huffman-code(tree, code)
if tree:
if tree. s:
397
```
