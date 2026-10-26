# Exercise 16.9: Pick up coins for maximum gain

**Printed textbook page:** 252. **Reference transcription pages:** 252–252.

> **Unverified OCR transcription:** This section retains the supplied PDF text layer. It is not certified verbatim: code syntax, mathematical symbols, and page boundaries may be corrupted. When two exercises begin on the same page, their excerpts overlap. Do not paste extracted code into a `.py` file without manual verification.

#### Printed page 252 (PDF page 266)

```text
min-weight-to-curr-row = [
rowljl +
nin(min-weight-to_curr-row[nax(j - 1, 0) ] ,
min_weight-to-curr-row Inin(j, len(min-weight-to-curr-row) -
for j in range(Ien(row))
l
return nin(min-weight-to-curr-row)
1) I )
ThetimespentperelementisO(i)andtherearel+2+...+n=n(n+1)lzelements,implyingan
O(nz) tLlrne complexity. The space complexity is O(n).
1,6.9 Prcx up corNs FoR MAXTMUM GAIN
In the pick-up-coins game, an even number of coins are placed in a line, as in Figure 16.11. Two
players take tums at choosing one coin each-they can only choose from the two coins at the ends
of the line. The game ends when all the coins have been picked up. The player whose coins have
the higher total value wins. A player cannot pass his tum.
Flgure 16.11 : A row of coins.
Design an efficient algorithm for computing the maximum total value for the starting player in the
pick-up-coins game.
Hlrf: Relate the best play for the first player to the best play for the second player.
Solution: First of all, note that greedily selecting the maximum of the two end coins does not yield
the best solution. If the coins are 5,25,10,1., if the first player is greedy and chooses 5, the second
player can pick up the 25. Now the first player will choose the 10, and the second player gets the
1, so the first player has a total of 15 and the second player has a total of 26. A better move for the
first player is picking up 1. Now the second player is forced to expose the25, so the first player will
achieve 26.
The drawback of greedy selection is that it does not consider the opportunities created for the
second player. Intuitively, the first player wants to balance selecting high coins with minimizing
the coins available to the second player.
The second player is assumed to play the best move he possibly can. Therefore, the second player
will choose the coin that maximizes his revenue. Call the sum of the coins selected by a player his
revenue. Let R(a, b) be the maximum revenue a player can get when it is his tum to play, and the coins
remaining on the table are at indice s a to b, inclusive. Let C be an array representing the line of coins,
i.e., C[i] is the value of the lth coin. If the first player selects the coin at a, since the second player plays
optimally, the first playerwill end up with a total revenue of C[a]+S(a+7,b)-R(a+ 1, b), where S(a,b)
is the sum of the coins from positions a to b, inclusive. If he selects the coin at b, he will end up with
a total revenue of C[b] + S(a,b - 7) - R(a, b - 1). Since the first player wants to maximize revenue, he
chooses the greater of the two, i.e., R(a ,b) = max(C[al+S(a+1,b)-R(a+1,b),C\b1+S(a,b-1)-R(a,b-l)).
This recursion for R can be solved easily using DP.
Now we present a slightly different recurrence for R. Since the second player seeks to maximize
his revenue, and the total revenue is a constant, it is equivalent for the the second player to move
252
```
