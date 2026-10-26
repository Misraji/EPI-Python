# Exercise 24.36: Test if arbitrage is possible

**Printed textbook page:** 403. **Reference transcription pages:** 403–405.

> **Unverified OCR transcription:** This section retains the supplied PDF text layer. It is not certified verbatim: code syntax, mathematical symbols, and page boundaries may be corrupted. When two exercises begin on the same page, their excerpts overlap. Do not paste extracted code into a `.py` file without manual verification.

#### Printed page 403 (PDF page 417)

```text
number of proposals times the number of pairs after we have computed the shortest path between
each pair of cities. This results tn anO(n3 + knz) time complexity, which improves substantially on
the brute-force approach.
HighwaySection = collections.namedtuple('HighwaySection', ('x',,y,,
'distance ') )
def find*best-proposals(H, P, n) :
# G stores the shortest path distances betr{een a77 pairs of vertices
c = [[float('inf')] 
o i + [0] + [float('inf')] 
o (n - i - 1)
for i in range (n) l
# BuiTds an und.irected graph G based on existing highway sections H.
for h in H:
Glh.xl [h.y] = Cth.yl [h.x] = h.distance
def floyd-warshall (G) :
for k, i, j in itertools.product(range(Ien(G)), repeat=3):
if Gtil tkl t= float('inf') 
and Gtkl tjl t= float('inf')
ctil tjl = nin(clil tjl, ctil tkl + Gtkl til)
# Perforns fToyd warshaTT to bujld the shortest path betrreen ve.rtjces
floyd-warshaII (G)
# Examines each proposal for shorter distance for aTL pairs.
best-distance-saving = float(' -inf ')
best-proposal = Highwaysection(-1, -1, 0) # DefauTt.
for p in P:
proposal-saving = 5
for a, b in itertools . product (range(n) , repeat=2) :
saving = clal tbl - (Ctal Ip. x] + p. distance + Glp.yl tbl )
proposal_saving += nar(saving, 0)
if proposal-saving > best_distance_saving:
best-distance_saving - proposal_saving
best-proposal = p
return best-proposal
24.36 Tssr rr ARBTTRAGE rs possrBr,E S
Suppose you are given a set of exchange rates among currencies and you want to determine if an
arbitrage exists, i.e., there is a way by which you can start with one unit of some currency C and
perform a series of barters which results in having more than one unit of C. Transaction costs are
zerol exchange rates do not fluctuate, fractional quantities of items can be sold, and the exchange
rate between each pair of currencies is finite.
Table 24.3 shows a representative example. An arbitrage is possible for this set of exchange
rates:1USD--+ 1x0.8123 =0.8123 EUR--+ 0.8123x1.2010 =0.9755723CHF--+ 0.9755723x80.39=
7 8.426257 197 IPY --+ 7 8.426257 197 x 0.0128 = 1.0038560921.2 U9D.
Design an efficient algorithm to determine whether there exists an arbitrage-a way to start with a
single unit of some currency C and convert it back to more than one unit of C through a sequence
of exchanges.
403
```

#### Printed page 404 (PDF page 418)

```text
Table 24.3: Exchange rates for seven major currencies.
Symbol USD EUR GBP IPY CHF CAD
AUD
USD
EUR
GBP
IPY
CHF
CAD
AUD
1
1.2275
1..5517
0.0128
1..02t9
1..0076
1.0567
0.8123
1
1.2724
0.0104
0.8327
0.8205
0.8509
0.6404
0.7860
1
0.0081
0.5546
0.u53
0.6767
78.1.25
96.55
122.83
1
80.39
79.26
83.1.2
0.9784
1.2010
1.s280
1.2442
1
0.9859
1.0339
0.9924
1.2182
1..5498
0.0126
1.01.42
1
1.0487
0.9465
t.t6't6
t.4n8
0.0120
0.9672
0.9535
1
Hint: The effect of a sequence of conversions is multiplicative. Can you recast the problem so that it can be
calculated additively?
Solution: Drawing pictures is a great way to brainstorm for a potential solution. Lr this case, the
relationships between the currencies can be represented using a graph. Specifically, we can model
the problem with a graph where currencies correspond to vertices, exchanges correspond to edges,
and the edge weight is set to the logarithm of the exchange rate, If we can find a cycle in the graph
with a positive weight, we would have found such a series of exchanges. Such a cycle can be solved
using the Bellman-Ford algorithm.
We define a weighted directed graph 5, : (V,E = V x V), where V corresponds to the set of
currencies. The weight w(e) of edge e = (u,a) is the amount of currency o we can buy with one unit
of currency a. Observe that an arbitrage exists if and only if there exists a cycle in G whose edge
weights multiply out to more than 1.
Create a new graph 6,' = (V,E) with weight function w'(e) = -logw(e). Since log(a xb) =
loga + log b, there exists a cycle in G whose edge weights multiply out to more than 1 if and only if
there exists a cycle in G' whose edge weights sum up to less than log 1 = 0. (This property is true
for logarithms to any base, so if it is more efficient for example to use base-e, we can do so.)
The Bellman-Ford algorithm detects negative-weight cycles. Usually, finding anegative-weight
cycle is done by adding a dummy vertex s with 0-weight edges to each vertex in the given graph and
running the Bellman-Ford single-source shortest path algorithm from s. However, for the arbitrage
problem, the graph is complete. Hence, we can run Bellman-Ford algorithm from any single vertex,
and get the right result.
def is-arbitrage-exist(G) 
:
def bellman-ford(G, source) :
dis-to-source = ([float('inf')] 
o (source - 1) + [0] + [float('inf')] 
o
(Ien(G) - source))
for - in range(l, Ien(c)):
have-update = False
for i , row in enunerate (G) :
for j, g in enunerate(row):
if (dis-to-sourcetil l= float('inf')
and dis-to-sourceIj] > dis-to-sourcetil + g)
have-update = True
dis-to-sourceIj] = dis-to-sourceIi] + g
# No update in this iteration mears no negative cycle
if not have-update:
404
```

#### Printed page 405 (PDF page 419)

```text
return False
# Detects cycle if there is any further update.
return any(dis-to-sourcetil != float('inf ')
and dis_to_sourceIj] > dis_to_sourceIi] + S
for i, row in enu[erate(G) f,or i, s in enulerat€(row))
# Uses BeTTnan-ford to find negative weight cycle,
return bellman-ford([[-uath.Iog10(edge) for edge ln edge_1ist]
for edge-list in Gl, 0)
The time complexity of the general Bellman-Ford algorithm is O(lyllEl). Here, lEl = O(lyP) and
lVl = n, so the time complexity is O(n3).
405
```
