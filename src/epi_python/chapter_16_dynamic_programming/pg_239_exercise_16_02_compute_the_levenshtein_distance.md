# Exercise 16.2: Compute the Levenshtein distance

**Printed textbook page:** 239. **Reference transcription pages:** 239–241.

> **Unverified OCR transcription:** This section retains the supplied PDF text layer. It is not certified verbatim: code syntax, mathematical symbols, and page boundaries may be corrupted. When two exercises begin on the same page, their excerpts overlap. Do not paste extracted code into a `.py` file without manual verification.

#### Printed page 239 (PDF page 253)

```text
num_combinations_for_score Ii] [j - individual_pIay_scores Ii] l
if j >= individual-play-scoreslil else 0)
num-combinations-for-score Ii] ij I = (
without-this_play + $,ith_this_play)
return num_combinations_for_score [-1] [-1]
The time complexity is O(sn) (two loops, one to s, the other to n) and the space complexity is O(sn)
(the size of the 2D array).
Variank Solve the same problem using O(s) space.
Variant Write a program that takes a final score and scores for individual plays, and retums the
number of sequences of plays that result in the final score. For example, 18 sequences of plays yield
a score of 12. Some examples are (2,2,2,3,3), <2,3,2,2,3>, <2,3,7), <7,3,2>.
Variant Suppose the final score is given in the form (s,s'), i.e., Team L scored s points and Team 2
scored s' points. How would you compute the number of distinct scoring sequences which result
in this score? For example, if the final score is (6,3) then Team 1 scores 3, Team 2 scores 3, Team L
scores 3 is a scoring sequence which results in this score.
Variant Suppose the final score is (s,s'). How would you compute the maximum number of times
the team that lead could have changed? For example, if s = 10 and s' = 6, the lead could have
changed 4 times: Team 1 scores 2, then Team 2 scores 3 (lead change), then Team L scores 2 (lead
change), then Team 2 scores 3 (lead change), then Team 1 scores 3 (lead change) followed by 3.
Variant You are climbing stairs. You can advance 1 to k steps at a time. Your destination is exactly
n steps uP. Write a program which takes as inputs n atrtdk and returns the number of ways in which
you can get to your destination. For example, rt n = 4 andk = 2, there are five ways in which to get
to the destination:
o four single stair advances,
o two single stair advances followed by a double stair advance,
o a single stair advance followed by a double stair advance followed by a single stair advance,
o a double stair advance followed by two single stairs advances, and
o two double stair advances.
1,6.2 Covrpurr rsr LrvrNsHTErN DTsTANCE
Spell checkers make suggestions for misspelled words. Given a misspelled shin& a spell checker
should retum words in the dictionary which are close to the misspelled string.
1n7965, Vladimir Levenshtein defined the distance between two words as the minimum number
of "edits" it would take to transform the misspelled word into a correct word, where a single edit
is the insertion, deletion, or substitution of a single character. For example, the Levenshtein distance
between "Satutday" and "Sundays" is 4--delete the hrst'a' arrd't', substifute ,r, by ,n,and insert
the trailing's'.
Write a Program that takes two strings and computes the minirnum number of edits needed to
transform the first string into the second string.
Hinf: Consider the same problem for prefixes of the two strings.
Solution: A brute-force approach would be to enumerate all strings that are distance '1,2,9,. ..
from the first string, stopping when we reach the second string. The number of strings may grow
239
```

#### Printed page 240 (PDF page 254)

