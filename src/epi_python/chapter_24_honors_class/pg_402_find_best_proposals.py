"""EPI Python — Exercise 24.35: Road Network

Chapter 24: Honors Class
Textbook: pages 402–403 (printed page numbers; problem and solution start
on 402).

PROBLEM (from the textbook)
---------------------------
Context: "The California Department of Transportation is considering adding
a new section of highway to the California Highway System. Each highway
section connects two cities. City officials have submitted proposals for the
new highway—each proposal includes the pair of cities being connected and
the length of the section."

"Write a program which takes the existing highway network (specified as a set
of highway sections between pairs of cities) and proposals for new highway
sections, and returns the proposed highway section which leads to the most
improvement in the total driving distance. The total driving distance is
defined to be the sum of the shortest path distances between all pairs of
cities. All sections, existing and proposed, allow for bi-directional
traffic, and the original network is connected."

HINT (from the textbook)
------------------------
"Suppose we add a new section from b_s to b_f. If the shortest path from u
to v passes through this section, what must be true of the part of the path
from u to b_s?"

SOLUTION DEVELOPMENT (following the textbook)
---------------------------------------------
Adding all proposals at once and running one shortest-path computation does
not work: a resulting shortest path might use several proposals.

Brute force: compute all-pairs shortest path distances for the original
network; then, for each of the k proposals separately, add it, recompute all
pairs, and record the total improvement. All-pairs shortest paths take
O(n^3) with the Floyd-Warshall algorithm, so this is O(k n^3).

Improvement: run all-pairs shortest paths only once. Let S(u, v) be the 2D
array of shortest distances. For a proposal p joining cities x and y with
length d(x, y), the best distance between cities a and b when p is available
is

    min(S(a, b), S(a, x) + d(x, y) + S(y, b), S(a, y) + d(y, x) + S(x, b)),

an O(1) computation. So all proposals are evaluated in time proportional to
(number of proposals) x (number of pairs) once S is known, for O(n^3 + k n^2)
overall, a substantial improvement over brute force.

The book prints one program; find_best_proposals below follows it, with the
differences listed in the code comparison block.

ADDITIONAL EXAMPLES (added for learning; not printed in this exercise)
---------------------------------------------------------------------
    cities 0, 1, 2; highways 0-1 (5) and 1-2 (5); proposals 0-2 (2) and
    0-2 (11)  ->  the 0-2 section of length 2 (the 11 one saves nothing)
"""

# Python standard library: specialized container types.
# Module documentation: https://docs.python.org/3/library/collections.html
# namedtuple API: https://docs.python.org/3/library/collections.html#collections.namedtuple
from collections import namedtuple


# collections.namedtuple creates a tuple subclass with named fields: a
# HighwaySection joins cities .x and .y (integers 0..n-1) with length
# .distance. Instances compare equal when all fields are equal, which the
# __main__ assertion relies on. Same definition as the book.
HighwaySection = namedtuple('HighwaySection',('x','y','distance'))


