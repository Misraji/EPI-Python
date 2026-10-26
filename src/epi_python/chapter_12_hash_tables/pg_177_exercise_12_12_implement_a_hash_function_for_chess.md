# Exercise 12.12: Implement a hash function for chess

**Printed textbook page:** 177. **Reference transcription pages:** 177–179.

> **Unverified OCR transcription:** This section retains the supplied PDF text layer. It is not certified verbatim: code syntax, mathematical symbols, and page boundaries may be corrupted. When two exercises begin on the same page, their excerpts overlap. Do not paste extracted code into a `.py` file without manual verification.

#### Printed page 177 (PDF page 191)

```text
o If multiplication and division are expensive, use bit shifting and addition.
o Partition the search set and use many computers in parallel to explore the subsets, as show in
Solution 19.9 on Page 299.
Since the numbers in a sequence may grow beyond 32 bits, you should use 64-bit integer and keep
testing for overflow; altemately, you can use arbitrary precision integers.
def test-colIatz-conjecture (n) :
# Stores odd nunbers aTready tested to convetge to 7
verified_numbers = seto
# Starts fron 3, hypothesis hoTds triviaTTy for 1.
foriinrange(3,n+1):
sequence = seto
test-i = i
rhile test-i >= i:
if test-i in sequence:
# We previously encountered test_i , so the CoTTatz sequence has
# fa77en into a 7oop. This disproves the hypothesis, so we
# short-circuit , returning FaIse.
return FaIse
sequence. add(test-i)
if test-i % 2: # Odd nunber.
if test-i in verified-numbers:
break # test-i has already been verified to converge to
verified-numbers . add (test-i )
test-i = 3 * test_i + 1 # IluTtiply by 3 and add 1.
else:
lesl-L //= Z # Even nunbet, haTve it.
return True
We cannot say much about time complexity beyond the obvious, namely that it is at least propor-
tional to n.
12.12 lNrpr-rvrsNr A HAsH FUNCTToN FoR cHEss
The state of a game of chess is determined by what piece is present on each square, as illustrated in
Figure 72.2 on the following page. Each square may be empty, or have one of six classes of pieces;
each piece may be black or white. Thus flog(1 + 6 x 2)l = 4 bits suffice per square, which means that
atotal of &x4=2i6bitscanrepresentthestateof thechessboard. (Theactualstateof thegameis
slightly more complex, as it needs to capture which side is to move, castling rights, en pnssant, etc.,
but we will use the simpler model for this question.)
Chess playing computers need to store sets of states, e.g., to determine if a particular state has
been evaluated before, or is known to be a winning state. To reduce storage, it is natural to apply
a hash function to the 256 bits of state, and ignore collisions. The hash code can be computed by
a conventional hash function for strings. However, since the computer repeatedly explores nearby
states, it is advantageous to consider hash functions that can be efficiently computed based on
incremental changes to the board.
Design a hash function for chess game states. Your function should take a state and the hash code
for that state, and a move, and efficiently compute the hash code for the updated state.
177
```

#### Printed page 178 (PDF page 192)

```text
8
7
6
5
4
3
2
1
1. f3, e5 2, g4,9h4
abcdefgh
Flgure 12.2: Chessboard corresponding to the fastest checkmate, Fools Mate.
Hint: XOR is associative, commutative, and fast to compute. Additionally, a @ a = 0.
Solution: A straightforward hash function is to treat the board as a sequence of 64 base 13 digits.
There is one digit per square, with the squares numbered from 0 to 63. Each digit encodes the state
of asquare: blank,whitepawn,whiterook,...,whiteking,blackpawn,...,blackking. Weusethe
hash functio" Iljo cipi , where c; is the digit in location i, and p is a prime (see on Page 159 for more
details).
Note that this hash function has some ability to be updated incrementally. If, for example, a
black knight taken by a white bishop the new hash code can be computed by subtracting the terms
corresponding to the initial location of the knight and bishop, and adding a term for a blank at the
initial location of the bishop and a term for the bishop at the knight's original position.
Now we describe a hash function which is much faster to update. It is based on creating a
random 64bit integer code for each of the 13 states that each of the 64 squares can be in. These
13 x 64 = 832 random codes are constants in the program. The hash code for the state of the
chessboard is the XOR of the code for each location. Updates are very fast-for the example above,
we XOR the code for black knight on lr, white bishop on i2, white bishop on 11, and blank on lz.
Incremental updates to the first hash function entail computing terms like p' which is more
expensive than computing an XO& which is why the second hash function is preferable. The
maximum number of word-level XORs performed is 4, for a capture or a castling.
As an example, consider a simpler game played on a 2x2board, with at most two pieces, P
and Q present on the board. At most one piece can be present at a board position. Denote the
board positions by (0,0), (0,1), (1,0), and (1, 1). We use the following random 7-bit codes for each
individual position:
r For (0,0): (1100111)2 for blank, (1011000)2 for P, (1100010)2 for Q.
o For (0,1): (1111100)2 for blank, (1000001)2 for P, (0001111)2 for Q.
o For (1,0): (1100101)2 for blank, (1101101)2 for P, (0011101)z for Q.
r For (1,1): (0100001)2 for blank, (0101100)2 for P, (1001011)2 for Q.
178
```

#### Printed page 179 (PDF page 193)

```text
Consider the following state: P is present at (0,0) and Q at (L, 1), with the remaining positions blank.
The hash code for this state is (1011000)2 o (1111100)2 o (1100101)2 o (1001011)2 = (0001010)2. Now
to compute the code for the state where Q moves to (Q 1), we XOR the code for the current state
with (L001011)2 (removes Q from (1, 1)), (0100001)2 (adds blank at (1,1)), (1111100)2 (removes blank
from (Q 1)), and (0001111)2 (adds Q at (0,1)). Note that, regardless of the size of the board and the
number of pieces, this approach uses four XORs to get the updated state.
Variant How can you include castling rights arrd m passant information in the state?
179
```
