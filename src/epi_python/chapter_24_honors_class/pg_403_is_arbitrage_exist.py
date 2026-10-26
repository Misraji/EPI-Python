"""EPI Python — Exercise 24.36: Test If Arbitrage Is Possible

Chapter 24: Honors Class
Textbook: pages 403–405 (printed page numbers; problem starts on 403,
solution on 404).

PROBLEM (from the textbook)
---------------------------
Context: given exchange rates among currencies, decide whether an arbitrage
exists, i.e. a way to start with one unit of some currency C and, through a
series of barters, end with more than one unit of C. Transaction costs are
zero, rates do not fluctuate, fractional quantities can be sold, and every
pair of currencies has a finite exchange rate.

Table 24.3 (page 404) gives rates for seven major currencies (row currency
to column currency):

    Symbol  USD     EUR     GBP     JPY     CHF     CAD     AUD
    USD     1       0.8123  0.6404  78.125  0.9784  0.9924  0.9465
    EUR     1.2275  1       0.7860  96.55   1.2010  1.2182  1.1616
    GBP     1.5617  1.2724  1       122.83  1.5280  1.5498  1.4778
    JPY     0.0128  0.0104  0.0081  1       1.2442  0.0126  0.0120
    CHF     1.0219  0.8327  0.6546  80.39   1       1.0142  0.9672
    CAD     1.0076  0.8206  0.6453  79.26   0.9859  1       0.9535
    AUD     1.0567  0.8609  0.6767  83.12   1.0339  1.0487  1

(The JPY -> CHF entry 1.2442 is transcribed as printed.)

An arbitrage is possible for these rates:
1 USD -> 1 x 0.8123 = 0.8123 EUR -> 0.8123 x 1.2010 = 0.9755723 CHF
-> 0.9755723 x 80.39 = 78.426257197 JPY
-> 78.426257197 x 0.0128 = 1.00385609212 USD.

"Design an efficient algorithm to determine whether there exists an
arbitrage—a way to start with a single unit of some currency C and convert
it back to more than one unit of C through a sequence of exchanges."

HINT (from the textbook)
------------------------
"The effect of a sequence of conversions is multiplicative. Can you recast
the problem so that it can be calculated additively?"

SOLUTION DEVELOPMENT (following the textbook)
---------------------------------------------
Model the problem as a graph: currencies are vertices and exchanges are
edges. (The book first describes using the logarithm of each rate as the
edge weight and looking for a positive-weight cycle, solvable with
Bellman-Ford, and then makes this precise as follows.)

Define the weighted directed graph G = (V, E = V x V), V being the set of
currencies, where the weight w(e) of edge e = (u, v) is the amount of
currency v that one unit of currency u buys. An arbitrage exists exactly
when G has a cycle whose edge weights multiply to more than 1.

Build G' = (V, E) with weights w'(e) = -log w(e). Because
log(a x b) = log a + log b, a cycle in G whose weights multiply to more than
1 corresponds exactly to a cycle in G' whose weights sum to less than
log 1 = 0, i.e. a negative-weight cycle. This holds for logarithms in any
base, so a convenient base (e.g. base e) may be used.

Bellman-Ford detects negative-weight cycles. Normally one adds a dummy
vertex s with 0-weight edges to every vertex and runs single-source
Bellman-Ford from s. Here the graph is complete, so running Bellman-Ford
from any single vertex gives the right answer.

The book prints one program; is_arbitrage_exist below follows it (using
natural logarithms and a small tolerance; see the code comparison).

ADDITIONAL EXAMPLES (added for learning; not printed in this exercise)
---------------------------------------------------------------------
    rates [[1, 2, 1], [0.5, 1, 2], [0.3, 0.5, 1]]  -> True
    (0 -> 1 -> 2 -> 0 gives 2 x 2 x 0.3 = 1.2 > 1)
"""

# Python standard library: mathematical functions.
# Module documentation: https://docs.python.org/3/library/math.html
# log API: https://docs.python.org/3/library/math.html#math.log
import math