# Type hints: two lists of HighwaySection and the city count n; the return
# value is unannotated (a HighwaySection or None). Annotations are not
# enforced at run time.
def find_best_proposals(highways: list[HighwaySection], proposals: list[HighwaySection], n: int):
    """Return the proposal that most reduces total all-pairs distance.

    This is the textbook's single implementation (one Floyd-Warshall run,
    then an O(1) test per proposal and city pair). Returns None if no
    proposal gives a positive saving (the book returns a default section).
    """

    # g stores the shortest path distances between all pairs of vertices.
    # float('inf') (positive infinity) marks "no known path yet"; inf plus a
    # number is still inf and every finite number compares smaller, so the
    # min() calls below need no special cases. The list comprehension gives
    # each row its own list.
    g=[[float('inf')]*n for _ in range(n)]
    for i in range(n):
        g[i][i]=0

    # Builds an undirected graph from the existing highway sections: chained
    # assignment sets both g[x][y] and g[y][x]; min() keeps the shorter of
    # duplicate sections between the same two cities.
    for road in highways:
        g[road.x][road.y]=g[road.y][road.x]=min(g[road.x][road.y],road.distance)

    # Floyd-Warshall: after processing intermediate city k, g[i][j] is the
    # shortest distance using only cities 0..k as intermediate stops. The
    # outer loop must be over k. O(n^3) time.
    for k in range(n):
        for i in range(n):
            for j in range(n):
                g[i][j]=min(g[i][j],g[i][k]+g[k][j])

    # Examines each proposal for shorter distances over all pairs.
    best = None
    best_saving = 0
    for proposed in proposals:
        total_saving=0
        for a in range(n):
            for b in range(n):

                # Shortest a -> b route that uses the new section, in either
                # direction (a .. x -> y .. b, or a .. y -> x .. b).
                proposed_distance = min(g[a][proposed.x] + proposed.distance + g[proposed.y][b],
                                        g[a][proposed.y] + proposed.distance + g[proposed.x][b])

                # Only an improvement counts; max(..., 0) ignores pairs
                # whose existing route is already shorter.
                total_saving += max(g[a][b]-proposed_distance,0)

        # Keep the proposal with the largest strictly positive saving.
        # Tuple assignment updates both variables at once.
        if total_saving>best_saving:
            best_saving,best=total_saving,proposed
    return best


# TEXTBOOK POST-SOLUTION DISCUSSION (pages 402–403)
# -------------------------------------------------
# The complexity analysis is part of the solution development: O(n^3) for
# the single all-pairs shortest path computation plus O(k n^2) to evaluate
# the k proposals over all pairs, i.e. O(n^3 + k n^2). The book gives no
# further discussion after the program.
#
# VARIANTS
# --------
# The book states no variants for this exercise.


# TEXTBOOK CODE COMPARISON
# ------------------------
# * Signature: book `def find_best_proposals(H, P, n)`; file
#   `find_best_proposals(highways, proposals, n)` with list/int type hints.
# * Import: book `collections.namedtuple`; file imports `namedtuple`
#   directly. The book also uses `itertools.product(...)` for its triple and
#   double loops; the file writes nested `for` loops and has no itertools
#   import.
# * Matrix: book `G = [[float('inf')] * i + [0] + [float('inf')] * (n - i - 1)
#   for i in range(n)]`; file builds an all-inf matrix and sets the
#   diagonal in a loop. Book assigns `G[h.x][h.y] = G[h.y][h.x] =
#   h.distance` directly; file keeps the minimum of duplicates.
# * Floyd-Warshall: book's nested `floyd_warshall(G)` skips updates when
#   `G[i][k]` or `G[k][j]` is inf; file inlines the loops and relies on inf
#   arithmetic. Same result.
# * Saving: book computes `G[a][b] - (G[a][p.x] + p.distance + G[p.y][b])`
#   (one direction only per ordered pair); file takes the minimum over both
#   directions, matching the formula in the text. Totals can differ.
# * Result: book starts `best_distance_saving = float('-inf')` with default
#   `best_proposal = HighwaySection(-1, -1, 0)`, so it returns the first
#   proposal even with zero saving; file starts at 0 and returns None when
#   no proposal saves anything.


# Python executes this block only when this source file is run directly.
# When pytest imports the file, this block is skipped automatically.
# Documentation: https://docs.python.org/3/library/__main__.html
if __name__=='__main__':

    # Added example: a path 0-1-2 of total length 10 between cities 0 and 2;
    # a direct section of length 2 helps, one of length 11 does not.
    roads=[HighwaySection(0,1,5),HighwaySection(1,2,5)]
    choices=[HighwaySection(0,2,2),HighwaySection(0,2,11)]
    print('Best highway:',find_best_proposals(roads,choices,3))

    # `assert` stops with an AssertionError if the condition is false; a
    # quick smoke check. pytest provides the more thorough verification.
    assert find_best_proposals(roads,choices,3)==choices[0]
