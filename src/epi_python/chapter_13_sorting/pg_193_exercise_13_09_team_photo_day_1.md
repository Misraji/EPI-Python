# Exercise 13.9: Team photo day - 1

**Printed textbook page:** 193. **Reference transcription pages:** 193–193.

> **Unverified OCR transcription:** This section retains the supplied PDF text layer. It is not certified verbatim: code syntax, mathematical symbols, and page boundaries may be corrupted. When two exercises begin on the same page, their excerpts overlap. Do not paste extracted code into a `.py` file without manual verification.

#### Printed page 193 (PDF page 207)

```text
13.9 Treu pnoro uay-1
You are a photographer for a soccer meet. You will be taking pictures of pairs of opposing teams.
A11 teams have the same number of players. A team photo consists of a front row of players and
a back row of players. A player in the back row must be taller than the player in front of him, as
illustrated in Figure 13.3. All players in a row must be from the same team.
Back row
Front row
Figure 13.3; A team photo. Each team has 1.1 players, and each player in the back row is taller than the corresponding
player in the front row.
Design an algorithm that takes as input two teams and the heights of the players in the teams and
checks if it is possible to place players to take the photo subject to the placement constraint.
Hint: First try some concrete inputs, then make a general conclusion.
Solution: A brute-force approach is to consider every permutation of one array, and compare it
against the other array, element by element. Suppose there are n players in each team. It takes
O(rz!) time to enumerate every possible permutation of a team, and testing if a permutation leads
to a satisfactory arrangement takes O(n) time. Therefore, the time complexity is O(nl x n), clearly
unacceptable.
Intuitively, we should narrow the search by focusing on the hardest to place players. Suppose
we want to place Team A behind Team B. If A's tallest player is not taller than the tallest player
in B, then it's not possible to place Team A behind Team B and satisfy the placement constraint.
Conversely, if Team A's tallest player is taller than the tallest player in B, we should place him in
front of the tallest player in B, since the tallest player in B is the hardest to place. Applying the same
logic to the remaining players, the second tallest player in A should be taller than the second tallest
player in B, and so on.
We can efficiently check whether A's tallest, second tallest, etc. players are each taller than B's
tallest, second tallest, etc. players by first sorting the arrays of player heights. Figure 13.4 shows the
teams in Figure 13.3 sorted by their heights.
Back row 
* ,t 'F ,i ,F fi i 
{,
Frontrow 
t I i t t t I I
Flgure 13.4r The teams lrom Figure 13.3 in sorted order
The program below uses this idea to test if a given team can be placed in front of another team.
fir ,fl rfi F ft * {,fi rf;r *, rfir
rrllrrlrrtt
.aa
rtT Er El
rtt
class Team:
Player = collections.namedtuple('Player', ('height'))
def --init-- 
(self , height) :
self.-p1ayer5 = [Team.Player(h) for h in height]
# Checks if A can be pTaced in front of B.
@stati cmethod
193
```