```text
enormously, e.g., if the first string is r 0s and the second is r 1s we will visit all of the 2n possible bit
strings from the first string before we reach the second string.
A better approach is to "prune" the search. For example, if the last character of the first string
equals the last character of the second string, we can ignore this character. If they are different, we
can focus on the initial portion of each string and perform a final edit step. (As we will soon see,
this final edit step may be an insertion, deletion, or substitution.)
Let a and b be the length of strings A and B, respectively. Let E(Al},a - 1),Bl0,b - lD be the
Levenshtein distance between the strings A and B. (Note that Al),a - 1] is just A, but we prefer to
write A using the subarray notation for exposition; we do the same for B.)
We now make some observations:
o IfthelastcharacterofAequalsthelastcharacterofB,thenE(A[0,a-1l,Bl0,b-1])=E(Al},a-
2l,Blo,b - 2)).
o If the last character ofA is not equal to the last character of B then
E(A10, a - 1.), Bl0, b - 1l) = L + min
E(A10, a - 21, Bl0, b - 2l),
E(Al},a-U,Bl},b-21),
E(Al},a-2),Bl0,b-11)
The three terms correspond to transforming A to B by the following three ways:
- Transforming Al0,a - 1l to Bl),b - 1l by transforming Al0,a - 2l to Bl0,b - 2l and then
substituting A's last character with B's last character.
- Transformng AIO,a - 1] to Bl},b - 1l by transforming Al},a - 1l to B[0, b - 2] and then
adding B's last character at the end.
- Transforming AlO,a - 1l to BlO,b - 1l by transforming Al},a - 27 to Bl},b - 1l and then
deleting A's last character.
These observations are quite intuitive. Their rigorous proof, which we do not give, is based on
reordering steps in an arbitrary optimum solution for the original problem.
DP is a great way to solve this recurrence relation: cache intermediate results on the way to
computing E(AIO,a - 7l,BI},b - 1)).
We illustrate the approach in Figure 16.4 on the facing page. This shows the E values for
"Carthorse" and "Orchestra". Uppercase and lowercase characters are treated as being different.
The Levenshtein distance for these two strings is 8.
def Ievenshtein-distance (A, B) :
def compute-distance-between-prefixes (A-idx , B-idx) :
if A-idx < 0:
# A is enpty so add a77 of B's characters.
return B-idx + 1
elif B-idx < 0:
# B is enpty so delete a77 of l's characters.
return A-idx + 1
if distance-between-prefixeslA-idxl IB-idx] == -1:
if AIA-idxl == BIB-idx]:
distance-between-prefixesIA-idx] [B-idx] = (
compute-distance-between-prefixes(A-idx - 1, B-idx - 1))
else:
substitute-1ast = compute-distance-between-prefixes (
A-idx - 1, B-idx - 1)
add-last = compute-distance-between-prefixes(A-idx - 1, B-idx)
delete-Iast = compute-distance-between-prefixes (
240
```

#### Printed page 241 (PDF page 255)

```text
A_idx, B_idx - 1)
distance-betvreen_prefixesIA_idx] [B_idx] = (
1 + nin(substitute_last, add_last, delete_Iast))
return di stance_between_prefi xe s I A_idx] [ B_idx ]
distance_between_prefixes = [[-1] " ten(B) for _ in Al
return compute_distance_between-prefixes(Ien(A) 
- l, 1en(B) - 1)
The value E(Al},a -17,810,b - 1l) takes time O(1) to compute once E(A[0,k], B[0,1]) is known for all
k < a and I < b. This implies O(ab) fine complexity for the algorithm. Our implementation uses
O(ab) space.
Carthorse
0
1,2
ins
1*2
J
J
456789
\.?a\
o
3
4
5
3
4
5
1
2
J
4
5
c
h
e
4
J
3
4
5
7
6
6
5
6
5
5
4
5
4
4
9
8
8
7
6
6
8
7
7
6
6
\
2
r
22
\&a\
J
4
5
\
J
4
6lo
l6?-
7lo
to
8
a
\e,\
lns
4*5 \\
666665555
\%z\
777766666
888777767
998888877
Figure 16.4: The E table for "Carthorse" and "Orchestra".
variant: Compute the Levenshtein distance using O(min(a, b)) space and O(ab) time.
Variant Given A and B as above, compute a longest sequence of characters that is a subsequence
of A and of B. For example, the longest subsequence which is present in both strings in Figure 16.4
is (r,h,s).
Varianh Given a stringA, compute the minimum number of characters you need to delete from A
to make the resulting string a palindrome.
Variant Given a stringA and a regular expression r, what is the string in the language of the regular
expression r that is closest to z4? The distance between strings is the Levenshtein distance specified
above.
Varianfi Define a string f to be an interleaving of strings sr and s2 if there is a way to interleave
the characters of s1 and s2, keeping the left-to-right order of each, to obtain f. For example, if s1
s
t
t
241.
```