# Type hints: `rates: list[list[float]]` is an n x n matrix where
# rates[u][v] is units of currency v per unit of u; `-> bool`. Annotations
# are documentation only and are not enforced.
def is_arbitrage_exist(rates: list[list[float]]) -> bool:
    """Return True if some cycle of exchanges multiplies money by > 1.

    This is the textbook's single implementation: transform rates by
    -log and run Bellman-Ford from vertex 0 to detect a negative cycle.
    """

    # Added guard (not in the book): no currencies, no arbitrage.
    if not rates:
        return False
    n=len(rates)

    # math.log(x) with one argument is the natural logarithm (base e). It
    # raises ValueError for x <= 0, so all rates must be positive. Negating
    # turns "product of rates > 1" into "sum of weights < 0". The nested
    # list comprehension builds a new matrix of the same shape.
    graph=[[-math.log(rate) for rate in row] for row in rates]

    # Bellman-Ford distances from source vertex 0; float('inf') (infinity)
    # means "not reached yet". Since the graph is complete, every vertex is
    # reached after the first round.
    distance=[float('inf')]*n
    distance[0]=0.0

    # n - 1 rounds of relaxing every edge; `_` marks an unused loop
    # variable.
    for _ in range(1,n):
        updated=False
        for i in range(n):
            for j in range(n):
                new_distance=distance[i]+graph[i][j]

                # Relax edge (i, j). The 1e-12 tolerance (scientific notation
                # for 0.000000000001) ignores tiny floating-point rounding
                # differences that would otherwise look like improvements.
                if new_distance<distance[j]-1e-12:
                    distance[j]=new_distance
                    updated=True

        # No update in this iteration means no negative cycle (book's
        # comment): the distances are final.
        if not updated:
            return False

    # Detects a cycle if any further update is possible (book's comment).
    # any() returns True as soon as one item of the generator expression is
    # true. The generator has two `for` clauses, ranging over all (i, j).
    return any(distance[i]+graph[i][j]<distance[j]-1e-12
               for i in range(n) for j in range(n))


# TEXTBOOK POST-SOLUTION DISCUSSION (page 405)
# --------------------------------------------
# General Bellman-Ford runs in O(|V||E|) time. Here |E| = O(|V|^2) and
# |V| = n, so the time complexity is O(n^3).
#
# VARIANTS
# --------
# The book states no variants for this exercise.


# TEXTBOOK CODE COMPARISON
# ------------------------
# * Signature: book `def is_arbitrage_exist(G)`; file renames `G` to
#   `rates` and adds type hints.
# * Logarithm: book uses `-math.log10(edge)` (base 10); file uses
#   `-math.log(rate)` (natural log). The book notes any base works.
# * Structure: book has a nested `bellman_ford(G, source)` called with
#   source 0 and builds `dis_to_source` with inf everywhere except the
#   source; file inlines Bellman-Ford with `distance[0]=0.0`.
# * Relaxation: book tests `dis_to_source[i] != float('inf') and
#   dis_to_source[j] > dis_to_source[i] + g`, iterating with `enumerate`;
#   file uses index loops and a `1e-12` tolerance instead of the inf check
#   (inf arithmetic makes that check unnecessary). The final `any(...)`
#   test likewise uses the tolerance.
# * Added: `if not rates: return False` guard.


# Python executes this block only when this source file is run directly.
# When pytest imports the file, this block is skipped automatically.
# Documentation: https://docs.python.org/3/library/__main__.html
if __name__ == '__main__':

    # Added example: 0 -> 1 -> 2 -> 0 multiplies by 2 x 2 x 0.3 = 1.2.
    rates=[[1,2,1],[0.5,1,2],[0.3,0.5,1]]
    print('Arbitrage detected:',is_arbitrage_exist(rates))

    # `assert` stops with an AssertionError if the condition is false; a
    # quick smoke check. pytest provides the more thorough verification.
    assert is_arbitrage_exist(rates)
